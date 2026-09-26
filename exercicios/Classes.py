#EXERCICIO 1
class Cachorro:
    def __init__(self, nome: str, raca: str, idade: int):
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
    def __init__(self, nome:str, cidade:str):
        self.nome = nome
        self.cidade = cidade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e moro em {self.cidade}."
pessoa = Pessoa("Ana", "São Paulo")

print(pessoa.apresentar())

#EXERCICIO 3
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        self.preco -= self.preco * (percentual / 100)


# Exemplo de uso
produto = Produto("Notebook", 2000)

print(produto.preco)  # 2000

produto.aplicar_desconto(10)

print(produto.preco)  # 1800

