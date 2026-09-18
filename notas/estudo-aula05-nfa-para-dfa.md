# Aula 05 — NFA → DFA

**Disciplina:** Teoria da Computação e Linguagens Formais (Prof. Diógenes Furlan)  
**Slide:** `material/slides/Aula05-NFA to DFA.pdf`

Segue [transições nulas / ε-NFA](estudo-aula04-transicoes-nulas.md). Aqui: **determinizar** um NFA (sem ε, ou já convertido).

---

## Ideia

Cada estado do DFA é um **conjunto** de estados do NFA.  
Unificar: todos os destinos possíveis com o mesmo símbolo viram **um** estado.

### Algoritmo (fila K)

1. Coloque o estado inicial `s` em K  
2. Enquanto houver estado `q` em K ainda não expandido:  
   - para cada símbolo `x ∈ Σ`:  
     - `r` = união de `δ(q, x)` (como um único nome de conjunto, sem repetir)  
     - defina `δ'(q, x) = r`  
     - se `r` for novo, coloque em K  
3. Resultado:  
   - `Σ' = Σ`  
   - `Q'` = todos os conjuntos gerados em K  
   - `s' = {s}` (ou o rótulo usado)  
   - `F'` = conjuntos que **contêm** algum estado final do NFA  
   - `|Q'| ≤ 2^|Q|`

Estado **morto** `M`: quando a transição no NFA é ∅ — no DFA, `M --a--> M` e `M --b--> M`.

---

## Exemplo 1 (slide)

NFA (`s=1`, `F=3`):

|  | a | b |
|--|---|---|
| →1 | {1} | {2} |
| 2 | {1,3} | {1,2} |
| =3 | ∅ | {1} |

DFA (rótulos concatenados):

|  | a | b |
|--|---|---|
| →1 | 1 | 2 |
| 2 | 13 | 12 |
| =13 | 1 | 12 |
| 12 | 13 | 12 |

`13` é final porque contém `3`.

---

## Exemplo 2 — estado morto

NFA (`s=1`, `F=2`): de 1 com `b` → ∅ → no DFA nasce **M**.

| DFA | a | b |
|-----|---|---|
| →1 | 2 | M |
| =2 | 2 | 2 |
| M | M | M |

---

## Exercícios do slide (construir NFA e/ou DFA)

Alfabeto típico `{a,b}`:

1. Palavras terminadas em `bb`  
2. Contêm substring `aa` **ou** `bb`  
3. Contêm substring `abba`  
4. Iniciam com prefixos de `aba`  
5. Sem `aa`  
6. Não iniciam por `bb`  
7. `(aab + aba + baa)(a+b)*`  
8. Terminam com sufixos de `aba`  
9. Começam por `ab` e terminam por `ba`

---

## Para a prova / lista

- Saber montar a tabela do DFA a partir do NFA  
- Marcar finais: conjunto que **inclui** algum final do NFA  
- Não esquecer o estado morto quando aparecer ∅  

---

- Anterior → [Aula 04 — Transições nulas](estudo-aula04-transicoes-nulas.md)
