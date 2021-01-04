from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
        {"name": "Thunder", "cost": 10, "dmg": 80},
        {"name": "Blizzard", "cost": 12, "dmg": 60}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

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
        print(f"You did {dmg} to the Enemy. Enemy HP: {enemy.get_hp()}")

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print(f"Enemy attacks for {enemy_dmg} Player HP: {player.get_hp()}")

    running = False
