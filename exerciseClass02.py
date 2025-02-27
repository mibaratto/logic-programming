import math
# /////////////////////////////////////////
# print("informe o seu nome")
# nome = input()
# print("nome: ", nome)

# /////////////////////////////////////////
# print("informe primeiro valor: ")
# valor01 = int(input())
# print("informe segundo valor: ")
# valor02 = int(input())

# soma = valor01 + valor02
# print("Soma: ", soma)

# /////////////////////////////////////////
# volume da esfera: volume = 4/3 * PI * raio**3 (potencia)
# valor_raio = float(input("""Cácula volume esfera. 
# Digite o raio da esfera: """))
# volume = 4/3 * (math.pi) * (math.pow(valor_raio, 3))
# area = 4 * math.pi * math.pow(valor_raio, 2)
# print( "O volume da esfera é: ", volume)
# print( "O area da esfera é: ", area)

# /////////////////////////////////////////
# |b**3 - 10| Módulo
# b = 2
# resultado = math.fabs(math.pow(b, 3) - 10)

# a = 2
# raiz quadadrada de (a + (b ** a + 1) / (2 * a -1)) + |b - a|
# math.sqrt(a + (math.pow(b, a + 1)) / (2 * a - 1)) + math.fabs(b - a)

# (math.sqrt((a + 3 * b) / (b + 1)) + (b ** 5)  / (math.fabs(b - a)))  +  (math.sqrt(math.sqrt(a) + 1))  / (b + 3 * a + b * (a ** 5)) - 1


# (6 * a * b ** (a + 1)) - (((a + 3 * b) / ( a + b - 1)) / (math.fabs((2 * b) - (a ** 3) - 1)))

# /////////////////////////////////////////
# valor_n = float(input("digite um número: "))

# valor_n_2 = math.pow(valor_n, 2)
# valor_n_3 = math.pow(valor_n, 3)
# valor_n_4 = math.pow(valor_n, 4)

# print(valor_n_2, valor_n_3, valor_n_4)

# /////////////////////////////////////////
# Fahrenheit to calesius
# temperature_F = float(input("digite a temperatura em Fahrenheit: "))
# temperature_C = 5 / 9 * (temperature_F - 32)
# print("A temperatura em celsius é: ", temperature_C)

# /////////////////////////////////////////

valor_a = float(input("digite o valor de a: "))
valor_b = float(input("digite o valor de b: "))

soma = valor_a + valor_b
diferenca = valor_a - valor_b
media = soma / 2
# distancia é o valor absoluto da diferença
distancia = math.fabs(diferenca)
maior_valor = ((valor_a + valor_b) + math.fabs(valor_a - valor_b)) / 2
menor_valor = (soma - distancia) / 2

print(soma, diferenca, media, distancia, maior_valor, menor_valor)