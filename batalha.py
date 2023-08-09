import random

def batalhar(personagem, guarda):
    print(f"Você está enfrentando o guarda {guarda['nome']} - {guarda['nome']}")
    
    while personagem["Vida"] > 0 and guarda["vida"] > 0:
        player_attack_damage = random.randint(5, 15)
        guarda["vida"] -= player_attack_damage
        print(f"{personagem['nome']} ataca {guarda['nome']} e causa {player_attack_damage} de dano.")
        
        if guarda["vida"] <= 0:
            print(f"Você derrotou o guarda {guarda['nome']}!")
            personagem["dinheiro"] += 10
            return True
        
        guard_attack_damage = random.randint(8, 12)
        personagem["Vida"] -= guard_attack_damage
        print(f"{guarda['nome']} ataca {personagem['nome']} e causa {guard_attack_damage} de dano.")
        
        if personagem["Vida"] <= 0:
            print("Você foi derrotado!")
            return False
