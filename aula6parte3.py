# chico = 1.5
# ze = 1.1
# anos = 0

# while ze <= chico:
#   chico = chico + 0.02
#   ze = ze + 0.03
#   anos = anos + 1
# print(anos)

contador = 0
somaIdades = 0
somaAlturaMeninas = 0
quantidadeMeninas = 0
quantidadeMaiorVinte = 0
IdadeAlunoMaisVelho = 0
alturaAlunoMaisVelho = 0

while True:
  print("contador:", contador)
  print("para encerrar a repetição informe uma idade negativa")
  idade = int(input("digite a idade: "))
  if idade < 0:
    print("fim do programa")
    break
  while idade <= 0 or idade >= 120:
    print(" > Idade invalida!")
    idade = int(input("digite a idade novamente: "))

  altura = float(input("digite a altura: "))
  while altura <= 0 or altura >= 2.5:
    print(" > Altura invalida!")
    altura = float(input("digite a altura novamente: "))
  
  genero = str(input("digite F para feminino e M para masculino: "))
  while genero != "F" and genero != "M":
    print(" > Genero invalido!")
    genero = str(input("digite F para feminino e M para masculino novamente: "))

  somaIdades = somaIdades + idade

  if idade > 20:
    quantidadeMaiorVinte =quantidadeMaiorVinte + 1

  if idade > IdadeAlunoMaisVelho:
    IdadeAlunoMaisVelho = idade
    alturaAlunoMaisVelho = altura

  if genero == "F":
    somaAlturaMeninas = somaAlturaMeninas + altura
    quantidadeMeninas = quantidadeMeninas + 1
  
  contador = contador + 1

if contador == 0:
  print("Dados não informados!")
else:
  print("Soma de todas as idades",somaIdades/contador)
  if quantidadeMeninas == 0:
    print("Não foram informados dados sobre mulheres")
  else:
    print("Media altura meninas: ", somaAlturaMeninas/quantidadeMeninas)
  print("Percentual de alunos maiores de 20 anos", (quantidadeMaiorVinte * 100) / contador)
  print("Altura aluno mais velho: ", alturaAlunoMaisVelho, "idade mais velho: ", IdadeAlunoMaisVelho)
