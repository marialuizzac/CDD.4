lista = [""]*3
tam = len(lista)

for i in range(tam):
    lista[i] = input("Digite um número: ")
print(lista)

for x in range(tam-1,-1,-1):
    print(lista[x], end=" ")
