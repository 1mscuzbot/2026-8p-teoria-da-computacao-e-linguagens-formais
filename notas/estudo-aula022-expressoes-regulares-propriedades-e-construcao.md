# Aula 02.2 — Expressões Regulares: propriedades e construção

**Disciplina:** Teoria da Computação e Linguagens Formais (Prof. Diógenes Furlan)
**Slide de referência:** `material/slides/Aula02-2-Expressoes Regulares.pdf`

Complementa a [Aula 02.1 (definição de ER, prioridades, exercícios 1–24)](estudo-aula01-02-linguagens-formais-e-expressoes-regulares.md).

---

## Parte 1 — Lendo as propriedades das ERs

Ideia central: **escreve-se apenas a parte "positiva"** — aquela que realmente importa para formar as palavras; o resto é "qualquer coisa" `(a+b)*`.

| ER (Σ={a,b}) | Propriedade (em português) |
|--------------|----------------------------|
| (a+b)\*aa(a+b)\* | palavras que **contêm** a sequência "aa" |
| aa(a+b)\* | palavras **iniciadas** em "aa" |
| (a+b)\*aaa\* | palavras **terminadas** com pelo menos 2 a's (`aaa*` = a·a·a\* = a²·a\*) |
| aab(a+b)\* + aa | palavras **iniciadas por exatamente 2 a's** (`aa` ou `aa` + `b` + qualquer coisa) |

Para Σ={a,b,c,d}, basta trocar `(a+b)*` por `(a+b+c+d)*` e `(a+b)(a+b)c` por `(a+b+c+d)...` etc.

---

## Parte 2 — Construindo Expressões Regulares (exemplos do slide)

Alfabeto Σ={a,b}. A "parte positiva" é o trecho fixo; `(a+b)*` preenche o resto.

| # | Pedido | ER |
|---|--------|-----|
| 1 | palavras **iniciadas em** "ab" | `ab(a+b)*` |
| 2 | palavras **terminadas em** "ab" | `(a+b)*ab` |
| 3 | palavras que **possuem** a sequência "ab" | `(a+b)*ab(a+b)*` |
| 4 | palavras com **"b" na 3ª posição** | `(a+b)(a+b)b(a+b)*` |
| 5 | começam com "ab" **e** terminam com "ba" | `ab(a+b)*ba` |
| 6 | começam por "ba" **ou** "ab" | `(ba+ab)(a+b)*` |
| 7 | **número par** de a's | `(b*ab*ab*)*` |
| 8 | iniciadas com **quantidade par** de a's | `(aa)*(ε+b(a+b)*)` |
| 9 | iniciadas por **pelo menos 2** a's | `aa(a+b)*` |
| 10 | iniciadas por **exatamente 2** a's | `aa + aab(a+b)*` |
| 11 | contêm **somente 2 a's** (no total) | `b*ab*ab*` |
| 12 | contêm **apenas uma** sequência "ab" | `b*a+b+a*` |
| 13 | contêm **exatamente 20 a's** | `b*(ab*)²⁰` |
| 14 | **não** contêm a sequência "bb" | `(a+ba)*(ε+b)` |
| 15 | **não** iniciadas por "aba" | `b(a+b)* + a + aa(a+b)* + ab(ε+b(a+b)*)` |
| 16 | possuem **no máximo 2** a's | `b*(a+ε)b*(a+ε)b*` |

**Por quê:**
- **7:** cada repetição `b*ab*ab*` acrescenta 2 a's (par); o grupo `(...)*` repete 0+ vezes → sempre par.
- **8:** `(aa)*` consome os a's do início aos pares; depois ou acaba ou segue um `b`.
- **12:** `b*a+b+a*` — a única transição `a→b` ocorre entre `a+` e `b+`, gerando um único "ab".
- **14:** blocos `a` ou `ba` (todo `b` não-final é seguido de `a`) + opcional `b` final → nunca há "bb".
- **15:** todos os começos possíveis exceto "aba": `b…`, `a` sozinha, `aa…`, `ab` + `b…`.
- **16:** `b*` no início, meio e fim com 0, 1 ou 2 a's (cada um opcional via `(a+ε)`).

---

## Exercício 25 — descrever em português as linguagens sobre {a,b}

| ER | Linguagem |
|----|-----------|
| a) (a+b)\*a | palavras que **terminam em "a"** |
| b) (a+b)\*aa(a+b)\* | palavras que **contêm** a sequência "aa" |
| c) a(a+b)\*b | palavras que **começam com "a" e terminam com "b"** (comprimento ≥ 2) |
| d) a\*(a+b)b\* | palavras **não vazias** da forma a's seguidas de b's: {aⁱbʲ \| i+j ≥ 1} |
| e) (a+ba)(a+b)\* | palavras **iniciadas por "a" ou por "ba"** |
| f) (a+b)\*b(a+b)(a+b) | palavras de **comprimento ≥ 3** com **"b" na antepenúltima posição** |
| g) (a+b)(a+b)(a+b).a.b | palavras de **comprimento exatamente 5** que **terminam em "ab"** |
| h) a\*.b.(a+b) | a's (talvez vazio) + **"b" + um único símbolo** no final |
| i) (ab)\*(a+ε)+(ba)\*(b+ε) | palavras **alternadas** (sem dois símbolos iguais consecutivos), incluindo ε |
| j) b\*(abb\*)\*(a+ε) | palavras que **não contêm "aa"** |
| k) (a+ε)(ba+b)\* | palavras que **não contêm "aa"** (mesma linguagem de (j), construída de outro jeito) |

