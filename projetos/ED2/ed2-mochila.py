#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Estudo Dirigido 2 - Teoria da Computacao e Linguagens Formais
Problema pratico: Mochila 0/1 (Knapsack)
Autor: Lucas Muller Scuzziato
"""

from __future__ import annotations

import argparse
import random
import time
from pathlib import Path
from typing import List, Optional, Sequence, Tuple

Item = Tuple[str, int, int]  # (nome, peso, valor)


def forca_bruta(itens: Sequence[Item], capacidade: int) -> Tuple[int, List[str], int]:
    """Algoritmo burro: enumera todos os 2^n subconjuntos. Retorna (valor, nomes, peso)."""
    n = len(itens)
    melhor_valor = 0
    melhor_peso = 0
    melhor_masc = 0
    for mascara in range(1 << n):
        peso = 0
        valor = 0
        for i in range(n):
            if mascara & (1 << i):
                peso += itens[i][1]
                valor += itens[i][2]
                if peso > capacidade:
                    break
        if peso <= capacidade and valor > melhor_valor:
            melhor_valor = valor
            melhor_peso = peso
            melhor_masc = mascara
    escolhidos = [itens[i][0] for i in range(n) if melhor_masc & (1 << i)]
    return melhor_valor, escolhidos, melhor_peso


def programacao_dinamica(
    itens: Sequence[Item], capacidade: int
) -> Tuple[int, List[str], int]:
    """PD classica O(n*W). Retorna (valor, nomes, peso)."""
    n = len(itens)
    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        _, peso, valor = itens[i - 1]
        for w in range(capacidade + 1):
            dp[i][w] = dp[i - 1][w]
            if peso <= w:
                candidato = dp[i - 1][w - peso] + valor
                if candidato > dp[i][w]:
                    dp[i][w] = candidato

    # reconstrucao
    w = capacidade
    escolhidos: List[str] = []
    peso_total = 0
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            nome, peso, _ = itens[i - 1]
            escolhidos.append(nome)
            peso_total += peso
            w -= peso
    escolhidos.reverse()
    return dp[n][capacidade], escolhidos, peso_total


def guloso_densidade(
    itens: Sequence[Item], capacidade: int
) -> Tuple[int, List[str], int]:
    """Heuristica gulosa por valor/peso (nao necessariamente otima)."""
    ordenados = sorted(
        itens, key=lambda it: (it[2] / it[1] if it[1] else 0), reverse=True
    )
    peso = 0
    valor = 0
    escolhidos: List[str] = []
    for nome, p, v in ordenados:
        if peso + p <= capacidade:
            escolhidos.append(nome)
            peso += p
            valor += v
    return valor, escolhidos, peso


INSTANCIA_PEQUENA: List[Item] = [
    ("caderno", 2, 3),
    ("garrafa", 3, 4),
    ("lanche", 4, 5),
    ("livro", 5, 8),
    ("fone", 1, 2),
]
CAP_PEQUENA = 8


def instancia_aleatoria(n: int, seed: int = 42) -> Tuple[List[Item], int]:
    rng = random.Random(seed)
    itens = [(f"i{i}", rng.randint(1, 15), rng.randint(1, 40)) for i in range(n)]
    capacidade = max(10, sum(it[1] for it in itens) // 3)
    return itens, capacidade


def medir(
    nome: str,
    func,
    itens: Sequence[Item],
    capacidade: int,
    repetir: int = 1,
) -> Tuple[float, Optional[Tuple[int, List[str], int]]]:
    resultado = None
    t0 = time.perf_counter()
    for _ in range(repetir):
        resultado = func(itens, capacidade)
    dt = (time.perf_counter() - t0) / repetir
    print(
        f"[{nome}] n={len(itens)} W={capacidade} "
        f"valor={resultado[0]} peso={resultado[2]} "
        f"itens={resultado[1]} tempo={dt*1000:.3f} ms"
    )
    return dt, resultado


def gerar_grafico(saida: Path) -> None:
    import matplotlib.pyplot as plt

    tamanhos = [8, 10, 12, 14, 16, 18, 20]
    tempos_fb: List[float] = []
    tempos_pd: List[float] = []
    for n in tamanhos:
        itens, cap = instancia_aleatoria(n, seed=100 + n)
        if n <= 18:
            t_fb, _ = medir(f"FB n={n}", forca_bruta, itens, cap)
            tempos_fb.append(t_fb * 1000)
        else:
            tempos_fb.append(float("nan"))
        t_pd, _ = medir(f"PD n={n}", programacao_dinamica, itens, cap, repetir=5)
        tempos_pd.append(t_pd * 1000)

    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    ax.plot(tamanhos, tempos_fb, "o-", label="Forca bruta O(2^n * n)")
    ax.plot(tamanhos, tempos_pd, "s-", label="PD O(n * W)")
    ax.set_xlabel("Numero de itens (n)")
    ax.set_ylabel("Tempo (ms)")
    ax.set_title("Mochila 0/1 - tempo: forca bruta x programacao dinamica")
    ax.legend()
    ax.grid(True, alpha=0.35)
    fig.tight_layout()
    saida.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(saida, dpi=150)
    print(f"Grafico salvo em {saida}")


def demo() -> None:
    print("=" * 60)
    print("ED2 - Mochila 0/1 | Lucas Muller Scuzziato")
    print("=" * 60)
    print("\n--- Instancia pequena (n=5, W=8) ---")
    for nome, p, v in INSTANCIA_PEQUENA:
        print(f"  {nome:8s} peso={p} valor={v} densidade={v/p:.2f}")

    medir("Forca bruta", forca_bruta, INSTANCIA_PEQUENA, CAP_PEQUENA)
    medir("PD", programacao_dinamica, INSTANCIA_PEQUENA, CAP_PEQUENA)
    medir("Guloso dens.", guloso_densidade, INSTANCIA_PEQUENA, CAP_PEQUENA)

    print("\n--- Instancias maiores (so PD + guloso; FB limitada) ---")
    for n in (12, 16, 22, 28):
        itens, cap = instancia_aleatoria(n)
        if n <= 16:
            medir(f"FB n={n}", forca_bruta, itens, cap)
        medir(f"PD n={n}", programacao_dinamica, itens, cap)
        medir(f"Guloso n={n}", guloso_densidade, itens, cap)


def main() -> None:
    parser = argparse.ArgumentParser(description="ED2 - Mochila 0/1")
    parser.add_argument(
        "--grafico",
        type=Path,
        default=None,
        help="Gera PNG comparando FB x PD",
    )
    args = parser.parse_args()
    demo()
    if args.grafico is not None:
        print("\n--- Gerando grafico de desempenho ---")
        gerar_grafico(args.grafico)


if __name__ == "__main__":
    main()
