#EXERCICIO 1
class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        print(f"Au au! O {self.nome} está latindo.")


# Criando um cachorro
cachorro1 = Cachorro("Rex", "Pastor Alemão", 3)

# Fazendo o cachorro latir
cachorro1.latir()

#EXERCICIO 2
class Pessoa:
    def __init__(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e moro em {self.cidade}."
pessoa = Pessoa("Ana", "São Paulo")

print(pessoa.apresentar())
