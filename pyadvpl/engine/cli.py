import argparse
import hashlib
import json
import os
import sys
import shutil
import tomllib  # Para ler pyadvpl.toml (Python 3.11+)
from pathlib import Path

CACHE_FILE = ".pyadvpl_cache.json"

from dotenv import load_dotenv

# Carrega .env a partir do diretório de trabalho atual (projeto do usuário)
# ou do diretório raiz do framework como fallback
_cwd_env = Path.cwd() / ".env"
_pkg_env = Path(__file__).parent.parent.parent / ".env"
load_dotenv(dotenv_path=_cwd_env if _cwd_env.exists() else _pkg_env)

API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = int(os.getenv("API_PORT", "8040"))
LOG_LEVEL = os.getenv("LOG_LEVEL", "info")

# Tentativa de importar os módulos do transpilador core
try:
    from .transpiler.python_to_ast import PythonToAST
    from .transpiler.advpl_generator import ADVPLGenerator
    from .transpiler.lexer import Lexer
    from .transpiler.parser import ADVPLParser
    from .transpiler.python_generator import PythonGenerator
except ImportError:
    # Fallback para execução direta no repositório
    # (script executado diretamente -> __package__=None -> imports relativos falham)
    # Adiciona a raiz do projeto e usa imports ABSOLUTOS.
    sys.path.append(str(Path(__file__).parent.parent.parent))
    try:
        from pyadvpl.engine.transpiler.python_to_ast import PythonToAST
        from pyadvpl.engine.transpiler.advpl_generator import ADVPLGenerator
        from pyadvpl.engine.transpiler.lexer import Lexer
        from pyadvpl.engine.transpiler.parser import ADVPLParser
        from pyadvpl.engine.transpiler.python_generator import PythonGenerator
    except ImportError:
        print("Erro: Não foi possível carregar os módulos do pyadvpl.")
        sys.exit(1)

def load_config():
    """Lê o arquivo pyadvpl.toml se existir."""
    config_path = Path("pyadvpl.toml")
    if config_path.exists():
        try:
            with open(config_path, "rb") as f:
                return tomllib.load(f)
        except Exception:
            pass
    return {}

def cmd_init(args):
    """Inicializa um novo projeto pyadvpl a partir do template."""
    project_path = Path(args.name)
    if project_path.exists():
        print(f"Erro: O diretório {args.name} já existe.")
        return

    # Caminho do template
    template_name = "project"
    base_path = Path(__file__).parent.parent
    template_path = base_path / template_name

    if template_path.exists():
        print(f"Inicializando projeto {args.name}...")
        shutil.copytree(template_path, project_path)
        
        # Ajusta o nome no arquivo de configuração se existir
        config_file = project_path / "pyadvpl.toml"
        if config_file.exists():
            with open(config_file, "r") as f:
                content = f.read()
            content = content.replace('name = "projeto"', f'name = "{args.name}"')
            with open(config_file, "w") as f:
                f.write(content)
        
        # Remove pasta 'exemplo' se existir no template
        exemplo_path = project_path / "exemplo"
        if exemplo_path.exists():
            shutil.rmtree(exemplo_path)
    else:
        print(f"Criando estrutura básica para {args.name}...")
        project_path.mkdir()
        (project_path / "src").mkdir()
        (project_path / "dist").mkdir()
        (project_path / "legacy").mkdir()
        
        with open(project_path / "pyadvpl.toml", "w") as f:
            f.write(f'[project]\nname = "{args.name}"\n\n[transpile]\ninput_dir = "src"\noutput_dir = "dist"\n')

        with open(project_path / "src" / "main.py", "w") as f:
            f.write('from pyadvpl import ui\n\ndef u_Main():\n    ui.MsgAlert("Novo Projeto!")\n')

    print(f"Sucesso! 'cd {args.name}' e comece a desenvolver.")

def cmd_build(args):
    """Atalho para Python -> ADVPL."""
    config = load_config()
    input_path = Path(args.input or config.get("transpile", {}).get("input_dir", "src"))
    output_path = Path(args.output or config.get("transpile", {}).get("output_dir", "dist"))
    
    print(f"🔨 Building: {input_path} -> {output_path}")
    process_transpile(input_path, output_path, "py2adv", incremental=args.incremental)

def cmd_convert(args):
    """Atalho para ADVPL -> Python."""
    input_path = Path(args.input or "legacy")
    output_path = Path(args.output or "src")
    
    print(f"📂 Converting legacy: {input_path} -> {output_path}")
    process_transpile(input_path, output_path, "adv2py")

def file_hash(path: Path) -> str:
    """Calcula o hash SHA-256 do conteúdo de um arquivo."""
    sha256 = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def load_cache(cache_path: Path) -> dict:
    """Carrega o cache de hashes das fontes transpiladas."""
    if cache_path.exists():
        with open(cache_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_cache(cache_path: Path, cache: dict) -> None:
    """Persiste o cache de hashes das fontes transpiladas."""
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)


