#!/bin/bash
# Script para fetch local de dados SISCAN

set -e

echo "🔄 Fetching SISCAN data locally..."
echo ""

cd "$(dirname "$0")"

# Rodar script R
Rscript fetch_siscan.R

echo ""
echo "✅ Dados atualizados!"
echo ""
echo "Próximo passo (opcional):"
echo "  git add data/siscan_*.json"
echo "  git commit -m 'data: update SISCAN'"
echo "  git push"
