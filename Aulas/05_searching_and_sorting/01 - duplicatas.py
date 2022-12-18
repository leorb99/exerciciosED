n = int(input())
roupas = list(input().split())
duplicatas = []

for i in roupas:
    if i not in duplicatas:
        duplicatas.append(i)

print(n - len(duplicatas))