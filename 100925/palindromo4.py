def palind(s):
    s = s.replace(" ", "").lower()
    
    if len(s) <= 1:
        return "é palíndromo"
    
    if s[0] != s[-1]:
        return "não é palíndromo"
    
    return palind(s[1:-1])

print(palind("beatriz"))
print(palind("arara"))
print(palind("abc"))
