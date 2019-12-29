import math
import random

hard_of_level = int(input())


class Boss:
    HP = 9999999999
    armor = 9999999999
    damage = 9999999999

    def __init__(self, hard_of_level):
        if hard_of_level == 1:
            self.HP = 150000
            self.armor = 0
            self.damage = 1250
        elif hard_of_level == 2:
            self.HP = 500000
            self.armor = 500
            self.damage = 2500
        elif hard_of_level == 3:
            self.HP = 1000000
            self.armor = 2000
            self.damage = 7500

    def taking_damage(self, hard_of_level):
        if hard_of_level != 3:
            if Player.damage - (self.armor - Player.physical_penetration) > 0:
                self.HP -= (Player.damage - (self.armor - Player.physical_penetration))
        else:
            if random.choice([True, False]):
                if Player.damage - (self.armor - Player.physical_penetration) > 0:
                    self.HP -= (Player.damage - (self.armor - Player.physical_penetration))

    def giving_damage(self):
        Player.taking_damage()


class miniBoss:
    HP = 9999999999
    armor = 9999999999
    damage = 9999999999

    def __init__(self, hard_of_level):
        if hard_of_level == 1:
            self.HP = 15000
            self.armor = 0
            self.damage = 125
        elif hard_of_level == 2:
            self.HP = 50000
            self.armor = 50
            self.damage = 250
        elif hard_of_level == 3:
            self.HP = 100000
            self.armor = 200
            self.damage = 750

    def taking_damage(self, hard_of_level):
        if hard_of_level != 3:
            if Player.damage - (self.armor - Player.physical_penetration) > 0:
                self.HP -= (Player.damage - (self.armor - Player.physical_penetration))
        else:
            if random.choice([True, False]):
                if Player.damage - (self.armor - Player.physical_penetration) > 0:
                    self.HP -= (Player.damage - (self.armor - Player.physical_penetration))

    def giving_damage(self):
        Player.taking_damage()


class Player:
    HP = 1
    armor = 1
    damage = 1
    vampirizm = 0
    regen = 1
    death = 0
    SHP = HP
    dod = 0
    physical_penetration = 0

    def __init__(self, hard_of_level):
        if hard_of_level == 1:
            self.SHP = 100
            self.HP = self.SHP
            self.armor = 200
            self.damage = 100
            self.regen = 25
        elif hard_of_level == 2:
            self.SHP = 50
            self.HP = self.SHP
            self.armor = 100
            self.damage = 20
            self.regen = 4
        elif hard_of_level == 3:
            self.SHP = 10
            self.HP = self.SHP
            self.armor = 50
            self.damage = 0
            self.regen = 1

    def taking_damage(self):
        if Boss.damage - self.armor > 0:
            self.HP -= (Boss.damage - self.armor)

    def giving_damage(self, hero):
        hero.taking_damage()
        if self.damage - hero.armor > 0:
            self.HP += ((self.damage - hero.armor) * (self.vampirizm / 100))
            self.HP = math.ceil(self.HP)
        if hero.HP <= 50 and self.dod > 0:
            self.dod = 0
            self.damage = math.ceil(self.damage * 1.25)

    def kill(self):
        if self.death > 0 and self.HP > 0:
            self.death -= 1
            self.SHP = self.SHP * 0.15
            self.HP = self.SHP
        else:
            pass  # допиши это конец ишры


def blade_of_despair():
    Player.dod += 1
    Player.damage += 170


def blade_of_the_seven_seas():
    Player.damage += 65
    Player.SHP += 250
    Player.physical_penetration += 15


def berserker_rage():
    Player.damage += 65
    Player.damage = math.ceil(Player.damage * 1.25)


def axe_of_bloodlust():
    Player.damage += 70
    Player.vampirizm += 20


def endless_battle():
    Player.damage += 65
    Player.SHP += 250
    Player.vampirizm += 15


def claws_of_chaos():
    Player.damage += 70
    Player.vampirizm += 20


def nature_wind():
    Player.damage += 10
    Player.vampirizm += 15


def armor_blade():
    Player.armor += 90


def benefit_of_courage():
    Player.SHP += 770
    Player.vampirizm += 45
    Player.armor = math.ceil(Player.armor * 1.1)
    Player.damage = math.ceil(Player.damage * 1.1)


def caller_of_the_devil():
    Player.damage += 15
    Player.SHP += 770


def forse_of_ice():
    Player.damage += 30
    Player.SHP += 1000


def trident():
    Player.damage += 80


def golden_meteor():
    Player.damage += 60
    Player.vampirizm += 5


def a_shot_of_the_hunter():
    Player.damage += 80


def the_Golden_stick():
    Player.damage += 100


def the_giants_axe():
    Player.damage += 30
    Player.SHP += 250


def the_sword_of_the_legionnaire():
    Player.damage += 60


def dagger():
    Player.damage += 15


def an_ordinary_spear():
    Player.damage += 40


def hammer_of_wrath():
    Player.damage += 35
    Player.physical_penetration += 15


def an_angry_growl():
    Player.damage += 60
    Player.physical_penetration += 40


def health_crystal():
    Player.SHP += 230


def leather_armor():
    Player.armor += 15


def healing_necklace():
    Player.regen += 20


def the_belt_of_ares():
    Player.SHP += 770


def studded_armor():
    Player.armor += 90


def queens_wings():
    Player.SHP += 1000
    Player.damage = 15


def storm_belt():
    Player.SHP += 800
    Player.armor += 40


def protective_helmet():
    Player.SHP += 1550
    Player.regen += 100


def immortality():
    Player.armor += 40
    Player.SHP += 800
    Player.death += 1
