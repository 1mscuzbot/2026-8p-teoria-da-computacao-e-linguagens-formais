# Revisão — Aulas 11 a 14 (Gramáticas → FNC)

**Disciplina:** Teoria da Computação e Linguagens Formais (Prof. Diógenes Furlan)  
**Escopo:** Aula 11 (Gramáticas) · Aula 12 (GLC) · Aula 13 (GR) · **Aula 14 (FNC)**  
**Slides:** `material/slides/2_BIMESTRE/Aula11-Gramaticas.pdf` … `Aula14-FNC.pdf`  
**Notas:** [estudo-aula13-gr](estudo-aula13-gr.md) · [estudo-aula14-fnc](estudo-aula14-fnc.md)  
**Outline de slides (opcional):** [revisao-aulas-11-14-slides-outline](revisao-aulas-11-14-slides-outline.md)

---

## Mapa mental (prova)

| Aula | Ideia em 1 linha | Forma das produções |
|------|------------------|---------------------|
| 11 | Gramática = gerador de palavras `G=(V,Σ,P,S)` | depende do tipo (hierarquia) |
| 12 | **GLC / LLC** — lado esquerdo = **1 variável** | `X → α`, `α ∈ (V∪Σ)*` |
| 13 | **GR / LR** — “quase” automato | `X→w` · `X→wY` · `X→ε` (`w` terminal) |
| 14 | **FNC** — árvores **binárias** (útil p/ CYK) | `A→V₁V₂` **ou** `A→t` |

**Hierarquia (Aula 11):** LRE ⊃ LSC ⊃ LLC ⊃ LR.  
**Ponte GR↔NFA (Aula 13):** variável ↔ estado; produção ↔ transição; `X→ε` ⇒ `X` final.

---

## Fórmulas / receitas para copiar

### Definição formal

`G = (V, Σ, P, S)` com `V ∩ Σ = ∅`, `S ∈ V`.

### GLC (Aula 12)

Toda produção: `X → α` com `X ∈ V`, `α ∈ (V ∪ Σ)*`.  
Exemplos clássicos: `{aⁿbⁿ | n≥0}`, palíndromos, parênteses balanceados.

### GR ↔ NFA (Aula 13)

| Direção | Regra |
|---------|--------|
| GR → NFA | `X→wY` ⇒ `Y ∈ δ(X,w)`; `X→w` ⇒ final auxiliar `Z ∈ δ(X,w)`; `X→ε` ⇒ `X` final |
| NFA → GR | `Y ∈ δ(X,w)` ⇒ `X→wY`; estado final `X` ⇒ `X→ε` |

### FNC — algoritmo (Aula 14)

1. **Simplificar** a GLC (inúteis, ε-produções, unitárias).
2. **Fase Δ:** em RHS com comprimento > 1, **só variáveis** — para cada terminal `a`, criar `Δₐ → a` e substituir.
3. **Fase Ω:** RHS com comprimento > 1 deve ter **exatamente 2** variáveis — quebrar com auxiliares `Ωᵢ`.

**Checklist FNC:** toda produção é `A→BC` ou `A→a`. Nada de `A→aB`, `A→ABC`, `A→ε` (exceto talvez S→ε se a linguagem incluir ε — fora do foco do slide).

---

## Bullets estilo prova

- [ ] Diferenciar **GR** (regular) de **GLC** (livre de contexto): `S→aSb` é GLC, **não** GR.
- [ ] Montar `G=(V,Σ,P,S)` a partir de uma ER simples (`a+`, `a*`, `(ab)*`).
- [ ] Converter **GR ↔ NFA** sem esquecer o estado final auxiliar `Z` quando há `X→w`.
- [ ] Reconhecer linguagens **não regulares** tipicamente GLC: `aⁿbⁿ`, palíndromo, balanceamento.
- [ ] Aplicar FNC na **ordem** simplificar → Δ → Ω (não inverter).
- [ ] Depois da FNC: AS fica **binária**; reproduzir o Exemplo 1 do slide até o fim.

---

## Exercícios de prática (com respostas)

### 1) Classificar a produção

Para cada produção, diga se é **permitida em GR**, **só em GLC** (não GR), ou **inválida até para GLC**:

a) `A → aB`  
b) `A → aBb`  
c) `AB → a`  
d) `A → ε`

**Respostas:**  
a) GR (e GLC).  
b) Só GLC (`w` na GR seria um terminal, não string com variável no meio).  
c) Inválida para GLC (LHS tem 2 símbolos — sensível/irrestrita).  
d) GR e GLC.

---

### 2) GR → NFA

```text
S → 0S | 1A
A → 1A | ε
```

**Resposta (esboço):** estados `S`, `A` (+ sem `Z` se não houver `X→w` puro; aqui `S→0S` e `S→1A` são `wY`; `A→1A`; `A→ε` ⇒ `A` final).  
`s=S`, `F={A}`:

|   | 0 | 1 |
|---|---|---|
| →S | S | A |
| =A | ∅ | A |

---

### 3) GLC clássica

Dê uma GLC para `L = { aⁿbⁿ | n ≥ 0 }`.

**Resposta:**

```text
S → aSb | ε
```

(`V={S}`, `Σ={a,b}`.)

---

### 4) FNC — fase Δ e Ω (mini Exemplo 1)

Partindo de (já “sem ε/unitárias” no espírito do slide):

```text
P → APB | Ca
A → AaaA | b
B → BBb | aC
C → cC | d
```

**Após Δ** (`X→a`, `Y→b`, `Z→c`):

```text
P → APB | CX
A → AXXA | b
B → BBY | XC
C → ZC | d
```

**Após Ω** (`K→AP`, `L→AX`, `M→XA`, `N→BB`):

```text
P → KB | CX
A → LM | b
B → NY | XC
C → ZC | d
X → a    Y → b    Z → c
K → AP   L → AX   M → XA   N → BB
```

---

### 5) FNC rápida

Coloque em FNC (sem ε):

```text
S → a | aSa
```

**Resposta (uma possível):**

- Δ: `X→a` ⇒ `S → X | XSX` (ou `S→a | XSX` mantendo `S→a`).
- Ω: `S → X | TY`, `T → XS`, `X → a`  
  (equivalente: `S→a | US`, `U→XS`, `X→a`).

Teste mental `"aaa"`: derivações binárias após FNC.

---

## Ordem sugerida de estudo (40–50 min)

1. Hierarquia + `G=(V,Σ,P,S)` (5 min) — Aula 11.  
2. GLC vs GR + 1 exemplo `aⁿbⁿ` (10 min) — Aulas 12–13.  
3. Uma conversão GR↔NFA no papel (10 min) — Aula 13.  
4. Exemplo 1 FNC completo + exercício 1 do slide (15–20 min) — Aula 14.  
5. Checklist final (5 min).

---

## Links rápidos

- Slide FNC: `material/slides/2_BIMESTRE/Aula14-FNC.pdf`
- Estudo FNC: [estudo-aula14-fnc.md](estudo-aula14-fnc.md)
- Estudo GR: [estudo-aula13-gr.md](estudo-aula13-gr.md)
