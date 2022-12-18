# le m, n m = qtd de numeros n = denominador e qtd de numeros a serem inseridos na estrutura de dados
from random import randint

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)
        # self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop(0)
        # return self.items.pop()

    def size(self):
        return len(self.items)

def media_movel(numbers, aux, n):
    soma = 0
    if aux.isEmpty() == True:
        for i in range(n):
            aux.enqueue(numbers.dequeue())
    elif aux.isEmpty() == False:    
        aux.enqueue(numbers.dequeue())
    media = somalista1(aux.items) // n
    aux.dequeue()

    return media, numbers, aux

def somalista1(aux):
    if aux.size() <= 1:
        return aux.dequeue()
    else:
        return aux.dequeue() + aux.items 


m, n = map(int, input().split())
numbers = Queue()
aux = Queue()

for i in list(map(int, input().split())):
    numbers.enqueue(i)

while numbers.isEmpty() == False:
    print(media_movel(numbers, aux, n)[0])

# 100000 1
# 1 2 3 4 5...100000