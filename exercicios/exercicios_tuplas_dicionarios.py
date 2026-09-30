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
def preco_medio(precos_dict):
    if not precos_dict:
        return 0.0

    return sum(precos_dict.values()) / len(precos_dict)

print(preco_medio({"livro": 30.0, "caneta": 10.0, "mochila": 80.0}))

#EXERCICIO 7
def classificar_paridade(numeros):
    pares = []
    impares = []

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    return {
        "pares": pares,
        "impares": impares
    }
print(classificar_paridade([1, 2, 3, 4, 5]))

#EXERCICIO 8
def contar_frequencia(palavras):
    frequencia = {}

    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

    return frequencia

print(contar_frequencia(["sol", "lua", "sol", "estrela", "sol"]))

#EXERCICIO 9
def inverter_dicionario(dicionario):
    novo_dicionario = {}
    return {valor: chave for chave, valor in dicionario.items()}

print(inverter_dicionario({"Brasil": "Brasília", "França": "Paris"}))

#EXERCICIO 10
def atualizar_estoque(estoque_atual, novas_compras):
    for produto, quantidade in novas_compras:
        if produto in estoque_atual:
            estoque_atual[produto] += quantidade
        else:
            estoque_atual[produto] = quantidade

    return estoque_atual


estoque = {"maçã": 10, "banana": 5}

compras = [("maçã", 5), ("laranja", 12)]

resultado = atualizar_estoque(estoque, compras)

print(resultado)

#EXERCICIO 11
def filtrar_funcionarios(funcionarios, departamento, salario_minimo):
    nomes = []

    for funcionario in funcionarios:
        if funcionario["depto"] == departamento and funcionario["salario"] >= salario_minimo:
            nomes.append(funcionario["nome"])

    return nomes

funcionarios = [
    {"nome": "Ana", "depto": "TI", "salario": 5000},
    {"nome": "Beto", "depto": "TI", "salario": 3000},
    {"nome": "Caio", "depto": "RH", "salario": 4000}
]

resultado = filtrar_funcionarios(funcionarios, "TI", 4000)

print(resultado)

#EXERCICIO 12
def processar_pedidos_fila(fila_pedidos, catalogo_precos):
    resultados = {}

    while fila_pedidos:
        id_pedido, nome_item, quantidade = fila_pedidos.pop(0)

        preco = catalogo_precos[nome_item]
        valor_total = preco * quantidade

        resultados[id_pedido] = valor_total

    return resultados

fila = [
    (101, "café", 2),
    (102, "bolo", 1)
]

catalogo = {
    "café": 5.0,
    "bolo": 12.0
}

resultado = processar_pedidos_fila(fila, catalogo)

print(resultado)

#EXERCICIO 13
def agrupar_por_idade(pessoas):
    grupos = {
        "jovens": [],
        "adultos": [],
        "idosos": []
    }

    for nome, idade in pessoas:
        if idade < 18:
            grupos["jovens"].append(nome)
        elif idade < 60:
            grupos["adultos"].append(nome)
        else:
            grupos["idosos"].append(nome)

    return grupos

pessoas = [
    ("Lucas", 15),
    ("Maria", 34),
    ("João", 68)
]

resultado = agrupar_por_idade(pessoas)

print(resultado)

#EXERCICIO 14
def melhor_jogador(pontuacoes):
    campeoes = {}

    for categoria, jogadores in pontuacoes.items():
        campeao = max(jogadores, key=lambda jogador: jogador[1])
        campeoes[categoria] = campeao[0]

    return campeoes

pontuacoes = {
    "FPS": [("Alex", 150), ("Bia", 200)],
    "RPG": [("Caio", 500), ("Dani", 450)]
}

print(melhor_jogador(pontuacoes))

#EXERCICIO 15
def chaves_acima_da_media(dados_dict):
    valores = list(dados_dict.values())
    media = sum(valores) / len(valores)

    resultado = []

    for chave, valor in dados_dict.items():
        if valor > media:
            resultado.append(chave)

    resultado.sort()

    return resultado

dados = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40
}

print(chaves_acima_da_media(dados))

#EXERCICIO 16
def consolidar_carrinho(compras):
    resultado = {}

    for compra in compras:
        produto = compra["produto"]
        preco = compra["preco"]
        qtd = compra["qtd"]

        valor = preco * qtd

        if produto not in resultado:
            resultado[produto] = (qtd, valor)
        else:
            qtd_antiga, valor_antigo = resultado[produto]

            nova_qtd = qtd_antiga + qtd
            novo_valor = valor_antigo + valor

            resultado[produto] = (nova_qtd, novo_valor)

    return resultado

compras = [
    {"produto": "pão", "preco": 2.0, "qtd": 3},
    {"produto": "leite", "preco": 4.0, "qtd": 1},
    {"produto": "pão", "preco": 2.0, "qtd": 2}
]

print(consolidar_carrinho(compras))

#EXERCICIO 17
def somar_matrizes_esparsas(m1, m2):
    resultado = {}

    posicoes = set(m1) | set(m2)

    for posicao in posicoes:
        valor1 = m1.get(posicao, 0)
        valor2 = m2.get(posicao, 0)

        soma = valor1 + valor2

        if soma != 0:
            resultado[posicao] = soma

    return resultado

m1 = {
    (0, 0): 5,
    (1, 2): 3
}

m2 = {
    (0, 0): -5,
    (1, 2): 4,
    (2, 2): 1
}

print(somar_matrizes_esparsas(m1, m2))

#EXERCICIO 18
def verificar_caminho(grafo, caminho):
    i = 0

    while i < len(caminho) - 1:
        atual = caminho[i]
        proximo = caminho[i + 1]

        if proximo not in grafo.get(atual, []):
            return False

        i += 1

    return True

grafo = {
    "A": ["B", "C"],
    "B": ["C"],
    "C": []
}

print(verificar_caminho(grafo, ["A", "B", "C"]))

#EXERCICIO 19
def analisar_turmas(escola):
    resultado = {}

    for turma, alunos in escola.items():
        maior_media = -1
        melhor_aluno = ""

        for aluno, notas in alunos.items():
            media = sum(notas) / len(notas)

            if media > maior_media:
                maior_media = media
                melhor_aluno = aluno

        resultado[turma] = melhor_aluno

    return resultado

escola = {
    "T1": {
        "Ana": [8, 9],
        "Beto": [5, 6]
    },
    "T2": {
        "Carla": [7, 8],
        "Daniel": [9, 10]
    }
}

print(analisar_turmas(escola))

#EXERCICIO 20
def criar_indice_invertido(documentos):
    indice = {}

    for id_doc, texto in documentos:
        texto = texto.lower()
        palavras = texto.split()

        for palavra in palavras:
            if palavra not in indice:
                indice[palavra] = []

            if id_doc not in indice[palavra]:
                indice[palavra].append(id_doc)

    return indice

documentos = [
    (1, "python eh legal"),
    (2, "aprender python eh bom"),
    (3, "java tambem eh legal")
]

print(criar_indice_invertido(documentos))






