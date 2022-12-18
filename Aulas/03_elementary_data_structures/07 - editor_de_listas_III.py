class Lista:
    def __init__(self):
        self.items = []
    
    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def remove_all(self, item):
        count = 0
        while item in self.items:
            self.items.remove(item)
            count += 1
        return count

    def remove_item(self, index):
        value = self.items[index]
        self.items.pop(index)
        return value

    def replacement(self, value, number):
        for i in self.items:
            if i == value:
                self.items.insert(self.items.index(i), number)
                self.items.remove(i)
                break

    def counter(self, value):
        count = 0
        for i in self.items:
            if i == value:
                count += 1
        return count


lista = Lista()
op = []
while 'X' not in op:
    op = list(input().split())
    if op[0] == 'I':
        lista.add_front(int(op[1]))
    elif op[0] == 'F':
        lista.add_rear(int(op[1]))
    elif op[0] == 'P':
        print(lista.remove_rear())
    elif op[0] == 'D':
        print(lista.remove_front())
    elif op[0] == 'V':
        print(lista.remove_all(int(int(op[1]))))
    elif op[0] == 'E':
        print(lista.remove_item((int(op[1]))-1))
    elif op[0] == 'T':
        lista.replacement(int(op[1]), int(op[2]))
    elif op[0] == 'C':
        print(lista.counter(int(op[1])))

print()
for i in lista.items:
    print(i)
# lista.add_rear(10)
# lista.add_rear(11)
# lista.add_rear(12)
# lista.add_front(32)
# lista.add_front(78)
# print(lista.remove_rear())
# print(lista.remove_front())
# print(lista.remove_all(10))
# print(lista.remove_item(2-1))
# lista.replacement(32, 89)
# lista.counter(89)