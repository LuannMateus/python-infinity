def func(lista):
    contador = 0

    for item in lista:
        if item not in 'aeiou':
            contador += 1
    
    print(contador)

lista = ['a', 'b', 'e', 'y', 'w']

func(lista)

