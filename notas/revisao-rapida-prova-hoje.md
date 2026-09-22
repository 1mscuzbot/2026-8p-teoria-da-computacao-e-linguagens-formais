# Teoria — revisão rápida (prova)

**Foco:** Aulas 03–05 (AF, ε, NFA→DFA). Use na ordem abaixo.

---

## 0. Definição em 20 s

AF = `(Q, Σ, δ, s, F)`

| | DFA | NFA |
|--|-----|-----|
| δ | **1** destino por (estado, símbolo) | **0, 1 ou vários** destinos |
| ∅ | rejeita (ou estado morto) | caminho morre |
| Aceita | termina em final | **existe** caminho que termina em final |

Círculo = estado · seta rotulada = transição · seta sem origem = inicial · **círculo duplo** = final.

---

## 1. ε — união / concat / *

| Operação | Como montar |
|----------|-------------|
| **L1 ∪ L2** | Novo inicial →ε→ inicial L1 e →ε→ inicial L2 |
| **L1 · L2** | Cada final de L1 →ε→ inicial de L2 |
| **L1\*** | Novo inicial (também final) →ε→ antigo inicial; cada final →ε→ antigo inicial (loop) |

**Fecho-ε(q)** = q + tudo alcançável só com ε.

**NFA-ε → NFA:** para cada (q, símbolo x), destino = fecho-ε dos estados alcançados com x a partir do fecho-ε(q).  
Final novo = quem tem final no fecho-ε.

---

## 2. NFA → DFA (o que mais cai agora)

Cada estado do DFA = **conjunto** de estados do NFA.

1. Comece com `{s}`  
2. Para cada conjunto Qᵢ e cada símbolo x:  
   `δ'(Qᵢ, x) = união de δ(q,x) para todo q ∈ Qᵢ`  
3. Se sair ∅ → estado **morto M** (`M --a--> M`, `M --b--> M`)  
4. **Final** = qualquer conjunto que **contém** algum final do NFA  
5. `|Q_DFA| ≤ 2^|Q_NFA|`

### Exemplo 1 (slide) — treine a mão

NFA `s=1`, `F=3`:

|   | a     | b     |
|---|-------|-------|
| →1 | {1}   | {2}   |
| 2  | {1,3} | {1,2} |
| =3 | ∅     | {1}   |

DFA:

|     | a  | b  |
|-----|----|----|
| →1  | 1  | 2  |
| 2   | 13 | 12 |
| =13 | 1  | 12 |
| 12  | 13 | 12 |

`13` final porque contém `3`.

### Exemplo 2 — morto

NFA: `1 --a--> 2`, `1 --b--> ∅`, `2` final e `2 --a/b--> 2`.

DFA: `1 --a--> 2`, `1 --b--> M`, `M --a/b--> M`.

---

## 3. Receitas rápidas (linguagens clássicas)

Alfabeto `{a,b}` — desenhe NFA (depois DFA se pedirem):

| Pedido | Ideia |
|--------|--------|
| Termina em `bb` | 3 estados: vazio → b → bb(final); `a` volta; em `bb`, `b` fica |
| Contém `aa` **ou** `bb` | Dois “detectores” + união (ε) ou DFA com flags |
| Contém `abba` | Cadeia de estados que avancem no padrão |
| Sem `aa` | Estados “último foi a?”; de “último a” com `a` → morto/rejeita |
| Não inicia por `bb` | Só rejeita se os 2 primeiros forem `bb` |
| Começa `ab` e termina `ba` | Prefixo fixo + sufixo (pode precisar memória do fim) |

---

## 4. Checklist na prova (ordem)

- [ ] Identificar: DFA, NFA ou NFA-ε?  
- [ ] Se ε: fecho-ε → tabela sem ε  
- [ ] Se NFA→DFA: tabela por conjuntos + marcar finais + morto  
- [ ] Teste de mesa numa palavra curta (aceita/rejeita)  
- [ ] Não inventar transição: ∅ = morto no DFA

---

## 5. Exercício express (faça agora, 5 min)

NFA `s=1`, `F=2`:

|   | a   | b   |
|---|-----|-----|
| →1 | {1} | {1,2} |
| =2 | {2} | ∅   |

**Tarefa:** monte o DFA completo (inclua morto se aparecer).

<details>
<summary>Gabarito</summary>

|     | a  | b   |
|-----|----|-----|
| →1  | 1  | 12  |
| =12 | 12 | 1   |

- `12` final (contém 2).  
- `δ(2,b)=∅`, mas de `12` com `b`: união `δ(1,b)∪δ(2,b) = {1,2}∪∅ = {1,2}` → **12**, não precisa de M neste caso.  
- Se aparecer um conjunto cujo a/b dá só ∅, aí entra M.

</details>

---

## Arquivos longos (se sobrar tempo)

- [Aula 05 — NFA→DFA](estudo-aula05-nfa-para-dfa.md)  
- [Aula 04 — ε](estudo-aula04-transicoes-nulas.md)  
- [Aula 03 — AF](estudo-aula03-automatos-finitos.md)
