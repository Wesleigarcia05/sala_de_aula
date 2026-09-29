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
def tuplas_para_dicionario(lista_tuplas):
    dicionario = {}

    for chave, valor in lista_tuplas:
        if valor >= 0:
            dicionario[chave] = valor

    return dicionario


# Exemplo de chamada
resultado = tuplas_para_dicionario([
    ("a", 10),
    ("b", -5),
    ("c", 20)
])

print(resultado)

#EXERCICIO 5
def buscar_codigo(produtos, codigo_alvo):
    i = 0

    while i < len(produtos):
        if produtos[i]["id"] == codigo_alvo:
            return produtos[i]["nome"]

        i += 1

    return None


# Exemplo de chamada
resultado = buscar_codigo(
    [{"id": 101, "nome": "Teclado"}, {"id": 102, "nome": "Mouse"}],
    102
)

print(resultado)

#EXERCICIO 6



