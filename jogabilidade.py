import random

def batalhar(personagem, guarda):
    print(f"Você está enfrentando o guarda {guarda['nome']}!")

    while personagem["Vida"] > 0 and guarda["vida"] > 0:
    
        player_attack_damage = random.randint(5, 15)
        guarda["vida"] -= player_attack_damage
        print(f"{personagem['nome']} ataca {guarda['nome']} e causa {player_attack_damage} de dano.")

        if guarda["vida"] <= 0:
            print(f"Você derrotou o guarda {guarda['nome']}!")
            personagem["dinheiro"] += 10
            return True

        guard_attack_damage = random.randint(3, 12)
        personagem["Vida"] -= guard_attack_damage
        print(f"{guarda['nome']} ataca {personagem['nome']} e causa {guard_attack_damage} de dano.")

        if personagem["Vida"] <= 0:
            print(f"Você foi derrotado por {guarda['nome']}!")
            return False

    return False

def escolherAcao(personagem, guarda):
    print("Escolha o que você quer fazer?")
    print(f"[1] - Batalha com o guarda {guarda['nome']}")
    print("[2] - Entrar na loja")

    escolha = int(input())
    if escolha == 1:
        venceu = batalhar(personagem, guarda)
        if not venceu:
            return None
    elif escolha == 2:
        personagem = barganhar(personagem)

    return personagem

def PassarPelosGuardas(personagem, guardas):
    for guarda in guardas:
        if personagem is None:
            print("Você perdeu a batalha e não pode continuar.")
            break
        personagem = escolherAcao(personagem, guarda)
        if personagem is None:
            print(f"{personagem['nome']} foi derrotado! O jogo terminou.")
            break
        venceu = batalhar(personagem, guarda)
        if not venceu:
            print(f"{personagem['nome']} foi derrotado por {guarda['nome']}! O jogo terminou.")
            break
        print(f"{personagem['nome']} venceu a batalha contra {guarda['nome']}!")

    if personagem is not None:
        print(f"{personagem['nome']} derrotou todos os guardas e é o grande campeão!")

        return personagem

def PassarPelosGuardas(personagem, guardas):
    for guarda in guardas:
        if personagem is None:
            print("Você perdeu a batalha e não pode continuar.")
            break
        personagem = escolherAcao(personagem, guarda)
        if personagem is None:
            print(f"{personagem['nome']} foi derrotado! O jogo terminou.")
            break
        venceu = batalhar(personagem, guarda)
        if not venceu:
            print(f"{personagem['nome']} foi derrotado por {guarda['nome']}! O jogo terminou.")
            break
        print(f"{personagem['nome']} venceu a batalha contra {guarda['nome']}!")

    if personagem is not None:
        print(f"{personagem['nome']} derrotou todos os guardas e é o grande campeão!")

personagem = {
    "nome": "CRT71",
    "dinheiro": 30,
    "Vida": 100,
    "mochila": [],
    "equipamentos": []
}

guardas = [
    {"nome": "Barão Ragnar, o Devorador de Almas", "vida": 30, "dano": 10},
    {"nome": "Aleron, o Senhor do Caos", "vida": 50, "dano": 7},
    {"nome": "REI matheus, o mestre da destruição", "vida": 90, "dano": 10}
]

quantidadeGuardas = len(guardas)

print("Vizão cria, está na hora de provar que você não é um medíocre. Mate o rei.")
print(f"Durante o jogo você irá precisar enfrentar desafios gigantes, são {quantidadeGuardas} guardas antes de chegar ao Rei, mate todos eles.")
print(f"Durante a tua vida medíocre, você conseguiu acumular {personagem['dinheiro']}$, antes de cada batalha você pode passar na loja.")

def barganhar(personagem):
    print("Bem-vindo à loja!")
    print("Itens disponíveis:")
    print("[1] - Poção de Cura (+20 HP) - 10$")
    print("[2] - Espada Mágica (+5 de Dano) - 20$")

    escolha = int(input("Escolha o item que deseja comprar: "))

    if escolha == 1:
        if personagem["dinheiro"] >= 10:
            personagem["mochila"].append("Poção de Cura")
            personagem["dinheiro"] -= 10
            print("Você comprou uma Poção de Cura!")
        else:
            print("Você não tem dinheiro suficiente para comprar esse item.")
    elif escolha == 2:
        if personagem["dinheiro"] >= 20:
            personagem["equipamentos"].append("Espada Mágica")
            personagem["dinheiro"] -= 20
            print("Você comprou uma Espada Mágica!")
        else:
            print("Você não tem dinheiro suficiente para comprar esse item.")
    else:
        print("Opção inválida.")

    return personagem
# Agora, você pode passar a lista de guardas para a função PassarPelosGuardas
PassarPelosGuardas(personagem, guardas)