**Explicações importantes:**
- **d:** o símbolo do meio `(a+b)` é ou `a` (vira `aⁱ⁺¹bʲ`) ou `b` (vira `aⁱbʲ⁺¹`); unindo os dois casos, sobra apenas ε (i=j=0) de fora.
- **i:** `(ab)*(a+ε)` gera toda palavra alternada que **começa com a** (par ou ímpar); `(ba)*(b+ε)` gera as que **começam com b**; a união cobre todas.
- **j/k:** todo `a` é seguido de `b⁺` (ou é o `a` final) → nunca há dois a's seguidos. Como toda palavra sem "aa" se encaixa nesse padrão, `L(j) = L(k)` = "sem a sequência aa".

---

## Exercícios 26–42 — construir a ER (Σ={a,b}, itens 36/37/38 com {0,1})

| # | Pedido | ER |
|---|--------|-----|
| 26 | contém "bab" | `(a+b)*bab(a+b)*` |
| 27 | iniciadas por pelo menos 1 a | `a(a+b)*` |
| 28 | iniciadas por pelo menos 3 a's | `aaa(a+b)*` |
| 29 | iniciadas por exatamente 1 a | `a + ab(a+b)*` |
| 30 | iniciadas por exatamente 3 a's | `aaa + aaab(a+b)*` |
| 31 | iniciadas por exatamente k a's (1≤k≤10) | `aᵏ + aᵏb(a+b)*`, para cada k ∈ {1,…,10} |
| 32 | iniciadas por a's | `a(a+b)*` |
| 33 | comprimento ≥ 3 | `(a+b)(a+b)(a+b)(a+b)*` |
| 34 | comprimento ≤ 3 | `ε + (a+b) + (a+b)(a+b) + (a+b)(a+b)(a+b)` |
| 35 | sem "a" | `b*` |
| 36 | {101, 1001, 10001, 100001, …} | `1 0 0* 1` (um 1, um ou mais 0's, um 1) |
| 37 | cada 0 é seguido de dois 1 | `(1 + 011)*` |
| 38 | contém exatamente três 0's | `1*0 1*0 1*0 1*` |
| 39 | número ímpar de a's | `b*a(b*ab*a)*b*` |
| 40 | não começam por "aa" | `a + ab(a+b)* + b(a+b)*` |
| 41 | sem a sequência "ab" | `b*a*` |
| 42 | número igual de a's e b's (desafio) | **não existe** (não é regular!) |

**Explicações:**
- **29/30:** "exatamente n a's no início" = `aⁿ` sozinha **ou** `aⁿ` seguida de `b` (senão teria n+1 a's): `aⁿ + aⁿb(a+b)*`.
- **31:** não há uma única ER fixa — é uma família `aᵏ(ε + b(a+b)*)` para cada k de 1 a 10.
- **34:** `ε` cobre comprimento 0; cada `(a+b)` soma um símbolo, até 3.
- **36:** os números são `10ⁿ1` com n≥1 → `1·0·0*·1 = 100*1`.
- **37:** cada 0 obrigatoriamente vem num bloco `011`; os 1's livres são blocos `1`. Toda palavra com "todo 0 seguido de dois 1" se decompõe assim.
- **38:** três 0's com 1's livres entre eles → `1*0 1*0 1*0 1*`.
- **39:** `b*a` garante o primeiro a; `(b*ab*a)*` acrescenta a's **aos pares** (par+1 = ímpar); `b*` no fim.
- **40:** começar com `b`, ou começar com `a` e o segundo símbolo não ser `a` (ou ser só "a").
- **41:** sem "ab", uma vez que aparece um `a` nunca mais pode vir `b` → tudo em `b*a*`.
- **42:** **linguagem não regular** (clássico do Lema do Bombeamento/Pumping Lemma: `aⁿbⁿ` não pode ser "bombeada"). Logo, **não existe ER** para ela. É livre de contexto (gerada, por exemplo, por `S → aSbS | bSaS | ε`).

---

## Referências cruzadas

- Definição formal de ER e prioridades → [Aula 02.1](estudo-aula01-02-linguagens-formais-e-expressoes-regulares.md)
- Fecho de Kleene `*`, união `+`, concatenação e a "parte positiva" → slide Aula02-2
