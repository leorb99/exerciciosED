class No_ABB():
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None


def nivel(raiz, n):
	if raiz == None:
		return -1
	altura = -1
	if raiz.dado == n:
		return altura + 1
	altura = nivel(raiz.esq, n)
	if altura >= 0:
		return altura + 1
	altura = nivel(raiz.dir, n)
	if altura >= 0:
		return altura + 1
	return altura


raiz = No_ABB(1)
raiz.esq = No_ABB(3)
raiz.dir = No_ABB(2)
raiz.esq.esq = No_ABB(5)
raiz.esq.dir = No_ABB(4)
raiz.esq.dir.esq = No_ABB(6)

print(nivel(raiz,5))
