# Aula 03 — Autômatos Finitos (AF/FA)

**Disciplina:** Teoria da Computação e Linguagens Formais (Prof. Diógenes Furlan)
**Slide de referência:** `material/slides/Aula03-Automatos Finitos.pdf`

Complementa as [Aulas 01–02 (linguagens e ERs)](estudo-aula01-02-linguagens-formais-e-expressoes-regulares.md) e a [Aula 02.2 (propriedades e construção de ERs)](estudo-aula022-expressoes-regulares-propriedades-e-construcao.md).

---

## Descrição informal

Um **autômato finito (AF / FA)** é um modelo matemático de um sistema com entradas e saídas discretas — um tipo de **Máquina de Estados**:

- O sistema pode estar em qualquer uma de suas **configurações internas**, chamadas de **estados**;
- **Estados** contêm informações relevantes sobre o **passado** do sistema (a "memória" do autômato);
- Cada **entrada** causa uma mudança de estado, chamada de **transição**.

### Exemplos do dia a dia

| Sistema | Estados | Transições |
|---------|---------|------------|
| Interruptor de luz | `ON`, `OFF` | pressionar botão alterna ON ↔ OFF |
| Elevador | `Parado`, `Vindo` | pressionar botão → Vindo; elevador chega → Parado |

---

## Exemplo introdutório — Problema do Fazendeiro

Um homem (h), um lobo (l), um carneiro (c) e uma alface (a) precisam atravessar um rio, com a restrição: **sem o homem, o lobo come o carneiro e o carneiro come a alface** (lobo e carneiro, ou carneiro e alface, nunca podem ficar sozinhos em uma margem).

- **Estado inicial:** `HLCA – ∅` (tudo na margem esquerda)
- **Estado final:** `∅ – HLCA` (tudo na margem direita)

Cada estado é da forma "margem esquerda / margem direita"; cada transição representa o homem atravessando **com ou sem** um passageiro.

| Passo | Transição | Estado | Observação |
|:-----:|-----------|--------|------------|
| 1 | h + c vão | `la – hc` | carneiro viaja primeiro |
| 2 | h volta | `hla – c` | alface fica com lobo? Não — lobo não come alface ✓ |
| 3 | h + a vão | `l – hca` | lobo sozinho ✓ |
| 4 | h + c voltam | `hlc – a` | **truque**: o carneiro volta para não ficar com o lobo... na margem esquerda: h, l, c (h presente ✓) |
| 5 | h + l vão | `c – hla` | carneiro sozinho ✓ |
| 6 | h volta | `hc – la` | lobo + alface juntos (não se comem ✓) |
| 7 | h + c vão | `∅ – hlca` | **fim!** |

---

## Descrição formal — Máquina de Estados

Componentes físicos/lógicos do modelo:

- **Fita de entrada:** guarda a palavra a ser processada (ex.: `a b a b a b`)
- **Cabeça de leitura:** lê **um símbolo por vez** e move-se para a direita
- **Controle finito:** aponta para o **estado atual** e decide a próxima transição

## Definição formal

Um autômato finito (AF) é uma **quíntupla** `(Q, Σ, δ, s, F)`:

| Componente | Símbolo | Significado |
|------------|---------|-------------|
| Q | conjunto de **estados** | configurações internas possíveis |
| Σ | **alfabeto de entrada** | símbolos que podem ser lidos |
| δ | **função de transição** | define o(s) estado(s) do passo seguinte: δ(qᵢ, α) = qⱼ |
| s ∈ Q | **estado inicial** | somente um |
| F ⊆ Q | conjunto de **estados finais** | estados de aceitação |

> Curiosidade: os autômatos finitos foram propostos originalmente para **modelar a função do cérebro humano**.

## Representação gráfica

| Elemento | Desenho |
|----------|---------|
| Estado | círculo com o nome dentro (ex.: q₁) |
| Transição α | seta de qᵢ para qⱼ rotulada com o símbolo lido |
| Estado inicial | seta sem origem entrando no estado |
| Estado final | círculo duplo |

## Funcionamento

1. **Início:** cabeça de leitura na extremidade **esquerda** da fita; controle no **estado inicial s**.
2. **A cada passo:** a cabeça **lê um símbolo** e move-se para a direita; o controle **muda de estado** conforme a função de transição.
3. **Condições de parada:**

| Situação | Resultado |
|----------|-----------|
| Fita processada por completo e estado atual é **final** | **Aceita** ✓ |
| Fita processada por completo e estado atual é **não final** | Rejeitada ✗ |
| δ é **indefinida** para (estado atual × símbolo lido) durante o processamento | Rejeitada ✗ |

---

## Exemplo: reconhecendo a palavra "FOR"

**Grafo:** estados 1 → 2 → 3 → 4, com o estado 4 final.

```
   F        O        R
1 ──→ 2 ──→ 3 ──→ 4   (4 = final)
```

**Tabela de transição (δ):**

| Estado | F | O | R |
|--------|---|---|---|
| 1 | 2 | – | – |
| 2 | – | 3 | – |
| 3 | – | – | 4 |
| 4 | – | – | – |

