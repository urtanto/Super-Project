import pygame
import os
import sys
import math
import random
from time import sleep

kick_boss = [[149, 148], [150, 148], [151, 149], [151, 150], [150, 151], [149, 151], [148, 150], [148, 149]]
kick_miniboss = []


class Timer:
    def __init__(self):
        self.dtime = 0
        self.htime = 0
        self.mtime = 0
        self.stime = 0

    def tick(self, time=1):
        for i in range(time):
            self.stime += 1
            if pc.regen >= pc.SHP - pc.HP:
                pc.HP = pc.SHP
            else:
                pc.HP += pc.regen
            if self.stime == 60:
                self.stime = 0
                self.mtime += 1
            if self.mtime == 60:
                self.mtime = 0
                self.htime += 1
            if self.htime == 24:
                self.htime = 0
                self.dtime += 1
            if self.dtime == 10:
                terminate()

    def print(self):
        d = str(self.dtime) if len(str(self.dtime)) == 2 else '0' + str(self.dtime)
        h = str(self.htime) if len(str(self.htime)) == 2 else '0' + str(self.htime)
        m = str(self.mtime) if len(str(self.mtime)) == 2 else '0' + str(self.mtime)
        s = str(self.stime) if len(str(self.stime)) == 2 else '0' + str(self.stime)
        return d + ':' + h + ':' + m + ':' + s


t = Timer()


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

    def geting_damage(self, hard_of_level):
        if hard_of_level != 3:
            if pc.damage - (
                    self.armor - pc.physical_penetration) > 0 and \
                    self.armor - pc.physical_penetration > 0:
                self.HP -= (pc.damage - (self.armor - pc.physical_penetration))
        else:
            if random.choice([True, False]):
                if pc.damage - (
                        self.armor - pc.physical_penetration) > 0 and \
                        self.armor - pc.physical_penetration > 0:
                    self.HP -= (pc.damage - (self.armor - pc.physical_penetration))

    def giving_damage(self):
        pc.geting_damage(b)


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

    def geting_damage(self, hard_of_level):
        if hard_of_level != 3:
            if pc.damage - (self.armor - pc.physical_penetration) > 0 and \
                    self.armor - pc.physical_penetration > 0:
                self.HP -= (pc.damage - (self.armor - pc.physical_penetration))
        else:
            if random.choice([True, False]):
                if pc.damage - (self.armor - pc.physical_penetration) > 0 and \
                        self.armor - pc.physical_penetration > 0:
                    self.HP -= (pc.damage - (self.armor - pc.physical_penetration))

    def giving_damage(self):
        pc.geting_damage(mb)


class Player_characters:
    SHP = 0
    armor = 0
    damage = 0
    vampirizm = 0
    regen = 0
    extra_life = 0
    HP = SHP
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

    def geting_damage(self, hero):
        if hero.damage - pc.armor > 0:
            pc.HP -= (hero.damage - pc.armor)

    def giving_damage(self, hero):
        hero.geting_damage()
        if pc.damage - hero.armor > 0:
            pc.HP += ((pc.damage - hero.armor) * (pc.vampirizm / 1000))
            pc.HP = math.ceil(pc.HP)
        if hero.HP <= 50 and pc.dod > 0:
            pc.dod = 0
            pc.damage = math.ceil(pc.damage * 1.25)

    def kill(self):
        if (pc.extra_life > 0) or (pc.HP < 0):
            pc.extra_life -= 1
            pc.SHP = pc.SHP * 0.15
            pc.SHP = math.ceil(pc.SHP)
            pc.HP = pc.SHP
        else:
            fon = pygame.transform.scale(load_image('game_over.jpg', True), (1000, 1000))
            screen.blit(fon, (0, 0))
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminate()
                    elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                        terminate()
                pygame.display.flip()
                clock.tick(FPS)


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
    pc.extra_life += 1


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


pygame.init()
size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
running = True
# a = input()
a = 'map.txt'
if not os.path.exists('data/' + a):
    sys.exit()
