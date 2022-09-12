print("********************************")
print("bem vindo no jogo de Adivinhação")
print("********************************")

numero_secreto = 42

#chute_str é uma string, se for comparado ao que o usuário digita no input será como falso pq o Python não compara string com inteiro
chute_str = input("Digite o seu número: ")

print("Você digitou ", chute_str)

#aqui tive que fazer essa função para que a comparação funcione, transformando string em inteiro(int)
chute = int(chute_str)

if(numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou")
