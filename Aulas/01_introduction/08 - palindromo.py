def palindromo(s: str, invertido: str) -> bool:
    count = 0
    for i in range((len(s) // 2)):
        if s[i] != invertido[i]:
            count += 1
    if count <= 1 and len(s) % 2:
        return True
    elif len(s) % 2 == 0 and count == 1:
        return True
    return False


s = input()
invertido = s[::-1]

if palindromo(s, invertido) == True:
    print("POSSÍVEL")
else:
    print("IMPOSSÍVEL")