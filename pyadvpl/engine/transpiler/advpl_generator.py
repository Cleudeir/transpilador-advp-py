from .parser import (
    ASTNode, Program, FunctionDeclaration, VariableDeclaration, Literal, 
    RawNode, CommentNode, IfStatement, WhileLoop, FunctionCall, 
    BinaryExpression, ArrayLiteral, ArrayAccess, PreprocessorNode,
    ForLoop, MethodCall, AliasAccess, AssignmentExpression, UnaryExpression,
    ClassDeclaration, MethodDeclaration, TryStatement
)

class ADVPLGenerator:
    def __init__(self, ast: Program):
        self.ast = ast
        self.indent_level = 0
        self.known_aliases = set()

    def generate(self) -> str:
        return self._generate_node(self.ast)

    def _indent(self) -> str:
        return "    " * self.indent_level

    def _generate_node(self, node: ASTNode) -> str:
        if node is None:
            return ""

        if isinstance(node, Program):
            return "\n".join(self._generate_node(stmt) for stmt in node.statements if stmt)
        
        elif isinstance(node, FunctionDeclaration):
            name = node.name
            if node.is_user:
                prefix = "USER FUNCTION"
            elif node.is_static:
                prefix = "STATIC FUNCTION"
            else:
                prefix = "FUNCTION"
            
            params_str = f"({', '.join(node.params)})" if node.params else "()"
            result = f"{prefix} {name}{params_str}\n"
            self.indent_level += 1
            
            # Local variable declarations
            locals_ = []
            def find_locals(nodes):
                for n in nodes:
                    if isinstance(n, (AssignmentExpression, VariableDeclaration)):
                        target = n.target if isinstance(n, AssignmentExpression) else n.name
                        if isinstance(target, Literal) and target.type == "VARIABLE":
                            v = target.value
                            if v not in locals_: locals_.append(v)
                        elif isinstance(target, str):
                            if target not in locals_: locals_.append(target)
                    if hasattr(n, 'body') and isinstance(n.body, list): find_locals(n.body)
                    if hasattr(n, 'then_body') and isinstance(n.then_body, list): find_locals(n.then_body)
                    if hasattr(n, 'else_body') and isinstance(n.else_body, list): find_locals(n.else_body)
            
            find_locals(node.body)
            params_set = set(node.params) if node.params else set()
            locals_ = [l for l in locals_ if l.upper() not in params_set and l.upper() not in ("SELF", "NIL")]
            
            if locals_:
                result += f"{self._indent()}LOCAL {', '.join(locals_)}\n\n"

            if not node.body:
                result += f"{self._indent()}RETURN Nil\n"
            else:
                for stmt in node.body:
                    res = self._generate_node(stmt)
                    if res:
                        result += f"{self._indent()}{res}\n"
                if not any(isinstance(s, FunctionCall) and s.name == "RETURN" for s in node.body):
                    result += f"{self._indent()}RETURN Nil\n"
            self.indent_level -= 1
            return result
        
        elif isinstance(node, ClassDeclaration):
            result = f"CLASS {node.name}\n"
            self.indent_level += 1
            
            for data in node.data:
                result += f"{self._indent()}DATA {data}\n"
            
            if node.data:
                result += "\n"
                
            for method in node.methods:
                result += f"{self._indent()}METHOD {method}()\n"
                
            self.indent_level -= 1
            result += "ENDCLASS\n"
            return result
        
        elif isinstance(node, MethodDeclaration):
            params_str = f"({', '.join(node.params)})" if node.params else "()"
            result = f"METHOD {node.name}{params_str} CLASS {node.class_name}\n"
            self.indent_level += 1
            
            locals_ = []
            def find_locals(nodes):
                for n in nodes:
                    if isinstance(n, (AssignmentExpression, VariableDeclaration)):
                        target = n.target if isinstance(n, AssignmentExpression) else n.name
                        if isinstance(target, Literal) and target.type == "VARIABLE":
                            v = target.value
                            if v not in locals_: locals_.append(v)
                        elif isinstance(target, str):
                            if target not in locals_: locals_.append(target)
                    if hasattr(n, 'body') and isinstance(n.body, list): find_locals(n.body)
                    if hasattr(n, 'then_body') and isinstance(n.then_body, list): find_locals(n.then_body)
                    if hasattr(n, 'else_body') and isinstance(n.else_body, list): find_locals(n.else_body)
            
            find_locals(node.body)
            params_set = set(node.params) if node.params else set()
            locals_ = [l for l in locals_ if l.upper() not in params_set and l.upper() not in ("SELF", "NIL")]
            
            if locals_:
                result += f"{self._indent()}LOCAL {', '.join(locals_)}\n\n"
            
            if not node.body:
                if node.name == "New":
                    result += f"{self._indent()}RETURN self\n"
                else:
                    result += f"{self._indent()}RETURN Nil\n"
            else:
                for stmt in node.body:
                    res = self._generate_node(stmt)
                    if res:
                        result += f"{self._indent()}{res}\n"
                
                has_return = any(isinstance(s, FunctionCall) and s.name == "RETURN" for s in node.body)
                if not has_return:
                    if node.name == "New":
                        result += f"{self._indent()}RETURN self\n"
                    else:
                        result += f"{self._indent()}RETURN Nil\n"
            
            self.indent_level -= 1
            return result
        
        elif isinstance(node, VariableDeclaration):
            val_str = self._generate_node(node.value)
            return f"{node.name} {node.operator} {val_str}"
            
        elif isinstance(node, AssignmentExpression):
            target = self._generate_node(node.target)
            value = self._generate_node(node.value)
            if node.operator in ("+=", "-=", "*=", "/="): return f"{target} {node.operator} {value}"
            return f"{target} {node.operator} {value}"

        elif isinstance(node, Literal):
            if node.type == "STRING": return f'"{node.value}"'
            if node.type == "BOOLEAN": return node.value
            if node.type == "NONE" or node.value == "Nil": return "Nil"
            return str(node.value)
            
        elif isinstance(node, IfStatement):
            result = f"If {self._generate_node(node.condition)}\n"
            self.indent_level += 1
            for stmt in node.then_body:
                res = self._generate_node(stmt)
                if res: result += f"{self._indent()}{res}\n"
            self.indent_level -= 1
            
            curr_else = node.else_body
            while curr_else and len(curr_else) == 1 and isinstance(curr_else[0], IfStatement):
                elseif_node = curr_else[0]
                result += f"{self._indent()}ElseIf {self._generate_node(elseif_node.condition)}\n"
                self.indent_level += 1
                for stmt in elseif_node.then_body:
                    res = self._generate_node(stmt)
                    if res: result += f"{self._indent()}{res}\n"
                self.indent_level -= 1
                curr_else = elseif_node.else_body
            
            if curr_else:
                result += f"{self._indent()}Else\n"
                self.indent_level += 1
                for stmt in curr_else:
                    res = self._generate_node(stmt)
                    if res: result += f"{self._indent()}{res}\n"
                self.indent_level -= 1
            
            result += f"{self._indent()}EndIf"
            return result

        elif isinstance(node, TryStatement):
            result = "BEGIN SEQUENCE\n"
            self.indent_level += 1
            for stmt in node.body:
                res = self._generate_node(stmt)
                if res: result += f"{self._indent()}{res}\n"
            self.indent_level -= 1
            
            if node.recover_body:
                recover_str = "RECOVER"
                if node.error_var:
                    recover_str += f" USING {node.error_var}"
                result += f"{self._indent()}{recover_str}\n"
                self.indent_level += 1
                for stmt in node.recover_body:
                    res = self._generate_node(stmt)
                    if res: result += f"{self._indent()}{res}\n"
                self.indent_level -= 1
                
            result += f"{self._indent()}END SEQUENCE"
            return result

        elif isinstance(node, WhileLoop):
            result = f"While {self._generate_node(node.condition)}\n"
            self.indent_level += 1
            for stmt in node.body:
                res = self._generate_node(stmt)
                if res: result += f"{self._indent()}{res}\n"
            self.indent_level -= 1
            result += f"{self._indent()}EndDo"
            return result

        elif isinstance(node, ForLoop):
            result = f"For {node.variable} := {self._generate_node(node.start)} To {self._generate_node(node.end)}\n"
            self.indent_level += 1
            for stmt in node.body:
                res = self._generate_node(stmt)
                if res: result += f"{self._indent()}{res}\n"
            self.indent_level -= 1
            result += f"{self._indent()}Next"
            return result

        elif isinstance(node, FunctionCall):
            name = node.name
            if name == "RETURN":
                if not node.args: return "RETURN"
                arg = self._generate_node(node.args[0])
                if arg == "Nil": return "RETURN"
                return f"RETURN {arg}"
            args_str = ", ".join(self._generate_node(arg) for arg in node.args)
            return f"{name}({args_str})"

        elif isinstance(node, MethodCall):
            obj = self._generate_node(node.object)
            method = node.method.lower()
            args_str = ", ".join(self._generate_node(arg) for arg in node.args)
            
            # Map Table methods to Db functions
            mapping = {
                "go_top": "DbGoTop", "go_bottom": "DbGoBottom",
                "skip": "DbSkip", "seek": "DbSeek", "eof": "DbEof",
                "bof": "DbBof", "rec_lock": "RecLock", "unlock": "MsUnlock"
            }
            db_func = mapping.get(method)
            if db_func:
                return f"{obj}->( {db_func}({args_str}) )"
            
            if obj.upper() == "SELF": return f"::{node.method}({args_str})"
            return f"{obj}:{node.method}({args_str})"

        elif isinstance(node, AliasAccess):
            alias = self._generate_node(node.alias)
            field = self._generate_node(node.field)
            if alias.upper() == "SELF": return f"::{field}"
            if isinstance(node.field, FunctionCall):
                return f"{alias}->( {field} )"
            return f"{alias}->{field}"

        elif isinstance(node, BinaryExpression):
            op = node.operator
            mapping = {"in": "$", "and": ".AND.", "or": ".OR.", "==": "=", "!=": "<>"}
            op = mapping.get(op.lower(), op)
            return f"{self._generate_node(node.left)} {op} {self._generate_node(node.right)}"

        elif isinstance(node, UnaryExpression):
            op = node.operator
            if op == "!": op = ".NOT."
            return f"{op} {self._generate_node(node.operand)}"

        elif isinstance(node, ArrayLiteral):
            elements = [self._generate_node(e) for e in node.elements]
            return f"{{ {', '.join(elements)} }}"

        elif isinstance(node, ArrayAccess):
            indices = "".join(f"[{self._generate_node(idx)}]" for idx in node.indices)
            return f"{self._generate_node(node.array)}{indices}"

        elif isinstance(node, CommentNode):
            content = node.content.strip()
            if node.is_block: return f"/* {content} */"
            return f"// {content}"

        elif isinstance(node, RawNode):
            return " ".join(t.value for t in node.tokens)

        elif isinstance(node, PreprocessorNode):
            return node.content if node.content.startswith("#") else f"#{node.content}"
            
        return ""