- `FOR` → 1 →F→ 2 →O→ 3 →R→ 4 (final) → **aceita**
- `FO` → para no estado 3 (não final) → **rejeitada**
- `FORA` → δ(4, A) indefinida → **rejeitada**

---

## Transformando ER em NFA

O slide pede a conversão de expressões regulares em **autômatos finitos não determinísticos (NFA)**, usando **transições nulas (ε)** quando necessário.

**Construção elementar (usando ε-transições):**

| ER | NFA resultante |
|----|----------------|
| `ε` ou `λ` ou `∅` | estado inicial que já é final (ou nenhum caminho) |
| `a` (símbolo) | i →a→ f |
| `R + S` (união) | ε-transições do novo inicial para os iniciais de R e de S; finais de R e S viram finais do todo |
| `R·S` (concatenação) | une o final de R ao inicial de S |
| `R*` (fecho de Kleene) | ε-transições: novo inicial → inicial de R; final de R → inicial de R e → novo final |
| `R+` | `R·R*` (uma ocorrência garantida + repetições) |

> Dica do slide: **problemas com loops exigem transição nula** (ex. exercícios 16 e 17).

**Ferramenta:** [JFLAP](http://www.jflap.org/jflaptmp/) (requer JVM / Java 8) permite montar e testar os autômatos graficamente.

## Exemplos do slide (ER → NFA)

Para cada ER, a construção segue o esquema acima. Esboços (estado inicial `1`, finais em negrito):

| # | ER | NFA (δ) |
|---|-----|---------|
| 1 | ε / λ | **1** (inicial e final, nenhuma transição) |
| 2 | a | 1 →a→ **2** |
| 3 | a + b | 1 →ε→ 2 (→a→ **3**); 1 →ε→ 4 (→b→ **5**) |
| 4 | a.b.c | 1 →a→ 2 →b→ 3 →c→ **4** |
| 5 | a\* | **1** →ε→ 2 →a→ 2 (loop); →ε→ **3** |
| 6 | a+ = a.a\* | 1 →a→ **2** →a→ 2 |
| 7 | (a+b)\* | **1** →ε→ 2 →a→ 3, 2 →ε(branch)→ 4 →b→ 5, retornos ε |
| 8 | (ab)\* | **1** →ε→ 2 →a→ 3 →b→ 2 |
| 9 | b + a\* | união: ramo b (1 →b→ **2**) + ramo a\* (**3** inicial-final do ramo) |
| 10 | b.a\* | 1 →b→ **2** →a→ 2 |
| 11 | (ba)\* | **1** →ε→ 2 →b→ 3 →a→ 2; →ε→ **4** |
| 12 | (ba)+ | 1 →b→ 2 →a→ **3** →b→ 2 |
| 13 | a\* + b\* | 1 →ε→ **2** →a→ 2; 1 →ε→ **3** →b→ 3 |
| 14 | a\*.b\* | 1 →a→ 1; 1 →ε→ **2** →b→ 2 |
| 15 | (a+b)² | 1 →a→ 2, 1 →b→ 2; 2 →a→ **3**, 2 →b→ **3** |
| 16 | (ab)² | 1 →a→ 2 →b→ 3 →a→ 4 →b→ **5** |
| 17 | a².b² | 1 →a→ 2 →a→ 3 →b→ 4 →b→ **5** |
| 18 | a⁰⁻² | 1 →ε→ **2** →a→ **3** →a→ **4** (todos finais: conta 0, 1 ou 2 a's) |

---

## Exercícios propostos (slide, 1–23)

Resoluções no mesmo estilo — `f` = final, `ε` = transição nula:

| # | ER | NFA (δ) |
|---|-----|---------|
| 1 | ab(c+d) | 1 →a→ 2 →b→ 3 →c→ f4; 3 →d→ f5 |
| 2 | (a+b)(a+b) | 1 →a→ 2, 1 →b→ 2; 2 →a→ f3, 2 →b→ f3 |
| 3 | ab + ba | 1 →a→ 2 →b→ f3; 1 →b→ 4 →a→ f5 |
| 4 | (ba)\* | f1 →b→ 2 →a→ 1 *(inicial também é final)* |
| 5 | b\*(a+b)a\* | f1 →b→ 1, 1 →ε→ 2; 2 →a→ f3, 2 →b→ f3; 3 →a→ 3 |
| 6 | (aaa)\* | f1 →a→ 2 →a→ 3 →a→ 1 |
| 7 | aaa\* | 1 →a→ 2 →a→ f3 →a→ 3 (dois a's + livre) |
| 8 | (a+b)\*aa(a+b)\* | 1 →a→ 2, 1 →b→ 1; 2 →a→ 3, 2 →b→ 1; f3 →a→ 3, 3 →b→ 3 |
| 9 | a(ba)\* | 1 →a→ f2 →b→ 3 →a→ 2 |
| 10 | a(b+a)\*b | 1 →a→ 2; 2 →a→ 2, 2 →b→ f3; 3 →a→ 2, 3 →b→ 3 |
| 11 | ba(baa)\* | 1 →b→ 2 →a→ f3 →b→ 4 →a→ 5 →a→ 3 |
| 12 | a(ba+abb) | 1 →a→ 2; 2 →b→ 3 →a→ f4; 2 →a→ 5 →b→ 6 →b→ f7 |
| 13 | a(ba+abb)\* | 1 →a→ f2; 2 →b→ 3 →a→ 2; 2 →a→ 4 →b→ 5 →b→ 2 |
| 14 | (ab+ba)ab | 1 →a→ 2 →b→ 3 →a→ f4; 1 →b→ 5 →a→ 6 →b→ f7 |
| 15 | (a+b)\*.b(a+b)(a+b) | 1 →a→ 1, 1 →b→ 1; 1 →b→ 2; 2 →a→ 3, 2 →b→ 3; 3 →a→ f4, 3 →b→ f4 |
| 16 | (a+ε)(ba+b)\* | f2 (ε de 1); 1 →a→ 2; 2 →b→ 2, 2 →b→ 3 →a→ 2 *(transição nula: 1 →ε→ 2)* |
| 17 | b\*(a.b\*.a.b\*)\* | 1 →b→ 1, 1 →ε→ f2; 2 →a→ 3 →b→ 3, 3 →ε→ 4 →a→ 5 →b→ 5, 5 →ε→ 2 *(loops pedem ε)* |
| 18 | a\*b\* | 1 →a→ 1, 1 →ε→ f2 →b→ 2 |
| 19 | a+(ba)\*ab+ | 1 →a→ 2; 2 →a→ 2, 2 →b→ 3 →a→ 2 *(loop (ba)\*)*; 2 →a→ 4 →b→ f5 →b→ 5 |
| 20 | ab + b\* | 1 →a→ 2 →b→ f3; f1 →b→ 1 |
| 21 | a\*b\*a\* | f1 →a→ 1, 1 →ε→ f2 →b→ 2, 2 →ε→ f3 →a→ 3 |
| 22 | a\*(ba)\*b\* | f1 →a→ 1, 1 →ε→ f2; 2 →b→ 3 →a→ 2, 2 →ε→ f4 →b→ 4 |
| 23 | a\* + b\* | f1 →a→ 1; f2 →b→ 2 (dois ramos finais) |

**Repare:** nos exercícios 16 e 17 a transição nula é **obrigatória** — sem ela o início do laço `(...)*` não teria por onde entrar (pega o caso ε do laço).

---

## Exercícios 2 (25–42): de linguagens descritas → NFA

Muitos repetem os pedidos da Aula 02.2, agora para **construir o autômato** (a ER da aula anterior vira o NFA):

| # | Pedido | ER (da Aula 02.2) → NFA |
|---|--------|--------------------------|
| 25 | contém "bab" | `(a+b)*bab(a+b)*` — estado-memória de 3 posições (b→a→b) |
| 26 | iniciadas por ≥ 2 a's | `aa(a+b)*` |
| 27 | iniciadas por exatamente 2 a's | `aa + aab(a+b)*` |
| 28 | cada 0 seguido de dois 1 | `(1+011)*` |
| 29 | exatamente dois 0's | `1*0 1*0 1*` |
| 30 | comprimento > 2 | `(a+b)(a+b)(a+b)(a+b)*` |
| 31 | comprimento < 4 | `ε + (a+b) + (a+b)² + (a+b)³` |
| 32 | número par de a's | `(b*ab*ab*)*` — 2 estados: pares (inicial/final) ↔ ímpares |
| 33 | `b*(abb*)*(a+ε)` | cadeia direta da ER, com ε no final |
| 34 | L = ∅ | NFA **sem estados finais** (nenhuma palavra aceita) |
| 35 | terminadas em "bb" | `(a+b)*bb` |
| 36 | contém "aa" **ou** "bb" | união de dois autômatos com ε-transições |
| 37 | aⁿ (n≥1) bᵐ (m≥2) a | `aa*bb b*a` (≥ 1 a, ≥ 2 b's, termina em a) |
| 38 | contém "abba" | `(a+b)*abba(a+b)*` |
| 39 | todos os prefixos de "aba" | `a + ab + aba` = `a(ε+b(ε+a))` |
| 40 | sem "aa" | `(b+ab)*(ε+a)` (ou `(a+ε)(ba+b)*`) |
| 41 | não iniciadas por "bb" | `a(a+b)* + b + ba(a+b)*` |
| 42 | **OU exclusivo**: tem "aa" **xor** "bb" | união de (com aa sem bb) e (com bb sem aa); Aula 02.2 mostrou que "aa" e "bb" são regulares — interseção/complemento preservam regularidade ✓ |

---

## Referências cruzadas

- Definição de ER e a Hierarquia de Chomsky ("Reconhecedor de linguagens regulares = Autômato Finito") → [Aula 01–02](estudo-aula01-02-linguagens-formais-e-expressoes-regulares.md)
- ERs candidatas dos exercícios 25–42 acima → [Aula 02.2](estudo-aula022-expressoes-regulares-propriedades-e-construcao.md)
- Ferramenta de verificação: [JFLAP](http://www.jflap.org/jflaptmp/) (Java 8)