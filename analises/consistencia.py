#!/usr/bin/env python3
"""Caça a artefatos no painel: zeros, saltos, repetições, somas e denominador."""
import csv
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from collections import defaultdict
from statistics import mean, pstdev

painel = defaultdict(dict)   # (serie, cod) -> {mes: exames}
pop = {}
nomes = {}
defasadas = 0
total_celulas = 0

with open(RAIZ + '/data/painel_ccu_pe.csv') as fh:
    for r in csv.DictReader(fh):
        total_celulas += 1
        if r['valido'] != 'True':
            continue
        k = (r['serie'], r['cod_ibge'])
        painel[k][r['ano_mes']] = painel[k].get(r['ano_mes'], 0) + int(r['exames'] or 0)
        nomes[r['cod_ibge']] = r['municipio']
        if r['pop_defasada'] == 'True':
            defasadas += 1
        if r['serie'] == 'citopatologico' and r['pop_alvo']:
            pop[(r['cod_ibge'], r['ano_mes'][:4], r['faixa'])] = int(r['pop_alvo'])

print(f"células no painel: {total_celulas:,} · com população defasada: {defasadas:,} "
      f"({100*defasadas/total_celulas:.1f}%)")

cito = {c: s for (sr, c), s in painel.items() if sr == 'citopatologico'}
print(f"municípios na série do desfecho: {len(cito)}")

# 1. códigos fora de PE
fora = [c for c in cito if not c.startswith('26')]
print(f"\n1. códigos fora de PE: {fora or 'nenhum'}")

# 2. zeros
print("\n2. ZEROS")
zeros_por_mun = {c: sum(1 for v in s.values() if v == 0) for c, s in cito.items()}
n_meses = len(next(iter(cito.values())))
tot_zeros = sum(zeros_por_mun.values())
print(f"   município-mês com zero: {tot_zeros:,} de {len(cito)*n_meses:,} "
      f"({100*tot_zeros/(len(cito)*n_meses):.1f}%)")
piores = sorted(zeros_por_mun.items(), key=lambda x: -x[1])[:6]
for c, z in piores:
    tot = sum(cito[c].values())
    print(f"   {nomes[c][:26]:28s} {z:3d}/{n_meses} meses zerados · total no período: {tot:,}")

# maior sequência consecutiva de zeros
def maior_seq(serie, meses_ord):
    m = cur = 0
    for k in meses_ord:
        cur = cur + 1 if serie.get(k) == 0 else 0
        m = max(m, cur)
    return m
meses_ord = sorted(next(iter(cito.values())))
seqs = sorted(((maior_seq(s, meses_ord), c) for c, s in cito.items()), reverse=True)[:5]
print("   maiores sequências consecutivas de zero:")
for n, c in seqs:
    print(f"     {nomes[c][:26]:28s} {n} meses seguidos")

# 3. saltos implausíveis
print("\n3. SALTOS acima de 5 desvios-padrão da própria série")
saltos = []
for c, s in cito.items():
    vals = [s.get(m, 0) for m in meses_ord]
    difs = [vals[i] - vals[i-1] for i in range(1, len(vals))]
    if len(difs) < 12:
        continue
    sd = pstdev(difs)
    if sd == 0:
        continue
    for i, dd in enumerate(difs, start=1):
        if abs(dd) > 5 * sd:
            saltos.append((abs(dd)/sd, nomes[c], meses_ord[i], vals[i-1], vals[i]))
saltos.sort(reverse=True)
print(f"   total: {len(saltos)}")
for z, nome, mes, a, b in saltos[:6]:
    print(f"     {nome[:24]:26s} {mes}  {a:,} → {b:,}  ({z:.1f} dp)")

# 4. séries repetidas — o bug do pipeline antigo
print("\n4. REPETIÇÃO SUSPEITA (o bug do pipeline anterior)")
suspeitos = []
for c, s in cito.items():
    vals = [s.get(m, 0) for m in meses_ord if s.get(m, 0) > 0]
    if len(vals) >= 12 and len(set(vals)) <= len(vals) * 0.3:
        suspeitos.append((nomes[c], len(vals), len(set(vals))))
print(f"   municípios com menos de 30% de valores distintos: {len(suspeitos)}")
for nome, n, u in suspeitos[:5]:
    print(f"     {nome[:26]:28s} {n} meses com dado, só {u} valores distintos")

# 5. soma bate com o dashboard?
print("\n5. SOMA CONFERE?")
d = json.load(open(RAIZ + '/data/dashboard.json'))
for i, m in enumerate(d['meses'][:0] + [d['meses'][0], d['meses'][30], d['meses'][-1]]):
    do_painel = sum(s.get(m, 0) for s in cito.values())
    do_dash = d['series']['citopatologico'][d['meses'].index(m)]
    ok = 'ok' if do_painel == (do_dash or 0) else 'DIVERGE'
    print(f"   {m}: painel {do_painel:,} · dashboard {do_dash} · {ok}")

# 6. denominador
print("\n6. DENOMINADOR")
por_mun_ano = defaultdict(int)
for (c, ano, fx), v in pop.items():
    por_mun_ano[(c, ano)] += v
# `pop` é indexado por (município, ano, faixa) e portanto já traz um valor por
# faixa, não um por competência — somar as oito faixas dá a população 25-64 do
# município no ano. Dividir por 12 aqui, como uma versão anterior fazia,
# produzia 225.805 mulheres em todo o estado e um alarme falso de denominador.
p2025 = {c: v for (c, ano), v in por_mun_ano.items() if ano == '2025'}
tot = sum(p2025.values())
print(f"   mulheres 25-64 em PE (2025): {tot:,}")
print(f"   menor município: {min(p2025.values()):,} · maior: {max(p2025.values()):,}")
zerados = [c for c, v in p2025.items() if v == 0]
print(f"   municípios com denominador zero: {zerados or 'nenhum'}")
menores = sorted(p2025.items(), key=lambda x: x[1])[:3]
for c, v in menores:
    print(f"     {nomes[c][:26]:28s} {v:,} mulheres 25-64")
