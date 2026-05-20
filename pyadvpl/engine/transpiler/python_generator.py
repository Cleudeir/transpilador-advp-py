import keyword
from .parser import ASTNode, Program, FunctionDeclaration, VariableDeclaration, Literal, RawNode, CommentNode, IfStatement, WhileLoop, FunctionCall, BinaryExpression, ArrayLiteral, ArrayAccess, PreprocessorNode, MethodCall, Macro, AliasAccess, MethodDeclaration, UnaryExpression, CodeBlock, MultiVariableDeclaration, DoCase, CaseBranch, LoopControl, AssignmentExpression, TryStatement, TransactionStatement, SQLBlock

class PythonGenerator:
    def __init__(self, ast: Program):
        self.ast = ast
        self.indent_level = 0

    def generate(self) -> str:
        return self._generate_node(self.ast)

    def _indent(self) -> str:
        return "    " * self.indent_level

    def _sanitize(self, name: str) -> str:
        if keyword.iskeyword(name.lower()):
            return f"{name}_"
        return name

    def _generate_node(self, node: ASTNode, is_expr: bool = False) -> str:
        if isinstance(node, Program):
            return "\n".join(self._generate_node(stmt) for stmt in node.statements)
        
        elif isinstance(node, FunctionDeclaration):
            params = [self._sanitize(p) for p in node.params] if node.params else []
            name = node.name
            if node.is_user:
                name = "u_" + name
            elif node.is_static:
                name = "s_" + name
            name = self._sanitize(name)
            result = f"def {name}({', '.join(params)}):\n"
            self.indent_level += 1
            has_body = False
            for stmt in node.body:
                res = self._generate_node(stmt)
                if res and res.strip():
                    result += f"{self._indent()}{res}\n"
                    if not res.strip().startswith("#"):
                        has_body = True
            if not has_body:
                result += f"{self._indent()}pass\n"
            self.indent_level -= 1
            return result
            
        elif isinstance(node, MethodDeclaration):
            params = [self._sanitize(p) for p in node.params] if node.params else []
            name = self._sanitize(node.name)
            class_name = self._sanitize(node.class_name)
            result = f"# Method {node.name} for class {node.class_name}\ndef {class_name}_{name}(self, {', '.join(params)}):\n"
            self.indent_level += 1
            has_body = False
            for stmt in node.body:
                res = self._generate_node(stmt)
                if res and res.strip():
                    result += f"{self._indent()}{res}\n"
                    if not res.strip().startswith("#"):
                        has_body = True
            if not has_body:
                result += f"{self._indent()}pass\n"
            self.indent_level -= 1
            return result
        
        elif isinstance(node, VariableDeclaration):
            val_str = self._generate_node(node.value, is_expr=True)
            op = node.operator
            if op == ":=": op = "="
            name = self._sanitize(node.name.replace(":", "."))
            return f"{name} {op} {val_str}"
            
        elif isinstance(node, AssignmentExpression):
            # Special case for MethodCall as target of assignment (pseudo-property)
            if isinstance(node.target, MethodCall) and not node.target.args:
                target = f"{self._generate_node(node.target.object)}.{node.target.method}"
            elif isinstance(node.target, FunctionCall) and not node.target.args:
                target = node.target.name
            else:
                target = self._generate_node(node.target)
                
            val = self._generate_node(node.value, is_expr=True)
            op = node.operator
            if op == ":=":
                if is_expr:
                    # In Python expression context, use walrus operator if target is a simple variable
                    if isinstance(node.target, Literal) and node.target.type == "VARIABLE":
                        return f"({target} := {val})"
                    # For attributes, we'll use a trick: (setattr(obj, 'attr', val) or val)
                    if "." in target:
                         obj_part, attr_part = target.rsplit('.', 1)
                         return f"(setattr({obj_part}, '{attr_part}', {val}) or {val})"
                    return f"({target} := {val})"
                else:
                    op = "="
            
            if is_expr:
                 if op == "=": 
                    if "." in target:
                        obj_part, attr_part = target.rsplit('.', 1)
                        return f"(setattr({obj_part}, '{attr_part}', {val}) or {val})"
                    return f"({target} := {val})"
                 elif op in ("+=", "-=", "*=", "/=", "%=", "**="):
                    # Convert augmented assignments to walrus in expressions
                    pure_op = op[:-1]
                    if "." in target:
                        obj_part, attr_part = target.rsplit('.', 1)
                        # Slightly complex for attributes: setattr(obj, attr, getattr(obj, attr) + val) or getattr(obj, attr)
                        return f"(setattr({obj_part}, '{attr_part}', getattr({obj_part}, '{attr_part}') {pure_op} {val}) or getattr({obj_part}, '{attr_part}'))"
                    return f"({target} := {target} {pure_op} {val})"
                 return f"({target} {op} {val})" 
            return f"{target} {op} {val}"
            
        elif isinstance(node, MultiVariableDeclaration):
            lines = [self._generate_node(d) for d in node.declarations]
            return ("\n" + self._indent()).join(lines)
            
        elif isinstance(node, Literal):
            if node.type == "NUMBER":
                val = str(node.value)
                if val.startswith('0') and len(val) > 1 and '.' not in val:
                    val = val.lstrip('0') or '0'
                return val
            elif node.type == "STRING":
                val = str(node.value)
                if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                    content = val[1:-1]
                    return repr(content)
                return repr(val)
            elif node.type == "BOOLEAN":
                val = node.value.upper()
                if '.T.' in val or 'TRUE' in val: return 'True'
                return 'False'
            elif node.type in ("VARIABLE", "NONE", "SPECIAL"):
                v = str(node.value)
                vu = v.upper()
                if vu == 'SELF': return 'self'
                if vu == 'TRUE' or v == '.T.': return 'True'
                if vu == 'FALSE' or v == '.F.': return 'False'
                if vu == 'NONE' or vu == 'NIL': return 'None'
                if v == ':=': return '='
                if node.type == "SPECIAL":
                    return f'"{v}"'
                return self._sanitize(v)
            else:
                # Comment out unexpected tokens that might come from unknown commands
                return f"# {node.value}"
            
        elif isinstance(node, IfStatement):
            result = f"if {self._generate_node(node.condition, is_expr=True)}:\n"
            self.indent_level += 1
            has_then = False
            for stmt in node.then_body:
                res = self._generate_node(stmt)
                if res and res.strip():
                    result += f"{self._indent()}{res}\n"
                    if not res.strip().startswith("#"):
                        has_then = True
            if not has_then:
                result += f"{self._indent()}pass\n"
            self.indent_level -= 1
            
            if node.else_body:
                if len(node.else_body) == 1 and isinstance(node.else_body[0], IfStatement):
                    elif_part = self._generate_node(node.else_body[0])
                    # Join with indentation if needed
                    result += f"{self._indent()}elif" + elif_part[2:]
                else:
                    result += f"{self._indent()}else:\n"
                    self.indent_level += 1
                    has_else = False
                    for stmt in node.else_body:
                        res = self._generate_node(stmt)
                        if res and res.strip():
                            result += f"{self._indent()}{res}\n"
                            if not res.strip().startswith("#"):
                                has_else = True
                    if not has_else:
                        result += f"{self._indent()}pass\n"
                    self.indent_level -= 1
            return result

        elif isinstance(node, TryStatement):
            result = "try:\n"
            self.indent_level += 1
            has_body = False
            for stmt in node.body:
                res = self._generate_node(stmt)
                if res and res.strip():
                    result += f"{self._indent()}{res}\n"
                    if not res.strip().startswith("#"):
                        has_body = True
            if not has_body:
                result += f"{self._indent()}pass\n"
            self.indent_level -= 1
            
            result += f"{self._indent()}except Exception"
            if node.error_var:
                result += f" as {self._sanitize(node.error_var)}"
            result += ":\n"
            
            self.indent_level += 1
            has_recover = False
            for stmt in node.recover_body:
                res = self._generate_node(stmt)
                if res and res.strip():
                    result += f"{self._indent()}{res}\n"
                    if not res.strip().startswith("#"):
                        has_recover = True
            if not has_recover:
                result += f"{self._indent()}pass\n"
            self.indent_level -= 1
            
            return result

        elif isinstance(node, TransactionStatement):
            result = "with Transaction():\n"
            self.indent_level += 1
            has_body = False
            for stmt in node.body:
                res = self._generate_node(stmt)
                if res and res.strip():
                    result += f"{self._indent()}{res}\n"
                    if not res.strip().startswith("#"):
                        has_body = True
            if not has_body:
                result += f"{self._indent()}pass\n"
            self.indent_level -= 1
            return result

        elif isinstance(node, SQLBlock):
            result = f"with BeginSQL(alias=\"{node.alias}\") as sql:\n"
            self.indent_level += 1
            
            for col in node.columns:
                col_str = f"sql.column(\"{col.name}\""
                if col.type:
                    col_str += f", \"{col.type}\""
                col_str += ")\n"
                result += f"{self._indent()}{col_str}"
            
            if node.sql_query:
                result += f"{self._indent()}sql.query(\"\"\"{node.sql_query}\"\"\")\n"
            
            if node.body:
                for stmt in node.body:
                    res = self._generate_node(stmt)
                    if res and res.strip():
                        result += f"{self._indent()}{res}\n"
            
            if not node.columns and not node.sql_query and not node.body:
                result += f"{self._indent()}pass\n"
            
            self.indent_level -= 1
            return result

        elif isinstance(node, DoCase):
            result = ""
            for i, case in enumerate(node.cases):
                prefix = "if" if i == 0 else "elif"
                result += f"{prefix} {self._generate_node(case.condition, is_expr=True)}:\n"
                self.indent_level += 1
                has_body = False
                for stmt in case.body:
                    res = self._generate_node(stmt)
                    if res and res.strip():
                        result += f"{self._indent()}{res}\n"
                        if not res.strip().startswith("#"):
                            has_body = True
                if not has_body:
                    result += f"{self._indent()}pass\n"
                self.indent_level -= 1
                result += self._indent()
            if node.otherwise:
                result += "else:\n"
                self.indent_level += 1
                has_body = False
                for stmt in node.otherwise:
                    res = self._generate_node(stmt)
                    if res and res.strip():
                        result += f"{self._indent()}{res}\n"
                        if not res.strip().startswith("#"):
                            has_body = True
                if not has_body:
                    result += f"{self._indent()}pass\n"
                self.indent_level -= 1
            return result.strip()

        elif isinstance(node, WhileLoop):
            result = f"while {self._generate_node(node.condition, is_expr=True)}:\n"
            self.indent_level += 1
            has_body = False
            for stmt in node.body:
                res = self._generate_node(stmt)
                if res and res.strip():
                    result += f"{self._indent()}{res}\n"
                    if not res.strip().startswith("#"):
                        has_body = True
            if not has_body:
                result += f"{self._indent()}pass\n"
            self.indent_level -= 1
            return result

        elif isinstance(node, LoopControl):
            if node.type == 'EXIT': return "break"
            return "continue"

        elif isinstance(node, FunctionCall):
            if node.name.upper() == 'RETURN':
                if not node.args: return "return"
                return f"return {', '.join(self._generate_node(arg, is_expr=True) for arg in node.args)}"
            args_str = ", ".join(self._generate_node(arg, is_expr=True) for arg in node.args)
            name = self._sanitize(node.name)
            if name.upper() == 'IIF':
                # Map Iif to Python ternary if it has 3 args
                if len(node.args) == 3:
                    cond = self._generate_node(node.args[0], is_expr=True)
                    then_val = self._generate_node(node.args[1], is_expr=True)
                    else_val = self._generate_node(node.args[2], is_expr=True)
                    return f"({then_val} if {cond} else {else_val})"
            return f"{name}({args_str})"

        elif isinstance(node, RawNode):
            raw_text = ' '.join(t.value for t in node.tokens)
            if not raw_text.strip(): return ""
            return f"# RAW: {raw_text}"
            
        elif isinstance(node, CommentNode):
            content = node.content
            if node.is_block:
                inner = content
                if inner.startswith('/*/'): inner = inner[3:]
                elif inner.startswith('/*'): inner = inner[2:]
                
                if inner.endswith('/*/'): inner = inner[:-3]
                elif inner.endswith('*/'): inner = inner[:-2]
                
                inner = inner.strip()
                lines = [f"# {l}" for l in inner.splitlines()]
                return ("\n" + self._indent()).join(lines)
            else:
                return f"# {content[2:].strip()}"
            
        elif isinstance(node, BinaryExpression):
            op = node.operator
            if op == "$":
                return f"{self._generate_node(node.left, is_expr=True)} in {self._generate_node(node.right, is_expr=True)}"
            elif op.upper() in (".AND.", "AND"):
                op = "and"
            elif op.upper() in (".OR.", "OR"):
                op = "or"
            elif op == "=":
                op = "=="
            elif op == "<>":
                op = "!="
            elif op == "^":
                op = "**"
            return f"{self._generate_node(node.left, is_expr=True)} {op} {self._generate_node(node.right, is_expr=True)}"

        elif isinstance(node, UnaryExpression):
            op = node.operator
            operand = self._generate_node(node.operand, is_expr=True)
            if op == "@": return f"ref_({operand})"
            if op == "!" or op.upper() in (".NOT.", "NOT"): op = "not "
            elif op == "++" or op == "POST_++":
                 return f"({operand} := {operand} + 1)" if is_expr else f"{operand} += 1"
            elif op == "--" or op == "POST_--":
                 return f"({operand} := {operand} - 1)" if is_expr else f"{operand} -= 1"
            return f"{op}{operand}"

        elif isinstance(node, ArrayLiteral):
            elements = [self._generate_node(e, is_expr=True) for e in node.elements]
            return f"[{', '.join(elements)}]"

        elif isinstance(node, ArrayAccess):
            array_str = self._generate_node(node.array, is_expr=True)
            indices = "".join(f"[{self._generate_node(idx, is_expr=True)}]" for idx in node.indices)
            return f"{array_str}{indices}"

        elif isinstance(node, PreprocessorNode):
            return f"# PREPROCESSOR: {node.content}"
            
        elif isinstance(node, MethodCall):
            args_str = ", ".join(self._generate_node(arg, is_expr=True) for arg in node.args)
            obj_str = self._generate_node(node.object, is_expr=True)
            return f"{obj_str}.{node.method}({args_str})"

        elif isinstance(node, Macro):
            expr = self._generate_node(node.expression, is_expr=True)
            return f"eval({expr})"
            
        elif isinstance(node, AliasAccess):
            alias_str = self._generate_node(node.alias, is_expr=True)
            field_str = self._generate_node(node.field, is_expr=True)
            return f"{alias_str}.{field_str}"

        elif isinstance(node, CodeBlock):
            return f"lambda {', '.join(node.params)}: {self._generate_node(node.expression, is_expr=True)}"

        return ""
