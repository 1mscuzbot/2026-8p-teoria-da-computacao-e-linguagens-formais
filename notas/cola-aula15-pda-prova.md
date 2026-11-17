# Cola — Prova hoje (PDA / AP)

**Matéria:** Teoria · Aula 15 · caderno + `Aula15-Automato-de-Pilha.pdf`  
**Foto:** `media/teoria-aula15-anotacoes.jpg`  
**Notação Furlan:** arco `λ / α` · `e(N)`/`emp(N)` empilha · `d(N)`/`des(N)` desempilha · `?` = fim de fita **ou** pilha vazia · `ε` = não lê / não mexe · aceita com **`?/?`** em estado final.

## Checklist mental
- [ ] Empilha numa fase, desempilha na outra (LIFO).
- [ ] `n,m≥1` ⇒ troca de estado no **1º** símbolo da próxima letra (**sem** `ε/ε` livre entre fases).
- [ ] Parênteses: no caderno há **`ε/ε`** entre fases (ex.3).
- [ ] `i≠j`: dois finais **F1** (sobra na pilha) e **F2** (`b` com pilha vazia).
- [ ] `aⁿbⁿcⁿ` **não** tem AP (uma pilha ≠ dois contadores livres).

---

## 0.5 — NFA curto
```text
> (q0) --a,ε--> (q1) --b,ε--> ((qf))
```

## 1 — `L={aⁿbⁿ | n≥1}`
```text
> (1) --a/e(N)--> (1)
   │ b/d(N)
   ▼
  (2) --b/d(N)--> (2)
   │ ?/?
   ▼
 ((0)) FINAL
```
Ex.: `aaabbb` — empilha 3×`N`, desempilha 3×, `?/?`.

## 2 — `S → aSa | b` → PDA
Palíndromo ímpar com `b` no meio (`aba`, `aabaa`…).
```text
> (0) --a/e(N)--> (0)
   │ b/ε
   ▼
  (2) --a/d(N)--> (2)
   │ ?/?
   ▼
 ((0))
```

## 3 — Parênteses casados *(estilo caderno: ε/ε)*
```text
> (1) --(/e(N)--> (1)
   │ ε/ε          (ida; no caderno pode haver volta)
   ▼
  (2) --)/d(N)--> (2)
   │ ?/?
   ▼
 ((0))
```
**Compacto (docs):** um só estado com `(/e(N)` e `)/d(N)` + `?/?` — aceita `()()` e `((()))`.

## 4 — `L={aⁿbᵐcᵐdⁿ | n,m≥1}`
Sem `ε/ε` entre letras. Preferir **N** (a/d) e **M** (b/c); no caderno b/c pode parecer só `N`.
```text
> (1)--a/e(N)-->(1)
   │ b/e(M)
   ▼
  (2)--b/e(M)-->(2)
   │ c/d(M)
   ▼
  (3)--c/d(M)-->(3)
   │ d/d(N)
   ▼
  (4)--d/d(N)-->(4)
   │ ?/?
   ▼
 ((5))
```

## 5 — `L={aⁱbʲ | i≠j, i,j≥1}` · F1 / F2
```text
> (1) --a/e(N)--> (1)
   │ b/d(N)
   ▼
  (2) --b/d(N)--> (2)
   │              │
   │ ?/?          │ b/?     (pilha vazia)
   ▼              ▼
 ((F1))          (3) --b/ε--> (3)
  i>j               │ ?/?
  (sobra N)         ▼
                  ((F2))  i<j
```
Caderno: F1 às vezes `?/d(N)`; F2 fecha com `?/ε`. **i=j** → não chega a final → rejeita.

---

## Gatilhos de prova
1. Desenhar AP de `aⁿbⁿ` ou parênteses com `e/d` + `?/?`.
2. Gramática `S→aSa|b` → PDA (meio `b/ε`).
3. `aⁿbᵐcᵐdⁿ` em 4 fases (troca no 1º símbolo).
4. `i≠j` com **dois** finais F1/F2.
5. Por que `aⁿbⁿcⁿ` é impossível no AP.
