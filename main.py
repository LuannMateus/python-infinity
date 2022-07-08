class Pessoa:
    nome = "",
    idade = 0

    def mudar_nome(self, valor): self.mudar_nome("")


p = Pessoa()

print(p.nome)

p.mudar_nome("John")

print(p.nome)
