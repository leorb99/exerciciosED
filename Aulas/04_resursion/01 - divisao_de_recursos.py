# mdc

def div(a, b):
    if a > 0 and b > 0:
        return div(b, a % b)    
    return a
    
a, b = map(int, input().split())

print(div(a, b))