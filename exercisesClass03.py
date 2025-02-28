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

numero = int(input("digite um numero de 4 digitos: "))
numero >= 1000 and numero <=  9999

digito_4 = numero % 10
digito_3 = (numero // 10) % 10
digito_2 = (numero // 100 ) % 10
digito_1 = (numero // 1000) % 10

if digito_1 == digito_4 and digito_2 == digito_3 :
  print ("numero é capicua")
else: print("numero não é capicua")

print(digito_1, digito_2, digito_3, digito_4)
print(digito_4, digito_3, digito_2, digito_1)

