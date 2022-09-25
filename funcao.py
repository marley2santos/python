#funções

'''print() #imprimi uma mensagem (int, float, str) no console (terminal, cmd)
input() #retorna um dado informado pelo usuário (entrada padrão) e pode receber uma string
len() #recebe uma lista e retorna o tamanho dessa lista
max() #retorna o maior valor de uma lista'''


def saudacao(nome, curso="Python"):
    print(f"Seja bem-vindo, {nome}!")
    print(f"Olá, que bom ter você por aqui no {curso}!")

saudacao("Marley")

def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)

print("O resultado da sima é", resultado)

def calcuradora(num1, num2, operacao="+"):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2

resultado = calcuradora(10, 20)

print(resultado)