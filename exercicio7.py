#Peça ao usuário para inserir seu nome e um número. 
#Se o número for menor que 10, exiba o nome dele esse número de vezes;
#caso contrário, exiba a mensagem “Numero muito alto" três vezes.
print("Isabella Carolina de Souza")
nome=(input("Digite seu nome: "))
num=int(input("Digite um numero menor que 10: "))
if num < 10:
    for i in range(num):
        print(nome)
else: 
   for i in range(3):
    print("Numero muito alto!")
