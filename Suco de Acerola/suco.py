
from pathlib import Path

pasta = Path(__file__).parent
entrada = pasta / "entrada.txt"
saida = pasta / "saida.txt"

resultados = []

with open(entrada, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()

        if not linha:
            continue

        n, f = map(int, linha.split())

        if n == 0 and f == 0:
            break

        volume = (f * 50) / (n * 1000)
        resultados.append(f"{volume:.2f}")

with open(saida, "w", encoding="utf-8") as arquivo:
    arquivo.write("\n".join(resultados))
