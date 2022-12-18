def remove_duplicatas(lista: list): 
    nova_lista = []
    for i in lista:
        if i not in nova_lista:
            nova_lista.append(i)
    return nova_lista

print(remove_duplicatas([1,2,2,3]))
print(remove_duplicatas([1,1,1]))
print(remove_duplicatas([0,0,1,1,2,2,3,3]))
