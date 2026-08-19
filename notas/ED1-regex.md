# ED1 — Expressões Regulares (REGEX)

**Disciplina:** Teoria da Computação e Linguagens Formais (Prof. Diógenes Cogo Furlan) · 1º Bimestre
**Fonte do trabalho:** `material/TCLF-Estudo Dirigido 1-Regex.pdf`
**Referência sugerida pelo professor:** https://www.devmedia.com.br/iniciando-expressoes-regulares/6557
**Formatação exigida:** documento ABNT (capa, capítulos, paginação, fonte única; fonte diferenciada só para código)

---

## Capítulo 1 — O que é REGEX

**REGEX (expressão regular)** é uma **sequência de caracteres que descreve um padrão de busca** em um texto. Em vez de procurar um texto exato (`"123.456.789-00"`), escrevemos um **padrão** que casa com todo texto naquele formato (ex.: `\d{3}\.\d{3}\.\d{3}-\d{2}`). Isso liga o conceito da disciplina (linguagens regulares, Aulas 02.1/02.2) às ferramentas reais de programação.

Fórmula mental: **`metacaracteres` + `literais` = padrão**. Metacaracteres dão "poder" ao padrão (repetição, alternância, posição, classes); literais são o texto fixo.

### 1.1 Caracteres especiais (metacaracteres)

