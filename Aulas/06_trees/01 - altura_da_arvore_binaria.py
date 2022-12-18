class No_ABB():
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None


def altura(raiz):
    if raiz == None or (raiz.esq == None and raiz.dir == None):
        return 0
    else:
        alt = max(altura(raiz.esq) + 1, altura(raiz.dir) + 1)
    return alt

# 1
# __3
# ____5
# ____4
# ______6
# __2

raiz = No_ABB(1)
raiz.esq = No_ABB(3)
raiz.dir = No_ABB(2)
raiz.esq.esq = No_ABB(5)
raiz.esq.dir = No_ABB(4)
raiz.esq.dir.esq = No_ABB(6)
print(altura(raiz))


#         1
#        / \
#       3   2
#      / \
#     5   4
#        /
#       6  


# 2
# raiz = No_ABB(1)

# 3
# __5
# __4
# ____6
# raiz = No_ABB(3)
# raiz.esq = No_ABB(5)
# raiz.dir = No_ABB(4)
# raiz.dir.esq = No_ABB(6)

# print("altura:", (mostra_arvore_e_altura(raiz)-1))




# myTree = ['a', ['b', ['d',[],[]], ['e',[],[]] ], ['c', ['f',[],[]], []] ]

# myTree = str(myTree).replace('[', '(')
# print((myTree).replace(']', ')'))