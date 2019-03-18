#!/bin/bash

echo "Executando teste"

coverage run -m pytest test/test_core.py

echo "Relatorio de cobertura"

coverage report -m