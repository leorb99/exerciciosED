n = int(input())
ceps = []
diff = []

for _ in range(n):
    ceps.append((input()))

ceps = sorted(ceps)

for i in range(len(ceps)-1):        # range vai ate len(ceps)-1 para evitar IndexError
    for j in range(len(ceps[i])):   # 'i' vai pegar a um cep e 'j' pega um numero do cep 
        if ceps[i][j] == ceps[i+1][j]:
            diff.append(ceps[i][j])

print(f"R$ {(len(diff) * 0.07):.2f}")