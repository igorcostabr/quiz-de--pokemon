print("Seja bem vindo ao Quiz de Pokemon criado por Igor Costa")
resposta_usuario = input("Quer começar agora? (S/N)")

if resposta_usuario != "S": 
    quit()

pontos = 0

print("Começando... \n")
print("Assinale com a alternativa correta (A,B,C ou D)\n")
print("Qual o nome do protagonista da série de TV Pokémon? \n (A)Elton \n (B)Ash \n (C)John \n (D)Goku \n")
resposta_1 = input("Resposta: ")

if resposta_1 == "B":
    print("Resposta Correta!")
    pontos = pontos + 1
else:
    print("Resposta incorreta!")

print("Qual é o primeiro Pokémon de Ash? \n (A)Bulbasauro \n (B)Charizard \n (C)Ditto \n (D)Pikachu \n")
resposta_2 = input("Resposta: ")

if resposta_2 == "D":
    print("Resposta Correta!")
    pontos = pontos + 1
else:
    print("Resposta incorreta!")

print("Com quantos anos o Ash saiu de casa? \n (A)10 \n (B)18 \n (C)13 \n (D)8 \n")
resposta_3 = input("Resposta: ")

if resposta_3 == "A":
    print("Resposta Correta!")
    pontos = pontos + 1
else:
    print("Resposta incorreta!")

print("Quem é o professor que inicia Ash em sua aventura? \n (A)Prof. Bambu \n (B)Prof. Eureca \n (C)Prof. Carvalho \n (D)Nenhuma das opções \n")
resposta_4 = input("Resposta: ")

if resposta_4 == "C":
    print("Resposta Correta!")
    pontos = pontos + 1
else:
    print("Resposta incorreta!")

print("Quais são os primeiros vilões que o Ash enfrenta em seu caminho? \n (A)Equipe Rocket \n (B)Irmãos Petralha \n (C)Garurumon \n (D)Piratas perdidos \n")
resposta_5 = input("Resposta: ")

if resposta_5 == "A":
    print("Resposta Correta!")
    pontos = pontos + 1
else:
    print("Resposta incorreta!")

print("Qual o nome do pokemon inseto que Ash captura no início de sua jornada? \n (A)Bedril \n (B)Scyter \n (C)Caterpie \n (D)Heracross \n")
resposta_6 = input("Resposta: ")

if resposta_6 == "C":
    print("Resposta Correta!")
    pontos = pontos + 1
else:
    print("Resposta incorreta!")

print("De quem é a bicicleta que Ash pega emprestada para fugir dos spearrows? \n (A)Brock \n (B)Policial Jane \n (C)Jessie \n (D)Misty \n")
resposta_7 = input("Resposta: ")

if resposta_7 == "D":
    print("Resposta Correta!")
    pontos = pontos + 1
else:
    print("Resposta incorreta!")

print("Qual o nome da enfermeira responsável pelo atendimento no Centro Pokemon? \n (A)Joy \n (B)Mary \n (C)Linda \n (D)Sabrina \n")
resposta_8 = input("Resposta: ")

if resposta_8 == "A":
    print("Resposta Correta!")
    pontos = pontos + 1
else:
    print("Resposta incorreta!")

print("Qual o Pokemon Lendário que Ash avista voando no céu, logo no início de sua aventura ? \n (A)Ho-Oh \n (B)Lugia \n (C)Moltres \n (D)Fearow \n")
resposta_9 = input("Resposta: ")

if resposta_9 == "A":
    print("Resposta Correta!")
    pontos = pontos + 1
else:
    print("Resposta incorreta!")

print("Qual é a primeira insígnia que o Ash conquista? \n (A)Raio \n (B)Pedra \n (C)Cáscata \n (D)Alma \n")
resposta_10 = input("Resposta: ")

if resposta_10 == "B":
    print("Resposta Correta!")
    pontos = pontos + 1
else:
    print("Resposta incorreta!")

print(f"Quiz finalizado. Sua pontuação foi: {pontos}/10")
