# fatorial
# se for maior que 2357 print o resto da divisao por 2357

def fatorial(n: int):
    if n <= 1:
        return n
    elif n < 7:
        return n * fatorial(n-1)
    return (n *  fatorial(n-1)) % 2357

print(fatorial(7))