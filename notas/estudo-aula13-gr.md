# Aula 13 — Gramática Regular (GR)

**Disciplina:** Teoria da Computação e Linguagens Formais (Prof. Diógenes Furlan)  
**Slide:** `material/slides/2_BIMESTRE/Aula13-GR.pdf`

---

## Ideia

**Gramática regular (GR):** cada produção é de uma das formas:

- `X → w`
- `X → wY`
- `X → ε`

com `X,Y ∈ V` (variáveis) e `w ∈ Σ` (terminal; no slide, `w` pode ser string de terminais conforme notação usada).

Linguagem **regular (LR)** ⇔ existe GR que a gera. Equivalência prática: **GR ↔ NFA**.

---

## Sumário

- Definição de GR / LR
- Exemplos a partir de ER
- Transformação GR → NFA
- Transformação NFA → GR
- Exercícios (GR↔NFA, linguagens, criar GRs)

---

## 1. Exemplos (criar GR a partir da ideia / ER)

| Linguagem | ER (slide) |
|-----------|------------|
| Todas as palavras sobre `{a,b}` (não vazias) | `(a+b)+` |
| Nº ímpar de `a`s | `b*ab*(ab*ab*)*` |
| Começam e terminam com `a` | `a(a+b)*a + a` |
| Tamanho múltiplo de 3 | `((a+b)(a+b)(a+b))*` |
| Antepenúltimo símbolo é `b` | `(a+b)*b(a+b)(a+b)` |

---

## 2. GR → NFA

- Cada **variável** → um **estado**
- Se há regras `X → w` (só terminais): criar estado final extra `Z`
- Regras → transições:
  - `X → wY` ⇒ `Y ∈ δ(X, w)`
  - `X → w` ⇒ `Z ∈ δ(X, w)`
  - `X → ε` ⇒ `X` é **final**

### Exemplo

```text
A → 0A | 0 | 1B
B → 1B | ε
```

NFA (`s=A`, `F={B,Z}`):

|   | 0   | 1 |
|---|-----|---|
| A | A,Z | B |
| B | ∅   | B |
| Z | ∅   | ∅ |

---

## 3. NFA → GR

- Cada **estado** → uma **variável**
- Cada transição `Y ∈ δ(X,w)` → produção `X → wY`
- Cada estado **final** `X` → produção `X → ε`

### Exemplo

NFA (`s=A`, `F={B,C}`):

|   | 0   | 1   |
|---|-----|-----|
| A | A,C | A,B |
| B | ∅   | B   |
| C | B   | A   |

GR:

```text
A → 0A | 0C | 1A | 1B
B → 1B | ε
C → 0B | 1A | ε
```

---

## 4. Exercícios do slide

**GR → NFA:** (1) `S→0S|ε` (2) `S→0S|1A`, `A→1A|ε` (3) `S→aA`, `A→aA|bA|b` (4) A/B/C com a,b,c (5) `S→abcS|ε`

**NFA → GR:** figuras 1–4 do slide (desenhar → escrever produções).

**Exercício 1 — linguagens geradas:** itens a–d (ex.: `S→aA`, `A→aA|a` → `aa+`).

**Exercício 2 — criar GRs:** `(a+b+c)+`; começa `a` termina `c`; começa/termina `0` com ≥1 `1`; nº ímpar de `0`s; `{ε}`; ímpar de `a`s; tamanho ×4; par de `a`s e par de `b`s; cada `a` seguido de ≥2 `b`s; penúltimo é `b`.

**Exercício 3:** GRs do ex. 2 → NFA.

---

## Checklist rápido

- [ ] Reconhecer as 3 formas de produção de uma GR
- [ ] Converter GR → NFA (incl. estado Z e finais por ε)
- [ ] Converter NFA → GR (finais → ε)
- [ ] Resolver pelo menos um bloco de exercícios do slide
