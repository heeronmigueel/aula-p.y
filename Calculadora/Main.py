from Adição import adição
from Subtração import subtração
from Multiplicação import multiplicação
from Divisão import divisão
def main():
    numero1 = int (input("numero1"))
    numero2 = int (input("numero2"))

    resultado = 0

    operação = input("operação:")
    if operação == "+":
        resultado = adição(numero1, numero2)

    elif operação == "-":
         resultado = subtração(numero1, numero2)

    elif operação == "*":
         resultado = multiplicação(numero1, numero2)

    elif operação == "/":
        resultado = divisão(numero1, numero2)

    print(resultado)
    

    return 0
main()