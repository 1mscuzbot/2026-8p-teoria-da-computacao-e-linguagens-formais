# Cola 1 tela — Provinhas 2·3·4 (GLC · GR · FNC)

**Furlan · 2º bimestre · Aulas 12–14** · Sem PDA (P5).

| | Forma | Ideia |
|---|--------|--------|
| **GLC** | `X → α` | LLC: `aⁿbⁿ`, palíndromo, `i≠j`, parênteses |
| **GR** | `X→w` · `X→wY` · `X→ε` | LR ⇔ GR ⇔ **NFA** |
| **FNC** | `A→BC` ou `A→a` | simplificar → **Δ** → **Ω** · AS binária |

## GLC (P2)
- Criar: `S → aSb \| ab` (`aⁿbⁿ`, n>0); palíndromo `S → aSa\|bSb\|a\|b\|ε`
- Ler: expandir produções → descrever L / ER quando der
- `A→aBb` = GLC **não** GR; `AB→a` = **inválida** em GLC

## GR ↔ NFA (P3)
- **GR→NFA:** var=estado; `X→wY`⇒`Y∈δ(X,w)`; `X→w`⇒ final `Z`; `X→ε`⇒`X` final
- **NFA→GR:** estado=var; `Y∈δ(X,w)`⇒`X→wY`; final⇒`X→ε`
- Ex.: `S→0S\|1A`, `A→1A\|ε` → `s=S`, `F={A}`; δ: `0:S→S`, `1:S→A`, `1:A→A`

## FNC (P4)
1. **Δ:** em RHS `\|RHS\|>1`, zero terminais → `X→a` e troca  
2. **Ω:** RHS longo → **exatamente 2** vars (`A→XYZ` → `A→XW`, `W→YZ`)
- Mini: `S→a\|aSa` → `S→a\|US`, `U→XS`, `X→a`
- Armadilha: Ω antes de Δ; deixar `A→aB` ou `A→ABC`

## Mini checklist
- [ ] GLC vs GR vs inválida  
- [ ] GR↔NFA com `Z` se houver `X→w`  
- [ ] FNC: ordem + só `BC`/`a`
