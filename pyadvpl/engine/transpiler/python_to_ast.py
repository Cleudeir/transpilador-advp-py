import ast
import binascii
from typing import List, Union
from .parser import (
    ASTNode, Program, FunctionDeclaration, VariableDeclaration, Literal, 
    IfStatement, WhileLoop, FunctionCall, BinaryExpression, CommentNode,
    ArrayLiteral, ArrayAccess, MethodCall, AliasAccess, ForLoop, 
    AssignmentExpression, RawNode, CodeBlock, UnaryExpression, PreprocessorNode,
    ClassDeclaration, MethodDeclaration
)

class PythonToAST:
    def __init__(self, python_code: str):
        self.python_code = python_code
        self.tree = ast.parse(self._preserve_comments(python_code))

    def _preserve_comments(self, code: str) -> str:
        lines = code.splitlines()
        for i, line in enumerate(lines):
            stripped = line.lstrip()
            if stripped.startswith('#') and not stripped.startswith('#!'):
                if line.strip() == stripped: # Full line comment
                    indent = line[:len(line) - len(stripped)]
                    comment_text = stripped[1:].strip()
                    encoded = binascii.hexlify(comment_text.encode('utf-8')).decode('ascii')
                    lines[i] = f'{indent}_advpl_comment_("{encoded}")'
        return '\n'.join(lines)

    def parse(self) -> Program:
        statements = []
        for node in self.tree.body:
            translated_node = self._translate_node(node)
            if translated_node:
                if isinstance(translated_node, list):
                    statements.extend(translated_node)
                else:
                    statements.append(translated_node)
        return Program(statements)

    def _translate_node(self, node: ast.AST) -> Union[ASTNode, List[ASTNode], None]:
        if isinstance(node, ast.Assign):
            if len(node.targets) == 1:
                # SPECIAL: x = Table("X") -> ignore
                if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name) and node.value.func.id == "Table":
                    return None
                target = self._translate_expression(node.targets[0])
                value = self._translate_expression(node.value)
                return AssignmentExpression(target, value, ":=")
        
        elif isinstance(node, ast.AugAssign):
            target = self._translate_expression(node.target)
            value = self._translate_expression(node.value)
            op_map = {ast.Add: "+=", ast.Sub: "-=", ast.Mult: "*=", ast.Div: "/="}
            op = op_map.get(type(node.op), ":=")
            return AssignmentExpression(target, value, op)


        elif isinstance(node, ast.FunctionDef):
            body = []
            for stmt in node.body:
                translated = self._translate_node(stmt)
                if translated:
                    if isinstance(translated, list): body.extend(translated)
                    else: body.append(translated)
            params = [arg.arg for arg in node.args.args]
            
            name = node.name
            is_user = False
            is_static = False
            if name.startswith("u_") and len(name) > 2:
                name = name[2:]
                is_user = True
            elif name.startswith("s_") and len(name) > 2:
                name = name[2:]
                is_static = True
            
            return FunctionDeclaration(name, body, params=params, is_user=is_user, is_static=is_static)

        elif isinstance(node, ast.ClassDef):
            class_name = node.name
            data_members = []
            methods = []
            method_decls = []
            
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    method_name = item.name
                    if method_name == "__init__":
                        method_name = "New"
                    
                    methods.append(method_name)
                    
                    # Scan for self.attr assignments
                    for stmt in item.body:
                        if isinstance(stmt, ast.Assign):
                            for target in stmt.targets:
                                if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == "self":
                                    if target.attr not in data_members:
                                        data_members.append(target.attr)
                    
                    params = [arg.arg for arg in item.args.args if arg.arg != "self"]
                    body = []
                    for s in item.body:
                        t = self._translate_node(s)
                        if t:
                            if isinstance(t, list): body.extend(t)
                            else: body.append(t)
                    
                    method_decls.append(MethodDeclaration(method_name, class_name, params, body))
            
            class_decl = ClassDeclaration(class_name, data_members, methods)
            return [class_decl] + method_decls

        elif isinstance(node, ast.If):
            condition = self._translate_expression(node.test)
            then_body = []
            for s in node.body:
                t = self._translate_node(s)
                if t: 
                    if isinstance(t, list): then_body.extend(t)
                    else: then_body.append(t)
            else_body = []
            for s in node.orelse:
                t = self._translate_node(s)
                if t:
                    if isinstance(t, list): else_body.extend(t)
                    else: else_body.append(t)
            return IfStatement(condition, then_body, else_body)

        elif isinstance(node, ast.While):
            condition = self._translate_expression(node.test)
            body = []
            for s in node.body:
                t = self._translate_node(s)
                if t:
                    if isinstance(t, list): body.extend(t)
                    else: body.append(t)
            return WhileLoop(condition, body)

        elif isinstance(node, ast.For):
            if isinstance(node.iter, ast.Call) and isinstance(node.iter.func, ast.Name) and node.iter.func.id == 'range':
                args = node.iter.args
                if len(args) == 1:
                    start = Literal("0", "NUMBER")
                    end = self._translate_expression(args[0])
                elif len(args) >= 2:
                    start = self._translate_expression(args[0])
                    end = self._translate_expression(args[1])
                target_name = node.target.id if isinstance(node.target, ast.Name) else "nI"
                body = []
                for s in node.body:
                    t = self._translate_node(s)
                    if t:
                        if isinstance(t, list): body.extend(t)
                        else: body.append(t)
                return ForLoop(target_name, start, end, body)

        elif isinstance(node, ast.Expr):
            if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name) and node.value.func.id == "_advpl_comment_":
                if node.value.args and isinstance(node.value.args[0], ast.Constant):
                    encoded = node.value.args[0].value
                    try:
                        comment = binascii.unhexlify(encoded).decode('utf-8')
                        if comment.startswith("PREPROCESSOR:"):
                            return PreprocessorNode(comment[13:].strip())
                        return CommentNode(comment, is_block=False)
                    except: pass
                return None
            return self._translate_expression(node.value)

        elif isinstance(node, ast.Return):
            val = self._translate_expression(node.value) if node.value else None
            return FunctionCall("RETURN", [val] if val else [])

        return None

    def _translate_expression(self, expr: ast.AST) -> ASTNode:
        if isinstance(expr, ast.Constant):
            if isinstance(expr.value, str): return Literal(expr.value, "STRING")
            if isinstance(expr.value, bool): return Literal(".T." if expr.value else ".F.", "BOOLEAN")
            if expr.value is None: return Literal("Nil", "NONE")
            return Literal(str(expr.value), "NUMBER")
        elif isinstance(expr, ast.Name):
            return Literal(expr.id, "VARIABLE")
        elif isinstance(expr, ast.Attribute):
            obj = self._translate_expression(expr.value)
            return AliasAccess(obj, Literal(expr.attr, "VARIABLE"))
        elif isinstance(expr, ast.Call):
            args = [self._translate_expression(a) for a in expr.args]
            
            # Handle namespaced calls (e.g., ui.MsgAlert, db.Table)
            func_name = None
            if isinstance(expr.func, ast.Name):
                func_name = expr.func.id
            elif isinstance(expr.func, ast.Attribute):
                # If obj is a known namespace, strip it for global functions
                namespaces = ('ui', 'db', 'protheus', 'math', 'date', 'array', 'string', 'Date', 'Array')
                if isinstance(expr.func.value, ast.Name) and expr.func.value.id in namespaces:
                    func_name = expr.func.attr
                else:
                    obj = self._translate_expression(expr.func.value)
                    return MethodCall(obj, expr.func.attr, args)

            if func_name:
                if func_name == "ref_":
                    return UnaryExpression("@", self._translate_expression(expr.args[0]))
                if func_name == "Table":
                    return Literal(expr.args[0].value, "STRING") if (expr.args and isinstance(expr.args[0], ast.Constant)) else Literal("ALIAS", "VARIABLE")
                if func_name == "today" and isinstance(expr.func, ast.Attribute) and isinstance(expr.func.value, ast.Name) and expr.func.value.id == "Date":
                    return FunctionCall("Date", [])
                if func_name == "print":
                    return FunctionCall("ConOut", args)
                return FunctionCall(func_name, args)
        elif isinstance(expr, ast.Compare):
            left = self._translate_expression(expr.left)
            op_map = {ast.In: "$", ast.Eq: "==", ast.NotEq: "!=", ast.Lt: "<", ast.LtE: "<=", ast.Gt: ">", ast.GtE: ">="}
            op_str = op_map.get(type(expr.ops[0]), "==")
            right = self._translate_expression(expr.comparators[0])
            return BinaryExpression(left, op_str, right)
        elif isinstance(expr, ast.BinOp):
            left = self._translate_expression(expr.left)
            op_map = {ast.Add: "+", ast.Sub: "-", ast.Mult: "*", ast.Div: "/"}
            op_str = op_map.get(type(expr.op), "+")
            right = self._translate_expression(expr.right)
            return BinaryExpression(left, op_str, right)
        elif isinstance(expr, ast.BoolOp):
            left = self._translate_expression(expr.values[0])
            op_str = "and" if isinstance(expr.op, ast.And) else "or"
            right = self._translate_expression(expr.values[1])
            return BinaryExpression(left, op_str, right)
        elif isinstance(expr, ast.UnaryOp):
            op_map = {ast.Not: "!", ast.USub: "-", ast.UAdd: "+"}
            op_str = op_map.get(type(expr.op), "!")
            operand = self._translate_expression(expr.operand)
            return UnaryExpression(op_str, operand)
        elif isinstance(expr, ast.List):
            elements = [self._translate_expression(e) for e in expr.elts]
            return ArrayLiteral(elements)
        elif isinstance(expr, ast.Subscript):
            array = self._translate_expression(expr.value)
            index = self._translate_expression(expr.slice.value if isinstance(expr.slice, ast.Index) else expr.slice)
            return ArrayAccess(array, [index])
        elif isinstance(expr, ast.JoinedStr):
            nodes = [self._translate_expression(v.value) if isinstance(v, ast.FormattedValue) else Literal(v.value, "STRING") for v in expr.values]
            if not nodes: return Literal("", "STRING")
            res = nodes[0]
            for i in range(1, len(nodes)): res = BinaryExpression(res, "+", nodes[i])
            return res
        return Literal("Nil", "NONE")
