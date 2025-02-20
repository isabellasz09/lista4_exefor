#Faça um programa que pergunte quantas pessoas o usuário deseja convidar para uma festa.
#Se ele digitar um número abaixo de 10, peça os nomes e após cada nome exiba a mensagem: "[nome] está convidado para a festa". 
#Se ele inserir um número 10 ou superior, exiba a mensagem "Muitas pessoas".
print("Isabella Carolina de Souza")
quantidade= int(input("Quantas o pessoas você ira convidar? "))
if quantidade <= 10:
    for i in range (quantidade):
        nome= (input("Digite o nome do convidado: "))
        print(nome,"está convidado a festa")
else:
    print("Você tem muitos convidados!")
    