n1 = 3
n2 = 2

def suma():
    return n1 + n2

def resta():
    return n1 - n2

def multiplicacion():
    return n1 * n2

def division():
    return n1 / n2

resultado = {
    "suma": suma(),
    "resta": resta(),
    "multiplicación": multiplicacion(),
    "división": division()
}

print(resultado)