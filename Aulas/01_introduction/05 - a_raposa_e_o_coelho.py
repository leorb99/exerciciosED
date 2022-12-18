number_of_holes = int(input())
x_rabbit, y_rabbit = map(float, input().split())
x_fox, y_fox = map(float, input().split())
holes = {}
escaped = False

for i in range(number_of_holes):
    x_hole, y_hole = map(float, input().split())
    holes[f"Hole {i+1}"] = x_hole, y_hole

for v in holes.values():
    rabbit_distance = ((((x_rabbit - v[0])**2) + ((y_rabbit - v[1])**2)) ** 0.5)
    fox_distance = ((((x_fox - v[0])**2) + ((y_fox - v[1])**2)) ** 0.5)
    if fox_distance > (2 * rabbit_distance):
        print(f"O coelho pode escapar pelo buraco ({(v[0]):.3f}, {(v[1]):.3f}).")
        escaped = True
        break

if escaped == False:
    print("O coelho nao pode escapar.")

# 5
# -3522.960 313.498
# -5357.456 -9701.160
# -1967.790 -3246.494
# -6627.929 -6444.518
# -5865.633 895.295
# -8393.116 -8953.570
# -1905.882 -6328.591
