count = []
def fibonacci(n):
    if n == 0:
        count.append(n)
        return 0
    elif n == 1:
        count.append(n)
        return 1
    count.append(n)
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(f"Fib({n}) = {fibonacci(n)} ({len(count)} chamadas)")
