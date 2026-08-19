import re

def show(title, label, code, output):
    print(f"### {title}")
    print(f"{label}: {code}")
    print(f"Saida: {output}")
    print()

# ---- Metodos do modulo re ----
texto = "O curso custa R$ 1999.90 e o outro R$ 350.00."
nums = "contato: (41) 99999-1234 | tel 41-3322-1000"
emails = "joao@abc.com vendas@loja.com.br invalido@"

show("metodo re.search()", "pattern", r"\d+\.\d{2}", [m.group() for m in re.finditer(r"\d+\.\d{2}", texto)])
m = re.search(r"\d+\.\d{2}", texto)
print("search():", m.group(), "| span:", m.span())
m2 = re.search(r"\d+\.\d{2}", "sem numero aqui")
print("search() sem match:", m2)
m = re.fullmatch(r"\d{3}\.?\d{3}\.?\d{3}-?\d{2}", "123.456.789-00")
print("fullmatch():", m.group() if m else None)
m = re.match(r"\d+\.\d{2}", "1999,90 reais")
print("match() no inicio:", m.group() if m else None)
m = re.match(r"\d+\.\d{2}", "custa 1999,90")
print("match() no meio:", m.group() if m else None)
import re
print("findall():", re.findall(r"\d+\.\d{2}", texto))
print("finditer():", [(x.group(), x.span()) for x in re.finditer(r"\d+\.\d{2}", texto)])
print("sub():", re.sub(r"\s+", " ", "um   texto   com   espacos  extras."))
print("split():", re.split(r"[;,]", "a;b,c;d"))
p = re.compile(r"\d+\.\d{2}", re.IGNORECASE)
print("compile():", p.findall(texto))
print("grupos nomeados:", re.sub(r"(?P<ano>\d{4})-(?P<mes>\d{2})", r"\g<mes>/\g<ano>", "2026-08"))
print("IGNORECASE:", re.findall(r"ab[cs]", "Abc abC aBc", re.IGNORECASE))
print("MULTILINE:", re.findall(r"^\w+", "linha1 Nol\nlinha2 Sim\nlinha3 Tal", re.MULTILINE))
print()

# ---- 10 problemas ----
print("=" * 60)
print("10 PROBLEMAS RESOLVIDOS")
print("=" * 60)

print("1) VALIDAR CPF (formato)")
entrada = ["123.456.789-00", "12345678900", "12.3.456.789-00", "ABC.DEF.GHI-JK"]
pat = r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$"
print("   entrada:", entrada)
print("   regex:", pat)
for e in entrada:
    print(f"   {e!r:22} -> {'VALIDO' if re.fullmatch(pat, e) else 'INVALIDO'}")

print("2) VALIDAR E-MAIL")
entrada = ["joao@abc.com", "vendas@loja.com.br", "invalido@", "sem-arroba.com", "ana@site.org.br"]
pat = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
print("   entrada:", entrada)
print("   regex:", pat)
for e in entrada:
    print(f"   {e!r:22} -> {'VALIDO' if re.fullmatch(pat, e) else 'INVALIDO'}")

print("3) EXTRAIR TELEFONES")
entrada = "Fale com Joao no (41) 99876-5432 ou com Maria no 41 3322-1000. Fixo: (45)9812 2233."
pat = r"\(\d{2}\)\s?\d{4,5}[ -]?\d{4}|\d{2}\s\d{4}[ -]?\d{4}"
print("   entrada:", entrada)
print("   regex:", pat)
print("   saida:", re.findall(pat, entrada))

print("4) VALIDAR PLACA DE CARRO (Mercosul)")
entrada = ["ABC1D23", "ABC-1234", "ABC1D2X", "AB1C2D3", "XYZ9A99"]
pat = r"^[A-Z]{3}\d[A-Z0-9]\d{2}$"
print("   entrada:", entrada)
print("   regex:", pat)
for e in entrada:
    print(f"   {e!r:10} -> {'VALIDA' if re.fullmatch(pat, e) else 'INVALIDA'}")

print("5) EXTRAIR DATAS dd/mm/aaaa")
entrada = "Prova dia 04/09/2026, entrega em 11/9/2026 e feriado 7/09. Sem data 99-99-9999."
pat = r"\b\d{1,2}/\d{1,2}/\d{4}\b"
print("   entrada:", entrada)
print("   regex:", pat)
print("   saida:", re.findall(pat, entrada))

print("6) VALIDAR CEP")
entrada = ["81200-100", "81200100", "8120-0100", "8120010"]
pat = r"^\d{5}-?\d{3}$"
print("   entrada:", entrada)
print("   regex:", pat)
for e in entrada:
    print(f"   {e!r:10} -> {'VALIDO' if re.fullmatch(pat, e) else 'INVALIDO'}")

print("7) SENHA FORTE (min 8, maiuscula, minuscula e digito)")
entrada = ["abc123", "SenhaForte1", "SENHA123", "senha123", "S3nha.Forte!"]
pat = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"
print("   entrada:", entrada)
print("   regex:", pat)
for e in entrada:
    print(f"   {e!r:15} -> {'OK' if re.fullmatch(pat, e) else 'FALHOU'}")

print("8) REMOVER ESPACOS EXTRAS E NORMALIZAR TEXTO")
entrada = "A  aula    de   Regex   sera  as   10h,    na sala   B-2.   "
pat = r"\s+"
print("   entrada:", repr(entrada))
print("   regex:", pat, "(substituir por ' ')")
print("   saida:", re.sub(pat, " ", entrada).strip())

print("9) EXTRAIR URLs DE UM TEXTO")
entrada = "Veja https://www.devmedia.com.br/iniciando-expressoes-regulares/6557 e http://example.com.br/aula?x=1. Site: www.uol.com.br"
pat = r"https?://[\w.-]+\.\w+(?:[/?#][^\s.,;]*)?"
print("   entrada:", entrada)
print("   regex:", pat)
print("   saida:", re.findall(pat, entrada))

print("10) MASCARAR NUMERO DE CARTAO (mostra so os 4 ultimos)")
entrada = "Cartao 5123 4678 9012 3456 aprovado; outro 9876-5432-1098-7654 negado."
pat = r"(?<!\d)(\d{4})[ -]?(\d{4})[ -]?(\d{4})[ -]?(\d{4})(?!\d)"
print("   entrada:", entrada)
print("   regex:", pat)
print("   saida:", re.sub(pat, r"**** **** **** \4", entrada))