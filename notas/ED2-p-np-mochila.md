# ED2 — Reduções de problemas em classes P e NP (Mochila)

**Disciplina:** Teoria da Computação e Linguagens Formais (Prof. Diógenes Cogo Furlan) · 2º Bimestre  
**Autor:** Lucas Müller Scuzziato  
**Enunciado:** `projetos/ED2/LFA-EstudoDirigido2.pdf`  
**Entrega ABNT:** `projetos/ED2/ed2-p-np-mochila.tex` → `ed2-p-np-mochila.pdf`  
**Código:** `material/exercicios/ed2-mochila.py`  
**Prazo do enunciado:** até 28/nov/2026

---

## Parte teórica (síntese)

### 1) Decisão × busca × otimização
- **Decisão:** sim/não (linguagem formal).
- **Busca:** devolve um certificado/solução viável.
- **Otimização:** melhor solução segundo um critério (a decisão associada costuma ser NP-completa).

### 2) Solúvel/insolúvel × computável/incomputável
Falam de **existência** de algoritmo que sempre termina (ex.: Parada = insolúvel). Não confundir com NP-difícil (que continua decidível, só que caro).

### 3) Decidibilidade × Computabilidade
- **Decidibilidade:** quais decisões têm algoritmo total.
- **Computabilidade:** o que significa calcular (MT, tese de Church–Turing). Complexidade pergunta o *custo*.

### 4) P, NP, NP-difícil, NP-completo
| Classe | Ideia | Exemplos |
|--------|-------|----------|
| P | decidível em tempo polinomial determinístico | ordenação, Dijkstra, 2-SAT |
| NP | certificado polinomial verificável em P | SAT, HamPath, Mochila (decisão) |
| NP-difícil | todo NP reduz a ele | SAT, Halting, TSP otimização |
| NP-completo | em NP e NP-difícil | 3-SAT, Clique, Knapsack decisão |

### 5) Técnicas (heurística, guloso, PL, genéticos, PD)
Resumo no PDF (cap. 5): heurística sem garantia; guloso rápido (ótimo na mochila fracionária); PL em P + arredondamento; AG estocástico; PD ótima pseudo-polinomial $O(nW)$ na mochila 0/1.

---

## Parte prática — Mochila 0/1

- **Burro:** força bruta $O(2^n\cdot n)$.
- **Exato:** PD $O(nW)$.
- **Heurística:** guloso por valor/peso $O(n\log n)$ (pode errar).

### Como validar
```bash
python3 material/exercicios/ed2-mochila.py \
  --grafico projetos/ED2/figuras/mochila-tempos.png
```
FB e PD devem coincidir; guloso pode divergir (ex.: n=22 nos testes).

### Compilar o PDF
```bash
cd projetos/ED2
pdflatex ed2-p-np-mochila.tex && bibtex ed2-p-np-mochila
pdflatex ed2-p-np-mochila.tex && pdflatex ed2-p-np-mochila.tex
```
