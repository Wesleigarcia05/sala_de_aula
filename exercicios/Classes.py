#EXERCICIO 1
class Cachorro:
    def __init__(self, nome: str, raca: str, idade: int):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        print(f"Au au! O {self.nome} está latindo.")



cachorro1 = Cachorro("Rex", "Pastor Alemão", 3)


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
      def __init__(self, nome:str, preco:int):
        self.nome = nome
        self.preco = preco

      def aplicar_desconto(self, percentual):
        self.preco -= self.preco * (percentual / 100)


# Exemplo de uso
produto = Produto("Notebook", 2000)

print(produto.preco)  # 2000

produto.aplicar_desconto(10)

print(produto.preco)  # 1800

#EXERCICIO 4
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


retangulo1 = Retangulo(10, 5)

print("Área:", retangulo1.calcular_area())
print("Perímetro:", retangulo1.calcular_perimetro())

#EXERCICIO 5
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor


conta1 = ContaBancaria("João")

print("Titular:", conta1.titular)
print("Saldo inicial:", conta1.saldo)

conta1.depositar(100)
print("Saldo após depósito:", conta1.saldo)

conta1.depositar(50)
print("Saldo após segundo depósito:", conta1.saldo)

#EXERCICIO 6
class carro:
    def __init__(self, marca:str, modelo:str):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False
meu_carro = carro("toyota", "corolla")

print(meu_carro.marca)
print(meu_carro.modelo)
print(meu_carro.ligado)

meu_carro.ligar()
print(meu_carro.ligado)

meu_carro.desligar()
print(meu_carro.ligado)

        
