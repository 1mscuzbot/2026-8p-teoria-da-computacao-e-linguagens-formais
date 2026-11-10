# Outline — slides da revisão (Aulas 11–14)

Uso: colar no PowerPoint / falar em ~10–12 min. Detalhe e exercícios: [revisao-aulas-11-14-gramaticas-fnc.md](revisao-aulas-11-14-gramaticas-fnc.md).

---

1. **Título** — Revisão gramáticas → FNC (Aulas 11–14) · Prof. Diógenes
2. **Mapa** — 11 definição · 12 GLC · 13 GR↔NFA · 14 FNC
3. **Hierarquia** — LRE ⊃ LSC ⊃ LLC ⊃ LR
4. **G = (V, Σ, P, S)** — convenções maiúscula/minúscula
5. **GLC** — `X → α` · exemplo `S → aSb | ε`
6. **GR** — só `X→w`, `X→wY`, `X→ε`
7. **GR → NFA** — variável=estado · `X→ε` ⇒ final
8. **NFA → GR** — transição ⇒ `X→wY` · final ⇒ `X→ε`
9. **Por que FNC** — AS binária / caminho para CYK
10. **Algoritmo FNC** — simplificar → Δ → Ω
11. **Δ** — terminais em RHS longos viram variáveis `X→a`
12. **Ω** — RHS com 3+ variáveis vira pares
13. **Exemplo 1 (resultado)** — `P→KB|CX` … auxiliares K,L,M,N,X,Y,Z
14. **Checklist prova** — classificar produção · GR↔NFA · `aⁿbⁿ` · FNC na ordem
15. **Treino** — 3 exercícios da nota de revisão (itens 2, 3 e 4)
