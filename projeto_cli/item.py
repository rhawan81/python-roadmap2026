class Item:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir(self):
        return f"Nome: {self.nome} | Idade: {self.idade}"
    def __str__(self):
        return f"{self.nome} ({self.idade} anos)"
