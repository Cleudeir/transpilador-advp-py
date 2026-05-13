import re
from dataclasses import dataclass
from typing import List

@dataclass
class Token:
    type: str
    value: str
    line: int
    column: int

class LexerError(Exception):
    pass

class Lexer:
    TOKEN_SPECIFICATION = [
        ('BLOCK_COMMENT_PROTHEUS', r'/\*/[\s\S]*?/\*/'),     # Protheus doc blocks
        ('BLOCK_COMMENT', r'/\*[\s\S]*?\*/'),              # Standard block comments 
        ('COMMENT',     r'//.*'),                            # Line comments
        ('PREPROCESSOR',r'#.*'),                             # Preprocessor directives
        ('STRING',      r'"[^"\n]*"?|\'[^\'\n]*\'?'),        # String Literal (suporta aspas abertas no fim da linha)
        ('NUMBER',      r'\d+(\.\d*)?'),                     # Integer or decimal number
        ('BOOLEAN',     r'\.[TtFf]\.'),                      # Boolean Literals .T. .F.
        ('LOGIC_OP',    r'\.[Aa][Nn][Dd]\.|\.[Oo][Rr]\.|\.[Nn][Oo][Tt]\.'), # .AND. .OR. .NOT.
        ('DOUBLE_COLON',r'::'),                              # Self reference
        ('ARROW',       r'->'),                              # Alias
        ('POWER',       r'\*\*|\^'),                         # Exponenciacao
        ('ASSIGN_OP',   r'\+=|-=|\*=|/='),                   # Augmented assignment
        ('ASSIGN',      r':='),                              # Assignment
        ('INC_DEC',     r'\+\+|--'),                         # Increment/Decrement
        ('GT_EQ',       r'>='),                              # Greater than or equal
        ('LT_EQ',       r'<='),                              # Less than or equal
        ('EQ',          r'==|='),                            # Equality
        ('NEQ',         r'!=|<>'),                           # Inequality
        ('GT',          r'>'),                               # Greater than
        ('LT',          r'<'),                               # Less than
        ('DOLLAR',      r'\$'),                              # Contains/Cifrao
        ('PLUS',        r'\+'),                              # Addition
        ('MINUS',       r'-'),                               # Subtraction
        ('STAR',        r'\*'),                              # Multiplication
        ('SLASH',       r'/'),                               # Division
        ('LPAREN',      r'\('),                              # Left Parenthesis
        ('RPAREN',      r'\)'),                              # Right Parenthesis
        ('LBRACKET',    r'\['),                              # Left Bracket
        ('RBRACKET',    r'\]'),                              # Right Bracket
        ('LBRACE',      r'\{'),                              # Left Brace
        ('RBRACE',      r'\}'),                              # Right Brace
        ('COMMA',       r','),                               # Comma
        ('DOT',         r'\.'),                              # Dot
        ('COLON',       r':'),                               # Colon (method call)
        ('SEMICOLON',   r';'),                               # Semicolon
        ('AMP',         r'&'),                               # Macro
        ('AT',          r'@'),                               # Pass by reference
        ('PIPE',        r'\|'),                              # Pipe
        ('QUESTION',    r'\?'),                              # Question
        ('BACKSLASH',   r'\\'),                              # Backslash
        ('PERCENT',     r'%'),                               # Percent
        ('NOT',         r'!'),                               # Not
        ('IDENTIFIER',  r'[A-Za-z_\u0080-\uFFFF][A-Za-z0-9_\u0080-\uFFFF]*'),  # Identificadores (suporta Unicode/acentos)
        ('NEWLINE',     r'\n'),                              # Line endings
        ('SKIP',        r'[ \t\r]+'),                        # Skip over spaces and tabs
    ]

    KEYWORDS = {
        'USER': 'USER',
        'FUNCTION': 'FUNCTION',
        'LOCAL': 'LOCAL',
        'RETURN': 'RETURN',
        'IF': 'IF',
        'ENDIF': 'ENDIF',
        'ELSE': 'ELSE',
        'ELSEIF': 'ELSEIF',
        'WHILE': 'WHILE',
        'ENDDO': 'ENDDO',
        'FOR': 'FOR',
        'TO': 'TO',
        'NEXT': 'NEXT',
        'STATIC': 'STATIC',
        'PRIVATE': 'PRIVATE',
        'PUBLIC': 'PUBLIC',
        'METHOD': 'METHOD',
        'CLASS': 'CLASS',
        'EXIT': 'EXIT',
        'CASE': 'CASE',
        'OTHERWISE': 'OTHERWISE',
        'ENDCASE': 'ENDCASE',
        'DO': 'DO',
        'BEGINSQL': 'BEGINSQL',
        'ENDSQL': 'ENDSQL',
        'BEGIN': 'BEGIN',
        'SEQUENCE': 'SEQUENCE',
        'RECOVER': 'RECOVER',
        'ENDSEQUENCE': 'ENDSEQUENCE',
    }

    def __init__(self, code: str):
        # Handle ADVPL statement continuation with ;
        self.code = re.sub(r';\s*(//.*)?\r?\n', ' ', code)
        self.tokens: List[Token] = []
        
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in self.TOKEN_SPECIFICATION)
        self.get_token = re.compile(tok_regex).match

    def tokenize(self) -> List[Token]:
        line_num = 1
        line_start = 0
        pos = 0
        
        while pos < len(self.code):
            mo = self.get_token(self.code, pos)
            if mo is not None:
                kind = mo.lastgroup
                value = mo.group(kind)
                column = mo.start() - line_start
                if kind == 'NEWLINE':
                    line_start = mo.end()
                    line_num += 1
                elif kind == 'SKIP':
                    pass
                elif kind in ('BLOCK_COMMENT', 'BLOCK_COMMENT_PROTHEUS', 'STRING'):
                    self.tokens.append(Token(kind, value, line_num, column))
                    line_num += value.count('\n')
                    if '\n' in value:
                        line_start = mo.start() + value.rfind('\n') + 1
                elif kind == 'IDENTIFIER':
                    kind = self.KEYWORDS.get(value.upper(), 'IDENTIFIER')
                    self.tokens.append(Token(kind, value, line_num, column))
                else:
                    self.tokens.append(Token(kind, value, line_num, column))
                pos = mo.end()
            else:
                raise LexerError('Unexpected character %r at line %d' % (self.code[pos], line_num))
        
        self.tokens.append(Token('EOF', '', line_num, len(self.code) - line_start))
        return self.tokens
