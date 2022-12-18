class Arvore():
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []


def mostra(raiz, sep):
    imprime(raiz, sep, level=0)

def imprime(raiz, sep, level=0):
    print(f'{sep * level}{raiz.dado}')
    for filho in raiz.filhos:
        imprime(filho, sep, (level + 1))

raiz = Arvore('A')
raiz.filhos.append(Arvore('B'))
raiz.filhos.append(Arvore('C'))
raiz.filhos[0].filhos.append(Arvore('D'))
raiz.filhos[0].filhos.append(Arvore('E'))
raiz.filhos[0].filhos.append(Arvore('F'))
raiz.filhos[1].filhos.append(Arvore('G'))
raiz.filhos[1].filhos[0].filhos.append(Arvore('H'))

raiz1 = Arvore('A')
raiz1.filhos.append(Arvore('B'))
raiz1.filhos.append(Arvore('C'))
raiz1.filhos[0].filhos.append(Arvore('D'))
raiz1.filhos[0].filhos.append(Arvore('E'))
raiz1.filhos[0].filhos.append(Arvore('F'))
raiz1.filhos[1].filhos.append(Arvore('G'))
raiz1.filhos[1].filhos[0].filhos.append(Arvore('H'))
mostra(raiz, '--')
mostra(raiz1, '   ')
# mostra(arvore, '--')
# print(raiz.filhos)