n = int(input())
impares = []
i = 0
while len(impares) < n:
    if i % 2:
        impares.append(i)
    i += 1

def soma(impares):
    if len(impares) == 1:
        print(impares[0])
        return impares
    print(f"{impares[0]} + soma({impares[1:]})")
    soma(impares[1:])
soma(impares)

print("---------------")
print(f"{n} ** 2 == {n**2}")

