from dataclasses import dataclass
from typing import List, Optional, Union
from .lexer import Token

@dataclass
class ASTNode:
    pass

@dataclass
class Literal(ASTNode):
    value: str
    type: str  # NUMBER, STRING, BOOLEAN, VARIABLE, NONE

@dataclass
class VariableDeclaration(ASTNode):
    name: str 
    value: ASTNode
    operator: str = ":="
    modifier: str = "LOCAL"

@dataclass
class SQLColumn(ASTNode):
    name: str
    type: str = ""

@dataclass
class SQLBlock(ASTNode):
    alias: str
    columns: List[SQLColumn]
    sql_query: str
    body: List[ASTNode]

@dataclass
class TransactionStatement(ASTNode):
    body: List[ASTNode]

@dataclass
class MultiVariableDeclaration(ASTNode):
    modifier: str
    declarations: List[VariableDeclaration]

@dataclass
class FunctionDeclaration(ASTNode):
    name: str
    body: List[ASTNode]
    params: List[str] = None
    is_user: bool = False
    is_static: bool = False

@dataclass
class IfStatement(ASTNode):
    condition: ASTNode
    then_body: List[ASTNode]
    else_body: List[ASTNode]

@dataclass
class CaseBranch(ASTNode):
    condition: ASTNode
    body: List[ASTNode]

@dataclass
class DoCase(ASTNode):
    cases: List[CaseBranch]
    otherwise: List[ASTNode]

@dataclass
class WhileLoop(ASTNode):
    condition: ASTNode
    body: List[ASTNode]

@dataclass
class ForLoop(ASTNode):
    variable: str
    start: ASTNode
    end: ASTNode
    body: List[ASTNode]

@dataclass
class FunctionCall(ASTNode):
    name: str
    args: List[ASTNode]

@dataclass
class ArrayLiteral(ASTNode):
    elements: List[ASTNode]

@dataclass
class ArrayAccess(ASTNode):
    array: ASTNode
    indices: List[ASTNode]

@dataclass
class PreprocessorNode(ASTNode):
    content: str

@dataclass
class BinaryExpression(ASTNode):
    left: ASTNode
    operator: str
    right: ASTNode

@dataclass
class UnaryExpression(ASTNode):
    operator: str
    operand: ASTNode

@dataclass
class CommentNode(ASTNode):
    content: str
    is_block: bool

@dataclass
class RawNode(ASTNode):
    tokens: List[Token]

@dataclass
class MethodCall(ASTNode):
    object: ASTNode
    method: str
    args: List[ASTNode]

@dataclass
class Macro(ASTNode):
    expression: ASTNode

@dataclass
class AliasAccess(ASTNode):
    alias: ASTNode
    field: ASTNode

@dataclass
class MethodDeclaration(ASTNode):
    name: str
    class_name: str
    params: List[str]
    body: List[ASTNode]
    is_user: bool = False

@dataclass
class ClassDeclaration(ASTNode):
    name: str
    data: List[str]
    methods: List[str]

@dataclass
class CodeBlock(ASTNode):
    params: List[str]
    expression: ASTNode

@dataclass
class TryStatement(ASTNode):
    body: List[ASTNode]
    recover_body: List[ASTNode]
    error_var: str = None

@dataclass
class LoopControl(ASTNode):
    type: str # EXIT or LOOP/CONTINUE

@dataclass
class AssignmentExpression(ASTNode):
    target: ASTNode
    value: ASTNode
    operator: str

@dataclass
class Program(ASTNode):
    statements: List[ASTNode]

class ParserError(Exception):
    pass

