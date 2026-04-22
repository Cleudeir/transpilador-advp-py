import os
import sys
import time
import re
from pathlib import Path
from difflib import SequenceMatcher

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../")))

from ..lexer import Lexer
from ..parser import ADVPLParser
from ..python_generator import PythonGenerator
from ..python_to_ast import PythonToAST
from ..advpl_generator import ADVPLGenerator

def normalize_advpl(code: str) -> str:
    """Normaliza o código ADVPL para comparação lógica."""
    # 1. Remove markers
    code = code.replace("// PREPROCESSOR:", "")
    
    # 2. Remove comentários
    code = re.sub(r'//.*', '', code)
    code = re.sub(r'/\*/[\s\S]*?/\*/', '', code)
    code = re.sub(r'/\*[\s\S]*?\*/', '', code)
    
    # 3. Normaliza para maiúsculas
    code = code.upper()
    
    # 4. Remove keywords
    for kw in ["LOCAL", "PRIVATE", "PUBLIC", "STATIC", "USER", "FUNCTION", "RETURN", "NIL"]:
        code = re.sub(rf'\b{kw}\b', '', code)
        
    # 5. Remove todos os espaços e separadores comuns
    code = re.sub(r'[\s\(\);,]+', '', code)
    
    # 6. Normaliza números
    code = re.sub(r'([^A-Z0-9_])0+(\d+)', r'\1\2', code)
    
    return code.strip()

def calculate_precision(original: str, converted: str) -> float:
    """Calcula a taxa de precisão entre o original e o reconvertido."""
    s1 = normalize_advpl(original)
    s2 = normalize_advpl(converted)
    if not s1 and not s2: return 100.0
    if not s1 or not s2: return 0.0
    return SequenceMatcher(None, s1, s2).ratio() * 100

def run_roundtrip_bulk():
    script_dir = Path(__file__).parent
    input_path = script_dir / "input"
    output_py_path = script_dir / "output" / "python"
    output_adv_path = script_dir / "output" / "advpl"
    
    output_py_path.mkdir(parents=True, exist_ok=True)
    output_adv_path.mkdir(parents=True, exist_ok=True)

    files = list(input_path.glob("*.prw"))
    total = len(files)
    
    print(f"Iniciando Teste Round-trip: {total} arquivos.")
    print(f"Original: {input_path}")
    print(f"Python:   {output_py_path}")
    print(f"ADVPL Re: {output_adv_path}")
    print("-" * 60)

    results = []
    start_time = time.time()

    for i, file_path in enumerate(files, 1):
        name = file_path.name
        try:
            with open(file_path, "r", encoding="latin-1") as f:
                original_content = f.read()

            # 1. ADVPL -> Python
            lexer = Lexer(original_content)
            parser = ADVPLParser(lexer.tokenize())
            ast_orig = parser.parse()
            python_code = PythonGenerator(ast_orig).generate()
            
            py_file = output_py_path / file_path.with_suffix(".py").name
            with open(py_file, "w", encoding="utf-8") as f:
                f.write(python_code)

            # 2. Python -> ADVPL
            py_to_ast = PythonToAST(python_code)
            ast_back = py_to_ast.parse()
            recon_advpl = ADVPLGenerator(ast_back).generate()
            
            adv_file = output_adv_path / name
            with open(adv_file, "w", encoding="latin-1") as f:
                f.write(recon_advpl)

            # 3. Comparação
            precision = calculate_precision(original_content, recon_advpl)
            results.append({"name": name, "precision": precision, "status": "Success"})
            
            if i % 50 == 0:
                print(f"Progresso: {i}/{total} processados...")

        except Exception as e:
            results.append({"name": name, "precision": 0.0, "status": f"Error: {str(e)}"})

    end_time = time.time()
    duration = end_time - start_time

    # Relatório Final
    successes = [r for r in results if r["status"] == "Success"]
    avg_precision = sum(r["precision"] for r in successes) / len(successes) if successes else 0
    
    print("-" * 60)
    print(f"Concluído em {duration:.2f}s")
    print(f"Sucessos Totais: {len(successes)}/{total}")
    print(f"Taxa de Precisão Média: {avg_precision:.2f}%")
    
    # Salva relatório detalhado
    report_file = script_dir / "output" / "_roundtrip_report.txt"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write("RELATÓRIO DE TESTE ROUND-TRIP (ADVPL -> PY -> ADVPL)\n")
        f.write("=" * 60 + "\n")
        f.write(f"Data: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total de Arquivos: {total}\n")
        f.write(f"Sucessos no Ciclo: {len(successes)}\n")
        f.write(f"Precisão Média: {avg_precision:.2f}%\n")
        f.write("-" * 60 + "\n\n")
        for r in sorted(results, key=lambda x: x['precision']):
            f.write(f"[{r['precision']:6.2f}%] {r['name']} - {r['status']}\n")

    print(f"\nRelatório detalhado salvo em: {report_file}")

if __name__ == "__main__":
    run_roundtrip_bulk()
