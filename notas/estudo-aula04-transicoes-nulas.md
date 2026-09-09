# Aula 04 — Transições nulas (ε) em NFA

**Disciplina:** Teoria da Computação e Linguagens Formais (Prof. Diógenes Furlan)  
**Slide de referência:** `material/slides/Aula04-Transicoes Nulas.pdf`

Complementa a [Aula 03 — Autômatos finitos](estudo-aula03-automatos-finitos.md).

---

## Sumário

- O que é transição ε (nula)
- Construir NFAs compostos: união, concatenação (produto), fechamento (*)
- Exemplos com L1 = `ab`, L2 = `ba`
- Converter **NFA-ε → NFA** (fecho-ε)
- Exercícios

---

## 1. Transição ε

- Lê o **símbolo vazio** ε (épsilon): muda de estado **sem consumir** entrada.
- Serve para montar NFAs **complexos** a partir de NFAs **simples**.
- Operações clássicas com ε:
  - **União** (`∪` ou `+`)
  - **Concatenação** (`·` ou `×`)
  - **Fechamento** (`*`)

---

## 2. Construções com ε

### União `L1 ∪ L2`

1. Novo estado inicial.
2. ε do novo inicial → inicial de L1 e → inicial de L2.
3. (conforme desenho da aula) finais de L1 e L2 ligados ao aceite da união via ε, se necessário.

### Concatenação `L1 · L2`

Ligar **cada estado final de L1** ao **estado inicial de L2** com ε.

### Fechamento `L1*`

1. Novo estado inicial (também final, para aceitar ε / palavra vazia).
2. ε do novo inicial → antigo inicial de L1.
3. ε de cada final de L1 → antigo inicial de L1 (loop).
4. Finais de L1 também finais do fechamento (ou ε para um novo final — seguir o diagrama do slide).

---

## 3. Exemplo-base

`L1 = ab` · `L2 = ba`

| Operação | Linguagem |
|----------|-----------|
| `L1 + L2` | `ab + ba` |
| `L1 · L2` | `abba` |
| `L1*` | `(ab)*` |

Faça **teste de mesa** nas cadeias do slide (união / concatenação / fechamento) marcando estados possíveis após cada símbolo (incluindo ε-closures mentais).

---

## 4. NFA-ε → NFA (sem ε)

### Fecho-ε

```
fecho-ε(q) = { todos os estados alcançáveis a partir de q só com ε }
```

Inclui o próprio `q`.

### Ideia do algoritmo (slide)

Para cada estado `q` e símbolo `x ∈ Σ`:

1. Veja para onde `q` vai com `x` (conjunto `D = δ(q,x)`).
2. Se `D` não vazio: para cada `d ∈ D`, inclua também `fecho-ε(d)`.
3. Se `D` vazio: olhe estados `f ∈ fecho-ε(q)`; se algum `f` tem transição com `x` para `G`, inclua `fecho-ε(g)` para cada `g ∈ G`.

**Estados finais:** todo estado cujo `fecho-ε` contém algum final original vira final.

**Atalho visual (casos básicos):** ε “antes” ou “depois” de um símbolo `α` colapsa na transição direta com `α` para o destino do fecho.

### Exemplos do slide

Trabalhe as tabelas dos Exemplos 1–3 (e 4–7 no PDF):

1. Calcular coluna `fecho-ε` de cada estado.
2. Preencher nova tabela **sem** coluna `&` / ε.
3. Marcar finais novos.

---

## 5. Exercícios (slide)

**Com ε (construção):**

1. `L1 = (a+b)*(aa+bb)(a+b)*` e `L2 =` palavras sem `aa` → `L1+L2`, `L2·L1`, `L1*`
2. `L = (b + a + ab* + ab*a)*` — montar pedaços (`b+a`, `ab*`, `ab*a`) e juntar com ε
3. `L = a*b*c*`
4. `L1 = (a+b)*aa`, `L2 = a*b*` → união, concat, `L2*`

**Após remover ε / desenhar NFA:**

1. `a*b*` (todos os `a` antes de todos os `b`)
2. `0*1*2*`
3. `ab + b*`
4. `a*(ba)*b*`
5. `a*b*a*`
6. `0*1*2*3*`
7. Mesmo L1/L2 do item 1 (união, concat, fechamento)
8. `L = (b + a + ab* + ab*a)+`

---

## Checklist de prova

- [ ] Desenhar união / concat / `*` com ε
- [ ] Calcular `fecho-ε(q)`
- [ ] Montar tabela NFA sem ε
- [ ] Identificar novos estados finais

---

- Anterior → [Aula 03 — Autômatos finitos](estudo-aula03-automatos-finitos.md)  
- Relacionado → [Aula 02.2 — ERs](estudo-aula022-expressoes-regulares-propriedades-e-construcao.md)
