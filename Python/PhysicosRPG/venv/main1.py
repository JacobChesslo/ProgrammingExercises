from lib.classes.game import bcolors
from lib.classes.player import Person
from lib.classes.magic import Spell
from lib.classes.inventory import Item
import random


# Spells
Firebolt = Spell("Firebolt", 10, 100, "elemental")
Thunderball = Spell("Thunderball", 10, 100, "elemental")
Frostspike = Spell("Frostspike", 10, 100, "elemental")
Meteors = Spell("Meteors", 20, 200, "elemental")
Earthquake = Spell("Earthquake", 14, 140, "elemental")

MinorHealing = Spell("Heal 100", 15, 100, "restoration")
MajorHealing = Spell("Heal 200", 28, 200, "restoration")


# Items
minorPotion = Item("Minor Potion", "potion", "Heals 50 points of HP", 50)
potion = Item("Potion", "potion", "Heals 100 points of HP", 100)
majorPotion = Item("Major Potion", "potion", "Heals 200 points of HP", 200)
manaBottle = Item("Mana Bottle", "manaPotion", "Restores 25 points of Mana", 25)
superManaBottle = Item("Super Mana Bottle", "manaPotion", "Restores 50 points of Mana", 50)
Elixer = Item("Elixer", "elixer", "Fully Restores HP and Mana", 9999)
maxElixer = Item("Max Elixer", "elixer", "Fully Restores each party member's HP and Mana", 9999)

grenade = Item("Grenade", "attack", "Deals 250 damage to the Enemy", 250)


# Magic
player_magic = [Firebolt, Thunderball,
                Frostspike, Meteors,
                Earthquake, MinorHealing,
                MajorHealing]
enemy_magic = [Firebolt, Thunderball,
                Frostspike]

# Items
player_items = [{"item": minorPotion, "quantity": 10},
                {"item": potion, "quantity": 5},
                {"item": majorPotion, "quantity": 1},
                {"item": manaBottle, "quantity": 5},
                {"item": superManaBottle, "quantity": 1},
                {"item": Elixer, "quantity": 2},
                {"item": maxElixer, "quantity": 1},
                {"item": grenade, "quantity": 2}]
enemy_items = []

# People
player1 = Person("Valos", 500, 65, 60, 34, player_magic, player_items, "player")
player2 = Person("Nicky", 500, 65, 60, 34, player_magic, player_items,  "player")
player3 = Person("Robot", 500, 65, 60, 34, player_magic, player_items, "player")

enemy = Person("Golem", 1200, 65, 45, 25, enemy_magic, enemy_items, "enemy")
enemy2 = Person("Imp", 100, 1, 10, 10, [], [], "enemy")
enemy3 = Person("Goblin", 200, 50, 25, 25, [], [], "enemy")

players = [player1, player2,
           player3]

enemies = [enemy, enemy2,
           enemy3]

# Initialization
running = True
i = 0
divider = "===================================================================="
stat_header = "NAME             HP  --------------------        MP  ----------"

def party_stats():
    print(stat_header)
    for player in players:
        player.get_stats()

def enemy_stats():
    print(stat_header)
    for enemy in enemies:
        enemy.get_stats()

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    for player in players:
        print(divider)

        player.choose_action()



        choice = input("Choose action: ")
        index = int(choice) - 1

        # Attack Enemy
        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You attacked for ", dmg)

        # Cast Spell
        elif index == 1:
            player.choose_magic()
            spell_choice = int(input("Choose spell: ")) - 1

            if spell_choice == -1:
                continue

            spell = player.magic[spell_choice]
            dmg = spell.generate_spell_damage()
            current_mana_points = player.get_mana()

            # Check if have enough mana
            if spell.cost > current_mana_points:
                print(bcolors.FAIL + "\nYou can't cast this spell, you don't have enough mana points!" + bcolors.ENDC)
                continue

            player.reduce_mana(spell.cost)

            if spell.type == "restoration":
                player.heal(dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for ", str(dmg), " HP." + bcolors.ENDC)
            elif spell.type == "elemental":
                enemy.take_damage(dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals ", str(dmg), " points of damage", bcolors.ENDC)

        # Use Item
        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose an item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            # Check if have item
            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
                continue

            # Minus quantity of item
            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for ", str(item.prop), " HP " + bcolors.ENDC)
            elif item.type == "manaPotion":
                player.mana_heal(item.prop)
                print(bcolors.OKBLUE + "\n" + item.name + " fills your Mana up ", str(item.prop),
                      " points " + bcolors.ENDC)
            elif item.type == "elixer":
                if item.name == "maxElixer":
                    # for player in party
                    player.mana_heal(item.prop)
                    player.heal(item.prop)
                else:
                    player.mana_heal(item.prop)
                    print(bcolors.OKBLUE + "\n" + item.name + " fills all of your Mana up." + bcolors.ENDC)
                    player.heal(item.prop)
                    print(bcolors.OKGREEN + "\n" + item.name + " heals all of your HP." + bcolors.ENDC)
            elif item.type == "attack":
                dmg = item.prop
                enemy.take_damage(dmg)
                print("\n" + item.name + " did ", str(dmg), "points of damage to the enemy.")

        # Rechecks if no valid choice
        else:
            continue


    enemy_player_choice = random.randrange(0, len(players))
    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    players[enemy_player_choice - 1].take_damage(enemy_dmg)
    print("Enemy attacks ", players[enemy_player_choice], " for ", enemy_dmg, " points of damage.")

    print(divider)
    party_stats()
    enemy_stats()

    if enemy.get_life() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_life() == 0:
        print(bcolors.FAIL + "You were defeated by your enemy!" + bcolors.ENDC)
        running = False
