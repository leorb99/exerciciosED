n = input()
elenco = sorted(list(map(int, input().split())), reverse=True)
titular = (elenco[:11])
reserva = (elenco[11:])

while len(reserva) > 11:
    reserva.pop()

print(sum(titular) - sum(reserva))
# print(titular - reserva)