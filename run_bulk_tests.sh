#!/bin/bash
# Script para rodar os testes round-trip em lote (Bulk Round-trip Tests)

echo "============================================================"
echo "  Limpando diretórios de teste anteriores..."
echo "============================================================"
rm -rf pyadvpl/engine/transpiler/tests/output/

echo ""
echo "============================================================"
echo "  Iniciando testes de transpiração round-trip em lote..."
echo "  (ADVPL -> Python -> ADVPL)"
echo "============================================================"
python3 -m pyadvpl.engine.transpiler.tests.test_roundtrip_bulk

echo ""
echo "Testes concluídos."
