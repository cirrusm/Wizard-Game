from classes.game import Person, bcolors
from classes.magic import Spell

fire = Spell('Fire', 10, 100, 'black')
thunder = Spell('Thunder', 10, 100, 'black')
blizzard = Spell('Blizzard', 10, 100, 'black')
meteor = Spell('Meteor', 20, 200, 'black')
quake = Spell('Quake', 14, 140, 'black')

cure = Spell("Cure", 12, 120, 'white')
cura = Spell("Cura", 18, 200, 'white')



player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, cure, cura])
enemy = Person(1200, 65, 45, 25, [])

running = True
i=0
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)

while running:
    print("==============================")
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

        spell = player.magic[magic_choice]
        magicdmg = player.magic[magic_choice].generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nYou dont have enough MP to use this move\n" +bcolors.ENDC)
            continue
        
        player.reduce_mp(spell.cost)
        enemy.take_damage(magicdmg)
        print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magicdmg), " points of damage")
        
    enemy_choice = 1

    
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print(f"Enemy attacks for {enemy_dmg}")

    print('--------------------------------')
    print(f"{bcolors.FAIL}Enemy HP: {str(enemy.get_hp())}/{enemy.get_max_hp()} {bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}Player HP: {str(player.get_hp())}/{player.get_max_hp()} {bcolors.ENDC}")
    print(f"Your MP: {bcolors.OKBLUE} {str(player.get_mp())} {bcolors.ENDC}")
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "The enemy killed you !")
        running = False
