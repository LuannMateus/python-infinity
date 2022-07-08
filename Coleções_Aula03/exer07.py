nome = input("Digite o seu nome: ")
media = float(input("Digite a sua média: "))
situcao = ""

if media >= 6:
    situcao = "Aprovado"
elif media >= 5:
    situcao = "Recuperação"
else:
    situcao = "Reprovado"

# aluno = {
#     'nome': nome,
#     'media': media,
#     'situcao': situcao
# }

aluno = dict(nome=nome, media=media, situcao=situcao)

print(aluno)


