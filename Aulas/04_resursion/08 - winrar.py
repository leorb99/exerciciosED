
def decompress(n):
    letras = " ABCDEFGHIJKLMNOPQRSTUVYXWZ"
    if n == 0:
        return letras[(n%32)] 

    return letras[(n%32)] + decompress(n//32)

print(decompress(33))
print(decompress(54579234))
print(decompress(6040945729))