# Provinha 2 — GLC (Gramática Livre de Contexto)

**Disciplina:** Teoria da Computação e Linguagens Formais (Prof. Diógenes Furlan)  
**Aula:** 12 · Slide `material/slides/2_BIMESTRE/Aula12-GLC.pdf`  
**Formato:** enunciados no estilo do professor + gabarito passo a passo

---

## Lembrete (1 linha)

GLC: toda produção `X → α` com `X ∈ V` e `α ∈ (V ∪ Σ)*`. Linguagem livre de contexto (LLC) ⇔ existe GLC que a gera.

---

## Enunciados

### 1) Definição

Diga, em uma frase, o que caracteriza uma **GLC** (forma das produções) e o que é uma **LLC**.

### 2) Criar GLC

Crie GLCs que gerem:

a) `L = { aⁱbⁱ | i > 0 }`  
b) `L =` palavras **palíndromos** sobre `{a,b}`  
c) `L = { aⁱbʲ | i ≠ j }` (i, j ≥ 0)

### 3) Linguagem gerada

Quais são as linguagens geradas?

a)
```text
S → A
A → aAb | ε
```

b)
```text
S → AB
A → aAb | ε
B → bBa | ε
```

c)
```text
S → AB
A → S | a
B → S | b
```

### 4) Criar GLC (exercício-tipo do slide)

a) `L = { w · wʳ | w ∈ {a,b}* }`  
b) strings sobre `{0,1}` com o **mesmo número** de 0’s e 1’s  
c) `L = { aⁱbⁱ ∪ bⁱaⁱ | i > 0 }`

### 5) Classificar produção

Para cada produção, diga se é **válida em GLC** e se também seria **válida em GR**:

a) `A → aB`  
b) `A → aBb`  
c) `AB → a`  
d) `A → ε`

### 6) (Opcional) Parênteses

Dê uma GLC para palavras com **parênteses balanceados** sobre `{x, y, (, )}` (os símbolos `x,y` podem aparecer livremente; `(`/`)` devem casar).

---

## Gabarito / resolução

### 1) Definição

- **GLC:** cada produção tem forma `X → α` (LHS = **uma** variável; RHS = qualquer string de variáveis e/ou terminais, inclusive ε).  
- **LLC:** linguagem para a qual **existe** alguma GLC que a gera.

---

### 2) Criar GLC

**a)** `aⁱbⁱ` com i > 0 (pelo menos um par):

```text
S → aSb | ab
```

(Equivalente: `S → aA`, `A → aAb | b`.)

**b)** Palíndromos sobre `{a,b}`:

```text
S → aSa | bSb | a | b | ε
```

Centro ímpar: `a` ou `b`; centro par / vazio: `ε`.

**c)** `aⁱbʲ` com i ≠ j:

Dois casos: mais `a`s **ou** mais `b`s.

```text
S → A | B
A → aA | aC          # sobra ≥1 a (i > j)
B → Bb | Cb          # sobra ≥1 b (j > i)
C → aCb | ε          # parte “igual” aᵏbᵏ
```

Ideia: `C` gera o núcleo balanceado; `A`/`B` acrescentam o excesso de `a` ou de `b`.

---

### 3) Linguagem gerada

**a)** `A → aAb | ε` gera `aⁿbⁿ` (n ≥ 0); `S → A` só renomeia.  
⇒ `L = { aⁿbⁿ | n ≥ 0 }`.

**b)** `A` gera `aᵐbᵐ`; `B` gera `bⁿaⁿ`; `S → AB` concatena.  
⇒ `L = { aᵐbᵐ bⁿ aⁿ | m,n ≥ 0 } = { aᵐ bᵐ⁺ⁿ aⁿ | m,n ≥ 0 }`.

**c)** Como no slide/Aula 11: `A` e `B` podem “voltar” a `S` ou emitir terminal.  
⇒ toda palavra da forma `a · (a+b)* · b` (começa com `a`, termina com `b`).  
ER: `a(a+b)*b`.

---

### 4) Criar GLC

**a)** `w · wʳ` (palíndromo **par** — sem símbolo central “solto” além do espelhamento):

```text
S → aSa | bSb | ε
```

(Se o slide pedir exatamente `w.wʳ`, essa é a forma canônica.)

**b)** Mesmo nº de 0’s e 1’s (clássico):

```text
S → SS | 0S1 | 1S0 | ε
```

(Alternativa: `S → 0S1S | 1S0S | ε`.)

**c)** `aⁱbⁱ` **ou** `bⁱaⁱ`, i > 0:

```text
S → A | B
A → aAb | ab
B → bBa | ba
```

---

### 5) Classificar

| | GLC? | GR? |
|---|------|-----|
| a) `A → aB` | sim | sim (`X→wY`) |
| b) `A → aBb` | sim | **não** (terminal dos dois lados da variável) |
| c) `AB → a` | **não** (LHS com 2 símbolos — fora de GLC) | não |
| d) `A → ε` | sim | sim (`X→ε`) |

---

### 6) Parênteses (opcional)

Ideia: `x` e `y` livres; `(` abre um “nível” GLC e `)` fecha.

```text
S → SS | (S) | x | y | ε
```

(Se o enunciado **não** incluir a palavra vazia, tire `| ε` e force pelo menos um símbolo, p.ex. `S → SS | (S) | x | y | ()`.)

---

## Checklist rápido

- [ ] Produção GLC = `X → α` (1 variável à esquerda)
- [ ] Sabemos montar `aⁿbⁿ`, palíndromo, `i≠j`
- [ ] Sabemos **ler** uma GLC e descrever L
- [ ] Distinguir GLC × GR × inválida
