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
        return "Menor de idade"
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
    