sp = []
clock = pygame.time.Clock()
game_map = []
dikt = {}
hard_of_level = 0
sp_of_gotten_things = []
with open('data/' + a, 'r') as mapFile:
    le = [line.strip() for line in mapFile]
    level_map = le[-1].split()
    for el in range(len(le)):
        game_map.append(list(le[el]))
        for ell in range(len(le[el])):
            if le[el][ell] == '#' or le[el][ell] == 'B':
                sp.append([ell, el])

coords = [299, 299]


def start_screen():
    global hard_of_level
    stop = True
    fon = pygame.transform.scale(load_image('first_fon.jpg', True), (1000, 1000))
    screen.blit(fon, (0, 0))
    while stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                stop = False
                break
        pygame.display.flip()
        clock.tick(FPS)
    fon = pygame.transform.scale(load_image('second_fon.jpg', True), (1000, 1000))
    screen.blit(fon, (0, 0))
    stop = True
    while stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 208) and (event.pos[1] > 391) and (
                    event.pos[0] < 784) and (event.pos[1] < 553):
                hard_of_level = 1
                stop = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 208) and (event.pos[1] > 570) and (
                    event.pos[0] < 776) and (event.pos[1] < 728):
                hard_of_level = 2
                stop = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 208) and (event.pos[1] > 745) and (
                    event.pos[0] < 774) and (event.pos[1] < 902):
                hard_of_level = 3
                stop = False
                break
        pygame.display.flip()
        clock.tick(FPS)
    stop = True
    fon = pygame.transform.scale(load_image('characteristic.jpg', True), (1000, 1000))
    screen.blit(fon, (0, 0))
    while stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                stop = False
                return
        pygame.display.flip()
        clock.tick(FPS)


