def main():
    idade = int( input ("digite a sua idade ") )

    if idade >= 18:
        print("entrada liberada")
    elif idade >= 16:
        acompanhante = input  ("Você está acompanhado? ")

        if acompanhante == "S":
            print("entrada liberada")
        else: 
            print("entrada proibida")
    else:
        print("entrada proibida")
    return 0
main()            