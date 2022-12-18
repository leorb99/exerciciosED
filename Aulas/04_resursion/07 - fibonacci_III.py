def fibonacci(n):
    if n < 1:    
        dictionary[0] += 1
        return 0
    elif n == 1:
        dictionary[1] += 1
        return 1
    else:
        dictionary[n] += 1
        res = fibonacci(n-1) + fibonacci(n-2)
        return res

n = int(input())
dictionary = {}

for i in range(n+1):
    dictionary[i] = 0

print(f"fibonacci({n}) = {fibonacci(n)}.")

for k in dictionary:
    print(f"{dictionary[k]} chamada(s) a fibonacci({k}).")

# fib(n,c,d,s)


# def fib(n):
#     ident = ' ' * n     # identacao para auxiliar a visualizacao
#     # print(ident, 'fib', n)
#     if n < 1:
#         print(ident, 'retorna', 0)
#         return 0
#     elif n == 1:
#         print(ident, 'retorna', 1)
#         return 1
#     else:
#         res = fib(n-1) + fib(n-2)
#         print(ident, 'retorna', res)
#         return res
# fib(2)