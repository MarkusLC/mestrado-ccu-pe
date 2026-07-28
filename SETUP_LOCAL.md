# Setup Local — Fetch Dados SISCAN

## 1. Instalar R (uma vez)

```bash
# Se não tiver R instalado, usar Homebrew
brew install r
```

Verificar:
```bash
R --version
```

## 2. Instalar dependências R (uma vez)

Abra R:
```bash
R
```

Dentro do R:
```r
install.packages(c('jsonlite', 'dplyr', 'tidyr', 'remotes'))
remotes::install_github('rfsaldanha/microdatasus')
q()  # Sair
```

## 3. Rodar fetch (toda vez que quiser dados novos)

```bash
cd /Users/markuscorgosinho/projects/Juliana/mestrado-ccu-pe
Rscript fetch_siscan.R
```

Demora ~2-3 minutos na primeira vez (DATASUS é lento).

## 4. Fazer push dos dados

```bash
git add data/siscan_*.json
git commit -m "data: update SISCAN com dados reais"
git push
```

Dashboard atualiza automaticamente em ~2 minutos! 🎉

---

**Pronto!** Agora você tem dados reais no seu mestrado.
