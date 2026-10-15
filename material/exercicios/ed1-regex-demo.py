"""ED1 - expressoes regulares. Gera as saidas usadas no relatorio."""

import re

texto = "O curso custa R$ 1999.90 e o outro R$ 350.00."


def titulo(nome):
    print()
    print("=" * 64)
    print(nome)
    print("=" * 64)


titulo("METODOS DA BIBLIOTECA re")
print("texto:", texto)

m = re.search(r"\d+\.\d{2}", texto)
print("search:", None if m is None else f"{m.group()} | span {m.span()}")
print("search sem match:", re.search(r"\d+\.\d{2}", "sem numero aqui"))

m = re.match(r"\d+\.\d{2}", "1999.90 reais")
print("match no inicio:", None if m is None else m.group())
m = re.match(r"\d+\.\d{2}", "custa 1999.90")
print("match no meio:", None if m is None else m.group())
m = re.search(r"\d+\.\d{2}", "custa 1999.90")
print("search no meio:", None if m is None else m.group())

m = re.fullmatch(r"^(\d{3}\.\d{3}\.\d{3}-\d{2}|\d{11})$", "123.456.789-00")
print("fullmatch:", None if m is None else m.group())

print("findall:", re.findall(r"\d+\.\d{2}", texto))
print("finditer:", [(x.group(), x.span()) for x in re.finditer(r"\d+\.\d{2}", texto)])
print("sub:", re.sub(r"\s+", " ", "um   texto   com   espacos  extras."))
print("split:", re.split(r"[;,]", "a;b,c;d"))

padrao = re.compile(r"\d+\.\d{2}")
print("compile:", padrao.findall(texto))
print(
    "grupos nomeados:",
    re.sub(r"(?P<ano>\d{4})-(?P<mes>\d{2})", r"\g<mes>/\g<ano>", "2026-08"),
)
print("IGNORECASE:", re.findall(r"ab[cs]", "Abc abC aBc", re.IGNORECASE))
print("MULTILINE:", re.findall(r"^\w+", "linha1\nlinha2\nlinha3", re.MULTILINE))


titulo("1) VALIDAR CPF (formato)")
entrada = [
    "123.456.789-00",
    "12345678900",
    "12.3.456.789-00",
    "123.456789-00",
    "ABC.DEF.GHI-JK",
]
pat = r"^(\d{3}\.\d{3}\.\d{3}-\d{2}|\d{11})$"
print("regex:", pat)
for item in entrada:
    print(f"  {item!r:22} -> {'VALIDO' if re.fullmatch(pat, item) else 'INVALIDO'}")


titulo("2) VALIDAR E-MAIL")
entrada = [
    "joao@abc.com",
    "vendas@loja.com.br",
    "invalido@",
    "sem-arroba.com",
    "ana@site.org.br",
]
pat = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
print("regex:", pat)
for item in entrada:
    print(f"  {item!r:22} -> {'VALIDO' if re.fullmatch(pat, item) else 'INVALIDO'}")


titulo("3) EXTRAIR TELEFONES")
entrada = "Fale com Joao no (41) 99876-5432 ou com Maria no 41 3322-1000. Fixo: (45)9812 2233."
pat = r"\(\d{2}\)\s?\d{4,5}[ -]?\d{4}|\d{2}\s\d{4}[ -]?\d{4}"
print("entrada:", entrada)
print("regex:", pat)
print("saida:", re.findall(pat, entrada))


titulo("4) VALIDAR PLACA MERCOSUL")
entrada = ["ABC1D23", "ABC-1234", "ABC1234", "ABC1D2X", "AB1C2D3", "XYZ9A99"]
pat = r"^[A-Z]{3}\d[A-Z]\d{2}$"
print("regex:", pat)
for item in entrada:
    print(f"  {item!r:10} -> {'VALIDA' if re.fullmatch(pat, item) else 'INVALIDA'}")


titulo("5) EXTRAIR DATAS dd/mm/aaaa")
entrada = "Prova dia 04/09/2026, entrega em 11/9/2026 e feriado 7/09. Sem data 99-99-9999."
pat = r"\b\d{1,2}/\d{1,2}/\d{4}\b"
print("entrada:", entrada)
print("regex:", pat)
print("saida:", re.findall(pat, entrada))


titulo("6) VALIDAR CEP")
entrada = ["81200-100", "81200100", "8120-0100", "8120010"]
pat = r"^\d{5}-?\d{3}$"
print("regex:", pat)
for item in entrada:
    print(f"  {item!r:12} -> {'VALIDO' if re.fullmatch(pat, item) else 'INVALIDO'}")


titulo("7) SENHA FORTE")
entrada = ["abc123", "SenhaForte1", "SENHA123", "senha123", "S3nha.Forte!"]
pat = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"
print("regex:", pat)
for item in entrada:
    print(f"  {item!r:15} -> {'OK' if re.fullmatch(pat, item) else 'FALHOU'}")


titulo("8) REMOVER ESPACOS EXTRAS")
entrada = "A  aula    de   Regex   sera  as   10h,    na sala   B-2.   "
pat = r"\s+"
print("entrada:", repr(entrada))
print("regex:", pat, "(re.sub por espaco, depois strip)")
print("saida:", re.sub(pat, " ", entrada).strip())


titulo("9) EXTRAIR URLs")
entrada = (
    "Veja https://www.devmedia.com.br/iniciando-expressoes-regulares/6557 "
    "e http://example.com.br/aula?x=1. Site: www.uol.com.br"
)
pat = r"https?://[\w.-]+\.\w+(?:[/?#][^\s.,;]*)?"
print("entrada:", entrada)
print("regex:", pat)
print("saida:", re.findall(pat, entrada))


titulo("10) MASCARAR CARTAO")
entrada = "Cartao 5123 4678 9012 3456 aprovado; outro 9876-5432-1098-7654 negado."
pat = r"(?<!\d)(\d{4})[ -]?(\d{4})[ -]?(\d{4})[ -]?(\d{4})(?!\d)"
print("entrada:", entrada)
print("regex:", pat)
print("saida:", re.sub(pat, r"**** **** **** \4", entrada))
