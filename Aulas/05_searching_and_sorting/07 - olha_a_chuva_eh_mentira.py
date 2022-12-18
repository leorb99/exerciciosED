from math import ceil


def sort(item):
    # -item[0] retorna o elemento 0 em ordem decrescente e
    #  se tiver itens repetidos o item[1] ordena em ordem crescente
    return -item[0], item[1]

n = int(input())
consumo_medio = []

for i in range(n):
    pessoas, consumo = map(int, input().split())
    # if para prevenir ZeroDivisonError, podia tere usado um try except tbm
    if pessoas == 0:
        consumo_medio.append((0, pessoas))
    else:
        consumo_medio.append((ceil(consumo/pessoas), pessoas))

consumo_medio = sorted((consumo_medio), key=sort)

for i in consumo_medio:
    print(i[0], "/", i[1])
