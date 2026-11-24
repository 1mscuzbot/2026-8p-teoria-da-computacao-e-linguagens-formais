# Teoria — Aula 15 · PDA `L = { aᵐ bᵐ⁺ᵖ cᵖ | m,p ≥ 1 }`

**Pedido (Lucas):** `a^m . b^(m+p) . c^p`  
**Notação Furlan:** `e`/`d`, `?/?`, troca no **1º** símbolo da próxima fase — **sem** `ε/ε` entre fases (`m,p≥1`).

---

## Ideia

```text
a a … a  |  b b … b  b b … b  |  c c … c
◄── m ──►  ◄── m ──►◄── p ──►  ◄── p ──►
 empilha N   desempilha N  empilha P   desempilha P
```

1. Nos **`a`**: `e(N)` — conta `m`.
2. Nos **`b`**: primeiro desempilha os `m` (`d(N)`); com pilha **vazia**, os `b`s restantes (`p≥1`) fazem `e(P)`.
3. Nos **`c`**: `d(P)` — casa com os `p` empilhados.
4. Fim + pilha vazia → **`?/?`**.

`m,p≥1` ⇒ sempre há ≥1 `a`, ≥1 `b` da fatia `m`, ≥1 `b` da fatia `p`, ≥1 `c` — dá para trocar de estado no 1º símbolo, sem `ε/ε`.

---

## Desenho

```text
 a/e(N)
 ┌──────────┐
 ▼          │
> (1) ──────┘
 │ b/d(N)
 ▼
  (2) ──b/d(N)──┐
 │              │
 │ b/e(P)       │   ← pilha vazia; 1º b da fatia p
 ▼              │
  (3) ──b/e(P)──┘
 │ c/d(P)
 ▼
  (4) ──c/d(P)──┐
 │              │
 │ ?/?          │
 ▼              │
 ((5)) FINAL    ┘
```

## Arcos

| De | Para | Arco | Significado |
|----|------|------|-------------|
| `(1)` | `(1)` | `a/e(N)` | empilha `m` |
| `(1)` | `(2)` | `b/d(N)` | 1º `b` (inicia fatia `m`) |
| `(2)` | `(2)` | `b/d(N)` | mais `b`s contra `N` |
| `(2)` | `(3)` | `b/e(P)` | pilha vazia; 1º `b` da fatia `p` |
| `(3)` | `(3)` | `b/e(P)` | mais `b`s → empilha `P` |
| `(3)` | `(4)` | `c/d(P)` | 1º `c` |
| `(4)` | `(4)` | `c/d(P)` | mais `c`s |
| `(4)` | `((5))` | `?/?` | fim + pilha vazia |

Em `(2)`, `b/d(N)` vs `b/e(P)`: o topo decide (tem `N` → desempilha; vazia → começa `p`).

---

## Exemplos

| Palavra | `m,p` | Resultado |
|---------|-------|-----------|
| `abbcc`? | — | **não** (forma `a b² c²` ⇒ `m=1` pediria `b^{1+p}c^p`; se `p=2` → `abb bcc` = `abbbcc`) |
| `abbc` | `m=1,p=1` → `a b² c` | **aceita** |
| `aabbbcc` | `m=2,p=1` → `a² b³ c` | **aceita** |
| `aabbbbcc` | `m=2,p=2` → `a² b⁴ c²` | **aceita** |
| `abc` | `m=1,p=0` | **fora** (`p≥1`); máquina: após `ab` pilha vazia, `c` pede `d(P)` sem `P` → rejeita |
| `aabbcc` | seria `a²b²c²` ≠ `aᵐbᵐ⁺ᵖcᵖ` com `m=2` (faltam `b`s da fatia `p`) | **rejeita** |

### Simulação: `abbc` (`m=1,p=1`)

| Passo | Lê | Pilha | Estado | Arco |
|------:|----|-------|--------|------|
| 0 | — | `ε` | 1 | — |
| 1 | `a` | `N` | 1 | `a/e(N)` |
| 2 | `b` | `ε` | 2 | `b/d(N)` |
| 3 | `b` | `P` | 3 | `b/e(P)` |
| 4 | `c` | `ε` | 4 | `c/d(P)` |
| 5 | fim | `ε` | 5 | `?/?` → **aceita** |

---

## Checklist

1. Empilha só nos `a` (`m`).
2. Nos `b`: primeiro zera a pilha (`m`); depois empilha `P` (`p`).
3. Nos `c`: só `d(P)` — tem de bater com `p`.
4. Sem `ε/ε`; `?/?` só no final.
