def main():
    nome = input("Digite o nome da escola")
    
    quantSalas = 0


    while quantSalas <= 0:

        quantSalas = int(input(" "))

        if quantSalas <= 0:
            print("Número inválido")

    mediaEscola  = [0.0] * quantSalas