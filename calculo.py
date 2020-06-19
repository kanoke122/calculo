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

print("3 atributos, 140\n")
pdd = 140
a1 = int(input("digite o tanto de acrobacia que você deseja ter : " ))
pdd = pdd - a1
print(pdd)

a1soma = a1 // 10 % 10

a2 = int(input("digite o tanto de furtividade que você quer ter : "))
pdd = pdd - a2
print(a2)
print(pdd)

a2soma = a2 // 10 % 10 

a3 = int(input("quanto de prestidigitação você vai querer? .. \n digite 0 para saber o que significa prestidigitação"))
if a3 == 0:
    print("Prestidigitação e a arte de iludir, \ntipo fazer alguma coisa 'sumir' na frente das pessoas em um piscar de olhos")
    a3 = int(input("quanto de prestidigitação você vai querer? : "))

a3soma = a3 // 10 % 10

calculo = (a1soma*3 + a2soma*3 + a3soma*3) / (a1soma - 2 + a2soma-2 + a3soma-2)
print(calculo + 1,"os 2 primeiros digitos da esquerda pra direita é sua destreza")

pdi = 186 
print("4 atributos , 186\n")
a1 = int(input("digite o tanto de ciencias humanas você quer ter"))

a1soma = a1 // 10 % 10

pdi = pdi - a1
print(pdi)

a2 = int(input("digite o tanto de ciencias forenses você deseja ter ?\ndigite 0 para saber o que forenses significa"))
if a2 == 0:
    print("forenses e a ciencia que os policiais usam para reconstituir cenas")
    a2 = int(input("digite o tanto de ciencias forenses que você quer ter : "))
    
pdi = pdi - a2
print(pdi)

a2soma = a2 // 10 % 10

a3 = int(input("quanto de ciencias naturais você quer ter?": ))

pdi = pdi - a3
print(pdi)

a3soma = a3 // 10 % 10

a4 = int(input("digite o tanto de ciencias religiosa voce vai querer : "))

a4soma = a4 // 10 % 10

calculo = (a1soma*4 + a2soma*4 + a3soma*4 + a4 soma*4)/(a1soma-2 + a2soma-2 + a3soma-2 +a4soma-2)
print(calculo + 1,"os 2 primeiros digitos da esquerda pra direita é sua inteligencia")

pdc = 100
print("2 atributos , 100")

a1 = int(input("digite quanto de escutar você quer ter : "))

pdc = pdc - a1

a1soma = a1 // 10 % 10
print(pdc)

a2 = int(input("insira quanto de encontrar você quer ter?: "))

pdc = pdc - a2
print(pdc)


a2soma = a2 // 10 % 10


calculo = (a1soma*2+ a2soma*2+)/(a1soma-2 + a2soma-2)
print(calculo + 1,"os 2 primeiros digitos da esquerda pra direita é sua constituição)


print("3 atributos, 140")
pds=140

a1 = int(input("quanto de medicina voce vai querer : ")

a1soma = a1 // 10 % 10
pds = pds - a1

a2 = int(input("digite quanto de p/socorros você quer ter :"))

a2soma = a2 // 10 % 10

pds = pds - a2

a3 = int(input("digite o quanto de intuição você quer ter ? : "))

a3soma = a3 // 10 % 10

pds = pds - a3

calculo = (a1soma*3 + a2soma*3 + a3soma*3) / (a1soma - 2 + a2soma-2 + a3soma-2)
print(calculo + 1,"os 2 primeiros digitos da esquerda pra direita é sua sabedoria")
     
pdca = 186
         
print(" 4 atributos, 186")

a1 = int(input("quanto de atuação você quer ter ?:"))

a1soma = a1 // 10 % 10
         
pdca =pdca - a1
         
a2 = int(input("quanto de labia você vai querer ? :"))

a2soma = a2 // 10 % 10

pdca = pdca - a2

a3 = int(input("digite o tanto de blefe que você quer ter : " ))

a3soma = a3 // 10 % 10

pdca = pdca - a3

a4 = int(input("digite quanto de intimidação você quer ter : "))

a4soma = a4 // 10 % 10

pdca = pdca - a4
         
calculo = (a1soma*4 + a2soma*4 + a3soma*4 + a4 soma*4)/(a1soma-2 + a2soma-2 + a3soma-2 +a4soma-2)
print(calculo + 1,"os 2 primeiros digitos da esquerda pra direita é seu carisma")

             
               
               
               
               
               
               
