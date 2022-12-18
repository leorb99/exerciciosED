from math import ceil

tamanho = int(input())
segundos = 0
velocidade = []

print(f"Transmitindo {tamanho} bytes...")
while tamanho > 0:
    baixando = int(input())
    velocidade.append(baixando)
    segundos += 1
    tamanho -= baixando
    if segundos % 5 == 0:
        if sum(velocidade) == 0:
            print("Tempo restante: pendente...")
        elif sum(velocidade) != 0 and tamanho != 0:
            velocidade_media = (sum(velocidade) / 5)
            tempo_restante = (tamanho*10 / velocidade_media*10) # gambiarra necessaria
            print(f"Tempo restante: {ceil(tempo_restante/100)} segundos.")
            # sem as gambiarras acima um dos casos dava errado
            # 69/4.6 = 15, mas no python = 15.000000000000002
            # e quando arredonda dava 16
        velocidade = []

print(f"Tempo total: {segundos} segundos.")     