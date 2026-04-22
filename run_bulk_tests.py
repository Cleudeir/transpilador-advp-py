import os
import sys
import subprocess
from pathlib import Path

def main():
    root_dir = Path(__file__).parent
    test_file = root_dir / "pyadvpl" / "engine" / "transpiler" / "tests" / "test_roundtrip_bulk.py"
    
    if not test_file.exists():
        print(f"Erro: Arquivo de teste no encontrado em {test_file}")
        sys.exit(1)
        
    print(f"Executando testes em lote a partir de: {test_file}")
    
    try:
        # Executa como módulo para suportar imports relativos
        subprocess.run([sys.executable, "-m", "pyadvpl.engine.transpiler.tests.test_roundtrip_bulk"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"\nErro durante a execução dos testes: {e}")
        sys.exit(e.returncode)
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
