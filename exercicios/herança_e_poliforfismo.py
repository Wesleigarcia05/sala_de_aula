class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print("Som de animal")


class Gato(Animal):
    def fazer_som(self):
        print("Miau")


# Exemplo de uso
animal = Animal("Animal")
animal.fazer_som()

gato = Gato("Mimi")
gato.fazer_som()
