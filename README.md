# Estudando Python - SESI / SENAI

Repositório dedicado à lista de exercícios fundamentais e resolução de desafios de lógica de programação em Python, desenvolvidos durante as aulas do curso **Técnico em Desenvolvimento de Sistemas (DES)** (Módulo de IoT e Automação).

---

## Tecnologias Utilizadas
- **Python 3.x** — Linguagem de programação principal
- **VS Code (Visual Studio Code)** — Ambiente de desenvolvimento (IDE)

---

## Estrutura do Repositório

```text
sesi_iot_estudando_python_2026/
│
├── README.md                <-- Documentação principal do repositório
├── exercicios.py            <-- Lista de exercícios básicos (1 ao 9)
│
└── desafios/                <-- Pasta contendo os desafios de lógica
    ├── portas/
    │   ├── entrada.txt
    │   ├── saida.txt
    │   ├── portas.py
    │   └── README.md
    ├── esquerda/
    │   ├── entrada.txt
    │   ├── saida.txt
    │   ├── esquerda.py
    │   └── README.md
    ├── suco/
    │   ├── entrada.txt
    │   ├── saida.txt
    │   ├── suco.py
    │   └── README.md
    └── help/
        ├── entrada.txt
        ├── saida.txt
        ├── help.py
        └── README.md

```

---

## Lista de Exercícios (1 a 9)

O arquivo `exercicios.py` contém as soluções para os seguintes enunciados:

1. **Média de três números:** Solicita três números e calcula a média aritmética.
2. **Conversor de temperatura:** Converte graus Celsius para Fahrenheit.
3. **Par ou Ímpar:** Identifica se um número inteiro inserido é par ou ímpar.
4. **Cálculo de fatorial:** Calcula o fatorial de um número inteiro positivo.
5. **Ano bissexto:** Verifica se um ano informado é bissexto seguindo as regras oficiais.
6. **Positivo, negativo ou zero:** Analisa o sinal de um número.
7. **Comparação de números:** Determina qual o maior entre dois números ou se são iguais.
8. **Verificação de idade:** Identifica se a pessoa é maior ou menor de idade.
9. **Classificação de triângulos:** Classifica um triângulo em Equilátero, Isósceles ou Escaleno com base nos lados.

---

## Desafios de Lógica e Manipulação de Arquivos

Cada desafio na pasta `desafios/` lê os dados de entrada de um arquivo `entrada.txt`, processa a lógica computacional e grava o resultado formatado em um arquivo `saida.txt`:

* **Fechem as portas! (`portas.py`):** Simula o estado das portas em uma mansão utilizando otimização matemática baseada em quadrados perfeitos.
* **Esquerda, Volver! (`esquerda.py`):** Controla a orientação cardeal (Norte, Leste, Sul, Oeste) de um recruta após uma sequência de comandos de giro.
* **Suco de Acerola (`suco.py`):** Calcula a divisão proporcional de suco de acerola em litros por amigo, com precisão de duas casas decimais.
* **Help! (`help.py`):** Computa o placar de submissões de uma maratona de programação, calculando problemas resolvidos e penalidades de tempo.

---

## Como Executar os Códigos

Para testar qualquer um dos scripts localmente na sua máquina através do terminal do VS Code, utilize o comando:

```bash
python nome_do_arquivo.py

```

*(Certifique-se de estar na mesma pasta do arquivo que deseja rodar).*

```

```