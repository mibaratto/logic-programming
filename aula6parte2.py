

# numeroTermos = int(input("Informe a quantidade de termos: "))
# if numeroTermos <=0:
#   print("invalido")
# else: 
#   soma = 0
#   cont = 1
#   while cont <= numeroTermos:
#     soma = soma + 1/cont
#     cont = cont + 1

#   print(soma)


# numeroTermos = int(input("Informe a quantidade de termos: "))
# if numeroTermos <=0:
#   print("invalido")
# else: 
#   soma = 0
#   while numeroTermos > 0:
#     soma = soma + 1 / numeroTermos
#     numeroTermos = numeroTermos - 1

#   print(soma)


# numeroTermos = int(input("Informe a quantidade de termos: "))
# if numeroTermos <= 0:
#   print("invalido")
# else: 
#   soma = 0
#   numerador = 2
#   denominador = 1
#   while numeroTermos > 0:
#     soma = soma + numerador / denominador
#     numerador = numerador + 2
#     denominador = denominador + 2
#     numeroTermos = numeroTermos - 1

#   print(soma)

# a = int(input("informe o valor inicial do intervalo: "))
# while a < 0: 
#   print("invalido")
#   a = int(input("informe novamente o valor inicial do intervalo: "))
# b = int(input("informe o valor final do intervalo: "))
# while b < 0: 
#   print("invalido")
#   b = int(input("informe o novamente valor final do intervalo: "))

# if a > b:
#   numerosTesteDivisão = a
#   a = b
#   b = numerosTesteDivisão
# if a % 2 == 0: a = a + 1
# soma = 0
# while a <= b:
#   print("valores impares do intervalo", a)
#   soma = soma + a
#   a = a + 2
# print("soma impares do intervalo:", soma)



# achando divisores
valor = int(input("informe um número: "))
numerosTesteDivisão = 1
somaDivisores = 0
# while numerosTesteDivisão <= valor / 2: PERFORMANCE
while numerosTesteDivisão <= valor:
  if valor % numerosTesteDivisão == 0:
    somaDivisores = somaDivisores + numerosTesteDivisão
  # numero teste funciona como contador
  numerosTesteDivisão = numerosTesteDivisão + 1

# if (somaDivisores) == valor: print(valor, "é um numero perfeito") 
if (somaDivisores - valor) == valor: print(valor, "é um numero perfeito")
else: print(valor, "não é um número perfeito")

# 6, 28 são perfeitos
# depois da metade de um número não há mais divisores, então para economia de processamento testamos valor / 2. para 10,  depois do 5 não há divisores. para 100 depois do 50 não há divisores