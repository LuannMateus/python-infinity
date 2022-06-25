john = {
    'nome': 'Jonh Doe',
    'idade': 20
}

mary = {
    'nome': 'Mary Doe',
    'idade': 70
}

alex = {
    'nome': 'Alex Doe',
    'idade': 65
}

pessoas = [john, mary, alex]
pessoas_acima_media = []

idade = 0

for pessoa in pessoas:
    idade += pessoa['idade']

media = idade / len(pessoas)

for pessoa in pessoas:
    if pessoa['idade'] > media:
        pessoas_acima_media.push(pessoa)
