#!/bin/bash
# Script para rodar os testes round-trip em lote (Bulk Round-trip Tests)

echo "Iniciando testes de transpiração round-trip (ADVPL -> Python -> ADVPL)..."
python3 -m pyadvpl.engine.transpiler.tests.test_roundtrip_bulk
