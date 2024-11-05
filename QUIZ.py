print("Seja bem vindo ao Quiz de Pokemon por Igor Costa")
resposta_usuario = input("Quer começar agora? (S/N)")

if resposta_usuario != "S": 
    quit()

pontos = 0

print("Começando...")

print("Qual o nome do protagonista da série de TV Pokémon? \n (A)Elton \n (B)Ash \n (C)John \n (D)Goku \n")
resposta_1 = input("Resposta: ")

if resposta_1 == "B":
    print("Resposta Correta!")
    pontos = pontos + 2
else:
    print("Resposta incorreta!")

print("Qual é o primeiro Pokémon de Ash? \n (A)Bulbasauro \n (B)Charizard \n (C)Ditto \n (D)Pikachu \n")
resposta_2 = input("Resposta: ")

if resposta_2 == "D":
    print("Resposta Correta!")
    pontos = pontos + 2
else:
    print("Resposta incorreta!")

print("Com quantos anos o Ash saiu de casa? \n (A)10 \n (B)18d \n (C)13 \n (D)8 \n")
resposta_3 = input("Resposta: ")

if resposta_3 == "A":
    print("Resposta Correta!")
    pontos = pontos + 2
else:
    print("Resposta incorreta!")

print("Quem é o professor que inicia Ash em sua aventura? \n (A)Prof. Bambu \n (B)Prof. Eureca \n (C)Prof. Carvalho \n (D)Nenhuma das opções \n")
resposta_4 = input("Resposta: ")

if resposta_4 == "C":
    print("Resposta Correta!")
    pontos = pontos + 2
else:
    print("Resposta incorreta!")

print("Quais são os primeiros vilões que o Ash enfrenta em seu caminho? \n (A)Equipe Rocket \n (B)Irmãos Petralha \n (C)Garurumon \n (D)Piratas perdidos \n")
resposta_5 = input("Resposta: ")

if resposta_5 == "A":
    print("Resposta Correta!")
    pontos = pontos + 2
else:
    print("Resposta incorreta!")

print(f"Quiz finalizado. Sua pontuação foi: {pontos}/10")