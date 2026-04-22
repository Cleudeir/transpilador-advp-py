@echo off
setlocal
echo ============================================================
echo   Limpando diretorios de teste anteriores...
echo ============================================================
if exist pyadvpl\engine\transpiler\tests\output rmdir /s /q pyadvpl\engine\transpiler\tests\output

echo.
echo ============================================================
echo   Iniciando testes de transpiracao round-trip em lote...
echo   (ADVPL -> Python -> ADVPL)
echo ============================================================
python -m pyadvpl.engine.transpiler.tests.test_roundtrip_bulk

echo.
echo Testes concluidos.
pause
