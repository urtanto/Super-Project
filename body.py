import math

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

    def taking_damage(self):
        if Player.damage - self.armor > 0:
            self.HP -= (Player.damage - self.armor)

    def giving_damage(self):
        Player.taking_damage()


class Player:
    HP = 1
    armor = 1
    damage = 1
    vampirizm = 0

    def __init__(self, hard_of_level):
        if hard_of_level == 1:
            self.HP = 100
            self.armor = 200
            self.damage = 100
        elif hard_of_level == 2:
            self.HP = 50
            self.armor = 100
            self.damage = 20
        elif hard_of_level == 3:
            self.HP = 10
            self.armor = 50
            self.damage = 0

    def taking_damage(self):
        if Boss.damage - self.armor > 0:
            self.HP -= (Boss.damage - self.armor)

    def giving_damage(self):
        Boss.taking_damage()
        if self.damage - Boss.armor > 0:
            self.HP += ((self.damage - Boss.armor) * (self.vampirizm / 100))
            self.HP = math.ceil(self.HP)

    def proverka(self):
        pass


class blade_of_despair:
    def __init__(self):
        self.damagebath = 170

    def use(self):
        Player.damage += self.damagebath


class blade_of_the_seven_seas:
    def __init__(self):
        self.damagebath = 65
        self.HPbfth = 250

    def use(self):
        Player.damage += self.damagebath
        Player.HP += self.HPbfth


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
        Player.HP += self.HPbath
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
        Player.HP += self.HPbath
        Player.vampirizm += self.vampirismbath
        Player.armor = math.ceil(Player.armor * self.boost)
        Player.damage = math.ceil(Player.damage * self.boost)


class caller_of_the_devil:
    def __init__(self):
        self.HPbath = 770
        self.damagebath = 15

    def use(self):
        Player.damage += self.damagebath
        Player.HP += self.HPbath


class forse_of_ice:
    def __init__(self):
        self.damagebath = 30
        self.HPbath = 1000

    def use(self):
        Player.damage += self.damagebath
        Player.HP += self.damagebath
