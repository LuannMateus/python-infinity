def func(n1, n2):
    if n1 < n2:
        print("N1 é menor que N2!")
    elif n2 < n1:
        print("N2 é menor que N1!")
    else:
        print("N1 é igual a N2!")

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

func(n1, n2)