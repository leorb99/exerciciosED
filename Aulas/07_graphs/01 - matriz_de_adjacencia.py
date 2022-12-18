class Matriz:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = []
        for i in range(vertices):
            self.grafo += [[0]*vertices]


def nao_direcionado(matriz, u, v, p):
        matriz.grafo[u-1][v-1] = p 
        matriz.grafo[v-1][u-1] = p

def direcionado(matriz, u, v, p):
        matriz.grafo[u-1][v-1] = p
    
def mostra_matriz(matriz):
    for i in matriz.grafo:
        for j in i:
            print(f"{j:4d}", end="")
        print()


espec = input().split()
matriz = Matriz(int(espec[0]))

if espec[2] == "N":
    for i in range(int(espec[1])):
        arestas = list(map(int, input().split()))
        nao_direcionado(matriz, arestas[0], arestas[1], arestas[2])

elif espec[2] == "D":
    for i in range(int(espec[1])):
        arestas = list(map(int, input().split()))
        direcionado(matriz, arestas[0], arestas[1], arestas[2])

mostra_matriz(matriz)
