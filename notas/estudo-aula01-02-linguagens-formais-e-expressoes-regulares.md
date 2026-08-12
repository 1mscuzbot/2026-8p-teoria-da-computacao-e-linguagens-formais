# Teoria da Computação e Linguagens Formais — Estudo (Aulas 01 e 02)

**Disciplina:** Teoria da Computação e Linguagens Formais (Prof. Diógenes Furlan)
**Slides de referência:**
- `material/slides/Aula01-IntroducaoTCLF.pdf`
- `material/slides/Aula02-1-Expressoes Regulares.pdf`

---

# Aula 01 — Introdução às Linguagens Formais

## Conceitos-chave

- **Áreas da disciplina:**
  - **Teoria dos Autômatos** (Linguagens Formais) — modelos matemáticos de computação
  - **Teoria da Complexidade** — problemas "fáceis" (polinomiais) × "difíceis" (exponenciais)
  - **Teoria da Computabilidade** — problemas "solúveis" × "insolúveis"
- **Complexidade × hardware:** um bom algoritmo em máquina lenta ganha de um algoritmo ruim em máquina rápida (ex.: bolha `2n²` vs quicksort `50·n·log n`; a partir de 10⁶ elementos o algoritmo bom domina).
- **Classificação de problemas:**
  - *Decisão:* resposta sim/não (decidibilidade)
  - *Busca:* devolve uma solução se existir
  - *Otimização:* melhor solução entre as viáveis
  - *Solucionável:* existe algoritmo que sempre para com ACEITA/REJEITA
- **Hipótese de Church:** a Máquina de Turing é o limite máximo de qualquer dispositivo de computação (equivalentes: máquina de Post, máquina de 2 pilhas, máquina Norma, funções recursivas).
- **Linguagens:**
  - Finita → pode ser enumerada; Infinita → precisa de representação finita (contável × incontável)
  - Formal = representável de forma finita e precisa
  - **Linguagem** L sobre alfabeto Σ: L ⊆ Σ* (conjunto de palavras)
- **Três formas de representar uma linguagem:**
  - **Descritor:** expressão regular (define quais palavras pertencem)
  - **Reconhecedor:** autômato finito (verifica se uma palavra pertence)
  - **Gerador:** gramática regular (gera as sentenças)
- **Hierarquia de Chomsky:**
  | Classe | Descritor | Reconhecedor | Gerador |
  |--------|-----------|--------------|---------|
  | Regular | Expressão Regular | Autômato Finito | Gramática Regular |
  | Livre de Contexto | — | Autômato de Pilha | Gramática Livre de Contexto |
  | Sensível ao Contexto | — | Autômato Linearmente Limitado | Gramática Sensível ao Contexto |
  | Enumerável Recursivamente | — | Máquina de Turing | Gramática Irrestrita |
- **Alfabeto (Σ):** conjunto **finito e não vazio** de símbolos.
- **Palavra:** sequência **finita** de símbolos justapostos por concatenação (sinônimos: sentença, string, cadeia). **ε** = palavra vazia (comprimento 0).

## Exercícios resolvidos

### 1. Quais conjuntos são alfabetos? (precisa ser finito e não vazio)

| Item | Conjunto | É alfabeto? | Justificativa |
|------|----------|:-----------:|---------------|
| a | números racionais | ✗ | conjunto infinito |
| b | letras gregas | ✓ | finito e não vazio ({α, β, γ, …}) |
| c | algarismos arábicos | ✓ | finito: {0,1,…,9} |
| d | 2^{a,b,c} (conjunto das partes) | ✓ | finito, 8 elementos: {∅,{a},{b},{c},{a,b},{a,c},{b,c},{a,b,c}} (os símbolos são subconjuntos) |
| e | {a,b,c}³ | ✓ | finito, 27 palavras de comprimento 3 |
| f | números primos | ✗ | conjunto infinito |

### 2. Prefixos e sufixos de `001122`

- **Prefixos** (pedaços iniciais, incluindo ε e a própria palavra): ε, `0`, `00`, `001`, `0011`, `00112`, `001122`
- **Sufixos** (pedaços finais): ε, `2`, `22`, `122`, `1122`, `01122`, `001122`

### 3. Σ = {0,1,2} — strings por comprimento

- **Σ²** = {00, 01, 02, 10, 11, 12, 20, 21, 22} → 3² = **9** strings
- **Σ³** = {000, …, 222} → 3³ = **27** strings
- **Σ⁴** → 3⁴ = **81** strings
- **Σ⁰** = {ε} (a palavra vazia; qualquer string elevada a 0)
- **Σ\*** = Σ⁰ ∪ Σ¹ ∪ Σ² ∪ … = **todas** as palavras finitas sobre Σ, incluindo ε (infinito contável)
- **Σ+** = Σ\* − {ε} = todas as palavras de comprimento ≥ 1

