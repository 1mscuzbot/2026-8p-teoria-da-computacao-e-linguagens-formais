# Aula 14 — Forma Normal de Chomsky (FNC)

**Disciplina:** Teoria da Computação e Linguagens Formais (Prof. Diógenes Furlan)  
**Slide:** `material/slides/2_BIMESTRE/Aula14-FNC.pdf`  
**Segue:** simplificação de GLC (aulas anteriores) e [Aula 13 — GR](estudo-aula13-gr.md) (contexto de gramáticas).

---

## Ideia

Uma **GLC** está na **Forma Normal de Chomsky (FNC)** se toda produção é:

- `A → V1 V2` (duas variáveis), ou
- `A → t` (um terminal)

**Importância:** todas as **árvores sintáticas** ficam **binárias** (úteis p/ parsing / CYK).

---

## Sumário

- Definição de FNC
- Algoritmo: simplificar → fase Δ → fase Ω
- Exemplo 1 completo (Δ e Ω)
- Exemplo 2 (enunciado)
- Exercícios do slide

---

## 1. Algoritmo

**a) Simplificar a GLC** (remover inúteis, ε-produções, unitárias — aulas anteriores).

**b) Fase Δ (delta)** — em produções com |RHS| > 1, o lado direito deve ter **só variáveis** (sem terminais misturados):

- Para cada terminal `a` que aparece em RHS longo: criar `Δa → a` (no exemplo: `X→a`, `Y→b`, `Z→c`) e substituir `a` por essa variável.

**c) Fase Ω (ômega)** — RHS com |RHS| > 1 deve ter **exatamente 2** variáveis:

- Produções com 3+ variáveis: quebrar com variáveis auxiliares `Ωi` / `K,L,M,N…` (ex.: `A → AXXA` → `L→AX`, `M→XA`, `A→LM`).

---

## 2. Exemplo 1 (passo a passo)

**Original (após simplificar, conforme slide):**

```text
P → APB | Ca
A → AaaA | b
B → BBb | aC
C → cC | d
```

**Após fase Δ** (`X→a`, `Y→b`, `Z→c`):

```text
P → APB | CX
A → AXXA | b
B → BBY | XC
C → ZC | d
```

**Após fase Ω** (`K→AP`, `L→AX`, `M→XA`, `N→BB`):

```text
P → KB | CX
A → LM | b
B → NY | XC
C → ZC | d
X → a    Y → b    Z → c
K → AP   L → AX   M → XA   N → BB
```

Todas as produções: 2 variáveis **ou** 1 terminal → **FNC**.

---

## 3. Exemplo 2 (enunciado)

```text
S → ABC | aS
A → CC | ab
B → bB | b
C → aC | ε
```

Aplicar: simplificar (há `ε`) → Δ → Ω. (Resolver no caderno.)

---

## 4. Exercícios do slide

1. `S → a | aSa` — testar com `"aaa"`
2. Gramática S/A/B — AS de `"bbaa"` **antes e depois** da FNC
3. `S → aSd | aAd`, `A → bAc | bc`
4. S/A/B/C/D com vários terminais misturados
5. `S → aaS | aSa | Saa | bbS | bSb | Sbb | a | b`

---

## Checklist rápido

- [ ] Enunciar as duas formas permitidas na FNC
- [ ] Ordem: simplificar → Δ → Ω
- [ ] Reproduzir o Exemplo 1 até o resultado final
- [ ] Fazer pelo menos os exercícios 1–2 do slide (com AS quando pedido)
