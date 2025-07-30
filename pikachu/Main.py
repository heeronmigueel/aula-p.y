import random
def main():
   vetor = [0.0] * 4
   i = 0
   media = 0.0
   while i < 4:
    vetor[i] = random.uniform(0.0, 10.0)
    media += vetor[i]
    i += 1

   media /=4
   print(media)
   if media >=6:
    print("Aprovado")
   elif media >= 4:
    print("recuperação")
   else:
    print("reprovado")

 
    return 0
main()
