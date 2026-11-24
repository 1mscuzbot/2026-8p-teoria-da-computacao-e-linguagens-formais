# Provinha 4 — FNC (Forma Normal de Chomsky)

**Disciplina:** Teoria da Computação e Linguagens Formais (Prof. Diógenes Furlan)  
**Aula:** 14 · Slide `material/slides/2_BIMESTRE/Aula14-FNC.pdf`  
**Formato:** enunciados no estilo do professor + gabarito passo a passo

---

## Lembrete (1 linha)

FNC: só `A → BC` (2 variáveis) **ou** `A → a` (1 terminal). AS binária. Ordem: **simplificar → Δ → Ω**.

---

## Enunciados

### 1) Definição e ordem

a) Quais formas de produção a FNC permite?  
b) Qual a ordem correta do algoritmo? Por que **não** fazer Ω antes de Δ?

### 2) Mini — `S → a | aSa`

Coloque em FNC e **teste** a palavra `"aaa"` (derivação ou esboço de AS).

### 3) Exemplo 1 do slide (completo)

Partindo de (já no espírito “simplificada” do slide):

```text
P → APB | Ca
A → AaaA | b
B → BBb | aC
C → cC | d
```

Aplique **Δ** e depois **Ω**. Mostre as duas etapas e o resultado final.

### 4) Exercício do slide

Coloque em FNC:

```text
S → aSd | aAd
A → bAc | bc
```

### 5) Com ε (Exemplo 2 — enunciado do slide)

```text
S → ABC | aS
A → CC | ab
B → bB | b
C → aC | ε
```

Indique **o que fazer antes** de Δ/Ω e por quê. (Não é obrigatório fechar toda a simplificação se o tempo apertar — mas diga os passos.)

### 6) Checklist / armadilhas

Marque V ou F:

a) `A → aB` pode aparecer no resultado final da FNC.  
b) `A → a` sozinha já está em FNC (não precisa de Δ).  
c) `A → ABC` após Δ ainda precisa de Ω.  
d) Toda AS após FNC é binária.

---

## Gabarito / resolução

### 1) Definição e ordem

**a)** `A → V₁V₂` ou `A → t`.

**b)** Ordem: **simplificar** (inúteis, ε, unitárias) → **Δ** (RHS longo só com variáveis) → **Ω** (RHS longo com exatamente 2 variáveis).

Se fizer Ω antes de Δ, ainda restam terminais misturados (`A → aBC` etc.) e a gramática **não** fica em FNC.

---

### 2) `S → a | aSa`

**Δ:** o RHS `aSa` mistura terminais → criar `X → a` e trocar:

```text
S → a | XSX
X → a
```

(`S → a` já é FNC; não “delta-ificar” à toa.)

**Ω:** `XSX` tem 3 variáveis → quebrar, p.ex.:

```text
S → a | UT
U → XS
T → SX
X → a
```

(Equivalente do slide/cola: `S → a | US`, `U → XS`, `X → a`.)

**Teste `"aaa"`** (com `S → a | US`, `U → XS`, `X → a`):

```text
S ⇒ US ⇒ XSS ⇒ aSS ⇒ aaS ⇒ aaa
```

AS binária: cada passo interno usa 2 filhos não-terminais (ou folha terminal).

---

### 3) Exemplo 1 — Δ e Ω

**Após Δ** (`X→a`, `Y→b`, `Z→c`):

```text
P → APB | CX
A → AXXA | b
B → BBY | XC
C → ZC | d
X → a
Y → b
Z → c
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

Conferência: só `BC` ou `a` → **FNC**.

---

### 4) `S → aSd | aAd`, `A → bAc | bc`

**Δ** (`X→a`, `Y→b`, `Z→c`, `W→d`):

```text
S → XSW | XAW
A → YAZ | YZ
X → a  Y → b  Z → c  W → d
```

**Ω** (quebrar ternários; `YZ` já é binário):

```text
S → XP | XQ
P → SW
Q → AW
A → YR | YZ
R → AZ
X → a  Y → b  Z → c  W → d
```

(Nomes das auxiliares podem variar; o esquema de pareamento deve ser consistente.)

---

### 5) Com ε

Há `C → ε` ⇒ **não** pular direto para Δ.

Antes: **simplificar** a GLC (remover ε-produções, depois unitárias/inúteis se surgirem), **aí** Δ → Ω.

Motivo: FNC do slide assume produções só `BC` ou `a`; `ε` (salvo tratamento especial de `S→ε` se L contém ε) não entra no resultado padrão.

Esboço após eliminar ε de `C` (ideia): onde `C` era anulável, duplicar produções com/sem `C`; `A → CC` vira `A → CC | C` (e se `C` ainda puder ser ε em cadeia, continuar até estabilizar); depois limpar unitárias etc. Só então Δ/Ω.

---

### 6) V/F

| | | |
|---|---|---|
| a) `A → aB` no final | **F** | falhou Δ |
| b) `A → a` já é FNC | **V** | |
| c) `A → ABC` precisa Ω | **V** | 3 variáveis |
| d) AS binária | **V** | importância da FNC |

---

## Checklist rápido (prova)

- [ ] Só `A→BC` ou `A→a`?
- [ ] Ordem: simplificar → Δ → Ω?
- [ ] Toda auxiliar (`X,Y,K…`) tem produção?
- [ ] Não deixei `A→aB`, `A→ABC`, `A→ε` no resultado?