### 4. Palavras que pertencem / não pertencem (Σ = {a,b})

| Linguagem | Pertence | Não pertence | Por quê |
|-----------|----------|--------------|---------|
| a) L = {w \| w ∈ Σ³} | `aaa`, `aba`, `bba` | `aa`, `aaaa`, `ε` | só palavras de comprimento exatamente 3 |
| b) L = {w \| ∃u∈ΣΣ, w = u·a·u} | `abaab` (u=ab), `baaba` (u=ba), `aaaaa` (u=aa) | `aab`, `ababa`, `baab` | formato: 2 letras + `a` + as mesmas 2 letras (5 letras) |
| c) L = {w \| ∃u∈ΣΣ, w = u·uᴿ·u} | `abbaab` (u=ab), `baabba` (u=ba), `aaaaaa` (u=aa) | `ababab`, `aabbaa` | u repetido, depois o reverso, depois u de novo (6 letras) |
| d) L = {w \| ww = www} | `ε` | `a`, `ab`, `aba` | 2\|w\| = 3\|w\| ⇒ \|w\|=0 ⇒ w=ε |
| e) L = {w \| ∃u,v∈Σ\*, uvw = wvu} | **qualquer palavra** (ex.: `ab`) | nenhuma | com u = v = ε a igualdade vira w = w, sempre verdadeira ⇒ L = Σ\* |
| f) L = {w \| ∃u∈Σ\*, www = uu} | `aaaa` (u=`aaaaaa`), `abab` (u=`ababab`) | `a`, `ab`, `aab` | www precisa ser um "quadrado" (w = t·t); \|w\| ímpar impossibilita |

### 5. Algoritmo: todas as palavras de 4 letras sobre Σ = {a,b,c,d,e}

```python
from itertools import product

Sigma = "abcde"
palavras = ["".join(w) for w in product(Sigma, repeat=4)]
print(len(palavras))  # 625 = 5^4
for p in palavras:
    print(p)
```

C++ equivalente: 5 laços encadeados (4 posições × 5 letras) ou recursão.

### 6. Dá para gerar Σ\*?

**Sim.** Σ\* é **infinito contável**, então é impossível gerar "tudo de uma vez", mas dá para **enumerar** todas as palavras em ordem de comprimento (cada palavra é gerada em tempo finito; o programa simplesmente nunca termina):

```python
from itertools import product

def sigma_star(Sigma):
    n = 0
    while True:
        for w in product(Sigma, repeat=n):
            yield "".join(w)   # ε, depois a,b,..., depois aa, ab, ...
        n += 1
```

---

# Aula 02 — Expressões Regulares

## Definição formal

Uma **ER** sobre um alfabeto Σ gera uma linguagem conforme a tabela abaixo (ρ = ER(R), σ = ER(S)):

| Regra | ER | Linguagem gerada |
|-------|-----|------------------|
| (1) conjunto vazio | ∅ | ∅ |
| (2) palavra vazia | ε | {ε} |
| (3) símbolo | a (∀a∈Σ) | {a} |
| (4) **união** | R ∪ S (escrito R+S) | L(R) ∪ L(S) |
| (5) **concatenação** | R·S (ou RS) | {xy \| x∈L(R), y∈L(S)} |
| (6) **fechamento de Kleene** | R\* | {ε} ∪ {x·y \| x,y∈L(R)} ∪ … (0 ou mais repetições) |

**Notações:** `R+` = uma ou mais repetições (= R·R\*); `a^k` = a repetida k vezes; `a^(0-3)` = a⁰|a¹|a²|a³.

## Omissão de parênteses e prioridades

1. União é **associativa** → `(r1+(r2+…+rn))` vira `r1+r2+…+rn`
2. Concatenação é **associativa** → `(r1·(r2·…·rn))` vira `r1·r2·…·rn`
3. Parênteses externos podem ser omitidos
4. **Prioridade:** fecho de Kleene (`*`) > concatenação (`.`) > união (`+`)

## Exemplos resolvidos (Σ = {a,b})