| Metacaractere | Significado | Exemplo | Casa com |
|---|---|---|---|
| `.` | qualquer caractere (exceto quebra de linha) | `a.c` | `abc`, `a1c`, `a c` |
| `*` | 0 ou mais repetições do elemento anterior | `ab*c` | `ac`, `abc`, `abbc` |
| `+` | 1 ou mais repetições | `ab+c` | `abc`, `abbc` (não `ac`) |
| `?` | 0 ou 1 vez (opcional) | `ab?c` | `ac`, `abc` |
| `{n}`, `{n,m}` | exatamente n / entre n e m repetições | `\d{3}` | `123` |
| `\` | **escape**: trata o caractere seguinte como literal | `\.` | só o ponto |
| `\|` | alternância ("ou") | `a\|b` | `a` **ou** `b` |
| `()` | agrupamento + captura | `(ab)+` | `ab`, `abab`, … |
| `[ ]` | classe de caracteres | `[abc]` | um de: a, b, c |
| `^` | âncora: início da string | `^abc` | só se **começa** com `abc` |
| `$` | âncora: fim da string | `abc$` | só se **termina** com `abc` |

Ligação com a disciplina: `(ab)+` ≡ a linguagem `(ab)(ab)*` da Aula 02; `a\|b` ≡ união `a+b`; `a?` ≡ `(a+ε)`.

### 1.2 Caracteres de agrupamento

| Símbolo | Papel | Exemplo |
|---|---|---|
| `( ... )` | agrupa + **captura** o trecho p/ uso depois | `(\d{2})/(\d{2})` captura dia e mês |
| `(?: ... )` | agrupa **sem capturar** | `(?:ab)+` |
| `(?P<nome> ... )` | grupo **nomeado** (Python) | `(?P<ano>\d{4})` |
| `\1`, `\2`, … | referência ao grupo capturado | `(\w)\1` = letra repetida (`aa`, `bb`) |

### 1.3 Caracteres âncora

| Âncora | Significado |
|---|---|
| `^` | início da string (ou da linha, com `re.MULTILINE`) |
| `$` | fim da string (ou da linha) |
| `\b` | **fronteira de palavra** (entre `\w` e não-`\w`) |
| `\B` | posição que **não** é fronteira de palavra |
| `(?=...)` | **lookahead**: exige que adiante siga o padrão (sem consumir) |
| `(?!...)` | **lookahead negativo** |
| `(?<=...)` | **lookbehind**: exige algo antes (sem consumir) |
| `(?<!...)` | **lookbehind negativo** |

### 1.4 Quantificadores

| Quantificador | Repetições | Equivalência com a disciplina |
|---|---|---|
| `*` | 0 ou mais | fecho de Kleene: `a*` ≡ `ε + a + aa + …` |
| `+` | 1 ou mais | `a+` ≡ `a·a*` |
| `?` | 0 ou 1 | `a?` ≡ `a + ε` |
| `{n}` | exatamente n | `a{3}` ≡ `aaa` |
| `{n,}` | n ou mais | `a{2,}` ≡ `aa·a*` |
| `{n,m}` | entre n e m | `a{1,3}` ≡ `a + aa + aaa` |
| **greedy vs lazy** | `*` é **guloso** (pega o máximo); `*?` é **preguiçoso** (pega o mínimo) | problema clássico: `<.*>` casa até o **último** `>`; `<.*?>` até o primeiro |

### 1.5 Classes de caracteres

| Classe | Significado | Equivale a |
|---|---|---|
| `[abc]` | um dos caracteres listados | `(a\|b\|c)` |
| `[a-z]`, `[0-9]` | faixa (range) | — |
| `[^abc]` | **negação**: tudo exceto a, b, c | — |
| `\d` | dígito | `[0-9]` |
| `\D` | não-dígito | `[^0-9]` |
| `\w` | caractere de palavra | `[A-Za-z0-9_]` |
| `\W` | não-palavra | `[^A-Za-z0-9_]` |
| `\s` | espaço em branco | `[ \t\n\r\f\v]` |
| `\S` | não-espaço | — |

---

## Capítulo 2 — Programação com Regex em Python (biblioteca `re`)

Python tem a biblioteca padrão **`re`** (importada com `import re`). Texto de exemplo usado abaixo: `"O curso custa R$ 1999.90 e o outro R$ 350.00."` e padrão `\d+\.\d{2}` (valores monetários).

### 2.1 Métodos principais

| Método | O que faz | Exemplo | Saída real |
|---|---|---|---|
| `re.search` | procura o padrão **em qualquer posição**; retorna o 1º match ou `None` | `re.search(r"\d+\.\d{2}", texto)` | `1999.90` · span `(17, 24)` |
| `re.match` | igual, mas só **a partir do início** da string | `re.match(r"\d+\.\d{2}", "1999.90 reais")` | `1999.90` |
| `re.fullmatch` | exige que a **string inteira** case | `re.fullmatch(r"\d{3}\.?\d{3}\.?\d{3}-?\d{2}", "123.456.789-00")` | `123.456.789-00` |
| `re.findall` | retorna a **lista de todos os matches** | `re.findall(r"\d+\.\d{2}", texto)` | `['1999.90', '350.00']` |
| `re.finditer` | igual, mas como **iterador de matches** (acesso ao span) | `[(m.group(), m.span()) for m in re.finditer(r"\d+\.\d{2}", texto)]` | `[('1999.90', (17,24)), ('350.00', (38,44))]` |
| `re.sub` | **substitui** os matches por outro texto | `re.sub(r"\s+", " ", "um  texto  com  espacos")` | `um texto com espacos` |
| `re.split` | **divide** a string pelos matches | `re.split(r"[;,]", "a;b,c;d")` | `['a','b','c','d']` |
| `re.compile` | pré-compila o padrão (reuso + flags) | `p = re.compile(r"\d+\.\d{2}")` | `p.findall(texto)` → `['1999.90','350.00']` |

### 2.2 Grupos, substituição e flags

| Recurso | Exemplo | Saída real |
|---|---|---|
| Grupo nomeado + referência | `re.sub(r"(?P<ano>\d{4})-(?P<mes>\d{2})", r"\g<mes>/\g<ano>", "2026-08")` | `08/2026` |
| Flag `re.IGNORECASE` | `re.findall(r"ab[cs]", "Abc abC aBc", re.IGNORECASE)` | `['Abc', 'abC', 'aBc']` |
| Flag `re.MULTILINE` (`^` por linha) | `re.findall(r"^\w+", "linha1\nlinha2\nlinha3", re.MULTILINE)` | `['linha1', 'linha2', 'linha3']` |

## Capítulo 3 — 10 problemas úteis resolvidos (entrada → regex → saída real)

Todos executados com **Python 3 + `re`** nesta máquina; as saídas são reais ("telas de execução").

### Problema 1 — Validar CPF (formato)

**Entrada:** `123.456.789-00`, `12345678900`, `12.3.456.789-00`, `ABC.DEF.GHI-JK`
**REGEX:** `^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$`
**Saída:**
```
'123.456.789-00'    -> VALIDO
'12345678900'       -> VALIDO
'12.3.456.789-00'   -> INVALIDO
'ABC.DEF.GHI-JK'    -> INVALIDO
```

### Problema 2 — Validar e-mail

**Entrada:** `joao@abc.com`, `vendas@loja.com.br`, `invalido@`, `sem-arroba.com`, `ana@site.org.br`
**REGEX:** `^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$`
**Saída:**
```
'joao@abc.com'      -> VALIDO
'vendas@loja.com.br' -> VALIDO
'invalido@'         -> INVALIDO
'sem-arroba.com'    -> INVALIDO
'ana@site.org.br'   -> VALIDO
```

### Problema 3 — Extrair telefones de um texto

**Entrada:** `Fale com Joao no (41) 99876-5432 ou com Maria no 41 3322-1000. Fixo: (45)9812 2233.`
**REGEX:** `\(\d{2}\)\s?\d{4,5}[ -]?\d{4}|\d{2}\s\d{4}[ -]?\d{4}`
**Saída:** `['(41) 99876-5432', '41 3322-1000', '(45)9812 2233']`

### Problema 4 — Validar placa de carro (padrão Mercosul)

**Entrada:** `ABC1D23`, `ABC-1234`, `ABC1D2X`, `AB1C2D3`, `XYZ9A99`
**REGEX:** `^[A-Z]{3}\d[A-Z0-9]\d{2}$`
**Saída:**
```
'ABC1D23'   -> VALIDA
'ABC-1234'  -> INVALIDA
'ABC1D2X'   -> INVALIDA
'AB1C2D3'   -> INVALIDA
'XYZ9A99'   -> VALIDA
```

### Problema 5 — Extrair datas dd/mm/aaaa

**Entrada:** `Prova dia 04/09/2026, entrega em 11/9/2026 e feriado 7/09. Sem data 99-99-9999.`
**REGEX:** `\b\d{1,2}/\d{1,2}/\d{4}\b`
**Saída:** `['04/09/2026', '11/9/2026']` (o `\b` impede que `99-99-9999` case)

### Problema 6 — Validar CEP

**Entrada:** `81200-100`, `81200100`, `8120-0100`, `8120010`
**REGEX:** `^\d{5}-?\d{3}$`
**Saída:**
```
'81200-100' -> VALIDO
'81200100'  -> VALIDO
'8120-0100' -> INVALIDO
'8120010'   -> INVALIDO
```

### Problema 7 — Senha forte (mín. 8, com maiúscula, minúscula e dígito)

**Entrada:** `abc123`, `SenhaForte1`, `SENHA123`, `senha123`, `S3nha.Forte!`
**REGEX:** `^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$` (lookaheads!)
**Saída:**
```
'abc123'       -> FALHOU
'SenhaForte1'  -> OK
'SENHA123'     -> FALHOU
'senha123'     -> FALHOU
'S3nha.Forte!' -> OK
```

### Problema 8 — Remover espaços extras e normalizar texto

**Entrada:** `'A  aula    de   Regex   sera  as   10h,    na sala   B-2.   '`
**REGEX:** `\s+` (substituir por espaço) via `re.sub`
**Saída:** `A aula de Regex sera as 10h, na sala B-2.`

### Problema 9 — Extrair URLs de um texto

**Entrada:** `Veja https://www.devmedia.com.br/iniciando-expressoes-regulares/6557 e http://example.com.br/aula?x=1. Site: www.uol.com.br`
**REGEX:** `https?://[\w.-]+\.\w+(?:[/?#][^\s.,;]*)?`
**Saída:** `['https://www.devmedia.com.br/iniciando-expressoes-regulares/6557', 'http://example.com.br/aula?x=1']` (o ponto final do texto não entra no match)

