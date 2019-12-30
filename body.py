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
            if pc.damage - (self.armor - pc.physical_penetration) > 0 and self.armor - pc.physical_penetration > 0:
                self.HP -= (pc.damage - (self.armor - pc.physical_penetration))
        else:
            if random.choice([True, False]):
                if pc.damage - (self.armor - pc.physical_penetration) > 0 and self.armor - pc.physical_penetration > 0:
                    self.HP -= (pc.damage - (self.armor - pc.physical_penetration))

    def giving_damage(self):
        pc.taking_damage()


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
            if pc.damage - (self.armor - pc.physical_penetration) > 0 and self.armor - pc.physical_penetration > 0:
                self.HP -= (pc.damage - (self.armor - pc.physical_penetration))
        else:
            if random.choice([True, False]):
                if pc.damage - (self.armor - pc.physical_penetration) > 0 and self.armor - pc.physical_penetration > 0:
                    self.HP -= (pc.damage - (self.armor - pc.physical_penetration))

    def giving_damage(self):
        pc.taking_damage()


class Player_characters:
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
            self.HP += ((self.damage - hero.armor) * (self.vampirizm / 1000))
            self.HP = math.ceil(self.HP)
        if hero.HP <= 50 and self.dod > 0:
            self.dod = 0
            self.damage = math.ceil(self.damage * 1.25)

    def kill(self):
        if self.death > 0 and self.HP < 0:
            self.death -= 1
            self.SHP = self.SHP * 0.15
            self.HP = self.SHP
        else:
            pass  # РґРѕРїРёС€Рё СЌС‚Рѕ РєРѕРЅРµС† РёС€СЂС‹

    def all_characters(self):
        print('-------------------------')
        print(str(self.HP) + '/' + str(self.SHP) + 'HP')
        print('защита:', pc.armor)
        print('урон:', pc.damage)
        print('вампиризм:', pc.vampirizm)
        print('реген:', pc.regen)
        print('жизни:', pc.death)
        print('Физ-проникновение:', pc.physical_penetration)
        print('-------------------------')


def blade_of_despair():
    pc.dod += 1
    pc.damage += 170


def blade_of_the_seven_seas():
    pc.damage += 65
    pc.SHP += 250
    pc.physical_penetration += 15


def berserker_rage():
    pc.damage += 65

    pc.damage = math.ceil(pc.damage * 1.25)


def axe_of_bloodlust():
    pc.damage += 70

    pc.vampirizm += 20


def endless_battle():
    pc.damage += 65

    pc.SHP += 250

    pc.vampirizm += 15


def claws_of_chaos():
    pc.damage += 70

    pc.vampirizm += 20


def nature_wind():
    pc.damage += 10

    pc.vampirizm += 15


def armor_blade():
    pc.armor += 90


def benefit_of_courage():
    pc.SHP += 770

    pc.vampirizm += 45

    pc.armor = math.ceil(pc.armor * 1.1)

    pc.damage = math.ceil(pc.damage * 1.1)


def caller_of_the_devil():
    pc.damage += 15

    pc.SHP += 770


def forse_of_ice():
    pc.damage += 30

    pc.SHP += 1000


def trident():
    pc.damage += 80


def golden_meteor():
    pc.damage += 60

    pc.vampirizm += 5


def a_shot_of_the_hunter():
    pc.damage += 80


def the_Golden_stick():
    pc.damage += 100


def the_giants_axe():
    pc.damage += 30
    pc.SHP += 250


def the_sword_of_the_legionnaire():
    pc.damage += 60


def dagger():
    pc.damage += 15


def an_ordinary_spear():
    pc.damage += 40


def hammer_of_wrath():
    pc.damage += 35
    pc.physical_penetration += 15


def an_angry_growl():
    pc.damage += 60
    pc.physical_penetration += 40


def health_crystal():
    pc.SHP += 230


def leather_armor():
    pc.armor += 15


def healing_necklace():
    pc.regen += 20


def the_belt_of_ares():
    pc.SHP += 770


def studded_armor():
    pc.armor += 90


def queens_wings():
    pc.SHP += 1000
    pc.damage += 15


def storm_belt():
    pc.SHP += 800
    pc.armor += 40


def protective_helmet():
    pc.SHP += 1550
    pc.regen += 100


def immortality():
    pc.armor += 40
    pc.SHP += 800
    pc.death += 1


def what_the_item(item):
    if item == 'a':
        axe_of_bloodlust()
    elif item == 'b':
        berserker_rage()
    elif item == 'c':
        blade_of_despair()
    elif item == 'd':
        blade_of_the_seven_seas()
    elif item == 'e':
        claws_of_chaos()
    elif item == 'g':
        endless_battle()
    elif item == 'f':
        nature_wind()
    elif item == 'h':
        a_shot_of_the_hunter()
    elif item == 'i':
        an_ordinary_spear()
    elif item == 'j':
        armor_blade()
    elif item == 'k':
        benefit_of_courage()
    elif item == 'l':
        caller_of_the_devil()
    elif item == 'm':
        dagger()
    elif item == 'n':
        golden_meteor()
    elif item == 'o':
        hammer_of_wrath()
    elif item == 'p':
        healing_necklace()
    elif item == 'q':
        health_crystal()
    elif item == 'r':
        leather_armor()
    elif item == 's':
        queens_wings()
    elif item == 'u':
        storm_belt()
    elif item == 'v':
        studded_armor()
    elif item == 'w':
        the_Golden_stick()
    elif item == 'x':
        the_giants_axe()
    elif item == 'y':
        the_sword_of_the_legionnaire()
    elif item == 't':
        trident()
    elif item == 'z':
        protective_helmet()
    elif item == 'A':
        immortality()


pc = Player_characters(hard_of_level)
