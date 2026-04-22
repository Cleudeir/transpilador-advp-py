from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import logging

from .transpiler.python_to_ast import PythonToAST
from .transpiler.advpl_generator import ADVPLGenerator
from .transpiler.lexer import Lexer
from .transpiler.parser import ADVPLParser
from .transpiler.python_generator import PythonGenerator

# Configuração de Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("pyadvpl_api")

app = FastAPI(title="Python-ADVPL Transpiler API", version="0.2.0")

# Habilitar CORS para o frontend (Vite normalmente roda na 5173 ou proximas)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, restringir para os domínios reais
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
        if request.direction == 'advpl-to-python':
            # ADVPL -> Python
            lexer = Lexer(request.code)
            tokens = lexer.tokenize()
            parser = ADVPLParser(tokens)
            ast_obj = parser.parse()
            generator = PythonGenerator(ast_obj)
            output = generator.generate()
            
        elif request.direction == 'python-to-advpl':
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
    uvicorn.run(app, host="0.0.0.0", port=8040)
