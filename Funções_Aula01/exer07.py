def func(a, b, limite):
    soma = a + b

    if soma > limite:
        return True
    else:
        return False

resultado = func(10, 20, 20)

print(resultado)