import random
from jogabilidade import PassarPelosGuardas  
1
personagem = {
    "nome": "CRT71",
    "dinheiro": 30,
    "Vida": 100,
    "mochila": [],
    "equipamentos": []
}

guardas = [
    {"nome": "Barão Ragnar, o Devorador de Almas", "vida": 30, "dano": 5},
    {"nome": "Aleron, o Senhor do Caos", "vida": 32, "dano": 7},
    {"nome": "REI matheus, o mestre da destruição", "vida": 50, "dano": 10}
]

quantidadeGuardas = len(guardas)


print("Vizão cria, está na hora de provar que você  não é um medíocre. Mate o rei.")
print(f"Durante o jogo você irá precisar enfrentar desafios gigantes, são {quantidadeGuardas} guardas antes de chegar ao Rei, mate todos eles.")
print(f"Durante a tua vida medíocre, você conseguiu acumular {personagem['dinheiro']}$, antes de cada batalha você pode passar na loja.")

PassarPelosGuardas(personagem, guardas)  
quantidadeGuardas = len(guardas)