### Problema 10 — Mascarar número de cartão (mostrar só os 4 últimos)

**Entrada:** `Cartao 5123 4678 9012 3456 aprovado; outro 9876-5432-1098-7654 negado.`
**REGEX:** `(?<!\d)(\d{4})[ -]?(\d{4})[ -]?(\d{4})[ -]?(\d{4})(?!\d)` com `re.sub(pat, r"**** **** **** \4", ...)`
**Saída:** `Cartao **** **** **** 3456 aprovado; outro **** **** **** 7654 negado.`

---

## Capítulo 4 — Formatação do documento (ABNT)

- **Capa principal:** universidade, faculdade, curso, título do trabalho, autor, disciplina/professor, data.
- **Capítulos:** paginados; títulos hierarquizados (1, 1.1, 1.2 …), como neste arquivo; sumário (se exigido).
- **Fonte única em todo o texto** (ex.: Times New Roman 12, espaçamento 1,5, margens 3/2 cm na conversão para DOCX/PDF).
- **Código fonte em fonte diferenciada** (ex.: Courier New 10, fundo ou recuo), como nos capítulos 2 e 3.
- **Referência:** DEVMEDIA. *Iniciando em Expressões Regulares*. Disponível em: https://www.devmedia.com.br/iniciando-expressoes-regulares/6557. STEINBRUCH segue como referência transversal da disciplina; complementares: documentação oficial `docs.python.org/3/library/re.html`.

## Checklist de entrega

- [ ] Capítulo 1: texto sobre o que é REGEX + tabelas (especiais, agrupamento, âncoras, quantificadores, classes)
- [ ] Capítulo 2: biblioteca `re` + métodos com exemplos rodando (search, match, fullmatch, findall, finditer, sub, split, compile, flags)
- [ ] Capítulo 3: 10 problemas com entrada, código REGEX e saída de execução
- [ ] Capa, capítulos, paginação, fonte única + fonte de código diferenciada
- [ ] Rodar tudo numa máquina Python 3 para regenerar as saídas (script: reproduzir os blocos acima)

---

- Aulas relacionadas → [Aula 02.1 — Linguagens Formais e ERs](estudo-aula01-02-linguagens-formais-e-expressoes-regulares.md) · [Aula 02.2 — propriedades e construção](estudo-aula022-expressoes-regulares-propriedades-e-construcao.md) · [Aula 03 — Autômatos Finitos](estudo-aula03-automatos-finitos.md)