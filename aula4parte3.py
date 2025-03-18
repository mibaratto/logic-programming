mes = int(input("digite o número do mês: "))
if mes == 2:
  dias = 28
elif mes <= 7:
  if mes % 2 == 0:
    dias = 30
  else:
    dias = 31
else:
  if mes % 2 == 0:
    dias = 31
  else:
    dias = 30

print(f"tem {dias} dias")

# ////// resposta prof

if mes == 2:
  dias = 28
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
  dias = 30
else:
  dias = 31

print(f"tem {dias} dias")