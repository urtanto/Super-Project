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


class blade_of_despair:
    def __init__(self):
        self.damagebath = 170
        Player.dod += 1

    def use(self):
        Player.damage += self.damagebath


class blade_of_the_seven_seas:
    def __init__(self):
        self.damagebath = 65
        self.HPbfth = 250
        self.physical_penetrationbath = 15

    def use(self):
        Player.damage += self.damagebath
        Player.SHP += self.HPbfth
        Player.physical_penetration += self.physical_penetrationbath
        Player.HP = Player.SHP


class berserker_rage:
    def __init__(self):
        self.damagebath = 65
        self.boost = 1.25

    def use(self):
        Player.damage += self.damagebath
        Player.damage = math.ceil(Player.damage * self.boost)


class axe_of_bloodlust:
    def __init__(self):
        self.damagebath = 70
        self.vampirizmbath = 20

    def use(self):
        Player.damage += self.damagebath
        Player.vampirizm += self.vampirizmbath


class endless_battle:
    def __init__(self):
        self.damagebath = 65
        self.HPbath = 250
        self.vampirizmbath = 15

    def use(self):
        Player.damage += self.damagebath
        Player.SHP += self.HPbath
        Player.HP = Player.SHP
        Player.vampirizm += self.vampirizmbath


class claws_of_chaos:
    def __init__(self):
        self.damagebath = 70
        self.vampirismbath = 20

    def use(self):
        Player.damage += self.damagebath
        Player.vampirizm += self.vampirismbath


class nature_wind:
    def __init__(self):
        self.damagebath = 10
        self.vampirizm = 15

    def use(self):
        Player.damage += self.damagebath
        Player.vampirizm += self.vampirizm


class armor_blade:
    def __init__(self):
        self.armorbath = 90

    def use(self):
        Player.armor += self.armorbath


class benefit_of_courage:
    def __init__(self):
        self.HPbath = 770
        self.vampirismbath = 45
        self.boost = 1.1

    def use(self):
        Player.SHP += self.HPbath
        Player.HP = Player.SHP
        Player.vampirizm += self.vampirismbath
        Player.armor = math.ceil(Player.armor * self.boost)
        Player.damage = math.ceil(Player.damage * self.boost)


class caller_of_the_devil:
    def __init__(self):
        self.HPbath = 770
        self.damagebath = 15

    def use(self):
        Player.damage += self.damagebath
        Player.SHP += self.HPbath
        Player.HP = Player.SHP


class forse_of_ice:
    def __init__(self):
        self.damagebath = 30
        self.HPbath = 1000

    def use(self):
        Player.damage += self.damagebath
        Player.SHP += self.HPbath
        Player.HP = Player.SHP


class trident:
    def __init__(self):
        self.damagebath = 80

    def use(self):
        Player.damage += self.damagebath


class golden_meteor:
    def __init__(self):
        self.damagebath = 60
        self.vampirizmbath = 5

    def use(self):
        Player.damage += self.damagebath
        Player.vampirizm += self.vampirizmbath


class a_shot_of_the_hunter:
    def __init__(self):
        self.damagebath = 80

    def use(self):
        Player.damage += self.damagebath


class the_Golden_stick:
    def __init__(self):
        self.damagebath = 100

    def use(self):
        Player.damage += self.damagebath


class the_giants_axe:
    def __init__(self):
        self.damagebath = 30
        self.HPbath = 230

    def use(self):
        Player.damage += self.damagebath
        Player.SHP += self.HPbath
        Player.HP = Player.SHP


class the_sword_of_the_legionnaire:
    def __init__(self):
        self.damagebath = 60

    def use(self):
        Player.damage += self.damagebath


class dagger:
    def __init__(self):
        self.damsgebath = 15

    def use(self):
        Player.damage += self.damsgebath


class an_ordinary_spear:
    def __init__(self):
        self.damagebath = 40

    def use(self):
        Player.damage += self.damagebath


class hammer_of_wrath:
    def __init__(self):
        self.damsgebath = 35
        self.physical_penetrationbath = 15

    def use(self):
        Player.damage += self.damsgebath
        Player.physical_penetration += self.physical_penetrationbath


class an_angry_growl:
    def __init__(self):
        self.damagebath = 60
        self.physical_penetrationbath = 40

    def use(self):
        Player.damage += self.damagebath
        Player.physical_penetration += self.physical_penetrationbath


class health_crystal:
    def __init__(self):
        self.HPbath = 230

    def use(self):
        Player.SHP += self.HPbath
        Player.HP = Player.SHP


class leather_armor:
    def __init__(self):
        self.armorbath = 15

    def use(self):
        Player.armor += self.armorbath


class healing_necklace:
    def __init__(self):
        self.rehenbath = 20

    def use(self):
        Player.regen += self.rehenbath


class the_belt_of_ares:
    def __init__(self):
        self.HPbath = 770

    def use(self):
        Player.SHP += self.HPbath
        Player.HP = Player.SHP


class studded_armor:
    def __init__(self):
        self.armorbath = 90

    def use(self):
        Player.armor += self.armorbath


class queens_wings:
    def __init__(self):
        self.HPbath = 1000
        self.damagebath = 15

    def use(self):
        Player.SHP += self.HPbath
        Player.HP = Player.SHP
        Player.damage = self.damagebath


class storm_belt:
    def __init__(self):
        self.HPbath = 800
        self.armorbath = 40

    def use(self):
        Player.SHP += self.HPbath
        Player.HP = Player.SHP
        Player.armor += self.armorbath


class protective_helmet:
    def __init__(self):
        self.regenbath = 100
        self.HPbath = 1550

    def use(self):
        Player.SHP += self.HPbath
        Player.HP = Player.SHP
        Player.regen += self.regenbath


class immortality:
    def __init__(self):
        self.HPbath = 800
        self.armorbath = 40

    def use(self):
        Player.armor += self.armorbath
        Player.SHP += self.HPbath
        Player.HP = Player.SHP
        Player.death += 1
