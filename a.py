import pygame
import os
import sys
from body import *

size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
running = True
a = input()
if not os.path.exists('data/' + a):
    sys.exit()
sp = []
clock = pygame.time.Clock()
game_map = []
dikt = {}
sp_of_gotten_things = []
with open('data/' + a, 'r') as mapFile:
    le = [line.strip() for line in mapFile]
    level_map = le[-1].split()
    for el in range(len(le)):
        game_map.append(list(le[el]))
        for ell in range(len(le[el])):
            if le[el][ell] == '#':
                sp.append([ell, el])

coords = [299, 299]



def start_screen():
    fon = pygame.transform.scale(load_image('game_over.jpg', True), (1000, 1000))
    screen.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


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


def generate_level(level):
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
            dikt[(y, x)] = level[y][x]
    return new_player, x, y


tile_images = {'wall': load_image('box.png'), 'empty': load_image('grass.jpg'), 'axe_of_bloodlust': load_image('axe_of_bloodlust.png'), 'berserker_rage': load_image('berserker_rage.png'),  'blade_of_despair': load_image('blade_of_despair.png'), 'blade_of_seven_seas': load_image('blade_of_the_seven_seas.png'),  'claws_of_chaos': load_image('claws_of_chaos.png'), 'endless_battle': load_image('endless_battle.png'), 'Wind_of_Nature': load_image('Wind_of_Nature.png'), 'the_sword_of_the_legionnaire': load_image('the_sword_of_the_legionnaire.png'), 'the_giants_axe': load_image('the_giants_axe.png'), 'the_belt_of_ares': load_image('the_belt_of_ares.png'), 'the Golden stick': load_image('the Golden stick.png'), 'studded_armor': load_image('studded_armor.png'), 'storm_belt': load_image('storm_belt.png'), 'queens_wings': load_image('queens_wings.png'), 'leather_armor': load_image('leather_armor.png'), 'health_crystal': load_image('health_crystal.png'), 'healing_necklace': load_image('healing_necklace.png'), 'hammer_of_wrath': load_image('hammer_of_wrath.png'), 'Golden meteor': load_image('Golden meteor.png'), 'dagger': load_image('dagger.png'), 'caller_of_the_devil': load_image('caller_of_the_devil.png'), 'benefit_of_courage': load_image('benefit_of_courage.png'), 'armor_blade': load_image('armor_blade.png'), 'an_ordinary_spear': load_image('an_ordinary_spear.png'), 'a_shot_of_the_hunter': load_image('a_shot_of_the_hunter.png'), 'trident': load_image('trident.png'),  'protective_helmet': load_image('protective_helmet.png'),  'immortality': load_image('immortality.png')}
player_image = load_image('mar.png', -1)
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
tile_width = tile_height = 50

FPS = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
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
        if self.rect.left - 50 > 0 and self.rect.left - 50 < 1000 and [coords[0] - 1, coords[1]] not in sp and coords[0] - 1 != -1:
            self.rect.topleft = (self.rect.left - 50, self.rect.top)
            game_map[coords[1]][coords[0]] = '.'
            coords = [coords[0] - 1, coords[1]]
            game_map[coords[1]][coords[0]] = '@'

    def mover(self):
        global coords
        if self.rect.left + 50 > 0 and self.rect.left + 50 < 1000 and [coords[0] + 1, coords[1]] not in sp and coords[0] + 1 != 300:
            self.rect.topleft = (self.rect.left + 50, self.rect.top)
            game_map[coords[1]][coords[0]] = '.'
            coords = [coords[0] + 1, coords[1]]
            game_map[coords[1]][coords[0]] = '@'

    def moveu(self):
        global coords
        if self.rect.top - 50 > 0 and self.rect.top - 50 < 1000 and [coords[0], coords[1] - 1] not in sp and coords[1] - 1 != -1:
            self.rect.topleft = (self.rect.left, self.rect.top - 50)
            game_map[coords[1]][coords[0]] = '.'
            coords = [coords[0], coords[1] - 1]
            game_map[coords[1]][coords[0]] = '@'

    def moved(self):
        global coords
        if self.rect.top + 50 > 0 and self.rect.top + 50 < 1000 and [coords[0], coords[1] + 1] not in sp and coords[1] + 1 != 300:
            self.rect.topleft = (self.rect.left, self.rect.top + 50)
            game_map[coords[1]][coords[0]] = '.'
            coords = [coords[0], coords[1] + 1]
            game_map[coords[1]][coords[0]] = '@'

 #   def to_coords(self):
  #      self.rect.topleft = [coords[0] * ]

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
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)



heal_pc = 0
camera = Camera()
# изменяем ракурс камеры
camera.update(player)
# обновляем положение всех спрайтов
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
                    pc.all_characters()
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
                    pc.all_characters()
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
                    pc.all_characters()
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
                    pc.all_characters()
                else:
                    Player.moved(player)
                    camera.update(player)
                for sprite in all_sprites:
                    camera.apply(sprite)
    heal_pc += 1
    if heal_pc == 25:
        if pc.regen >= pc.SHP - pc.HP:
            pc.HP = pc.SHP
        else:
            pc.HP += pc.regen
        heal_pc = 0
        pc.all_characters()
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    tiles_group.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)