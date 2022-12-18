class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)
      
    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

s = Stack() 
s.push(0)
s.push(2)
s.push(0)
s.push(2)
s.push('D')
s.push('E')
for i in s.items:
    print(i)

s = Stack()
s.push('x')
s.push('y')
s.pop()
s.push('z')
s.peek()
for i in s.items:
    print(i)

s = Stack() 
s.push(0)
s.push(2)
s.pop()
s.pop()
for i in s.items:
    print(i)