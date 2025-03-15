import math

# numero = int(input("digite um numero de 1 a 7: "))

# if numero == 1:
#   print("hoje é domingo")
# if numero == 2:
#   print("hoje é segunda")
# if numero == 3:
#   print("hoje é terça")
# if numero == 4:
#   print("hoje é quarta")
# if numero == 5:
#   print("hoje é quinta")
# if numero == 6:
#   print("hoje é sexta")
# if numero == 7:
#   print("hoje é sábado")

# /////////////////////////////

# nota1 = float(input("digite a primeira nota: "))
# nota2 = float(input("digite a segunda nota: "))
# nota3 = float(input("digite a terceira nota: "))

# if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10 or nota3 < 0 or nota3 > 10: 
#   print("nota invalida")
# else:
#   if nota1 > nota2:
#     aux = nota1
#     nota1 = nota2
#     nota2 = aux
#   if nota1 > nota3:
#     aux = nota1
#     nota1 = nota3
#     nota3 = aux
#   if nota2 > nota3:
#     aux = nota2
#     nota2 = nota3
#     nota3 = aux

# print(nota1 ,nota2, nota3)

# mediaPonderada = ((nota3 * 5) + (nota1 * 2.5) + (nota2 *2.5)) / 10

# # ////// resposta da prof
# maiorNota = nota1
# if nota2 > nota1 : maiorNota = nota2
# if nota3 > maiorNota: maiorNota = nota3

# media = 0.5 * maiorNota + 0.25 * ((nota1 + nota2 + nota3) - maiorNota)

# print(mediaPonderada, media)

# ////////calculo de bascara

# a = int(input("digite valor de a: "))
# b = int(input("digite valor de b: "))
# c = int(input("digite valor de c: "))
# delta = b ** 2 - (4 * a * c)

# if a == 0 or delta < 0:
#   print("Erro: Delta negativo ou divisão por zero!")
# else:
#   x1 = (- b + math.sqrt(delta))/(2 * a)
#   x2 = (- b - math.sqrt(delta))/(2 * a)
#   print("x1: " , x1)
#   print("x2: " , x2)


saldo = float(input("informe saldo médio: "))

if saldo < 500:
  print("sem limite")
if saldo >= 500 and saldo < 1000:
  print("limite: ", saldo * 0.08)
if saldo >= 1000: 
  print("limite: ", saldo * 0.15)

