def func(nascimento):
    ano = 2022 - nascimento    

    if ano >= 16 and ano <= 17 or ano > 69:
        return "OPCIONAL!"
    elif ano >= 18 and ano <= 69:
        return "OBRIGATÓRIO!"
    else:
        return "NEGADO!"
 
nascimento = int(input("Digite seu ano de nascimento: "))

resultado = func(nascimento)

print(resultado)