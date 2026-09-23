def dobrar(numeros:list):
    for numero in numeros:
        numero = numero * 2
        print(numero)

#EXERCICIO 1
def filtrar_pares(numeros:list):
    pares = list()
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    
    return pares

if __name__ == '__main__':
    numeros_pares = filtrar_pares([1, 2, 3, 4, 5,6])
    print(numeros_pares)

#EXERCICIO 2 
def contar_negativos(numeros:list):
    count = 0
    for numero in numeros:
        if numero < 0:
            count+=1
    return count

#EXERCICIOS 3
def somar_maiores_que(numeros: list, limite:int):
    soma = 0
    for numero in numeros:
        if numero > limite:
            soma+=numero
    return soma

#EXERCICIOS 4
def zerar_negativos(numeros: list):
    aux = numeros.copy()
    for numero in numeros:
        if numero < 0:
            indice = numeros.index(numero)
            aux[indice] = 0
    return aux

#EXERCICIO 5 
def contem_valor(lista:list, alvo):
    index = 0
    while(index < len(lista)):
        if lista[index] == alvo:
            return True
        index=+1
    return False

#EXERCICIO 6
def contar_aprovados(notas: list):
    count = 0
    for nota in notas:
        if nota >= 7:
            count+=1
    return count

#EXERCICIO 7
def filtrar_palavras_curtas(palvras:list, tamanho_maximo:int):
    filtro = []
    for palavra in palvras:
        if len(palavra) <= tamanho_maximo:
            filtro.append(palavra)
    return filtro

#EXERCICIO 8
def separar_pares_impares(numeros:list):
    pares, impares = 0
    for numero in numeros:
        if numero % 2 !=0:
            impares+=1
        else:
            pares+=1
    return f"Pares: {pares} | Impares: {impares}"   

#EXERCICIO 9
def encontrar_extremos(numeros: list):
    maior, menor = 0
    for numero in numeros:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    return (menor, maior)         

#EXERCICIO 10
def simular_saque(saldo_inicial: float, saques: list):
    index = 0
    permitidos = []
    negados = []
    while (index < len(saques)):
        if saldo_inicial - saques[index] >= 0:
            permitidos.append(saques[index])
            saldo_inicial-=saques[index]
        else:
            negados.append(saques[index])
        index+=1

    return saldo_inicial           

#EXERCICIO 11
def remover_duplicados(lista: list):
    not_duplicados = []
    for numero in lista:
        if numero not in not_duplicados:
            not_duplicados.append(numero)
    return not_duplicados

#EXERCICIO 12
def media_positivos(numeros:list):
    if not numeros:
        return 0.0
    divisor = 0
    valor = 0
    for numero in numeros:
        if numero > 0:
            valor += numero
            divisor += 1
    return valor/divisor

#EXERCICIO 13
def validador_senha(senhas:list[str]):
    validas = []
    for senha in senhas:
        if len(senha) > 8:
            validas.append(senha)
    return validas

#EXERCICIO 14
def primeiro_impar(numeros: list):
    index = 0
    while (index < len(numeros)):
        if numeros[index] % 2 != 0:
            return numeros[index]
        return None

#EXERCICIO 15
def contar_ocorrencias(lista:list, target):
    ocurrences = 0
    for element in lista:
        if element == target:
            ocurrences+=1
    return ocurrences

#EXERCICIO 16                
def is_estritamente_crescente(palavras: list):
    index = 1
    while (index < len(palavras) - 1):
        if len(palavras[index] > len(palavras[index-1])):
            pass
        else:
            return False
    return True    


                                                     
                                            

    