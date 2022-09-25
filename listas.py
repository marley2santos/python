notas = [7.9, 9.7, 8.2]

lista = []
lista = list()
lista = [26, "Marley", 3.1415, False]
lista_de_listas = [10, [1, 2, 3]]

lista = [10, "Marley", 3.1415, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])
print(lista[3:6])

for elemento in lista:
    print(elemento)

print("Comprimento: ", len(lista))

for i in range(len(lista)):
    print(i)

lista = [1, 3, 12, 8, 2]

print("Antes do append: ", lista)

lista.append(3)

print("Depois do append: ", lista)

lista.insert(2, 10)

print("Depois do insert: ", lista)

lista2 = [1, 2, 3]

lista.extend(lista2)

print("Depois do extend:", lista)

lista.pop(0)

print("lista após o pop: ", lista)

lista.remove(3)

print("LIsta depois do remove: ", lista)

print("quantidade de 2 na lista:", lista.count(2))

print(len(lista))

print(sum(lista))

print(max(lista))

print(min(lista))