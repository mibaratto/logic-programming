import math

# se detal == 0 --- há apenas 1 raiz, se delta < 0 --- não há raiz real, se delta > 0 --- há duas raizes.

# a = float(input("Ler valor A: "))
# b = float(input("Ler valor B: "))
# c = float(input("Ler valor C: "))

# delta = b ** 2 - 4 * a *c

# if delta < 0:
#   print("não há raíz real!")
# else:
#   if delta == 0:
#     x1 = -b/(2 * a)
#     print (f"Raíz é {x1}")
#   else:
#     x1 = (- b + math.sqrt(delta)) / (2 * a)
#     x2 = (- b - math.sqrt(delta)) / (2 * a)
#     print(f"Raízes são {x1} e {x2}")

# ////////////////////////////////////////


temperatura = float(input("digite a temperatura: "))
umidade = float(input("digite a umidade: "))

if temperatura > 30:
  if umidade > 60: 
    print("quente e úmido")
  else:
    print("quente")
else:
  if temperatura > 20 and temperatura <= 30:
    print("Ameno")
  if temperatura >= 10 and temperatura <=20:
    print("frio")
  if temperatura < 10:
    print("muito frio")