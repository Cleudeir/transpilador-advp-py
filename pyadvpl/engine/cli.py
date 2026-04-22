import argparse
import os
import sys
import shutil
import tomllib  # Para ler pyadvpl.toml (Python 3.11+)
from pathlib import Path

# Tentativa de importar os módulos do transpilador core
try:
    from .transpiler.python_to_ast import PythonToAST
    from .transpiler.advpl_generator import ADVPLGenerator
    from .transpiler.lexer import Lexer
    from .transpiler.parser import ADVPLParser
    from .transpiler.python_generator import PythonGenerator
except ImportError:
    # Fallback para execução direta no repositório
    sys.path.append(str(Path(__file__).parent.parent.parent))
    try:
        from .transpiler.python_to_ast import PythonToAST
        from .transpiler.advpl_generator import ADVPLGenerator
        from .transpiler.lexer import Lexer
        from .transpiler.parser import ADVPLParser
        from .transpiler.python_generator import PythonGenerator
    except ImportError:
        print("Erro: Não foi possível carregar os módulos do pyadvpl.")

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
    process_transpile(input_path, output_path, "py2adv")

def cmd_convert(args):
    """Atalho para ADVPL -> Python."""
    input_path = Path(args.input or "legacy")
    output_path = Path(args.output or "src")
    
    print(f"📂 Converting legacy: {input_path} -> {output_path}")
    process_transpile(input_path, output_path, "adv2py")

def process_transpile(input_path, output_path, direction):
    input_ext = ".prw" if direction == "adv2py" else ".py"
    output_ext = ".py" if direction == "adv2py" else ".prw"

    if input_path.is_dir():
        output_path.mkdir(parents=True, exist_ok=True)
        for file in input_path.glob(f"**/*{input_ext}"):
            if file.name == "__init__.py": continue
            relative_path = file.relative_to(input_path)
            target_file = output_path / relative_path.with_suffix(output_ext)
            target_file.parent.mkdir(parents=True, exist_ok=True)
            transpile_file(file, target_file, direction)
    else:
        if not output_path.suffix:
            output_path = output_path / input_path.with_suffix(output_ext).name
        transpile_file(input_path, output_path, direction)

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
    except Exception as e:
        print(f"Erro em {input_file}: {e}")

def main():
    parser = argparse.ArgumentParser(description="pyadvpl CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("init", help="Inicia projeto").add_argument("name")
    
    build = subparsers.add_parser("build", help="Python -> ADVPL")
    build.add_argument("input", nargs="?", help="Entrada (padrão: src/)")
    build.add_argument("-o", "--output", help="Saída (padrão: dist/)")

    convert = subparsers.add_parser("convert", help="ADVPL -> Python")
    convert.add_argument("input", nargs="?", help="Entrada (padrão: legacy/)")
    convert.add_argument("-o", "--output", help="Saída (padrão: src/)")

    subparsers.add_parser("dev", help="Inicia Dashboard")
    
    # Manter transpile para compatibilidade
    trans = subparsers.add_parser("transpile", help="Transpile (legacy)")
    trans.add_argument("input")
    trans.add_argument("-o", "--output")
    trans.add_argument("-d", "--direction", default="py2adv")

    args = parser.parse_args()

    if args.command == "init": cmd_init(args)
    elif args.command == "build": cmd_build(args)
    elif args.command == "convert": cmd_convert(args)
    elif args.command == "dev" or args.command == "serve":
        import uvicorn
        from .server import app
        uvicorn.run(app, host="0.0.0.0", port=8040)
    elif args.command == "transpile":
        process_transpile(Path(args.input), Path(args.output) if args.output else Path("dist"), args.direction)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
