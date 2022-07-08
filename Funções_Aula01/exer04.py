def area(larg, comp):
    return larg * comp

larg = float(input("Digite a largura: "))
comp = float(input("Digite o comprimento: "))

resultado = area(larg, comp)

print(f"Sua área será: {resultado}")