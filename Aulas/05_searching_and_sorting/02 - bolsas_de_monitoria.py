def bubbleSort(lista):
    for passnum in range((len(lista)-1), 0, -1):
        for i in range(passnum):
            if lista[i] < lista[i+1]:
                temp, lista[i] = lista[i], lista[i+1]
                lista[i+1] = temp
    return lista

n = int(input())
ira = []
for _ in range(n):
    ira.append(float(input()))
# ordenado = sorted((ira), reverse=True)
ordenado = bubbleSort(ira)
for i in ordenado: 
    print(f"{i:.2f}")