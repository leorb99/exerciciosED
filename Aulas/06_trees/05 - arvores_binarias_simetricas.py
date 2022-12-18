class ArvoreBinaria():
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir


travessia_em_ordem = []
def em_ordem(raiz, node=None):
    if node is None:
        node = raiz
    if node.esq:
        em_ordem(node.esq)
    travessia_em_ordem.append(node.dado)
    if node.dir:
        em_ordem(node.dir)

def verificaSimetria(raiz):
    em_ordem(raiz)
    global travessia_em_ordem
    if travessia_em_ordem == travessia_em_ordem[::-1]:
        travessia_em_ordem = []
        return True
    travessia_em_ordem = []
    return False    

raiz = ArvoreBinaria(1, ArvoreBinaria(0, ArvoreBinaria(1), ArvoreBinaria(0)), ArvoreBinaria(0, ArvoreBinaria(0), ArvoreBinaria(1)))
print(verificaSimetria(raiz))

raiz = ArvoreBinaria(1, ArvoreBinaria(0, ArvoreBinaria(0), ArvoreBinaria(1)), ArvoreBinaria(0, ArvoreBinaria(0), ArvoreBinaria(1)))
print(verificaSimetria(raiz))

raiz = ArvoreBinaria(0, ArvoreBinaria(1, ArvoreBinaria(1, None, None), ArvoreBinaria(0, None, None)), ArvoreBinaria(1, ArvoreBinaria(1, None, None), ArvoreBinaria(0, None, None)))
print(verificaSimetria(raiz))

raiz = ArvoreBinaria(0)
print(verificaSimetria(raiz))

raiz = ArvoreBinaria(1)
print(verificaSimetria(raiz))

raiz = ArvoreBinaria(0, ArvoreBinaria(0, None, None), ArvoreBinaria(1, None, None))
print(verificaSimetria(raiz))

raiz = ArvoreBinaria(0, ArvoreBinaria(1, None, None), ArvoreBinaria(1, None, None))
print(verificaSimetria(raiz))

raiz = ArvoreBinaria(1, ArvoreBinaria(1, None, None), ArvoreBinaria(1, None, None))
print(verificaSimetria(raiz))

raiz = ArvoreBinaria(0, ArvoreBinaria(1, None, None), ArvoreBinaria(1, None, None))
print(verificaSimetria(raiz))

raiz = ArvoreBinaria(0, ArvoreBinaria(0, None, None), ArvoreBinaria(0, None, None))
print(verificaSimetria(raiz))

raiz = ArvoreBinaria(1, ArvoreBinaria(1, None, None), ArvoreBinaria(0, None, None))
print(verificaSimetria(raiz))