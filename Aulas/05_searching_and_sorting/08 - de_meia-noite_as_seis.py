def task(plano, turno):
    for conteudo in turno:
        if conteudo in plano:
            plano.remove(conteudo)
        elif conteudo not in plano:
            plano.append(-1)   
    return plano 

n = int(input())
plano = []

for i in range(n):
    plano = list(input())
    matutino = input()
    vespertino = input()
    noturno = input()
    task(plano, matutino)
    task(plano, vespertino)
    task(plano, noturno)
    if len(plano) == 0:
        print("It's in the box!")
    elif -1 not in plano:
        print(f"Bora ralar: {''.join(sorted(set((plano))))}")
    else:
        print("You died!")
