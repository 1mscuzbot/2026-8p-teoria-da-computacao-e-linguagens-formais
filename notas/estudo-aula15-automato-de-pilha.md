# Aula 15 — Autômato de Pilha (AP)

**Disciplina:** Teoria da Computação e Linguagens Formais (Prof. Diógenes Furlan)  
**Slide:** `material/slides/2_BIMESTRE/Aula15-Automato-de-Pilha.pdf`  
**Segue:** [Aula 14 — FNC](estudo-aula14-fnc.md) (contexto LLC) · GLC ↔ LLC.

---

## Ideia

**Autômato de pilha (AP / PDA):** modelo **reconhecedor** de palavras para **LLC** (linguagens livres de contexto).

Além da fita de entrada (só leitura, cabeça à direita), tem uma **pilha** (LIFO): empilha / desempilha / ε / teste de vazio (`?`).

---

## Sumário

- Modelo de máquina (fita + pilha + δ)
- Funcionamento e condição de aceitação
- Notação da transição `λ / α`
- Exemplos de arcos (emp, des, ε, ?)
- Exercícios do slide (incl. `aⁿbⁿcⁿ` impossível)

---

## 1. Modelo

Componentes do slide:

- **Fita de entrada** — palavra a avaliar; cabeça só lê e avança.
- **Pilha** — começa vazia; um símbolo do topo é manipulado por vez.
- **Função de transição** — depende de: estado atual + símbolo lido + topo da pilha.

### Início / meio / fim

| Momento | Fita | Pilha |
|---------|------|-------|
| Início | cabeça no 1º símbolo | vazia |
| Meio | lê 1 símbolo (→) | empilha **ou** desempilha |
| Fim | cabeça após o último símbolo | (conforme δ) |

### Aceitação / rejeição

- Terminou a palavra **e** está em estado **final** → **aceita**.
- Terminou em estado **não final** → **rejeita**.
- δ **indefinida** para o argumento → máquina para → **rejeita**.

---

## 2. Notação da transição

Arco: `qi -- λ/α --> qk`

| Símbolo | Significado |
|---------|-------------|
| `λ` | o que se lê da fita |
| `α` | manipulação da pilha |
| `?` | testa fim da fita **ou** pilha vazia |
| `ε` | não lê fita / não altera pilha |
| `emp(A)` / `e(A)` | empilha `A` |
| `des(A)` / `d(A)` | desempilha `A` (exige `A` no topo) |

### Exemplos (slide)

| Arco | Leitura |
|------|---------|
| `a / emp(A)` | lê `a`, empilha `A` |
| `b / des(A)` | lê `b`, topo=`A` → desempilha |
| `b / d(A), e(AA)` | lê `b`, desempilha `A`, empilha `AA` |
| `ε / emp(X)` | sem ler fita, empilha `X` |
| `? / des(B)` | fim da fita + topo=`B` → desempilha |
| `b / ε` | lê `b`, pilha inalterada |
| `b / ?` | lê `b` **só se** pilha vazia |
| `ε/emp(A)` e `ε/des(A)` mútuos | possível **loop** |

---

## 3. Intuição clássica

Para `L = { aⁿbⁿ | n ≥ 1 }`: empilhar nos `a`s, desempilhar nos `b`s; no fim da fita a pilha deve “bater” (vazia / marcador).

**Não** reconhece `aⁿbⁿcⁿ` (LLC ≠ LSC; AP não guarda “dois contadores” independentes além da pilha única).

---

## 4. Exercícios do slide

1. `L = {aⁿbⁿ | n≥1}`  
2. `S → aSa | b`  
3. Parênteses casados  
4. `L = {aⁿbᵐcᵐdⁿ | n,m≥1}`  
5. `L = {aⁱbʲ | i≠j, i,j≥1}`  
6. `L = {aⁿcᵐb²ⁿ | n,m≥1}`  
7. `L = {w·wʳ | w ∈ {a,b}*}`  
8. Nº de `a`s = nº de `b`s  
9. `L = {aⁿ⁺ᵐbᵐaⁿ | n,m≥0}`  
10. `L = {ε}`  
11. Palavras de tamanho par sobre `{a,b}`  
12. Parênteses e colchetes casados  
13. AP em **loop** infinito  
14. `L = {aⁿbⁿcⁿ | n≥1}` — **impossível**. Por quê?

---

## Checklist rápido

- [ ] AP = reconhecedor de **LLC** (não de qualquer LSC)
- [ ] δ depende de estado + fita + topo da pilha
- [ ] Ler `emp` / `des` / `ε` / `?` num arco
- [ ] Esboçar AP para `aⁿbⁿ` e para parênteses
- [ ] Explicar por que `aⁿbⁿcⁿ` não tem AP
