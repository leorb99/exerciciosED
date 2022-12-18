# fibonacci
fib = []
def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
        return 0
    elif n == 2:
        return [0, 1]
    fib = fibonacci(n-1)
    fib.append(fib[-2] + fib[-1])
    return fib


print(fibonacci(2))
print(fibonacci(1))
print(fibonacci(10))
print(fibonacci(0))
print(fibonacci(30))

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
# fib2 = []

# def fibonacci(n):
#     t1 = 0
#     t2 = 1
#     t3 = 0
#     for _ in range(0, n):
#         fib2.append(t1)
#         t3 = t1 + t2
#         t1 = t2
#         t2 = t3
#     return fib2

# print(fibonacci(2))
# print(fibonacci(1))
# print(fibonacci(10))
# # print(fibonacci(10))
