# Provinha 3 — GR (Gramática Regular)

**Disciplina:** Teoria da Computação e Linguagens Formais (Prof. Diógenes Furlan)  
**Aula:** 13 · Slide `material/slides/2_BIMESTRE/Aula13-GR.pdf`  
**Formato:** enunciados no estilo do professor + gabarito passo a passo

---

## Lembrete (1 linha)

GR: só `X → w`, `X → wY` ou `X → ε` (`w ∈ Σ`). LR ⇔ existe GR. Equivalência prática: **GR ↔ NFA**.

---

## Enunciados

### 1) Formas

Liste as **três** formas de produção de uma GR. Dê um exemplo de produção **válida em GLC mas inválida em GR**.

### 2) Linguagem gerada

Quais são as linguagens (ou ERs) geradas?

a)
```text
S → aA
A → aA | a
```

b)
```text
S → 0S | 1A
A → 1A | ε
```

c)
```text
S → bA
A → aA | bA | a
```

### 3) Criar GR

Crie GRs para:

a) `(a+b+c)+`  
b) palavras que começam com `a` e terminam com `c` (ER: `a(a+b+c)*c`)  
c) número **ímpar** de `a`s sobre `{a,b}`  
d) tamanho **múltiplo de 3** sobre `{a,b}`  
e) penúltimo símbolo é `b` (sobre `{a,b}`)

### 4) GR → NFA

Transforme em NFA (tabela ou desenho; indique `s` e `F`):

a)
```text
S → 0S | ε
```

b)
```text
S → 0S | 1A
A → 1A | ε
```

c)
```text
S → aA
A → aA | bA | b
```

### 5) NFA → GR

Dado o NFA (`s = A`, `F = {B,C}`):

|   | 0   | 1   |
|---|-----|-----|
| A | A,C | A,B |
| B | ∅   | B   |
| C | B   | A   |

Obtenha a GR correspondente.

### 6) (Opcional) Armadilha

A produção `S → aSb` é GR? Justifique em uma linha.

---

## Gabarito / resolução

### 1) Formas

1. `X → w`  
2. `X → wY`  
3. `X → ε`  

Exemplo só-GLC: `S → aSb` (terminais dos dois lados da variável).

---

### 2) Linguagem gerada

**a)** `S → aA`, `A → aA | a` ⇒ pelo menos dois `a`s: `aa+`.  
ER: `aa⁺` (ou `aaa*`).

**b)** Zero ou mais `0`, depois zero ou mais `1`, e a palavra **pode** terminar após os `0`s (`A→ε` e também dá para “pular” via… na verdade: de `S` só sai `0S` ou `1A`; para aceitar só `0*`, precisa `S→ε` — **aqui não há**.  
Caminho: `0*` depois **pelo menos um** `1`, depois `1*`.  
⇒ ER: `0*11*` = `0*1⁺`.

**c)** Começa com `b`, depois `(a+b)*`, termina com `a`.  
⇒ ER: `b(a+b)*a`.

---

### 3) Criar GR

**a)** `(a+b+c)+` — pelo menos um símbolo:

```text
S → aA | bA | cA
A → aA | bA | cA | ε
```

(Ou `S → aS | bS | cS | a | b | c`.)

**b)** Começa `a`, termina `c`:

```text
S → aA
A → aA | bA | cA | c
```

(Se a palavra mínima for `ac`; `a` sozinho **não** entra — coerente com a ER `a(a+b+c)*c`.)

**c)** Ímpar de `a`s (paridade; `b` não muda):

```text
P → bP | aI          # P = par (inicial)
I → bI | aP | ε      # I = ímpar (final via ε)
```

Começamos em **par** (0 `a`s). Aceita só em ímpar ⇒ estado/variável `I` final.

**d)** Tamanho ×3:

```text
S → aA | bA | ε      # resto 0 (mod 3) — final
A → aB | bB          # resto 1
B → aS | bS          # resto 2
```

**e)** Penúltimo = `b` (precisa ≥2 símbolos):

```text
S → aS | bS | aB | bB   # “ainda não fixou o penúltimo”
B → a | b               # B = “último símbolo foi b” → emite o último
```

Mais limpo (estados: viu algo / último foi b):

```text
S → aS | bA
A → aS | bA | a | b
```

`A` = “o símbolo anterior foi `b`”; ao emitir o último terminal a partir de `A`, o penúltimo fica `b`.

---

### 4) GR → NFA

**Receita Furlan:** variável → estado; `X→wY` ⇒ `Y ∈ δ(X,w)`; `X→w` ⇒ criar final `Z`, `Z ∈ δ(X,w)`; `X→ε` ⇒ `X` final.

**a)** `S → 0S | ε`  
`s = S`, `F = {S}` (por `ε`). Sem `Z`.

|   | 0 |
|---|---|
| →=S | S |

**b)** `S → 0S | 1A`, `A → 1A | ε`  
`s = S`, `F = {A}`.

|   | 0 | 1 |
|---|---|---|
| →S | S | A |
| =A | ∅ | A |

**c)** `S → aA`, `A → aA | bA | b`  
Há `A → b` (forma `X→w`) ⇒ criar `Z` final.  
`s = S`, `F = {Z}`.

|   | a | b |
|---|---|---|
| →S | A | ∅ |
| A  | A | A,Z |
| =Z | ∅ | ∅ |

---

### 5) NFA → GR

**Receita:** estado → variável; `Y ∈ δ(X,w)` ⇒ `X → wY`; final `X` ⇒ `X → ε`.

```text
A → 0A | 0C | 1A | 1B
B → 1B | ε
C → 0B | 1A | ε
```

(Exemplo do próprio slide.)

---

### 6) Armadilha

`S → aSb` **não** é GR: o RHS tem terminal **depois** da variável (forma livre de contexto, não regular).

---

## Checklist rápido

- [ ] 3 formas: `w`, `wY`, `ε`
- [ ] GR → NFA (não esquecer `Z` quando há `X→w`)
- [ ] NFA → GR (finais → `X→ε`)
- [ ] Criar GR a partir de ER / linguagem
