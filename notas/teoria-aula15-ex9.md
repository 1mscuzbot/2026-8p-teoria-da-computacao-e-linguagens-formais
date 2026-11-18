# Teoria — Aula 15, Exercício 9 (AP)

**Enunciado (slide):** `L = { aⁿ⁺ᵐ bᵐ aⁿ | n,m ≥ 0 }`  
**Fonte:** `material/slides/2_BIMESTRE/Aula15-Automato-de-Pilha.pdf` · `notas/estudo-aula15-automato-de-pilha.md`

---

## O que é essa linguagem?

Palavras da forma:

```text
a a … a  |  b b … b  |  a a … a
◄─ n+m ─►  ◄── m ──►  ◄── n ──►
```

| Caso | Forma | Exemplo |
|------|--------|---------|
| `n=m=0` | `ε` | `ε` |
| `m=0` | `aⁿ aⁿ` = `a²ⁿ` | `aa`, `aaaa` |
| `n=0` | `aᵐ bᵐ` | `ab`, `aabb` |
| ambos >0 | `aⁿ⁺ᵐ bᵐ aⁿ` | `aaba` (`n=m=1`), `aaabbbaa` (`n=2,m=3`) |

**Não** está em L: `a`, `aba`, `abb` (contagens não fecham).

---

## Ideia

1. Empilha **todos** os `a`s do primeiro bloco (`e(N)`).
2. Nos `b`s: desempilha a parcela **m** (`d(N)`).
3. Nos `a`s finais: desempilha a parcela **n** (`d(N)`).
4. Aceita com **`?/?`** (fita acabou **e** pilha vazia).

Como `n,m ≥ 0`, fases podem ser vazias:

- `ε` → `?/?` já no início.
- `m=0` → do empilhar, o **1º `a` da segunda metade** já desempilha (`a/d(N)`) — **não-determinismo** (chute do meio).
- `n=0` → após os `b`s, `?/?` com pilha vazia (sem fase final de `a`).

**Sem `ε/ε` entre fases:** troca no **1º** símbolo da próxima fase (`b/d` ou `a/d`), no padrão Furlan dos ex. ≥1; o ≥0 entra via `?/?` e o não-determinismo em `a`.

---

## Desenho (estilo da aula)

```text
 a/e(N)
 ┌──────────┐
 ▼          │
> (1) ──────┘
 │ ╲
 │  ╲ a/d(N)     ← chute m=0 (1º a da 2ª metade)
 │   ╲
 │ b/d(N) ╲
 ▼         ╲
 (2)        ╲
 │ b/d(N)    ╲
 │            ╲
 │ a/d(N)      ╲
 ▼             ▼
 (3) ──a/d(N)──┘
 │
 │ ?/?   (também de (1) e de (2) se pilha vazia)
 ▼
((4)) FINAL
```

## Arcos

| De | Para | Arco | Significado |
|----|------|------|-------------|
| `(1)` | `(1)` | `a/e(N)` | 1º bloco: empilha |
| `(1)` | `(2)` | `b/d(N)` | 1º `b` (`m≥1`) |
| `(1)` | `(3)` | `a/d(N)` | chute `m=0`, começa `aⁿ` |
| `(1)` | `((4))` | `?/?` | `ε` (`n=m=0`) |
| `(2)` | `(2)` | `b/d(N)` | mais `b`s |
| `(2)` | `(3)` | `a/d(N)` | 1º `a` final (`n≥1`) |
| `(2)` | `((4))` | `?/?` | `n=0`, acabou após `b`s |
| `(3)` | `(3)` | `a/d(N)` | mais `a`s finais |
| `(3)` | `((4))` | `?/?` | fim + pilha vazia |

`(1)--a/e(N)-->` e `(1)--a/d(N)-->` convivem → **AP não-determinístico** (ok para LLC).

---

## Simulações

### Aceita: `aaba` (`n=1,m=1` → `a²ba`)

| Passo | Lê | Pilha | Estado | Arco |
|------:|----|-------|--------|------|
| 0 | — | `ε` | 1 | — |
| 1 | `a` | `N` | 1 | `a/e(N)` |
| 2 | `a` | `NN` | 1 | `a/e(N)` |
| 3 | `b` | `N` | 2 | `b/d(N)` |
| 4 | `a` | `ε` | 3 | `a/d(N)` |
| 5 | fim | `ε` | 4 | `?/?` → **aceita** |

### Aceita: `aa` (`n=1,m=0`)

`a/e(N)` → pilha `N`; chute `a/d(N)` → `(3)` pilha vazia; `?/?` → **aceita**.

### Aceita: `ab` (`n=0,m=1`)

`a/e(N)`; `b/d(N)` → `(2)` vazia; `?/?` → **aceita**.

### Aceita: `ε`

`(1)--?/?-->((4))`.

### Rejeita: `aba`

`a/e`; `b/d` → vazia em `(2)`; próximo `a` pede `d(N)` sem `N` → δ indefinida → **rejeita**.

---

## Checklist

1. Empilha o 1º bloco inteiro (`n+m`).
2. `b`s comem a fatia `m`; `a`s finais comem a fatia `n`.
3. `m=0` ⇒ não-determinismo no meio dos `a`s; `n=0` ⇒ `?/?` após os `b`s.
4. Aceita **só** com pilha vazia no fim.
