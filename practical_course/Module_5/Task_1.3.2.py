import random

class Warrior():
    
    def __init__(self, warrior, health=100, armor=100, endurance=100):
        self.warrior = warrior
        self.health = health
        self.armor = armor
        self.endurance = endurance


    def attack(self, other):  
        self.endurance -= 10
        other.health -= random.randint(10, 30) 
        print(f"{self.warrior} attacks {other.warrior}. {other.warrior}'s health: {other.health}")


    def defend(self, other): 
        if self.armor <= 0:
            damage_taken = random.randint(10, 30)
        else:
            damage_taken = random.randint(0, 20)
            self.armor -= random.randint(0, 10)
        self.health -= damage_taken

        print(f'{self.warrior} defends with -{damage_taken}HP. {self.warrior}\'s armor: {self.armor}, {self.warrior}\'s health: {self.health}')

player_1 = Warrior(str(input('First player\'s name: ')))
player_2 = Warrior(str(input('Second player\'s name: ')))


while player_1.health > 10 and player_2.health > 10:
    attacker = random.choice([player_1, player_2])
    act1 = random.choice(["attack", "defend"])
    act2 = random.choice(["attack", "defend"])

    if attacker == player_1:
        if act1 == "attack":
            attacker.attack(player_2)  
        else:
            attacker.defend(player_2) 
    else:
        if act2 == "attack":
            attacker.attack(player_1)  
        else:
            attacker.defend(player_1)  


    if player_1.health <= 10 and player_1.health != 0:
        answer = input(f'{player_1.warrior} is almost out of HP. Finish them? (\'yes\' or \'no\'): ')
        if answer.lower() == "yes":
            print(f'{player_2.warrior} wins!')
        else:
            print('And so we end up with no winner :)')
        break


    if player_2.health <= 10 and player_2.health != 0:
        answer = input(f'{player_2.warrior} is almost out of HP. Finish them? (\'yes\' or \'no\'): ')
        if answer.lower() == "yes":
            print(f'{player_1.warrior} wins!')
        else:
            print('And so we end up with no winner :)')
        break
