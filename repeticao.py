numero_sorteado = 15

numero_escolhido = int(input("informe um número entre 1 e 20"))

while numero_escolhido != numero_sorteado:
    print("Que pena! Não foi dessa vez!Tente novamente")
    numero_escolhido = int(input("informe um número entre 1 e 20"))

print("Congratulations!!!")

contador = 0

while contador < 5:
    print(contador)

    contador= contador + 1