class Bosss(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(boss_group, all_sprites)
        self.image = tile_images['boss']
        self.x = pos_x
        self.y = pos_y
        self.rect = self.image.get_rect().move(tile_width * self.x, tile_height * self.y)

    def draw(self):
        self.rect = self.image.get_rect().move(tile_width * self.x, tile_height * self.y)


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
        image = image.convert_alpha()
        return image
    else:
        image = image.convert_alpha()
        return pygame.transform.scale(image, (50, 50))


bx, by = 0, 0


def generate_level(level):
    global bx, by
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if [y, x] in sp_of_gotten_things:
                Tile('empty', x, y)
            elif level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
                sp.append((x * 50 + 15, y * 50 + 5))
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
            elif level[y][x] == 'a':
                Tile('axe_of_bloodlust', x, y)
            elif level[y][x] == 'b':
                Tile('berserker_rage', x, y)
            elif level[y][x] == 'c':
                Tile('blade_of_despair', x, y)
            elif level[y][x] == 'd':
                Tile('blade_of_seven_seas', x, y)
            elif level[y][x] == 'e':
                Tile('claws_of_chaos', x, y)
            elif level[y][x] == 'g':
                Tile('endless_battle', x, y)
            elif level[y][x] == 'f':
                Tile('Wind_of_Nature', x, y)
            elif level[y][x] == 'h':
                Tile('a_shot_of_the_hunter', x, y)
            elif level[y][x] == 'i':
                Tile('an_ordinary_spear', x, y)
            elif level[y][x] == 'j':
                Tile('armor_blade', x, y)
            elif level[y][x] == 'k':
                Tile('benefit_of_courage', x, y)
            elif level[y][x] == 'l':
                Tile('caller_of_the_devil', x, y)
            elif level[y][x] == 'm':
                Tile('dagger', x, y)
            elif level[y][x] == 'n':
                Tile('Golden meteor', x, y)
            elif level[y][x] == 'o':
                Tile('hammer_of_wrath', x, y)
            elif level[y][x] == 'p':
                Tile('healing_necklace', x, y)
            elif level[y][x] == 'q':
                Tile('health_crystal', x, y)
            elif level[y][x] == 'r':
                Tile('leather_armor', x, y)
            elif level[y][x] == 's':
                Tile('queens_wings', x, y)
            elif level[y][x] == 'u':
                Tile('storm_belt', x, y)
            elif level[y][x] == 'v':
                Tile('studded_armor', x, y)
            elif level[y][x] == 'w':
                Tile('the Golden stick', x, y)
            elif level[y][x] == 'x':
                Tile('the_giants_axe', x, y)
            elif level[y][x] == 'y':
                Tile('the_sword_of_the_legionnaire', x, y)
            elif level[y][x] == 't':
                Tile('trident', x, y)
            elif level[y][x] == 'z':
                Tile('protective_helmet', x, y)
            elif level[y][x] == 'A':
                Tile('immortality', x, y)
            elif level[y][x] == 'B':
                Tile('boss', x, y)
            dikt[(y, x)] = level[y][x]
    return new_player, x, y


tile_images = {'boss': pygame.transform.scale(load_image('boss.png', True), (100, 100)), 'wall': load_image('box.png'),
               'empty': load_image('floor.png'), 'axe_of_bloodlust': load_image('axe_of_bloodlust.png'),
               'berserker_rage': load_image('berserker_rage.png'),
               'blade_of_despair': load_image('blade_of_despair.png'),
               'blade_of_seven_seas': load_image('blade_of_the_seven_seas.png'),
               'claws_of_chaos': load_image('claws_of_chaos.png'), 'endless_battle': load_image('endless_battle.png'),
               'Wind_of_Nature': load_image('Wind_of_Nature.png'),
               'the_sword_of_the_legionnaire': load_image('the_sword_of_the_legionnaire.png'),
               'the_giants_axe': load_image('the_giants_axe.png'),
               'the_belt_of_ares': load_image('the_belt_of_ares.png'),
               'the Golden stick': load_image('the Golden stick.png'), 'studded_armor': load_image('studded_armor.png'),
               'storm_belt': load_image('storm_belt.png'), 'queens_wings': load_image('queens_wings.png'),
               'leather_armor': load_image('leather_armor.png'), 'health_crystal': load_image('health_crystal.png'),
               'healing_necklace': load_image('healing_necklace.png'),
               'hammer_of_wrath': load_image('hammer_of_wrath.png'), 'Golden meteor': load_image('Golden meteor.png'),
               'dagger': load_image('dagger.png'), 'caller_of_the_devil': load_image('caller_of_the_devil.png'),
               'benefit_of_courage': load_image('benefit_of_courage.png'), 'armor_blade': load_image('armor_blade.png'),
               'an_ordinary_spear': load_image('an_ordinary_spear.png'),
               'a_shot_of_the_hunter': load_image('a_shot_of_the_hunter.png'), 'trident': load_image('trident.png'),
               'protective_helmet': load_image('protective_helmet.png'), 'immortality': load_image('immortality.png')}
player_image = load_image('mar.png', -1)
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
boss_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
tile_width = tile_height = 50

FPS = 50


class Tile(pygame.sprite.Sprite):
    x = -5
    y = -5
    f = False

    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        if tile_type == 'boss':
            Tile.x = pos_x
            Tile.y = pos_y
            Tile.f = True
            self.image = tile_images[tile_type]
            self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
        else:
            if Tile.f and (pos_x == Tile.x + 1 and pos_y == Tile.y) or (
                    pos_x == Tile.x + 1 and pos_y == Tile.y + 1) or (pos_x == Tile.x and pos_y == Tile.y + 1):
                self.image = tile_images[tile_type]
                self.rect = self.image.get_rect().move(-1000, -1000)
            else:
                self.image = tile_images[tile_type]
                self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * pos_x + 15, tile_height * pos_y + 5)

    def rect(self):
        return self.rect.topleft

    def movel(self):
        global coords
        if self.rect.left - 50 > 0 and self.rect.left - 50 < 1000 and [coords[0] - 1, coords[1]] not in sp and coords[
            0] - 1 != -1:
            self.rect.topleft = (self.rect.left - 50, self.rect.top)
            game_map[coords[1]][coords[0]] = '.'
            coords = [coords[0] - 1, coords[1]]
            game_map[coords[1]][coords[0]] = '@'

    def mover(self):
        global coords
        if self.rect.left + 50 > 0 and self.rect.left + 50 < 1000 and [coords[0] + 1, coords[1]] not in sp and coords[
            0] + 1 != 300:
            self.rect.topleft = (self.rect.left + 50, self.rect.top)
            game_map[coords[1]][coords[0]] = '.'
            coords = [coords[0] + 1, coords[1]]
            game_map[coords[1]][coords[0]] = '@'

    def moveu(self):
        global coords
        if self.rect.top - 50 > 0 and self.rect.top - 50 < 1000 and [coords[0], coords[1] - 1] not in sp and coords[
            1] - 1 != -1:
            self.rect.topleft = (self.rect.left, self.rect.top - 50)
            game_map[coords[1]][coords[0]] = '.'
            coords = [coords[0], coords[1] - 1]
            game_map[coords[1]][coords[0]] = '@'

    def moved(self):
        global coords
        if self.rect.top + 50 > 0 and self.rect.top + 50 < 1000 and [coords[0], coords[1] + 1] not in sp and coords[
            1] + 1 != 300:
            self.rect.topleft = (self.rect.left, self.rect.top + 50)
            game_map[coords[1]][coords[0]] = '.'
            coords = [coords[0], coords[1] + 1]
            game_map[coords[1]][coords[0]] = '@'


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def terminate():
    pygame.quit()
    sys.exit()


