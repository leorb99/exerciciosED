class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()

s = input()         # le a string
queue = Queue()     # cria uma fila chamada queue
aux = []            # lista onde vou armazenar as letras dequeued

for char in s: 
    if char != '*':
        queue.enqueue(char)
    elif char == '*':
        aux.append(queue.dequeue())

for i in aux:
    print(i, end="")
print()

# ola*** mundo        ola
# c > python***       c >
# rir***,* o brev*******e verb******o *rir****        rir, o breve verbo rir
# arara*****      arara
# Ha  * quem  * me  *julgue  *perdido         Ha
# O atari piratao***************              O atari piratao