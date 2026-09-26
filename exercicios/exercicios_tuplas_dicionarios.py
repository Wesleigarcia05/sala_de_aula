#EXERCICIO 1
def contar_maiores_de_idade(pessoas):
    return sum(idade >= 18 for nome, idade in pessoas)

resultado = contar_maiores_de_idade([
    ("Ana", 17),
    ("Bruno", 22),
    ("Carla", 19)
])

print(resultado)  # 2

#EXERCICIO 2
def calcular_estoque_total(produtos):
    return sum(produtos.values())

resultado = calcular_estoque_total({
    "caneta": 10,
    "caderno": 5,
    "borracha": 8
})

print(resultado)  # 23

#EXERCICIO 3 
def filtrar_aprovados(notas_alunos):
    return [nome for nome, nota in notas_alunos.items() if nota >= 7.0]


# Exemplo de chamada
resultado = filtrar_aprovados({
    "Alice": 8.5,
    "Bruno": 5.0,
    "Carla": 7.0
})

print(resultado)
# Saída: ["Alice", "Carla"]

#EXERCICIO 4


