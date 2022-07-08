count = 0

pergunta1 = input("Telefonou para a vítima [S/N]: ")
pergunta2 = input("Esteve no local do crime [S/N]: ")
pergunta3 = input("Mora perto da vítima [S/N]: ")
pergunta4 = input("Devia para a vítima [S/N]: ")
pergunta5 = input("Já trabalhou com a vítima [S/N]: ")

if pergunta1 == 'S':
    count += 1

if pergunta2 == 'S':
    count += 1

if pergunta3 == 'S':
    count += 1

if pergunta4 == 'S':
    count += 1

if pergunta5 == 'S':
    count += 1

if count == 2:
    print("Suspeita!")
elif count == 3 or count == 4:
    print("Cúmplice!")
elif count == 5:
    print("Assassino")
else:
    print("Inocente!")