def process_transpile(input_path, output_path, direction, incremental=False):
    input_ext = ".prw" if direction == "adv2py" else ".py"
    output_ext = ".py" if direction == "adv2py" else ".prw"
    use_cache = direction == "py2adv"

    if input_path.is_dir():
        output_path.mkdir(parents=True, exist_ok=True)
        cache_path = output_path / CACHE_FILE
        cache = load_cache(cache_path) if use_cache else {}
        seen = []
        for file in input_path.glob(f"**/*{input_ext}"):
            if file.name == "__init__.py": continue
            relative_path = file.relative_to(input_path)
            target_file = output_path / relative_path.with_suffix(output_ext)
            target_file.parent.mkdir(parents=True, exist_ok=True)
            key = str(relative_path)
            seen.append(key)
            current_hash = file_hash(file)
            if incremental and cache.get(key) == current_hash and target_file.exists():
                print(f"⏭️  Inalterado, pulando: {relative_path}")
                continue
            if transpile_file(file, target_file, direction):
                if use_cache:
                    cache[key] = current_hash

        if use_cache:
            # Remove entradas de fontes que não existem mais
            for key in [k for k in cache if k not in seen]:
                del cache[key]
            save_cache(cache_path, cache)
    else:
        if not output_path.suffix:
            output_path = output_path / input_path.with_suffix(output_ext).name
        output_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path = output_path.parent / CACHE_FILE
        cache = load_cache(cache_path) if use_cache else {}
        key = str(input_path)
        current_hash = file_hash(input_path)
        if incremental and cache.get(key) == current_hash and output_path.exists():
            print(f"⏭️  Inalterado, pulando: {input_path}")
        elif transpile_file(input_path, output_path, direction):
            if use_cache:
                cache[key] = current_hash
                save_cache(cache_path, cache)

def transpile_file(input_file, output_file, direction):
    try:
        with open(input_file, 'r', encoding='utf-8' if direction == "py2adv" else 'latin-1') as f:
            code = f.read()

        if direction == "py2adv":
            parser = PythonToAST(code)
            ast_obj = parser.parse()
            output_code = ADVPLGenerator(ast_obj).generate()
            output_code = "#Include 'Protheus.ch'\n\n" + output_code
        else:
            lexer = Lexer(code)
            parser = ADVPLParser(lexer.tokenize())
            output_code = PythonGenerator(parser.parse()).generate()

        with open(output_file, 'w', encoding='utf-8' if direction == "adv2py" else 'latin-1') as f:
            f.write(output_code)
        return True
    except Exception as e:
        print(f"Erro em {input_file}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="pyadvpl CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("init", help="Inicia projeto").add_argument("name")
    
    build = subparsers.add_parser("build", help="Python -> ADVPL")
    build.add_argument("input", nargs="?", help="Entrada (padrão: src/)")
    build.add_argument("-o", "--output", help="Saída (padrão: dist/)")
    build.add_argument("--incremental", action="store_true", help="Recompila apenas fontes modificadas desde o último build (cache por hash)")

    convert = subparsers.add_parser("convert", help="ADVPL -> Python")
    convert.add_argument("input", nargs="?", help="Entrada (padrão: legacy/)")
    convert.add_argument("-o", "--output", help="Saída (padrão: src/)")

    subparsers.add_parser("dev", help="Inicia Dashboard")
    
    # Manter transpile para compatibilidade
    trans = subparsers.add_parser("transpile", help="Transpile (legacy)")
    trans.add_argument("input")
    trans.add_argument("-o", "--output")
    trans.add_argument("-d", "--direction", default="py2adv")

    subparsers.add_parser("test", help="Roda a suíte de testes (CLI + round-trip)")

    args = parser.parse_args()

    if args.command == "init": cmd_init(args)
    elif args.command == "build": cmd_build(args)
    elif args.command == "convert": cmd_convert(args)
    elif args.command == "test": cmd_test(args)
    elif args.command == "dev" or args.command == "serve":
        import uvicorn
        from .server import app
        uvicorn.run(app, host=API_HOST, port=API_PORT, log_level=LOG_LEVEL.lower())
    elif args.command == "transpile":
        process_transpile(Path(args.input), Path(args.output) if args.output else Path("dist"), args.direction)
    else:
        parser.print_help()

def cmd_test(args):

    # Roda a suíte de testes (CLI incremental + round-trip) e imprime resumo.
    import subprocess
    import os
    import sys
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    root = project_root
    # 1) unitários do CLI
    print("# Suíte de testes pyadvpl")
    p_cli = subprocess.run(
        [sys.executable, "-m", "pytest", "pyadvpl/engine/tests/", "-q"],
        cwd=root, capture_output=True, text=True,
    )
    print(p_cli.stdout.strip())
    if p_cli.returncode != 0:
        print(p_cli.stderr.strip())
    # 2) round-trip bulk
    p_bulk = subprocess.run(
        [sys.executable, "-m", "pyadvpl.engine.transpiler.tests.test_roundtrip_bulk"],
        cwd=root, capture_output=True, text=True,
    )
    print("# Round-trip bulk")
    print(p_bulk.stdout.strip())
    if p_bulk.returncode != 0:
        print(p_bulk.stderr.strip())
    if p_cli.returncode != 0 or p_bulk.returncode != 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
