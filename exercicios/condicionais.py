def fizz_buzz(numero:int):
    if numero % 3 == 0 and numero % 5 == 0:
        return "fizzbuzz"
    elif numero % 5 == 0:
        return "buzz"
    elif numero % 3 == 0:
        return "fizz"
    else:
        return numero
    
if __name__ == "__main__":

    pass

#EXERCICIO 1
def verificar_maioridade(idade:int):
    if idade >  18:
        return "Maior de idade"
    
    if idade < 18:
        return "f 1 - Menor de idade"
"Maior de idade" == 20
"Menor de idade" == 15
print(f" {20>18} maior de idade")
print(f" {15<18} menor de idade")

#EXERCICIO 2 
def verificar_paridade(numero:int):
    if numero % 2 == 0:
        return "par"
    else:
    
        return "impar"
print(f"o numero é par")

#EXERCICIO 3
def classificar_numero(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Zero"

classificar_numero(-5)  # "Negativo"
classificar_numero(0)   # "Zero"
classificar_numero(8)   # "Positivo"
numero = int(input("Digite um número: "))
print(classificar_numero(numero))


#EXERCICIO 4 
def calcular_resultado(nota_1: float, nota_2:float):
    if (nota_1 + nota_2) / 2 > 7:
        return "Aprovado"
    return "Reprovado"
print(calcular_resultado(8.0, 6.0))
print(calcular_resultado(5.0, 6.5))


#EXERCICIO 5
def maior_de_dois(a:int, b:int):
    if a > b:
        return "O primeiro é maior"
    if a == b:
        return "São iguais"
    
    return "São iguais"
print(maior_de_dois(10, 20))

print(maior_de_dois(5, 5))

print(maior_de_dois(30, 10))


#EXERCICIO 6
def calcular_desconto(valor_compra:float, 
                      cliente_vip:bool):
    if cliente_vip or valor_compra > 200:
        return f"Valor final: R$ {valor_compra*0.85}"
    return f"Valor final: R$ {valor_compra * 0.95}"
print(calcular_desconto(150.0, True))
# Valor final: R$ 127.50

print(calcular_desconto(100.0, False))
# Valor final: R$ 95.00


#EXERCICIO 7
def conceito_nota(nota:float):
    if nota >= 9 and nota < 10:
        return "A"
    if nota >= 7 and nota < 9:
        return "B"
    if nota > 5 and nota < 7:
        return "C"
    return "F"
print(conceito_nota(8.5))
# B

print(conceito_nota(4.2))
# F


#EXERCICIO 8
def validar_triangulo(a:float, b:float, c:float):
    if (a+b > c) and (b+c > a) and (a+c > b):
        if a == b == c:
            return "Equilátero"

        if a == b != c:
            return "Isóceles"
        
        if a != b != c:
            return "Escaleno"
    else:
        return "Não é triângulo"
    
print(validar_triangulo(5, 5, 5))
# Equilátero

print(validar_triangulo(1, 2, 10))
# Não é um triângulo



#EXERCICIO 9
def calcular_imposto(salario:float):
    excedente = salario - 20000
    if salario >= 2000 and salario < 4000:
        return excedente * 0.1
    if salario >= 4000:
        return 200 + (excedente * 0.2)
    return 0
print(calcular_imposto(1800.0))  # 0.0
print(calcular_imposto(3000.0))  # 100.0
print(calcular_imposto(5000.0))  # 400.0


#EXERCICIO 10
def validador_ano_bissexto(ano:int):
    if ano%4 == 0 and ano%400 == 0:
        return True
    return False
print(validador_ano_bissexto(2024))  # True
print(validador_ano_bissexto(2025))  # False
print(validador_ano_bissexto(1900))  # False
print(validador_ano_bissexto(2000))  # True    
    



