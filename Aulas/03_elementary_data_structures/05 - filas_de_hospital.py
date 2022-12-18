class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

fila_original = Queue()
fila_preferencial = Queue()
fila_atualizada = Queue()
res_preferencial = Queue()
res_geral = Queue()
senha = 0
nova = 0

while True:
    senha += 1
    try:
        idade = int(input())
    except ValueError:
        break
    fila_original.enqueue(f"{senha} - {idade}")
    if idade >= 60:
        fila_preferencial.enqueue(f"{senha} - {idade}")
        res_preferencial.enqueue(senha)
    elif idade <= 60:
        fila_atualizada.enqueue(f"{senha} - {idade}")
        res_geral.enqueue(senha)

print("Fila geral original")
for i in range(fila_original.size()):
    print(fila_original.dequeue())

print("\nFila preferencial")
for i in range(fila_preferencial.size()):
    print(fila_preferencial.dequeue())

print("\nFila geral atualizada")
for i in range(fila_atualizada.size()):
    print(fila_atualizada.dequeue())

print("\nResultado esperado fila preferencial")
for i in range(res_preferencial.size()):
    print(i+1, "-", res_preferencial.dequeue())

print("\nResultado esperado fila geral")
for i in range(res_geral.size()):
    print(i+1, "-", res_geral.dequeue())

