
from pathlib import Path

pasta = Path(__file__).parent
entrada = pasta / "entrada.txt"
saida = pasta / "saida.txt"

with open(entrada, "r", encoding="utf-8") as arquivo:
    dados = arquivo.read().split()

direcoes = ["N", "L", "S", "O"]
resultados = []
posicao = 0
indice = 0

while indice < len(dados):
    n = int(dados[indice])
    indice += 1

    if n == 0:
        break

    comandos = dados[indice]
    indice += 1

    for comando in comandos:
        if comando == "D":
            posicao = (posicao + 1) % 4
        elif comando == "E":
            posicao = (posicao - 1) % 4

    resultados.append(direcoes[posicao])
    posicao = 0

with open(saida, "w", encoding="utf-8") as arquivo:
    arquivo.write("\n".join(resultados))
