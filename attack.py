import random

class Enemy:
    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print(self.atkl)

enemy1 = Enemy(50, 60)
enemy1.getAtk()

'''
playerhp = 260 
enemyatkl = 600
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30
    print("Enemy strikes for ", dmg, "damage ponts. current hp is ", playerhp)
    
    if playerhp == 30:
        print("You have low health")
        break
    '''