| # | Expressão | Linguagem (o que ela representa) |
|----|-----------|----------------------------------|
| 1 | L = ∅ | linguagem **vazia** — nenhuma palavra pertence |
| 2 | L = {ε} | apenas a **palavra vazia** |
| 3 | L = {a,b} = {a} ∪ {b} | união: a palavra "a" ou a palavra "b" |
| 4 | L = {aa} = {a}×{a} | concatenação: "aa" |
| 5 | L = {a,b}×{b,c} | concatenação (produto): {ab, ac, bb, bc} |
| 6 | a\* | {ε, a, aa, aaa, …} — **0 ou mais** repetições de `a` |
| 7 | a+ | {a, aa, aaa, …} — **1 ou mais** repetições de `a` (a+ = a·a\*) |
| 8 | (a+b)\* | **todas** as palavras sobre {a,b}, incluindo ε |
| 9 | (ab)\* | {ε, ab, abab, ababab, …} — repetições de "ab" |
| 10 | b+a\* | (b+)(a\*) = {bⁱaʲ \| i≥1, j≥0} — **um ou mais b's** seguidos de a's (ex.: b, bb, ba, bba, bbaa) |
| 11 | (b+a)\* | blocos "b⁺" ou "a" repetidos; como todo bloco de b's pode ser seu próprio bloco, **equivale a {a,b}\*** |
| 12 | ba\* | {b·aʲ \| j≥0} = {b, ba, baa, baaa, …} — um `b` seguido de a's |
| 13 | (ba)\* | {ε, ba, baba, bababa, …} — repetições de "ba" |
| 14 | (a+b\*)\* | blocos "a" ou "b\*" repetidos; equivale a **{a,b}\*** (cada a é um bloco, cada run de b's é um bloco b\*) |
| 15 | a\* + b\* | {aⁱ \| i≥0} ∪ {bʲ \| j≥0} — **só a's ou só b's** (não mistura; inclui ε) |
| 16 | a\*.b\* | {aⁱbʲ \| i,j ≥ 0} — a's seguidos de b's (ex.: ε, a, b, ab, aab, abb) |
| 17 | (a+b)² | todas as palavras de comprimento exatamente 2: {aa, ab, ba, bb} |
| 18 | (ab)² | (ab)(ab) = **{abab}** |
| 19 | a².b² | **{aabb}** |
| 20 | (a+b)³ | todas as palavras de comprimento exatamente 3: {aaa, aab, aba, abb, baa, bab, bba, bbb} (2³ = 8) |
| 21 | a⁰⁻⁵ | {a⁰, a¹, a², a³, a⁴, a⁵} = {ε, a, aa, aaa, aaaa, aaaaa} — de 0 a 5 a's |
| 22 | a³.b⁴ | **{aaabbbb}** — 3 a's seguidos de 4 b's |

## Exercícios resolvidos

### 1–10: descrever as linguagens das ERs

| # | ER | Linguagem (conjunto de palavras) | Exemplos de palavras |
|----|-----|----------------------------------|----------------------|
| 1 | (a+b+c)\* | **todas** as strings sobre {a,b,c}, incluindo ε | ε, a, c, abc, cba, aabbcc |
| 2 | (bc)\* | {ε, bc, bcbc, bcbcbc, …} — repetições de "bc" | ε, bc, bcbc, bcbcbc |
| 3 | b\* + c\* | {b^k \| k≥0} ∪ {c^k \| k≥0} — só b's **ou** só c's (sem misturar) | ε, b, c, bb, ccc; **não**: bc, bcb |
| 4 | a\*·c\* | {aⁱcʲ \| i,j ≥ 0} — a's seguidos de c's | ε, a, c, ac, aac, acc, aacc |
| 5 | (a+b+c)³ | todas as 27 palavras de comprimento exatamente 3 | aaa, aab, abc, cba, ccc; **não**: ε, aa, abcd |
| 6 | (abc)³ | {abcabcabc} — uma única palavra | abcabcabc (única) |
| 7 | a³·b²·c⁴ | {aaabbcccc} — uma única palavra | aaabbcccc (única) |
| 8 | a + b³ | {a, bbb} — a palavra "a" ou a palavra "bbb" | a, bbb; **não**: ab, bb, aa |
| 9 | (ab)^(0-3) | {ε, ab, abab, ababab} | ε, ab, abab, ababab; **não**: aba, ababa, abababab |
| 10 | a·(a+b)\*·b | strings que **começam com `a` e terminam com `b`** (com qualquer meio) | ab, aaab, abab, aabb; **não**: a, b, aba |

### 23: retirar o máximo de parênteses sem mudar o significado

**a) `((a+((a+b)a))+(bb))`**
- externos: `a+((a+b)a)+(bb)`; `(bb)` → `bb`
- `((a+b)a)` = (a+b)·a → precisa manter `(a+b)a`, pois `a+ba` ≠ (a+b)a
- **resultado:** `a+(a+b)a+bb`

