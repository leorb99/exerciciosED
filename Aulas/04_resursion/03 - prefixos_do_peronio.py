def peronio(string1: str, string2: str):
    try:
        if string1[0] == string2[0]:
            return peronio(string1[1:], string2[1:]) + 1
    except:
        IndexError()
    return 1
    # return len(str1) -  len(string1) + 1
str1 = 'quasenada'
str2 = 'quasetudo'

print(peronio(str1, str2)) #6



def funcao(lista, x):
    if len(lista) == 0: # lista vazia, não há o que comparar 
        return 0
    # verifica o primeiro elemento 
    qtd = 1 if lista[0] > x else 0
    # soma com a contagem do restante da lista 
    return qtd + funcao(lista[1:], x)
 
print(funcao([1,2,3,4,5], 3)) # 2