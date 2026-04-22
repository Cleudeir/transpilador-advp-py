import re
from difflib import SequenceMatcher

def normalize_advpl(code: str) -> str:
    # 1. Markers
    code = code.replace("// PREPROCESSOR:", "")
    # 2. Comments
    code = re.sub(r'//.*', '', code)
    code = re.sub(r'/\*/[\s\S]*?/\*/', '', code)
    code = re.sub(r'/\*[\s\S]*?\*/', '', code)
    # 3. Uppercase
    code = code.upper()
    # 4. Remove keywords
    for kw in ["LOCAL", "PRIVATE", "PUBLIC", "STATIC", "USER", "FUNCTION", "RETURN", "NIL"]:
        code = re.sub(rf'\b{kw}\b', '', code)
    # 5. Remove delimiters
    code = re.sub(r'[\s\(\);,]+', '', code)
    return code.strip()

file1 = "/root/Documents/Server/projetos/advp-python/pyadvpl/engine/transpiler/tests/input/Exemplo_134_Classe_DBTree.prw"
file2 = "/root/Documents/Server/projetos/advp-python/pyadvpl/engine/transpiler/tests/output/advpl/Exemplo_134_Classe_DBTree.prw"

with open(file1, "r", encoding="latin-1") as f:
    s1 = normalize_advpl(f.read())
with open(file2, "r", encoding="latin-1") as f:
    s2 = normalize_advpl(f.read())

import difflib
diff = difflib.unified_diff(s1.split(), s2.split(), lineterm='')
print('\n'.join(list(diff)[:20]))

precision = SequenceMatcher(None, s1, s2).ratio() * 100
print(f"Precision: {precision:.2f}%")
