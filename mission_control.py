# ============================================================
# MISSION CONTROL AI
# GS2026.1 - Pensamento Computacional e Automação com Python
# ============================================================

nome_missao = "Missão Fé na Orbita"
nome_equipe = "Equipe Tropa"

dados_missao = [
    [23, 95, 90, 97, 92],
    [26, 84, 76, 94, 87],
    [30, 68, 63, 90, 75],
    [35, 50, 45, 86, 60],
    [38, 33, 25, 81, 42],
    [33, 60, 40, 85, 58]
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]


# ============================================================
# FUNÇÕES DE ANÁLISE
# ============================================================

def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", 1
    elif valor <= 30:
        return "NORMAL", 0
    elif valor <= 35:
        return "ATENÇÃO", 1
    else:
        return "CRÍTICO", 2


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", 2
    elif valor < 60:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2
    elif valor < 50:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2
    elif valor < 90:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", 2
    elif valor < 70:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


# ============================================================
# CLASSIFICAÇÃO DO CICLO
# ============================================================

def classificar_ciclo(risco):
    if risco <= 2:
        return "MISSÃO ESTÁVEL"
    elif risco <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


# ============================================================
# TENDÊNCIA
# ============================================================

def analisar_tendencia(primeiro, ultimo):
    if ultimo > primeiro:
        return "A missão apresentou tendência de piora."
    elif ultimo < primeiro:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


# ============================================================
# ÁREA MAIS AFETADA
# ============================================================

def identificar_area_mais_afetada(pontuacoes):
    maior = max(pontuacoes)
    indice = pontuacoes.index(maior)
    return areas_monitoradas[indice]


# ============================================================
# RECOMENDAÇÕES
# ============================================================

def gerar_recomendacao(ciclo):
    temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo

    recomendacoes = []

    if temperatura > 35:
        recomendacoes.append(
            "Verificar controle térmico da missão"
        )

    if comunicacao < 30:
        recomendacoes.append(
            "Restabelecer contato com a base"
        )

    if bateria < 20:
        recomendacoes.append(
            "Ativar modo de economia de energia"
        )

    if oxigenio < 80:
        recomendacoes.append(
            "Acionar protocolo de suporte à vida"
        )

    if estabilidade < 40:
        recomendacoes.append(
            "Reduzir operações não essenciais"
        )

    if len(recomendacoes) == 0:
        return "Manter operação normal e continuar monitoramento."

    return " | ".join(recomendacoes)


# ============================================================
# PROCESSAMENTO DOS DADOS
# ============================================================

riscos_ciclos = []
pontuacao_areas = [0, 0, 0, 0, 0]

soma_temp = 0
soma_com = 0
soma_bat = 0
soma_oxi = 0
soma_est = 0

print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)
print("Missão:", nome_missao)
print("Equipe:", nome_equipe)
print("Quantidade de ciclos analisados:", len(dados_missao))
print("=" * 60)

for i in range(len(dados_missao)):

    temperatura = dados_missao[i][0]
    comunicacao = dados_missao[i][1]
    bateria = dados_missao[i][2]
    oxigenio = dados_missao[i][3]
    estabilidade = dados_missao[i][4]

    status_temp, risco_temp = analisar_temperatura(temperatura)
    status_com, risco_com = analisar_comunicacao(comunicacao)
    status_bat, risco_bat = analisar_bateria(bateria)
    status_oxi, risco_oxi = analisar_oxigenio(oxigenio)
    status_est, risco_est = analisar_estabilidade(estabilidade)

    risco_total = (
        risco_temp +
        risco_com +
        risco_bat +
        risco_oxi +
        risco_est
    )

    riscos_ciclos.append(risco_total)

    pontuacao_areas[0] += risco_temp
    pontuacao_areas[1] += risco_com
    pontuacao_areas[2] += risco_bat
    pontuacao_areas[3] += risco_oxi
    pontuacao_areas[4] += risco_est

    soma_temp += temperatura
    soma_com += comunicacao
    soma_bat += bateria
    soma_oxi += oxigenio
    soma_est += estabilidade

    print("\nCICLO", i + 1)
    print("-" * 60)

    print("Temperatura:", temperatura, "°C |", status_temp)
    print("Comunicação:", comunicacao, "% |", status_com)
    print("Bateria:", bateria, "% |", status_bat)
    print("Oxigênio:", oxigenio, "% |", status_oxi)
    print("Estabilidade:", estabilidade, "% |", status_est)

    print("Pontuação de risco:", risco_total)
    print("Classificação:", classificar_ciclo(risco_total))

    print("Recomendação:")
    print(gerar_recomendacao(dados_missao[i]))

# ============================================================
# RELATÓRIO FINAL
# ============================================================

print("\n")
print("=" * 60)
print("RELATÓRIO FINAL DA MISSÃO")
print("=" * 60)

quantidade = len(dados_missao)

media_temp = soma_temp / quantidade
media_com = soma_com / quantidade
media_bat = soma_bat / quantidade
media_oxi = soma_oxi / quantidade
media_est = soma_est / quantidade

maior_risco = max(riscos_ciclos)
ciclo_critico = riscos_ciclos.index(maior_risco) + 1

risco_medio = sum(riscos_ciclos) / quantidade

ciclos_criticos = 0
for risco in riscos_ciclos:
    if risco >= 6:
        ciclos_criticos += 1

tendencia = analisar_tendencia(
    riscos_ciclos[0],
    riscos_ciclos[-1]
)

area_mais_afetada = identificar_area_mais_afetada(
    pontuacao_areas
)

classificacao_final = classificar_ciclo(
    int(risco_medio)
)

print("Missão:", nome_missao)
print("Equipe:", nome_equipe)
print("Quantidade de ciclos:", quantidade)

print(f"Média de temperatura: {media_temp:.2f} °C")
print(f"Média de comunicação: {media_com:.2f}%")
print(f"Média de bateria: {media_bat:.2f}%")
print(f"Média de oxigênio: {media_oxi:.2f}%")
print(f"Média de estabilidade: {media_est:.2f}%")

print("Ciclo mais crítico:", ciclo_critico)
print("Maior pontuação de risco:", maior_risco)
print(f"Risco médio da missão: {risco_medio:.2f}")

print("Quantidade de ciclos críticos:",
      ciclos_criticos)

print("\nTendência da missão:")
print(tendencia)

print("\nPontuação acumulada por área:")

for i in range(len(areas_monitoradas)):
    print(
        areas_monitoradas[i] + ":",
        pontuacao_areas[i],
        "pontos"
    )

print("\nÁrea mais afetada:")
print(area_mais_afetada)

print("\nClassificação final da missão:")
print(classificacao_final)

print("\nConclusão:")

if classificacao_final == "MISSÃO ESTÁVEL":
    print("Todos os sistemas operam dentro dos limites aceitáveis.")
elif classificacao_final == "MISSÃO EM ATENÇÃO":
    print("Existem sistemas que exigem monitoramento contínuo.")
else:
    print("A missão apresenta riscos críticos e necessita intervenção imediata.")