**b) `(((aa)+(b(bb*)))*((ab)((ab)(a+b))))`**
- `(aa)` → `aa`; `(b(bb*))` → `b(bb*)` → `bbb*`
- grupo estrelado: `(aa+bbb*)*` (parênteses **obrigatórios**, senão `aa+bbb**` mudaria)
- `((ab)((ab)(a+b)))` → `ab·ab·(a+b)` → `abab(a+b)` (só `(a+b)` precisa de parênteses)
- **resultado:** `(aa+bbb*)*abab(a+b)`

**c) `(((aa)a+b)+((aa)+(a+(bb))))`**
- `((aa)a)` = aa·a → `aaa`; `(bb)` → `bb`; `(a+(bb))` → `a+bb`
- uniões associativas → juntar tudo
- **resultado:** `aaa+b+aa+a+bb` (ou `a³+b+a²+a+bb`)

**d) `(((a)(a)+(ab))+((ba)+(b)(b)))*+(a(b(c)))`**
- `((a)(a)+(ab))` → `aa+ab`; `((ba)+(b)(b))` → `ba+bb`
- grupo estrelado: `(aa+ab+ba+bb)*`
- `(a(b(c)))` → `abc`
- **resultado:** `(aa+ab+ba+bb)*+abc`

### 24: verificar se a palavra pertence ao conjunto regular

**a) `aababaaab` ∈ `(a*b)*`?** → **pertence** ✓
Segmente em blocos `aⁱ·b`: `aab` (a²b) + `ab` (a¹b) + `aab` (a²b). Todo bloco é `aⁱb`.

**b) `baaab` ∈ `ba*`?** → **não pertence** ✗
`ba*` = um `b` seguido **só de a's**. A palavra `baaab` tem um `b` sobrando no final.

**c) `abaaabaa` ∈ `(a+b)*.a.a.(a+b)*`?** → **pertence** ✓
Basta conter "aa". Segmentação: `ab` + `aa` + `abaa`. (O prefixo e o sufixo são qualquer coisa.)

**d) `ababbaa` ∈ `(b+ab)*.aa.(a+b)*`?** → **pertence** ✓
`ababb` + `aa` + `ε`. E `ababb` = `(ab)(ab)(b)` ∈ (b+ab)\*.

**e) `abbbabbb` ∈ `(b*a.b)*.(b.b+a*)`?** → **pertence** ✓
Note que `(b*b)·a` = `b⁺a`. Segmentação: `ab` (b⁰ab) + `bbab` (b²ab) + `bb`. Ou seja `(b⁰ab)(b²ab)(bb)`.

**f) `bbbaabbb` ∈ `((b*.a)*+a*.b.b)`?** → **não pertence** ✗
Primeira opção `(b*·a)*` termina sempre em `a`, mas a palavra termina em `b`. Segunda opção `a*·b·b` = a's seguidos de **exatamente dois** b's, mas a palavra começa com b's.

**g) `abbbaabab` ∈ `a.b*.b.a*.(b.b*.a)`?** → **não pertence** ✗
O último fator `b·b*·a` (= `b⁺a`) termina obrigatoriamente em `a`, mas a palavra termina em `b`. (Sem nem precisar testar o restante.)

**h) `baaaabb` ∈ `(b.a*+b.b)*.(a*.b)*`?** → **pertence** ✓
Segmentação: `baaaa` (b·a⁴ ∈ b·a\*) + `bb` (b·b ∈ b·b), e a segunda parte `(a*b)*` com zero repetições (ε). Ou seja `(ba⁴)(bb)·ε`.

---

## Dica de verificação

Todas as pertinências do exercício 24 foram conferidas por programa:

```python
import re
casos = [
    ("aababaaab", r"^(a*b)*$"),
    ("baaab",     r"^ba*$"),
    ("abaaabaa",  r"^(a|b)*aa(a|b)*$"),
    ("ababbaa",   r"^(b|ab)*aa(a|b)*$"),
    ("abbbabbb",  r"^(b*ab)*(bb|a*)$"),
    ("bbbaabbb",  r"^((b*a)*|a*bb)$"),
    ("abbbaabab", r"^ab*b a*(bb*a)$"),
    ("baaaabb",   r"^(ba*|bb)*(a*b)*$"),
]
for palavra, er in casos:
    print(palavra, "->", bool(re.fullmatch(er, palavra)))
```

Resultado: a, c, d, e, h pertencem; b, f, g não pertencem.
