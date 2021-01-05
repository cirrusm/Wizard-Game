from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

print("\n\n")


print("\n\n")
#Black Magic
fire = Spell('Fire', 10, 100, 'black')
thunder = Spell('Thunder', 10, 100, 'black')
blizzard = Spell('Blizzard', 10, 100, 'black')
meteor = Spell('Meteor', 20, 200, 'black')
quake = Spell('Quake', 14, 140, 'black')

#White Magic (Healing)
cure = Spell("Cure", 12, 120, 'white')
cura = Spell("Cura", 18, 200, 'white')

#Creating items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack","Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item" : potion, 'quantity': 5}, {"item" : hipotion, 'quantity': 1}, {"item" : superpotion, 'quantity': 1}, {"item" : elixer, 'quantity': 1}, {"item" : hielixer, 'quantity': 2}, {"item" : grenade, 'quantity': 2}]


player1 = Person('Jim', 460, 65, 60, 34, player_spells, player_items)
player2 = Person('Bob',460, 65, 60, 34, player_spells, player_items)
player3 = Person('Dog', 460, 65, 60, 34, player_spells, player_items)
enemy = Person('Meanie', 1200, 65, 45, 25, [], [])

players = [player1]
running = True
i=0
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)


while running:

    print("==============================")
    print("NAME                   HP                           MP")
  
    for player in players:
        player.get_stats()
    for player in players:
        player.choose_action()
        choice = input("Choose action:")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print(f"You did {dmg} to the Enemy. ")
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic:")) - 1
            if magic_choice == -1:
                continue
            spell = player.magic[magic_choice]
            magicdmg = player.magic[magic_choice].generate_damage()
            current_mp = player.get_mp()
            

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nYou dont have enough MP to use this move\n" +bcolors.ENDC)
                continue

            if spell.type == "white":
                player.heal(magicdmg)
                print(f'{bcolors.OKBLUE} \n {spell.name} heals for {magicdmg} HP {bcolors.ENDC}')    
            elif spell.type == "black":
                enemy.take_damage(magicdmg)
                print(f'{bcolors.OKBLUE} \n {spell.name} deals {magicdmg} points of damage {bcolors.ENDC}')
            player.reduce_mp(spell.cost)
        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose item to use: ")) - 1

            if item_choice == -1:
                continue
            
            item = player.items[item_choice]['item']

            if player.items[item_choice]['quantity'] == 0:
                print(bcolors.FAIL + "\n" + "None Left..." + bcolors.ENDC)
                continue
            player.items[item_choice]['quantity'] -= 1
            
            
            if item.type == "potion":
                player.heal(item.prop)
                print(f'{bcolors.OKGREEN} \n {item.name} heals for {item.prop} HP {bcolors.ENDC}')
            elif item.type =="elixer":
                player.hp = player.get_max_hp
                player.mp = player.maxmp
                print(f'{bcolors.OKGREEN} \n HP/MP Fully restored')
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(f'{bcolors.FAIL} \n {item.name} deals {item.prop} damage to the enemy')

        
    
    
        
        
    enemy_choice = 1

    
    enemy_dmg = enemy.generate_damage()
    player.take_damage(int(enemy_dmg))
    print(f"Enemy attacks for {(enemy_dmg)}")

    print('--------------------------------')
    print(f"{bcolors.FAIL}Enemy HP: {str(enemy.get_hp())}/{enemy.get_max_hp()} {bcolors.ENDC}")
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "The enemy killed you !")
        running = False