start_screen()
level_map = load_level(a)
player, level_x, level_y = generate_level(level_map)


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


b = Boss(hard_of_level)
mb = miniBoss(hard_of_level)
heal_pc = 0
pc = Player_characters(hard_of_level)
camera = Camera()
camera.update(player)
for sprite in all_sprites:
    camera.apply(sprite)
while True:
    for event in pygame.event.get():
        k = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            terminate()
        if k[pygame.K_LEFT]:
            if coords[0] - 1 > -1:
                if dikt[(coords[1]), coords[0] - 1].isalpha():
                    what_the_item(dikt[(coords[1]), coords[0] - 1])
                    Player.movel(player)
                    camera.update(player)
                    player_image = load_image('mar.png', -1)
                    all_sprites = pygame.sprite.Group()
                    tiles_group = pygame.sprite.Group()
                    player_group = pygame.sprite.Group()
                    player, level_x, level_y = generate_level(game_map)
                    tile_width = tile_height = 50
                    camera.update(player)
                else:
                    Player.movel(player)
                    camera.update(player)
                for sprite in all_sprites:
                    camera.apply(sprite)
        elif k[pygame.K_RIGHT]:
            if coords[0] + 1 < 300:
                if dikt[(coords[1]), coords[0] + 1].isalpha():
                    what_the_item(dikt[(coords[1]), coords[0] + 1])
                    Player.mover(player)
                    camera.update(player)
                    player_image = load_image('mar.png', -1)
                    all_sprites = pygame.sprite.Group()
                    tiles_group = pygame.sprite.Group()
                    player_group = pygame.sprite.Group()
                    player, level_x, level_y = generate_level(game_map)
                    tile_width = tile_height = 50
                    camera.update(player)
                else:
                    Player.mover(player)
                    camera.update(player)
                for sprite in all_sprites:
                    camera.apply(sprite)
        elif k[pygame.K_UP]:
            if coords[1] - 1 > -1:
                if dikt[(coords[1] - 1), coords[0]].isalpha():
                    what_the_item(dikt[(coords[1] - 1), coords[0]])
                    Player.moveu(player)
                    camera.update(player)
                    player_image = load_image('mar.png', -1)
                    all_sprites = pygame.sprite.Group()
                    tiles_group = pygame.sprite.Group()
                    player_group = pygame.sprite.Group()
                    player, level_x, level_y = generate_level(game_map)
                    tile_width = tile_height = 50
                    camera.update(player)
                else:
                    Player.moveu(player)
                    camera.update(player)
                for sprite in all_sprites:
                    camera.apply(sprite)
        elif k[pygame.K_DOWN]:
            if coords[1] + 1 < 300:
                if dikt[(coords[1] + 1), coords[0]].isalpha():
                    what_the_item(dikt[(coords[1] + 1), coords[0]])
                    Player.moved(player)
                    camera.update(player)
                    player_image = load_image('mar.png', -1)
                    all_sprites = pygame.sprite.Group()
                    tiles_group = pygame.sprite.Group()
                    player_group = pygame.sprite.Group()
                    player, level_x, level_y = generate_level(game_map)
                    tile_width = tile_height = 50
                    camera.update(player)
                else:
                    Player.moved(player)
                    camera.update(player)
                for sprite in all_sprites:
                    camera.apply(sprite)
        elif k[pygame.K_SPACE]:
            if coords in kick_boss:
                pc.geting_damage(b)
            elif coords in kick_miniboss:
                pc.giving_damage(mb)
        elif k[pygame.K_d]:
            pc.kill()
        elif k[pygame.K_t]:
            t.tick(10)
    heal_pc += 1
    if heal_pc == 25:
        t.tick()
        heal_pc = 0
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    tiles_group.draw(screen)
    player_group.draw(screen)
    pygame.draw.rect(screen, [0, 0, 200], [800, 0, 1000, 110])
    pygame.draw.rect(screen, [200, 0, 0], [800, 110, 1000, 320])
    f1 = pygame.font.Font(None, 24)
    text1 = f1.render(str(b.HP) + 'HP', 0, (0, 0, 0))
    screen.blit(text1, (810, 10))
    f1 = pygame.font.Font(None, 24)
    text1 = f1.render('armor: ' + str(b.armor), 0, (0, 0, 0))
    screen.blit(text1, (810, 44))
    f1 = pygame.font.Font(None, 24)
    text1 = f1.render('damage: ' + str(b.damage), 0, (0, 0, 0))
    screen.blit(text1, (810, 78))
    f1 = pygame.font.Font(None, 24)
    text1 = f1.render('Time: ' + t.print(), 0, (0, 0, 0))
    screen.blit(text1, (810, 120))
    f1 = pygame.font.Font(None, 24)
    text1 = f1.render(str(pc.HP) + '/' + str(pc.SHP) + 'HP', 0, (0, 0, 0))
    screen.blit(text1, (810, 154))
    f1 = pygame.font.Font(None, 24)
    text1 = f1.render('armor: ' + str(pc.armor), 0, (0, 0, 0))
    screen.blit(text1, (810, 188))
    f1 = pygame.font.Font(None, 24)
    text1 = f1.render('damage: ' + str(pc.damage), 0, (0, 0, 0))
    screen.blit(text1, (810, 223))
    f1 = pygame.font.Font(None, 24)
    text1 = f1.render('vampirizm: ' + str(pc.vampirizm), 0, (0, 0, 0))
    screen.blit(text1, (810, 256))
    f1 = pygame.font.Font(None, 24)
    text1 = f1.render('regen: ' + str(pc.regen), 0, (0, 0, 0))
    screen.blit(text1, (810, 290))
    f1 = pygame.font.Font(None, 24)
    text1 = f1.render('extra life: ' + str(pc.extra_life), 0, (0, 0, 0))
    screen.blit(text1, (810, 324))
    f1 = pygame.font.Font(None, 24)
    text1 = f1.render('physical penetration: ' + str(pc.physical_penetration), 0, (0, 0, 0))
    screen.blit(text1, (810, 358))
    f1 = pygame.font.Font(None, 24)
    text1 = f1.render('coords: ' + str(coords[0] + 1) + ',' + str(coords[1] + 1), 0, (0, 0, 0))
    screen.blit(text1, (810, 392))
    pygame.display.flip()
    clock.tick(FPS)
