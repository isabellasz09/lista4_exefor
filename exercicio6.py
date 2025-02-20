#Peça um número abaixo de 50 e, em seguida,
#faça uma contagem regressiva de 50 até esse número,
#certificando-se de mostrar o número que eles inseriram na saída.
print("Isabella Carolina de Souza")
num= int(input("Digite um numero menor que 50: "))
if num >=50:
    print("O numero deve ser menor que 50.")
    for i in range(50,num -1,-1):
        print(i)
else:
    print("Muito bem, Obrigada!")