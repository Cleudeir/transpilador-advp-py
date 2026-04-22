import argparse
import os
import sys
import shutil
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
    except ImportError:
        print("Erro: Não foi possível carregar os módulos do pyadvpl. Certifique-se de que o pacote está instalado.")

def cmd_init(args):
    """Inicializa um novo projeto pyadvpl a partir do template."""
    project_path = Path(args.name)
    if project_path.exists():
        print(f"Erro: O diretório {args.name} já existe.")
        return

    # Caminho do template
    template_name = "projeto_exemplo"
    base_path = Path(__file__).parent
    template_path = base_path / "templates" / template_name

    if template_path.exists():
        print(f"Inicializando projeto {args.name} a partir do template {template_name}...")
        shutil.copytree(template_path, project_path)
        
        # Ajusta o nome no arquivo de configuração se existir
        config_file = project_path / "pyadvpl.toml"
        if config_file.exists():
            with open(config_file, "r") as f:
                content = f.read()
            content = content.replace('name = "projeto_exemplo"', f'name = "{args.name}"')
            with open(config_file, "w") as f:
                f.write(content)
    else:
        # Fallback caso o template não seja encontrado
        print(f"Aviso: Template não encontrado em {template_path}. Criando estrutura básica...")
        project_path.mkdir()
        (project_path / "src").mkdir()
        (project_path / "dist").mkdir()
        (project_path / "tests").mkdir()
        
        with open(project_path / "pyadvpl.toml", "w") as f:
            f.write(f'[project]\nname = "{args.name}"\nauthor = "Dev"\nprotheus_version = "12.1.2310"\n\n[transpile]\ninput_dir = "src"\noutput_dir = "dist"\ninclude_header = true\nheader = "#Include \'Protheus.ch\'"\n')

        with open(project_path / "src" / "main.py", "w") as f:
            f.write('from pyadvpl.engine import ui\n\ndef u_HelloWorld():\n    ui.MsgAlert("Olá do Python Transpilado!")\n    return None\n')

    print(f"Projeto {args.name} inicializado com sucesso.")

def cmd_transpile(args):
    """Transpila arquivos .py para .prw."""
    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else None

    if input_path.is_dir():
        # Transpilar diretório
        if not output_path:
            output_path = input_path.parent / "dist"
        output_path.mkdir(parents=True, exist_ok=True)
        
        for py_file in input_path.glob("**/*.py"):
            if py_file.name == "__init__.py": continue
            
            relative_path = py_file.relative_to(input_path)
            target_file = output_path / relative_path.with_suffix(".prw")
            target_file.parent.mkdir(parents=True, exist_ok=True)
            
            print(f"Transpilando {py_file} -> {target_file}")
            transpile_file(py_file, target_file)
    else:
        # Transpilar arquivo único
        if not output_path:
            output_path = input_path.with_suffix(".prw")
        
        print(f"Transpilando {input_path} -> {output_path}")
        transpile_file(input_path, output_path)

def transpile_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            code = f.read()

        # Python to ADVPL
        parser = PythonToAST(code)
        ast_obj = parser.parse()
        generator = ADVPLGenerator(ast_obj)
        output_code = generator.generate()

        # Add Header
        header = "#Include 'Protheus.ch'\n\n"
        with open(output_file, 'w', encoding='latin-1') as f:
            f.write(header + output_code)
    except Exception as e:
        print(f"Erro ao transpilar {input_file}: {e}")

def main():
    parser = argparse.ArgumentParser(description="pyadvpl CLI — Python para Protheus")
    subparsers = parser.add_subparsers(dest="command")

    # Command: init
    init_parser = subparsers.add_parser("init", help="Inicializa um novo projeto pyadvpl")
    init_parser.add_argument("name", help="Nome do projeto")

    # Command: transpile
    trans_parser = subparsers.add_parser("transpile", help="Transpila Python para ADVPL")
    trans_parser.add_argument("input", help="Arquivo .py ou diretório de entrada")
    trans_parser.add_argument("-o", "--output", help="Arquivo .prw ou diretório de saída")

    # Command: serve
    serve_parser = subparsers.add_parser("serve", help="Inicia o servidor de API para o dashboard web")
    serve_parser.add_argument("--host", default="0.0.0.0", help="Host do servidor")
    serve_parser.add_argument("--port", type=int, default=8040, help="Porta do servidor")

    args = parser.parse_args()

    if args.command == "init":
        cmd_init(args)
    elif args.command == "transpile":
        cmd_transpile(args)
    elif args.command == "serve":
        import uvicorn
        from .server import app
        uvicorn.run(app, host=args.host, port=args.port)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
