inicio = list(map(int, input().replace(":", " ").split(" ")))
final = list(map(int, input().replace(":", " ").split(" ")))
invalido = False
dia = hora = minuto = seg = 0

if final[0] >= inicio[0]:
    dia = final[0] - inicio[0]
    hora = final[1] - inicio[1]
    minuto = final[2] - inicio[2]
    seg = final[3] - inicio[3]
    if hora < 0:
        hora += 24
        dia -= 1
    if minuto < 0:
        minuto += 60
        hora -= 1
    if seg < 0:
        seg += 60
        minuto -= 1
    if dia < 0 or hora < 0 or minuto < 0 or seg < 0:
        invalido = True
if dia == 0 and hora == 0 and minuto == 0 and seg == 0:
    invalido = True

if invalido == False and final[0] >= inicio[0]:
    print(f"{dia} dia(s)")
    print(f"{hora} hora(s)")
    print(f"{minuto} minuto(s)")
    print(f"{seg} segundo(s)")
elif invalido == True or final[0] < inicio[0]:
    print("Data inválida!")

# 5 08:12:23
# 9 06:13:23

# 8 08:53:12
# 7 08:58:14

# 1 2:0:2
# 1 2:1:2
	
# 2 08:05:59
# 10 07:04:58

# 5 08:12:20
# 5 07:12:20

# 5 08:12:20
# 5 08:12:20

# 1 2:2:2
# 2 2:2:2

# 5 08:12:20
# 5 08:10:15

# 5 08:12:20
# 5 08:12:15

# 5 08:12:15
# 5 09:15:10

# 5 08:12:15
# 5 08:12:20

# 5 08:12:20
# 5 08:12:54

# 5 08:12:20
# 5 08:30:15

# 5 08:12:20
# 5 09:10:15

# 5 08:12:20
# 5 09:10:30

# 5 08:12:20
# 5 09:20:15

# 5 08:12:20
# 5 09:20:15