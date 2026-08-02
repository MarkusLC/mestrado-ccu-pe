#!/usr/bin/env python3
"""Teste de falsificação: marcos reais contra datas-placebo.

Se datas sem nenhum evento normativo produzirem degraus da mesma magnitude que
os marcos do estudo, o desenho não distingue sinal de ruído. A banca apontou a
ausência deste teste como problema grave.

Comparação descritiva, sem ajustar modelo: média dos 12 meses antes contra os 12
depois, na razão mensal de exames. Competências ausentes e provisórias saem.
"""
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from statistics import mean, pstdev

d = json.load(open(RAIZ + '/data/dashboard.json'))
meses, razao = d['meses'], d['razao_mensal']
corte_prov = d['provisorio_a_partir_de']
idx = {m: i for i, m in enumerate(meses)}

def janela(centro, n=12):
    """Médias dos n meses antes e depois, com as janelas balanceadas por mês.

    Quando a janela pós é truncada — por competência provisória ou por fim de
    série —, comparar 12 meses contra 8 mistura efeito com sazonalidade: os 8
    restantes são de um semestre só. A correção é truncar a janela pré aos
    **mesmos meses do calendário** que sobraram na pós, de modo que as duas
    médias tenham a mesma composição sazonal.

    Sem isso, τ4 aparecia como +3,6% quando o que se media era em boa parte a
    diferença entre um ano inteiro e o segundo semestre.
    """
    if centro not in idx:
        return None
    c = idx[centro]
    usavel = lambda i: (0 <= i < len(meses) and razao[i] is not None
                        and meses[i] < corte_prov)

    pos_i = [i for i in range(c, c + n) if usavel(i)]
    pre_i = [i for i in range(c - n, c) if usavel(i)]
    if len(pos_i) < 6 or len(pre_i) < 6:
        return None

    # equilibra a composição sazonal das duas janelas
    if len(pos_i) < len(pre_i):
        meses_pos = {meses[i][5:] for i in pos_i}
        pre_i = [i for i in pre_i if meses[i][5:] in meses_pos]
    elif len(pre_i) < len(pos_i):
        meses_pre = {meses[i][5:] for i in pre_i}
        pos_i = [i for i in pos_i if meses[i][5:] in meses_pre]
    if len(pre_i) < 6 or len(pos_i) < 6:
        return None

    return (mean(razao[i] for i in pre_i), mean(razao[i] for i in pos_i),
            len(pre_i), len(pos_i))

REAIS = [
    ('τ1', '2020-01', 'Previne Brasil'),
    ('τ2', '2020-03', 'COVID-19'),
    ('τ2b', '2021-01', 'recuperação'),
    ('τ3', '2024-05', 'Saúde Brasil 360 — estimando primário'),
    ('τ4', '2025-05', 'mensuração do C7'),
]

# datas sem evento normativo conhecido, distribuídas pela janela
PLACEBOS = ['2018-07', '2019-03', '2019-09', '2021-07', '2022-03', '2022-11',
            '2023-04', '2023-10', '2024-11', '2025-02']

def linha(rot, mes, desc, r):
    if r is None:
        return f"  {rot:5s} {mes}  {'—':>34s}  {desc}"
    pre, pos, np_, ns = r
    delta = pos - pre
    pct = 100 * delta / pre
    return (f"  {rot:5s} {mes}  pré {pre:.4f} → pós {pos:.4f}  "
            f"Δ {delta:+.4f} ({pct:+6.1f}%)  {desc}")

print("=" * 96)
print("MARCOS REAIS")
print("=" * 96)
efeitos_reais = []
for rot, mes, desc in REAIS:
    r = janela(mes)
    print(linha(rot, mes, desc, r))
    if r:
        efeitos_reais.append((rot, 100 * (r[1] - r[0]) / r[0]))

print()
print("=" * 96)
print("DATAS-PLACEBO (sem evento normativo)")
print("=" * 96)
efeitos_placebo = []
for mes in PLACEBOS:
    r = janela(mes)
    print(linha('—', mes, 'placebo', r))
    if r:
        efeitos_placebo.append((mes, 100 * (r[1] - r[0]) / r[0]))

print()
print("=" * 96)
print("VEREDITO")
print("=" * 96)
mags_placebo = sorted(abs(v) for _, v in efeitos_placebo)

# exporta o resultado para o painel consumir
export = {
    'metodo': ('média da razão de exames nos 12 meses anteriores contra os 12 posteriores, '
               'excluindo competências ausentes e provisórias'),
    'marcos': [], 'placebos': [{'mes': m, 'delta_pct': round(v, 1)} for m, v in efeitos_placebo],
    'placebo_mediana_abs': round(mags_placebo[len(mags_placebo) // 2], 1),
    'placebo_max_abs': round(mags_placebo[-1], 1),
    'placebo_n': len(mags_placebo),
}
for (rot, mes, desc), (_, v) in zip(
        [r for r in REAIS if janela(r[1])], efeitos_reais):
    r = janela(mes)
    maiores = sum(1 for m in mags_placebo if m >= abs(v))
    export['marcos'].append({
        'marco': rot, 'mes': mes, 'descricao': desc,
        'pre': round(r[0], 4), 'pos': round(r[1], 4), 'delta_pct': round(v, 1),
        'placebos_maiores': maiores, 'p_aprox': round((maiores + 1) / (len(mags_placebo) + 1), 2),
    })
json.dump(export, open(RAIZ + '/data/falsificacao.json', 'w'), ensure_ascii=False, indent=1)
print(f"  placebos: n={len(mags_placebo)}, mediana |Δ%| = {mags_placebo[len(mags_placebo)//2]:.1f}%, "
      f"máximo = {mags_placebo[-1]:.1f}%")
print(f"  desvio-padrão dos efeitos placebo: {pstdev([v for _, v in efeitos_placebo]):.1f} pontos percentuais")
print()
for rot, v in efeitos_reais:
    # quantos placebos têm magnitude igual ou maior que este marco?
    maiores = sum(1 for m in mags_placebo if m >= abs(v))
    p = (maiores + 1) / (len(mags_placebo) + 1)
    veredito = ("distinguível" if p <= 0.10 else
                "indistinguível de ruído" if p > 0.30 else "limítrofe")
    print(f"  {rot:5s} Δ {v:+7.1f}%  ·  {maiores}/{len(mags_placebo)} placebos "
          f"tão grandes ou maiores  ·  p ≈ {p:.2f}  ·  {veredito}")
