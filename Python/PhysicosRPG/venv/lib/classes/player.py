import random
from .magic import Spell
from .inventory import Item
from .game import bcolors

indent = "    "

class Person:
    def __init__(self, name, life, mana, attack, defense, magic, items, type):
        self.name = name
        self.minlife = 0
        self.maxlife = life
        self.life = life
        self.minmana = 0
        self.maxmana = mana
        self.mana = mana
        self.minattack = attack - 10
        self.maxattack = attack + 10
        self.defense = defense
        self.magic = magic
        self.items = items
        self.actions = ["Attack Enemy", "Use Magic", "Use Item"]

    def generate_damage(self):
        return random.randrange(self.minattack, self.maxattack)

    def take_damage(self, dmg):
        self.life -= dmg
        if self.life < 0:
            self.life = 0
        return self.life

    def heal(self, dmg):
        self.life += dmg
        if self.life > self.maxlife:
            self.life = self.maxlife

    def mana_heal(self, dmg):
        self.mana += dmg
        if self.mana > self.maxmana:
            self.mana = self.maxmana

    def get_life(self):
        return self.life

    def get_max_life(self):
        return self.maxlife

    def get_mana(self):
        return self.mana

    def get_max_mana(self):
        return self.maxmana

    def reduce_mana(self, cost):
        self.mana -= cost

    def choose_action(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "Actions" + bcolors.ENDC)
        for item in self.actions:
            print(indent + str(i) + ": ", item)
            i += 1

    def choose_magic(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "\nSpells" + bcolors.ENDC)
        for spell in self.magic:
            print(indent + str(i) + ": ", spell.name, "cost: ", str(spell.cost))
            i += 1

    def choose_item(self):
        i = 1
        print(bcolors.OKGREEN + bcolors.BOLD + "\nItems:" + bcolors.ENDC)
        for item in self.items:
            print(indent + str(i) + ":", item["item"].name, "description:", item["item"].description, " ( x", str(item["quantity"]), ")")
            i += 1

    def get_stats(self):
        #Needs fixed
        progress_block = "█"
        space = " "
        out_of = " / "
        divider = "|"
        first_tab_length = 20
        second_tab_length = 30
        third_tab_length = 10
        after_name_space = first_tab_length - len(self.name) -  len(str(self.get_life())) - len(str(self.get_max_life())) - len(out_of) - len(divider)
        life_bar_length = 20
        life_length = round(life_bar_length * self.get_life() / self.get_max_life())
        life_lost = life_bar_length - life_length
        after_life_bar_space = second_tab_length - len(str(self.get_mana())) - len(str(self.get_max_mana())) - len(out_of) - len(divider) - life_bar_length
        mana_bar_length = 10
        mana_length = round(mana_bar_length * self.get_mana() / self.get_max_mana())
        mana_lost = mana_bar_length - mana_length

        print(self.name + space*after_name_space +
              str(self.get_life()) + out_of +
              str(self.get_max_life()) + space +
              divider + progress_block*life_length +
              space*life_lost + divider +
              space*after_life_bar_space + str(self.get_mana()) +
              out_of + str(self.get_max_mana()) +
              space + divider +
              progress_block*mana_length + space*mana_lost +
              divider
              )