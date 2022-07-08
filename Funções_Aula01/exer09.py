def inverso(num):
    n1 = int(num[::-1])

    return n1

num = input("Digite um valor inteiro: ")

resultado = inverso(num)

print(f"Valor invertido: {resultado }")