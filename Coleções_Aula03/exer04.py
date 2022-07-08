palavras = ('DOING', 'EXERCISES', 'IS', 'THE', 'BEST', 'WAY', 'TO', 'LEARN')

palavra_lista = []

vogais = ""

for palavra in palavras:
    for letra in palavra:
        if letra in 'AEIOU':
            vogais += letra
    palavra_lista.append(vogais)

    vogais = ""
    
print(palavra_lista)