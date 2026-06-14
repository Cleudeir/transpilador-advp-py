from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from pydantic import BaseModel
from typing import Optional
import logging
import os
from pathlib import Path

from dotenv import load_dotenv

# Carrega .env a partir da raiz do projeto (dois níveis acima de engine/)
_ENV_PATH = Path(__file__).parent.parent.parent / ".env"
load_dotenv(dotenv_path=_ENV_PATH)

API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = int(os.getenv("API_PORT", "8040"))
_raw_origins = os.getenv("ALLOWED_ORIGINS", "*")
ALLOWED_ORIGINS = [o.strip() for o in _raw_origins.split(",")] if _raw_origins != "*" else ["*"]
LOG_LEVEL = os.getenv("LOG_LEVEL", "info").upper()

from .transpiler.python_to_ast import PythonToAST
from .transpiler.advpl_generator import ADVPLGenerator
from .transpiler.lexer import Lexer
from .transpiler.parser import ADVPLParser
from .transpiler.python_generator import PythonGenerator

# Configuração de Logging
logging.basicConfig(level=getattr(logging, LOG_LEVEL, logging.INFO))
logger = logging.getLogger("pyadvpl_api")

app = FastAPI(title="Python-ADVPL Transpiler API", version="0.2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_private_network_access_header(request: Request, call_next):
    """
    Suporte ao Chrome Private Network Access (PNA).
    Requisições de origens públicas (HTTPS) para localhost exigem este header
    na resposta ao preflight OPTIONS para serem permitidas pelo browser.
    """
    if (
        request.method == "OPTIONS"
        and "access-control-request-private-network" in request.headers
    ):
        response = Response(status_code=204)
        response.headers["Access-Control-Allow-Private-Network"] = "true"
        response.headers["Access-Control-Allow-Origin"] = request.headers.get(
            "origin", "*"
        )
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "*"
        return response
    response = await call_next(request)
    response.headers["Access-Control-Allow-Private-Network"] = "true"
    return response


class TranspileRequest(BaseModel):
    code: str
    direction: str  # 'advpl-to-python' ou 'python-to-advpl'


class TranspileResponse(BaseModel):
    success: bool
    output: str
    error: Optional[str] = None


@app.get("/api/health")
async def health():
    return {"status": "ok", "version": "0.2.0"}


@app.post("/api/transpile", response_model=TranspileResponse)
async def transpile(request: TranspileRequest):
    logger.info(f"Recebida requisição de transpiração: {request.direction}")

    try:
        if request.direction == "advpl-to-python":
            # ADVPL -> Python
            lexer = Lexer(request.code)
            tokens = lexer.tokenize()
            parser = ADVPLParser(tokens)
            ast_obj = parser.parse()
            generator = PythonGenerator(ast_obj)
            output = generator.generate()

        elif request.direction == "python-to-advpl":
            # Python -> ADVPL
            parser = PythonToAST(request.code)
            ast_obj = parser.parse()
            generator = ADVPLGenerator(ast_obj)
            output = generator.generate()

        else:
            return TranspileResponse(success=False, output="", error="Direção inválida")

        return TranspileResponse(success=True, output=output)

    except Exception as e:
        logger.error(f"Erro na transpiração: {str(e)}")
        return TranspileResponse(success=False, output="", error=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=API_HOST, port=API_PORT, log_level=LOG_LEVEL.lower())
