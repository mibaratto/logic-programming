import math
# altura = float(input("Digite sua altura: "))
# genero = int(input("digite 1 para mulher e dois para homem: "))

# if genero != 1 and genero != 2: 
#   print("escolha um genero valido")
#   resultado = 0

# if genero == 2 :
#   resultado = 72.7 * altura - 58
# if genero == 1 :
#   resultado = 62.1 * altura - 44.7

# print(resultado)

# ///////////////////////////////////////////////

# horario_hora_inicio = int(input("Informe a hora de inicio: "))
# horario_minutos_inicio = int(input("Informe os minutos de inicio: "))
# horario_hora_fim = int(input("Informe a hora de fim: "))
# horario_minutos_fim = int(input("Informe os minutos de fim: "))


# hora_inicio_em_minutos = (horario_hora_inicio * 60 ) + horario_minutos_inicio
# hora_fim_em_minutos = (horario_hora_fim * 60) + horario_minutos_fim

# if horario_hora_inicio > horario_hora_fim :
#   minutos_total_dia = 24 * 60
#   tempo_total_jogo_minutos = (minutos_total_dia - hora_inicio_em_minutos) + hora_fim_em_minutos


# else:
#   tempo_total_jogo_minutos = hora_fim_em_minutos - hora_inicio_em_minutos

# tempo_jogo_horas = tempo_total_jogo_minutos // 60
# tempo_parcial_minutos = tempo_total_jogo_minutos%60

# print(tempo_jogo_horas, tempo_parcial_minutos)

# ///////////////////////////////////////////

# numero = int(input("digite um numero de 4 digitos: "))
# numero >= 1000 and numero <=  9999

# digito_4 = numero % 10
# digito_3 = (numero // 10) % 10
# digito_2 = (numero // 100 ) % 10
# digito_1 = (numero // 1000) % 10

# if digito_1 == digito_4 and digito_2 == digito_3 :
#   print ("numero é capicua")
# else: print("numero não é capicua")

# print(digito_1, digito_2, digito_3, digito_4)
# print(digito_4, digito_3, digito_2, digito_1)

# /////////////////////////////////////////// maior de 3 valores em ordem crescente

# valor1 = int(input("Digite valor 1: "))
# valor2 = int(input("Digite valor 2: "))
# valor3 = int(input("Digite valor 3: "))
# valor4 = int(input("Digite valor 4: "))

# valorMax = valor1
# if valor2 > valorMax :
#   valorMax = valor2
# if valor3 > valorMax :
#   valorMax = valor3
# if valor4 > valorMax:
#   valorMax = valor4

# valorMin = valor1
# if valor2 < valorMin:
#   valorMin = valor2
# if valor3 < valorMin:
#   valorMin = valor3
# if valor4 < valorMin:
#   valorMin = valor4

# valorInterm1 = valor1
# if valor2 != valorMax and valor2 != valorMin:
#   valorInterm1 = valor2
# elif valor3 != valorMax and valor3 != valorMin:
#   valorInterm1 = valor3
# elif valor4 != valorMax and valor4 != valorMin:
#   valorInterm1 = valor4

# valorInterm2 = valor1
# if valor2 != valorMax and valor2 != valorMin and valor2 != valorInterm1:
#   valorInterm2 = valor2
# elif valor3 != valorMax and valor3 != valorMin  and valor3 != valorInterm1:
#   valorInterm2 = valor3
# elif valor4 != valorMax and valor4 != valorMin  and valor4 != valorInterm1:
#   valorInterm2 = valor4

# valorIntermMenor = valorInterm1
# if valorInterm2 < valorIntermMenor:
#   valorIntermMenor = valorInterm2

# valorIntermMaior = valorInterm1
# if valorInterm2 > valorIntermMaior:
#   valorIntermMaior = valorInterm2


# # responsta do prof
# valorMeio = valor1 + valor2 + valor3 - valorMax - valorMin

# print(valorMin, valorIntermMenor, valorIntermMaior, valorMax )

# /////////////////Respota de professora

# valor1 precisa ser menor valor2 senão:
# if valor1 > valor2:
#   aux = valor1
#   valor1 = valor2
#   valor2 = aux

# if valor1 > valor3:
#   aux = valor1
#   valor1 = valor3
#   valor3 = aux

# if valor1 > valor4:
#   aux = valor1
#   valor1 = valor4
#   valor4 = aux

# # se valor dois for maior que valor3
# if valor2 > valor3: 
#   aux = valor2
#   valor2 = valor3
#   valor3 = aux

# if valor2 > valor4:
#   aux = valor2
#   valor2 = valor4
#   valor4 = aux

# if valor3 > valor4:
#   aux = valor3
#   valor3 = valor4
#   valor4 = aux

# print(valor1, valor2, valor3, valor4)

# //////////////// cacula valor de produto

precoCusto = float(input("Digite o valor do produto: "))


if precoCusto < 0:
  print("valor invalido")
else:
  if precoCusto < 10:
    valorProdutoVenda = precoCusto + (precoCusto * 0.7)
    # ou valorProdutoVenda = precoCusto * 1.7
  if precoCusto >= 10 and precoCusto < 30:
    valorProdutoVenda = precoCusto + (precoCusto * 0.5)
  if precoCusto >= 30 and precoCusto < 50:
    valorProdutoVenda = precoCusto + (precoCusto * 0.4)
  if precoCusto >= 50:
    valorProdutoVenda = precoCusto + (precoCusto * 0.3)

print(valorProdutoVenda)
  

