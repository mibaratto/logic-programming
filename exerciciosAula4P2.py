# nota1 = float(input("nota 1: "))
# nota2 = float(input("nota 2: "))
# nota3 = float(input("nota 3: "))
# frequencia = int(input("Qual a frequencia: "))

# G1 = (nota1 + nota2 + nota3) / 3

# if frequencia < 75:
#   print("reprovado por frequencia: {frequencia}")
# else:
#   if G1 >= 7:
#     print("aprovado por média")
#   else:
#     if G1 < 4:
#      print("reprovado por média")
#     else:
#       # em exame
#       G2 = float(input("Qual a nota G2: "))
#       final = (G1 + G2) / 2
#       if final >= 5:
#         print("Aprovado em G2")
#       else:
#         print("reprovado em G2")
  

# ///////////////// Cálculo data páscoa

ano = int(input("Ano: "))
if ano < 1900 or ano > 2099:
  print("impossível calcular")
else:
  a = ano % 19
  b = ano % 4
  c = ano % 7
  d = (19 * a + 24) % 30
  e = (2 * b + 4 * c + 6 * d + 5) % 7
  dia = 22 + d + e
  if ano == 1964 or ano == 1981 or ano == 2049 or ano == 2076:
    dia = dia - 7
  if dia > 31:
    dia = dia -31
    print(f"Dia da Páscoa é: {dia} de abril")
  else:
    print(f"Dia da Páscoa: {dia} de março")