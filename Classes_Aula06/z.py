class Pessoa:
    def __init__(self, nome, data_nascimento, altura):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.altura = altura

    def troca_nome(self, nome):
        self.nome = nome

    def troca_data_nascimento(self, data_dascimento):
        self.data_nascimento = data_dascimento

    def troca_altura(self, altura):
        self.altura = altura

    def calcula_idade(self):
        year = int(self.data_nascimento[6:10])

        print(year)

        return 2022 - year

    def __str__(self):
        return f"""
        Nome: {self.nome}\n
        Data Nascimento: {self.data_nascimento}\n
        Altura: {self.altura}
        Idade: {self.calcula_idade()}
        """

pessoa = Pessoa("John Doe", "21/09/2001", 1.90)

print(pessoa.nome)

pessoa.troca_nome("Mary Doe")

print(pessoa.nome)

print(pessoa.calcula_idade())

print(pessoa)
