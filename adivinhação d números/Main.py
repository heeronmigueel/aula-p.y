import random
def main():
    numeroAle = random.randint(0, 210)

    i = 0

    numero = -1

    while numero != numeroAle:
        numero = int (input("digite um numero"))

        if numero < numeroAle:
            print("o numero aleatório é maior")
        elif numero >numeroAle:
            print("o numero aleatório é memor")

        i += 1
    
    print("voce acertou com", i, " tentativas")
    return 0
main()