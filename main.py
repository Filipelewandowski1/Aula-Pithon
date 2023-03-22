print("Olá Senhor!")
#Operações básicas
num1 = 10
num2 = 20
#Agregação
n1 = 'Filipe '
n2 = 'Gomes Vitorino'
total = n1 + n2
print(total)

#num1 = int(input('Insira um numero:'))
#num2 = int(input('Insira o segundo numero:'))
#total = num1 + num2
#print(f"o valor da soma é {total} ")

#salario = int(input('insira seu salario:'))

#if salario <= 1000:
 # aumento = salario + (salario*0.2)
  #print(f"Seu salário sofreu um aumento de 20% totalizando {aumento}")
#elif salario <= 5000:
 # aumento = salario
 # print(f"Seu salário sofreu um aumento de 10% totalizando {aumento}")

#Boletim

#nota1 = int(input('insira sua primeira nota: '))
#nota2 = int(input('insira sua segunda nota: '))
#media = (nota1 + nota2) /2
#if media >= 6:
 # print("Você foi aprovado")
#else:
 # print("Você foi reprovado")

#Nome

#nome = input('Insira seu nome: ')
#idade = int(input('Insira sua idade: '))
#if idade >= 18:
 # print("Você é maior de idade")
#else:
 # print("Você tem que criar vergonha na cara")

#case tabuada
#tabuada = int(input("Qual tabuada você deseja: "))
#cont = 9
#soma = 0
#while cont != 0:
 # soma = tabuada + cont
 # print(f"{tabuada} + {cont} = {soma}")
 # cont = cont -1

#parada = ""
#while True:
 # fruta = input("Insira o nome de uma fruta: ")
 # parada = input("Deseja continuar S/N: ").upper()
 # if parada != "S":
  #  break

while True:
  nome = input("Insira seu nome: ")
  idade = int(input("Insira sua idade: "))
  estado = input("Seu estado: ")
  parada = input("Você deseja continuar S/N: ").upper()
  if parada != "S":
    break