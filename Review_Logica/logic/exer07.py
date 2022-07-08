metros = float(input("""
Digite o tamanho em metros quadrados: """))

if metros % 18 == 0:
    latas = metros / 18
else:
    latas = int(metros / 18) + 1

if metros % 3.6 == 0:
    galoes = metros / 3.6
else:
    galoes = int(metros / 3.6) + 1

print(f"A quantidades de latas será: {latas}\nO valor total será: {latas * 80}")
print(f"A quantidades de galões será: {galoes}\nO valor total será: {galoes * 25}")
