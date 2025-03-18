# for num in range(1, 11):
#   print(num)

# num = 1
# while num <= 10:
#   print(num)
#   num = num + 1


# Fatorial
# num = int(input("informe um número natural: "))
# multiplicador = 1
# # quando iniciamos variaveis que vao multiplicar o valor neutro é 1, e não zero como na soma
# fatorial = 1
# while multiplicador <= num:
#   fatorial = fatorial * multiplicador
#   multiplicador = multiplicador +1

# print(fatorial)

# achando divisores
# valor = int(input("informe um número: "))
# aux = 1
# while aux <= valor:
#   if valor % aux == 0:
#     print(aux)
#   aux = aux + 1


# achando primos
valor = int(input("informe um número: "))
divisores = 1
contadorDivisores = 0
while divisores <= valor:
  if valor % divisores == 0:
    contadorDivisores = contadorDivisores + 1
  divisores = divisores + 1

if contadorDivisores == 2:
  print(valor, "é primo")
else: print(valor, "não é primo")
    

