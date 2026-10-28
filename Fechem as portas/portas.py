
from pathlib import Path
from math import isqrt

pasta = Path(__file__).parent
entrada = pasta / "entrada.txt"
saida = pasta / "saida.txt"

with open(entrada, "r", encoding="utf-8") as arquivo:
    numeros = arquivo.read().split()

resultados = []

for valor in numeros:
    n = int(valor)

    if n == 0:
        break

    portas_abertas = [str(i * i) for i in range(1, isqrt(n) + 1)]
    resultados.append(" ".join(portas_abertas))

with open(saida, "w", encoding="utf-8") as arquivo:
    arquivo.write("\n".join(resultados))
