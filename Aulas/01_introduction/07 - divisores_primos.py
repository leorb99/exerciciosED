n = int(input())

def is_prime(number: int):
    eh_primo = 0
    for i in range(1, number):
        if number % i == 0:
            eh_primo += 1
    if eh_primo == 1:
        return 1
    return 0


def primos_gemeos(n: int):
    a = 3
    lista = []
    while len(lista) < n:
        b = a + 2
        eh_primo = is_prime(a) + is_prime(b)
        if eh_primo == 2:
            tupla = a, b
            lista.append(tupla)
        a += 2        
    return lista

print(primos_gemeos(n))