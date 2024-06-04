import random

class Warrior():
    
    def __init__(self, warrior, health = 100):
        self.warrior = warrior
        self.health = health

    def damage(self, other):
        other.health -= 20

        if other.health > 1 :
            print(self.warrior, 'attacked', other.warrior, ', -20 HP,\n', other.warrior, 'has', other.health,  'HP left.')
        elif other.health == 1:
            print(self.warrior, 'attacked', other.warrior, '.', other.warrior, 'has 1 HP left.')
        else:
            print(other.warrior, 'got hurt. -20HP.\n', 'No HP left.\n', self.warrior, 'wins.')


player_1 = Warrior(input('First player\'s name: '))
player_2 = Warrior(input('Second player\'s name: '))

while (player_1.health > 0) and (player_2.health > 0):
    attack = random.choice([player_1, player_2])

    if attack == player_1:
        attack.damage(player_2)
    else:
        attack.damage(player_1)
