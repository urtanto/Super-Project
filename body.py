import math

hard_of_level = int(input())


class Boss:
    def __init__(self, hard_of_level):
        self.HP = 9999999999
        self.armor = 9999999999
        self.damage = 9999999999
        if hard_of_level == 1:
            self.HP = 10000
            self.armor = 200
            self.damage = 100
        elif hard_of_level == 2:
            self.HP = 50000
            self.armor = 1000
            self.damage = 500
        elif hard_of_level == 3:
            self.HP = 250000
            self.armor = 5000
            self.damage = 2500

    def taking_damage(self):
        if Player.damage - self.armor > 0:
            self.HP -= (Player.damage - self.armor)

    def giving_damage(self):
        Player.taking_damage()


class Player:
    def __init__(self, hard_of_level):
        self.HP = 1
        self.armor = 1
        self.damage = 1
        self.vampirizm = 0
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
        self.boost = 1.025

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
