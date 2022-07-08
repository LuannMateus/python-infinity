def func(n):
    if n > 0:
        return "Positivo!"
    elif n < 0:
        return "Negativo!"
    else:
        return "Neutro!"

n = int(input("Digite um número inteiro: "))

resultado = func(n)

print(resultado)