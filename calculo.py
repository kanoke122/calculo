a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0 
a6 = 0
a7 = 0
a1soma = 0
a2soma = 0 
a3soma = 0
a4soma = 0
a5soma = 0
a6soma = 0
a7soma = 0



pdf=140
print("3 atributos\n")
print (pdf, "você não pode colocar mais que sua pontuação, mas você tem que gastar todos os pontos.\nexistem 5 atributos gerais e atributos secundarios, esses",pdf, " vão distribuir entre esses 3 atributos secundarios, então relaxe e escolha com sabedoria\n")
a1 = int(input("digite o tanto de luta que vc quer ter : "))
pdf = pdf - a1
print(pdf)

a1soma = a1 // 10 % 10

a2 = int(input("digite o tanto de arremesso que vc quer ter : "))
pdf = pdf - a2
print(pdf)

a2soma = a2 // 10 % 10

a3 = int(input("digite o tanto de atletismo que você quer ter : "))
pdf = pdf - a3
print(pdf)

a3soma = a3 // 10 % 10

calculo = (a1soma*3 + a2soma*3 + a3soma*3) / (a1soma - 2 + a2soma-2 + a3soma-2)
print(calculo + 1,"os 2 primeiros digitos da esquerda pra direita é sua força")