class ADVPLParser:
    def __init__(self, tokens: List[Token]):
        self.tokens = [t for t in tokens if t.type not in ('SKIP', 'NEWLINE')]
        self.pos = 0

    def current_token(self) -> Token:
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return Token('EOF', '', 0, 0)

    def skip_comments(self):
        while self.current_token().type in ('COMMENT', 'BLOCK_COMMENT', 'BLOCK_COMMENT_PROTHEUS'):
            self.pos += 1

    def consume(self, expected_type: str = None) -> Token:
        token = self.current_token()
        if expected_type and token.type != expected_type:
            # Skip comments if we are looking for something specific that is not a comment
            if expected_type not in ('COMMENT', 'BLOCK_COMMENT', 'BLOCK_COMMENT_PROTHEUS'):
                while token.type in ('COMMENT', 'BLOCK_COMMENT', 'BLOCK_COMMENT_PROTHEUS'):
                    self.pos += 1
                    token = self.current_token()
            
            if token.type != expected_type:
                if expected_type == 'IDENTIFIER' and token.type in (
                    'FUNCTION', 'LOCAL', 'CASE', 'DO', 'CLASS', 'STATIC', 'PRIVATE', 
                    'PUBLIC', 'IF', 'ELSE', 'ELSEIF', 'ENDIF', 'WHILE', 'ENDDO', 
                    'FOR', 'NEXT', 'TO', 'RETURN', 'EXIT', 'USER', 'METHOD', 
                    'BEGINSQL', 'ENDSQL', 'OTHERWISE', 'ENDCASE', 'TRANSACTION',
                    'COLUMN', 'AS'
                ):
                    self.pos += 1
                    return token
                raise ParserError(f"Expected {expected_type}, got {token.type} at line {token.line} value {token.value}")
        
        if self.pos < len(self.tokens):
            self.pos += 1
        return token

    def parse(self) -> Program:
        statements = []
        while self.current_token().type != 'EOF':
            statements.append(self.parse_statement())
        return Program(statements)

    def parse_statement(self) -> ASTNode:
        token = self.current_token()
        
        if token.type == 'LOCAL' or token.type == 'STATIC' or token.type == 'PRIVATE' or token.type == 'PUBLIC':
            if token.type == 'STATIC' and self.tokens[self.pos+1].type == 'FUNCTION':
                 pass # Will be handled by FUNCTION check
            else:
                 return self.parse_variable_declaration()
            
        if token.type == 'AT':
            # Check if it's followed by a number (UI command like @ 10,10)
            next_t = self.tokens[self.pos + 1] if self.pos + 1 < len(self.tokens) else None
            if next_t and next_t.type == 'NUMBER':
                self.consume('AT')
                line = token.line
                tokens = [token] 
                while self.current_token().line == line and self.current_token().type != 'EOF':
                    tokens.append(self.consume())
                return RawNode(tokens)
            # Else let it fall through to parse_expression
            
        if token.type == 'USER':
            self.consume('USER')
            if self.current_token().type == 'FUNCTION':
                self.consume('FUNCTION')
            return self.parse_function_declaration(is_user=True)
        elif token.type == 'STATIC':
            self.consume('STATIC')
            if self.current_token().type == 'FUNCTION':
                self.consume('FUNCTION')
            return self.parse_function_declaration(is_static=True)
        elif token.type == 'FUNCTION':
            self.consume('FUNCTION')
            return self.parse_function_declaration(is_user=False)
        elif token.type == 'METHOD':
            self.consume('METHOD')
            return self.parse_method_declaration()
        elif token.type == 'BEGIN':
            if self.pos + 1 < len(self.tokens) and self.tokens[self.pos+1].type == 'SEQUENCE':
                return self.parse_try_statement()
            elif self.pos + 1 < len(self.tokens) and self.tokens[self.pos+1].type == 'TRANSACTION':
                return self.parse_transaction_statement()
        elif token.type == 'IF':
            return self.parse_if_statement()
        elif token.type == 'DO':
            self.consume('DO')
            if self.current_token().type == 'CASE':
                return self.parse_do_case()
            elif self.current_token().type == 'WHILE':
                return self.parse_while_loop()
        elif token.type == 'WHILE':
            return self.parse_while_loop()
        elif token.type == 'FOR':
            return self.parse_for_loop()
        elif token.type == 'EXIT':
            self.consume('EXIT')
            return LoopControl('EXIT')
        elif token.type == 'RETURN':
            self.consume('RETURN')
            self.skip_comments()
            if self.current_token().type not in ('EOF', 'USER', 'FUNCTION', 'METHOD', 'ENDIF', 'ELSE', 'ELSEIF', 'ENDDO', 'NEXT', 'ENDCASE', 'OTHERWISE'):
                val = self.parse_expression()
                return FunctionCall('RETURN', [val])
            return FunctionCall('RETURN', [])
        elif token.type == 'COMMENT':
            content = self.consume('COMMENT').value
            return CommentNode(content, is_block=False)
        elif token.type == 'BLOCK_COMMENT':
            content = self.consume('BLOCK_COMMENT').value
            return CommentNode(content, is_block=True)
        elif token.type == 'BLOCK_COMMENT_PROTHEUS':
            content = self.consume('BLOCK_COMMENT_PROTHEUS').value
            return CommentNode(content, is_block=True)
        elif token.type == 'PREPROCESSOR':
            content = self.consume('PREPROCESSOR').value
            return PreprocessorNode(content)
        elif token.type == 'BEGINSQL':
            return self.parse_sql_block()
        
        if token.type == 'SEMICOLON':
            self.consume('SEMICOLON')
            return RawNode([])
            
        if token.type == 'INC_DEC':
            op = self.consume('INC_DEC').value
            operand = self.parse_expression()
            return UnaryExpression(op, operand)
            
        while self.current_token().type in ('COMMENT', 'BLOCK_COMMENT', 'BLOCK_COMMENT_PROTHEUS'):
            self.consume()
            
        expr = self.parse_expression()
        
        # Suffix ++/-- moved to parse_primary
        
        if self.current_token().type in ('ASSIGN', 'ASSIGN_OP', 'EQ'):
            op_token = self.consume()
            op = op_token.value
            val = self.parse_expression()
            return AssignmentExpression(expr, val, operator=op)
            
        return expr

    def parse_expression(self) -> ASTNode:
        expr = self.parse_logic_or()
        if self.current_token().type in ('ASSIGN', 'ASSIGN_OP'):
            op = self.consume().value
            val = self.parse_expression()
            return AssignmentExpression(expr, val, op)
        return expr

    def parse_logic_or(self) -> ASTNode:
        expr = self.parse_logic_and()
        while self.current_token().type == 'LOGIC_OP' and self.current_token().value.upper() == '.OR.':
            op = self.consume().value
            right = self.parse_logic_and()
            expr = BinaryExpression(expr, op, right)
        return expr

    def parse_logic_and(self) -> ASTNode:
        expr = self.parse_comparison()
        while self.current_token().type == 'LOGIC_OP' and self.current_token().value.upper() == '.AND.':
            op = self.consume().value
            right = self.parse_comparison()
            expr = BinaryExpression(expr, op, right)
        return expr

    def parse_comparison(self) -> ASTNode:
        expr = self.parse_additive()
        while self.current_token().type in ('EQ', 'NEQ', 'GT', 'LT', 'GT_EQ', 'LT_EQ', 'DOLLAR'):
            op = self.consume().value
            right = self.parse_additive()
            expr = BinaryExpression(expr, op, right)
        return expr

    def parse_additive(self) -> ASTNode:
        expr = self.parse_multiplicative()
        while self.current_token().type in ('PLUS', 'MINUS'):
            op = self.consume().value
            right = self.parse_multiplicative()
            expr = BinaryExpression(expr, op, right)
        return expr

    def parse_multiplicative(self) -> ASTNode:
        expr = self.parse_power()
        while self.current_token().type in ('STAR', 'SLASH', 'PERCENT'):
            op = self.consume().value
            right = self.parse_power()
            expr = BinaryExpression(expr, op, right)
        return expr

    def parse_power(self) -> ASTNode:
        expr = self.parse_unary()
        while self.current_token().type == 'POWER':
            op = self.consume('POWER').value
            right = self.parse_unary()
            expr = BinaryExpression(expr, op, right)
        return expr

    def parse_unary(self) -> ASTNode:
        token = self.current_token()
        if token.type in ('NOT', 'PLUS', 'MINUS', 'INC_DEC'):
            op = self.consume().value
            operand = self.parse_unary()
            return UnaryExpression(op, operand)
        if token.type == 'LOGIC_OP' and token.value.upper() == '.NOT.':
            op = self.consume().value
            operand = self.parse_unary()
            return UnaryExpression(op, operand)
        return self.parse_primary()

    def parse_primary(self) -> ASTNode:
        token = self.current_token()
        if token.type == 'AT': 
            self.consume('AT')
            return UnaryExpression("@", self.parse_primary())
        
        # token = self.current_token() # Re-fetched if not AT
        
        if token.type == 'AMP':
            self.consume('AMP')
            if self.current_token().type == 'LPAREN':
                self.consume('LPAREN')
                expr = self.parse_expression()
                self.consume('RPAREN')
            else:
                expr = self.parse_primary()
            if self.current_token().type == 'DOT':
                self.consume('DOT')
                if self.current_token().type == 'LPAREN':
                    self.consume('LPAREN')
                    args = self.parse_argument_list()
                    self.consume('RPAREN')
                    return FunctionCall("__macro_call__", [expr] + args)
            return Macro(expr)
            
        if token.type == 'DOUBLE_COLON':
            self.consume('DOUBLE_COLON')
            expr = Literal("self", "VARIABLE")
            method_name = self.consume('IDENTIFIER').value
            if self.current_token().type == 'LPAREN':
                self.consume('LPAREN')
                args = self.parse_argument_list()
                self.consume('RPAREN')
                expr = MethodCall(expr, method_name, args)
            else:
                expr = MethodCall(expr, method_name, [])
        elif token.type in ('NUMBER', 'STRING', 'BOOLEAN'):
            self.consume()
            expr = Literal(token.value, token.type)
        elif token.type == 'PREPROCESSOR':
            content = self.consume('PREPROCESSOR').value
            return PreprocessorNode(content)
        elif token.type == 'IDENTIFIER' or token.type in (
            'FUNCTION', 'LOCAL', 'CASE', 'DO', 'CLASS', 'STATIC', 'PRIVATE', 
            'PUBLIC', 'IF', 'ELSE', 'ELSEIF', 'ENDIF', 'WHILE', 'ENDDO', 
            'FOR', 'NEXT', 'TO', 'RETURN', 'EXIT', 'USER', 'METHOD', 
            'OTHERWISE', 'ENDCASE'
        ):
            name = self.consume('IDENTIFIER').value
            if self.current_token().type == 'LPAREN':
                self.consume('LPAREN')
                args = self.parse_argument_list()
                self.consume('RPAREN')
                expr = FunctionCall(name, args)
            else:
                expr = Literal(name, 'VARIABLE')
        elif token.type == 'LBRACE':
            self.consume('LBRACE')
            if self.current_token().type == 'PIPE':
                self.consume('PIPE')
                params = []
                while self.current_token().type != 'PIPE' and self.current_token().type != 'EOF':
                    if self.current_token().type in ('IDENTIFIER', 'FUNCTION', 'LOCAL', 'CASE', 'PRIVATE', 'PUBLIC', 'STATIC'):
                         params.append(self.current_token().value)
                         self.pos += 1
                    elif self.current_token().type == 'COMMA':
                        self.consume('COMMA')
                    else:
                        break
                self.consume('PIPE')
                self.skip_comments()
                if self.current_token().type == 'RBRACE':
                    expr_body = Literal('None', 'NONE')
                else:
                    exprs = [self.parse_expression()]
                    while self.current_token().type == 'COMMA':
                        self.consume('COMMA')
                        self.skip_comments()
                        if self.current_token().type == 'RBRACE': # Trailing comma
                            break
                        exprs.append(self.parse_expression())
                    if len(exprs) == 1:
                        expr_body = exprs[0]
                    else:
                        expr_body = ArrayLiteral(exprs)
                self.skip_comments()
                self.consume('RBRACE')
                return CodeBlock(params, expr_body)
            
            elements = []
            while self.current_token().type != 'RBRACE' and self.current_token().type != 'EOF':
                if self.current_token().type in ('COMMENT', 'BLOCK_COMMENT', 'BLOCK_COMMENT_PROTHEUS'):
                    self.consume()
                    continue
                if self.current_token().type == 'COMMA':
                    elements.append(Literal('None', 'NONE'))
                    self.consume('COMMA')
                    continue
                
                elements.append(self.parse_expression())
                self.skip_comments()
                if self.current_token().type == 'COMMA':
                    self.consume('COMMA')
                    self.skip_comments()
                    if self.current_token().type == 'RBRACE': # Trailing comma
                        elements.append(Literal('None', 'NONE'))
            self.consume('RBRACE')
            return ArrayLiteral(elements)
        elif token.type == 'LPAREN':
            self.consume('LPAREN')
            expr = self.parse_expression()
            self.consume('RPAREN')
        else:
            t = self.consume()
            return Literal(t.value, 'UNKNOWN')

        while True:
            if self.current_token().type == 'COLON':
                self.consume('COLON')
                method_name = self.consume('IDENTIFIER').value
                if self.current_token().type == 'LPAREN':
                    self.consume('LPAREN')
                    args = self.parse_argument_list()
                    self.consume('RPAREN')
                    expr = MethodCall(expr, method_name, args)
                else:
                    expr = MethodCall(expr, method_name, [])
            elif self.current_token().type == 'LBRACKET':
                self.consume('LBRACKET')
                indices = []
                while self.current_token().type != 'RBRACKET' and self.current_token().type != 'EOF':
                    indices.append(self.parse_expression())
                    if self.current_token().type == 'COMMA':
                        self.consume('COMMA')
                self.consume('RBRACKET')
                expr = ArrayAccess(expr, indices)
            elif self.current_token().type == 'ARROW':
                self.consume('ARROW')
                if self.current_token().type == 'LPAREN':
                    self.consume('LPAREN')
                    field = self.parse_expression()
                    self.consume('RPAREN')
                else:
                    field = self.parse_primary()
                expr = AliasAccess(expr, field)
            elif self.current_token().type == 'INC_DEC':
                op = self.consume('INC_DEC').value
                expr = UnaryExpression(f"POST_{op}", expr)
            else:
                break
        
        return expr

    def parse_argument_list(self) -> List[ASTNode]:
        args = []
        while self.current_token().type != 'RPAREN' and self.current_token().type != 'EOF':
            if self.current_token().type in ('COMMENT', 'BLOCK_COMMENT', 'BLOCK_COMMENT_PROTHEUS'):
                self.consume()
                continue
            if self.current_token().type == 'COMMA':
                args.append(Literal('None', 'NONE'))
                self.consume('COMMA')
            elif self.current_token().type in ('ASSIGN', 'ASSIGN_OP'):
                op = self.consume().value
                args.append(Literal(op, 'SPECIAL'))
                if self.current_token().type == 'COMMA':
                   self.consume('COMMA')
            else:
                args.append(self.parse_expression())
                self.skip_comments()
                if self.current_token().type == 'COMMA':
                    self.consume('COMMA')
                    self.skip_comments()
                    if self.current_token().type == 'RPAREN': # Trailing comma
                        args.append(Literal('None', 'NONE'))
                    # Trailing comma
                    if self.current_token().type == 'RPAREN':
                        args.append(Literal('None', 'NONE'))
        return args

    def parse_variable_declaration(self) -> ASTNode:
        modifier_token = self.consume()
        modifier = modifier_token.type 
        
        declarations = []
        while True:
            name_token = self.consume('IDENTIFIER')
            if self.current_token().type in ('ASSIGN', 'EQ'):
                op = self.consume().value
                val_node = self.parse_expression()
                declarations.append(VariableDeclaration(name_token.value, val_node, operator=op, modifier=modifier))
            else:
                declarations.append(VariableDeclaration(name_token.value, Literal('None', 'NONE'), modifier=modifier))
            
            if self.current_token().type == 'COMMA':
                self.consume('COMMA')
            else:
                break
        
        if len(declarations) == 1:
            return declarations[0]
        return MultiVariableDeclaration(modifier, declarations)

    def parse_if_statement(self) -> IfStatement:
        self.consume('IF')
        condition = self.parse_expression()
        then_body = []
        while self.current_token().type not in ('ELSEIF', 'ELSE', 'ENDIF', 'EOF'):
            then_body.append(self.parse_statement())
        
        else_body = []
        if self.current_token().type == 'ELSEIF':
            self.consume('ELSEIF')
            else_body = [self._parse_elseif_as_if()]
        elif self.current_token().type == 'ELSE':
            self.consume('ELSE')
            while self.current_token().type != 'ENDIF' and self.current_token().type != 'EOF':
                else_body.append(self.parse_statement())
                
        if self.current_token().type == 'ENDIF':
            self.consume('ENDIF')
        return IfStatement(condition, then_body, else_body)

    def _parse_elseif_as_if(self) -> IfStatement:
        # Same as parse_if_statement but doesn't consume IF (already consumed ELSEIF)
        condition = self.parse_expression()
        then_body = []
        while self.current_token().type not in ('ELSEIF', 'ELSE', 'ENDIF', 'EOF'):
            then_body.append(self.parse_statement())
        
        else_body = []
        if self.current_token().type == 'ELSEIF':
            self.consume('ELSEIF')
            else_body = [self._parse_elseif_as_if()]
        elif self.current_token().type == 'ELSE':
            self.consume('ELSE')
            while self.current_token().type != 'ENDIF' and self.current_token().type != 'EOF':
                else_body.append(self.parse_statement())
        # Note: ENDIF is consumed by the parent IF call
        return IfStatement(condition, then_body, else_body)

    def parse_do_case(self) -> DoCase:
        self.consume('CASE')
        cases = []
        otherwise = []
        while self.current_token().type not in ('ENDCASE', 'EOF'):
            if self.current_token().type == 'CASE':
                self.consume('CASE')
                cond = self.parse_expression()
                body = []
                while self.current_token().type not in ('CASE', 'OTHERWISE', 'ENDCASE', 'EOF'):
                    body.append(self.parse_statement())
                cases.append(CaseBranch(cond, body))
            elif self.current_token().type == 'OTHERWISE':
                self.consume('OTHERWISE')
                while self.current_token().type not in ('ENDCASE', 'EOF'):
                    otherwise.append(self.parse_statement())
            else:
                self.consume()
        if self.current_token().type == 'ENDCASE':
            self.consume('ENDCASE')
        return DoCase(cases, otherwise)

    def parse_while_loop(self) -> WhileLoop:
        if self.current_token().type == 'WHILE':
            self.consume('WHILE')
        condition = self.parse_expression()
        body = []
        while self.current_token().type not in ('ENDDO', 'EOF'):
            body.append(self.parse_statement())
        if self.current_token().type == 'ENDDO':
            self.consume('ENDDO')
        return WhileLoop(condition, body)

    def parse_for_loop(self) -> ASTNode:
        self.consume('FOR')
        target_expr = self.parse_statement() 
        target_name = ""
        start_val = None
        if isinstance(target_expr, VariableDeclaration):
            target_name = target_expr.name
        elif isinstance(target_expr, MultiVariableDeclaration):
            target_name = target_expr.declarations[0].name
        elif isinstance(target_expr, AssignmentExpression):
             if isinstance(target_expr.target, Literal):
                 target_name = target_expr.target.value
        else:
            target_name = str(target_expr)
            
        self.consume('TO')
        limit = self.parse_expression()
        step = None
        if self.current_token().type == 'STEP':
            self.consume('STEP')
            step = self.parse_expression()
            
        body = []
        while self.current_token().type not in ('NEXT', 'EOF'):
            body.append(self.parse_statement())
        if self.current_token().type == 'NEXT':
            next_token = self.consume('NEXT')
            if self.current_token().type == 'IDENTIFIER' and self.current_token().line == next_token.line:
                self.consume('IDENTIFIER')
        return ForLoop(target_name, start_val if 'start_val' in locals() else target_expr.value if isinstance(target_expr, VariableDeclaration) else Literal("0", "NUMBER"), limit, body)

    def parse_try_statement(self) -> ASTNode:
        self.consume('BEGIN')
        self.consume('SEQUENCE')
        
        body = []
        while self.current_token().type not in ('EOF', 'RECOVER', 'ENDSEQUENCE'):
            if self.current_token().type == 'IDENTIFIER' and self.current_token().value.upper() == 'END':
                if self.pos + 1 < len(self.tokens) and self.tokens[self.pos+1].type == 'SEQUENCE':
                    break
            body.append(self.parse_statement())
            
        recover_body = []
        error_var = None
        if self.current_token().type == 'RECOVER':
            self.consume('RECOVER')
            if self.current_token().type == 'IDENTIFIER' and self.current_token().value.upper() == 'USING':
                self.consume('IDENTIFIER')
                error_var = self.consume('IDENTIFIER').value
                
            while self.current_token().type not in ('EOF', 'ENDSEQUENCE'):
                if self.current_token().type == 'IDENTIFIER' and self.current_token().value.upper() == 'END':
                    if self.pos + 1 < len(self.tokens) and self.tokens[self.pos+1].type == 'SEQUENCE':
                        break
                recover_body.append(self.parse_statement())
                
        if self.current_token().type == 'ENDSEQUENCE':
            self.consume('ENDSEQUENCE')
        elif self.current_token().type == 'IDENTIFIER' and self.current_token().value.upper() == 'END':
            self.consume('IDENTIFIER')
            self.consume('SEQUENCE')
            
        return TryStatement(body, recover_body, error_var)

    def parse_transaction_statement(self) -> ASTNode:
        self.consume('BEGIN')
        self.consume('TRANSACTION')
        
        body = []
        while self.current_token().type not in ('EOF', 'END'):
            if self.current_token().type == 'IDENTIFIER' and self.current_token().value.upper() == 'END':
                if self.pos + 1 < len(self.tokens) and self.tokens[self.pos+1].type == 'TRANSACTION':
                    break
            body.append(self.parse_statement())
            
        if self.current_token().type == 'IDENTIFIER' and self.current_token().value.upper() == 'END':
            self.consume('IDENTIFIER')
            self.consume('TRANSACTION')
            
        return TransactionStatement(body)

    def parse_sql_block(self) -> ASTNode:
        self.consume('BEGINSQL')
        
        alias = ""
        if self.current_token().type == 'IDENTIFIER' and self.current_token().value.upper() == 'ALIAS':
            self.consume('IDENTIFIER')
            alias_token = self.current_token()
            if alias_token.type == 'STRING':
                alias = alias_token.value.strip('"\'')
                self.pos += 1
            elif alias_token.type == 'IDENTIFIER':
                alias = alias_token.value
                self.pos += 1
        
        columns = []
        sql_lines = []
        
        while self.current_token().type != 'ENDSQL' and self.current_token().type != 'EOF':
            if self.current_token().type == 'COMMENT':
                self.consume()
                continue
                
            if self.current_token().type == 'COLUMN':
                self.consume('COLUMN')
                col_name = self.consume('IDENTIFIER').value
                col_type = ""
                if self.current_token().type == 'AS':
                    self.consume('AS')
                    col_type = self.consume('IDENTIFIER').value
                columns.append(SQLColumn(col_name, col_type))
            else:
                token = self.current_token()
                sql_lines.append(token.value)
                self.pos += 1
        
        if self.current_token().type == 'ENDSQL':
            self.consume('ENDSQL')
        
        sql_query = ' '.join(sql_lines).strip()
        
        body = []
        while self.current_token().type not in ('EOF', 'USER', 'FUNCTION', 'METHOD', 'STATIC'):
            next_token = self.current_token()
            if next_token.type == 'IDENTIFIER' and next_token.value.upper() in ('END', 'RETURN', 'IF', 'WHILE', 'FOR', 'DO'):
                break
            if next_token.type in ('FUNCTION', 'USER', 'STATIC', 'METHOD'):
                break
            body.append(self.parse_statement())
        
        return SQLBlock(alias, columns, sql_query, body)

    def parse_function_declaration(self, is_user=False, is_static=False) -> FunctionDeclaration:
        name_token = self.consume('IDENTIFIER')
        params = []
        if self.current_token().type == 'LPAREN':
            self.consume('LPAREN')
            while self.current_token().type != 'RPAREN' and self.current_token().type != 'EOF':
                if self.current_token().type in ('IDENTIFIER', 'FUNCTION', 'LOCAL', 'CASE', 'PRIVATE', 'PUBLIC', 'STATIC'):
                    params.append(self.current_token().value)
                    self.pos += 1
                elif self.current_token().type == 'COMMA':
                    self.consume('COMMA')
                else:
                    if self.current_token().type != 'RPAREN':
                       self.consume()
            if self.current_token().type == 'RPAREN':
                self.consume('RPAREN')
        body = []
        while self.current_token().type not in ('EOF', 'USER', 'FUNCTION', 'METHOD', 'STATIC'):
            body.append(self.parse_statement())
        return FunctionDeclaration(name_token.value, body, params=params, is_user=is_user, is_static=is_static)

    def parse_method_declaration(self) -> MethodDeclaration:
        name = self.consume('IDENTIFIER').value
        params = []
        if self.current_token().type == 'LPAREN':
            self.consume('LPAREN')
            while self.current_token().type != 'RPAREN' and self.current_token().type != 'EOF':
                if self.current_token().type == 'IDENTIFIER':
                    params.append(self.consume('IDENTIFIER').value)
                if self.current_token().type == 'COMMA':
                    self.consume('COMMA')
            self.consume('RPAREN')
        class_name = ""
        if self.current_token().type == 'CLASS':
            self.consume('CLASS')
            class_name = self.consume('IDENTIFIER').value
        body = []
        while self.current_token().type not in ('EOF', 'USER', 'FUNCTION', 'METHOD'):
            body.append(self.parse_statement())
        return MethodDeclaration(name, class_name, params, body)
