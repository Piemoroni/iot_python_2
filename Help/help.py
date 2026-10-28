
from pathlib import Path

pasta = Path(__file__).parent
entrada = pasta / "entrada.txt"
saida = pasta / "saida.txt"

with open(entrada, "r", encoding="utf-8") as arquivo:
    dados = arquivo.read().split()

resultados = []
indice = 0

while indice < len(dados):
    n = int(dados[indice])
    indice += 1

    if n == 0:
        break

    erros = {}
    resolvidos = set()
    penalidade = 0

    for _ in range(n):
        problema = dados[indice]
        tempo = int(dados[indice + 1])
        julgamento = dados[indice + 2]
        indice += 3

        if problema in resolvidos:
            continue

        if julgamento == "incorrect":
            erros[problema] = erros.get(problema, 0) + 1

        elif julgamento == "correct":
            resolvidos.add(problema)
            penalidade += tempo
            penalidade += erros.get(problema, 0) * 20

    resultados.append(f"{len(resolvidos)} {penalidade}")

with open(saida, "w", encoding="utf-8") as arquivo:
    arquivo.write("\n".join(resultados))
