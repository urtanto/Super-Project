# импорт всех нужных библиотек
import pygame
import os
import sys
import math
import random
import sqlite3
from time import sleep
from random import choice as c


# обновление дб
def sq(name, cp, hard):
    # переводим переменную в строку
    name = str(name[0]).upper() + str(name[1:])
    con = sqlite3.connect('chet.db')
    # Создаём курсор
    cur = con.cursor()
    r2esult = None
    result = None
    # Получаем имя и счёт из БД в порядке убывания и переводим в матрицу из списков для дальнеёшего изменения
    if hard == 1:
        result = cur.execute("SELECT name, s FROM che1 ORDER BY s DESC, name").fetchall()
        result = [list(i) for i in result]
        con.commit()
        # Делаем тоже самое только в другую переменную, эту му будем изменять, а из той брать старую информацию
        r2esult = cur.execute("SELECT name, s FROM che1 ORDER BY s DESC, name").fetchall()
        r2esult = [list(i) for i in r2esult]
    elif hard == 2:
        result = cur.execute("SELECT name, s FROM che2 ORDER BY s DESC, name").fetchall()
        result = [list(i) for i in result]
        con.commit()
        # Делаем тоже самое только в другую переменную, эту му будем изменять, а из той брать старую информацию
        r2esult = cur.execute("SELECT name, s FROM che2 ORDER BY s DESC, name").fetchall()
        r2esult = [list(i) for i in r2esult]
    elif hard == 3:
        result = cur.execute("SELECT name, s FROM che3 ORDER BY s DESC, name").fetchall()
        result = [list(i) for i in result]
        con.commit()
        # Делаем тоже самое только в другую переменную, эту му будем изменять, а из той брать старую информацию
        r2esult = cur.execute("SELECT name, s FROM che3 ORDER BY s DESC, name").fetchall()
        r2esult = [list(i) for i in r2esult]
    result = result[:: -1]
    r2esult = r2esult[:: -1]
    # Изменение рейтинга
    if name == r2esult[0][0]:
        if cp < r2esult[0][1]:
            r2esult[0] = [name, cp]
    elif name == r2esult[1][0]:
        if cp < r2esult[0][1]:
            r2esult[0] = [name, cp]
            r2esult[1] = result[0]
        elif cp < r2esult[1][1]:
            r2esult[1] = [name, cp]
    elif name == r2esult[2][0]:
        if cp < r2esult[0][1]:
            r2esult[0] = [name, cp]
            r2esult[1] = result[0]
            r2esult[2] = result[1]
        elif cp < r2esult[1][1]:
            r2esult[1] = [name, cp]
            r2esult[2] = result[1]
        elif cp < r2esult[2][1]:
            r2esult[2] = [name, cp]
    elif name == r2esult[3][0]:
        if cp < r2esult[0][1]:
            r2esult[0] = [name, cp]
            r2esult[1] = result[0]
            r2esult[2] = result[1]
            r2esult[3] = result[2]
        elif cp < r2esult[1][1]:
            r2esult[1] = [name, cp]
            r2esult[2] = result[1]
            r2esult[3] = result[2]
        elif cp < r2esult[2][1]:
            r2esult[2] = [name, cp]
            r2esult[3] = result[2]
        elif cp < r2esult[3][1]:
            r2esult[3] = [name, cp]
    elif name == r2esult[4][0]:
        if cp < r2esult[0][1]:
            r2esult[0] = [name, cp]
            r2esult[1] = result[0]
            r2esult[2] = result[1]
            r2esult[3] = result[2]
            r2esult[4] = result[3]
        elif cp < r2esult[1][1]:
            r2esult[1] = [name, cp]
            r2esult[2] = result[1]
            r2esult[3] = result[2]
            r2esult[4] = result[3]
        elif cp < r2esult[2][1]:
            r2esult[2] = [name, cp]
            r2esult[3] = result[2]
            r2esult[4] = result[3]
        elif cp < r2esult[3][1]:
            r2esult[3] = [name, cp]
            r2esult[4] = result[3]
        elif cp < r2esult[4][1]:
            r2esult[4] = [name, cp]
    else:
        if cp < r2esult[0][1]:
            r2esult[0] = [name, cp]
            r2esult[1] = result[0]
            r2esult[2] = result[1]
            r2esult[3] = result[2]
            r2esult[4] = result[3]
        elif cp < r2esult[1][1]:
            r2esult[1] = [name, cp]
            r2esult[2] = result[1]
            r2esult[3] = result[2]
            r2esult[4] = result[3]
        elif cp < r2esult[2][1]:
            r2esult[2] = [name, cp]
            r2esult[3] = result[2]
            r2esult[4] = result[3]
        elif cp < r2esult[3][1]:
            r2esult[3] = [name, cp]
            r2esult[4] = result[3]
        elif cp < r2esult[4][1]:
            r2esult[4] = [name, cp]
    con.commit()
    # Обновление данных в БД
    if hard == 1:
        forma = "UPDATE che1 SET name = '" + r2esult[0][0] + "' WHERE nom = 1"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che1 SET s = " + str(r2esult[0][1]) + " WHERE nom = 1"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che1 SET name = '" + r2esult[1][0] + "' WHERE nom = 2"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che1 SET s = " + str(r2esult[1][1]) + " WHERE nom = 2"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che1 SET name = '" + r2esult[2][0] + "' WHERE nom = 3"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che1 SET s = " + str(r2esult[2][1]) + " WHERE nom = 3"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che1 SET name = '" + r2esult[3][0] + "' WHERE nom = 4"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che1 SET s = " + str(r2esult[3][1]) + " WHERE nom = 4"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che1 SET name = '" + r2esult[4][0] + "' WHERE nom = 5"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che1 SET s = " + str(r2esult[4][1]) + " WHERE nom = 5"
        cur.execute(forma).fetchall()
        con.commit()
    elif hard == 2:
        forma = "UPDATE che2 SET name = '" + r2esult[0][0] + "' WHERE nom = 1"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che2 SET s = " + str(r2esult[0][1]) + " WHERE nom = 1"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che2 SET name = '" + r2esult[1][0] + "' WHERE nom = 2"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che2 SET s = " + str(r2esult[1][1]) + " WHERE nom = 2"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che2 SET name = '" + r2esult[2][0] + "' WHERE nom = 3"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che2 SET s = " + str(r2esult[2][1]) + " WHERE nom = 3"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che2 SET name = '" + r2esult[3][0] + "' WHERE nom = 4"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che2 SET s = " + str(r2esult[3][1]) + " WHERE nom = 4"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che2 SET name = '" + r2esult[4][0] + "' WHERE nom = 5"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che2 SET s = " + str(r2esult[4][1]) + " WHERE nom = 5"
        cur.execute(forma).fetchall()
        con.commit()
    elif hard == 3:
        forma = "UPDATE che3 SET name = '" + r2esult[0][0] + "' WHERE nom = 1"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che3 SET s = " + str(r2esult[0][1]) + " WHERE nom = 1"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che3 SET name = '" + r2esult[1][0] + "' WHERE nom = 2"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che3 SET s = " + str(r2esult[1][1]) + " WHERE nom = 2"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che3 SET name = '" + r2esult[2][0] + "' WHERE nom = 3"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che3 SET s = " + str(r2esult[2][1]) + " WHERE nom = 3"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che3 SET name = '" + r2esult[3][0] + "' WHERE nom = 4"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che3 SET s = " + str(r2esult[3][1]) + " WHERE nom = 4"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che3 SET name = '" + r2esult[4][0] + "' WHERE nom = 5"
        cur.execute(forma).fetchall()
        con.commit()
        forma = "UPDATE che3 SET s = " + str(r2esult[4][1]) + " WHERE nom = 5"
        cur.execute(forma).fetchall()
        con.commit()
    con.close()
    okk()


# генерация случайной карты
def create_file():
    f = open("data/map.txt", 'w')
    st = []
    flag = False
    for i in range(300):
        for j in range(300):
            if flag:
                flag = False
                continue
            if i == 299 and j == 289:
                st.append('#.#...#...@')
                print(f.write(''.join(st) + '\n'))
                flag = 'a'
                break
            elif i == 149 and j == 149:
                st.append('B#')
                flag = True
            elif i == 150 and j == 149:
                st.append('##')
                flag = True
            else:
                a = c(
                    ['#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
                     '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '#',
                     '.', '.', '.', '#', '.', '.', '.', '#', '.', '.', '.', '#', '.', '.', '.', '#', '.', '.', '.', '#',
                     '.', '.', '.', '#', '.', '.', '.', '#', '.', '.', '.', '#', '.', '.', '.', '#', '.', '.', '.', '#',
                     'P'])
                if a == 'P':
                    a = c(
                        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'C'])
                st.append(a)
        if flag == 'a':
            break
        print(f.write(''.join(st) + '\n'))
        st = []


# класс таймер, где идет работа со временем
class Timer:
    def __init__(self):
        self.dtime = 0
        self.htime = 0
        self.mtime = 0
        self.stime = 0
        self.atak_time = -1
        self.slep = 0

    # это добавление 1 секунды и регенерация сдоровья
    def tick(self, time=1, h=1):
        for i in range(time):
            self.stime += 1
            t.sleep()
            pc.cash += h
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

    # при вызове функции, она возращает время ввиде строки
    def print(self):
        d = str(self.dtime) if len(str(self.dtime)) == 2 else '0' + str(self.dtime)
        h = str(self.htime) if len(str(self.htime)) == 2 else '0' + str(self.htime)
        m = str(self.mtime) if len(str(self.mtime)) == 2 else '0' + str(self.mtime)
        s = str(self.stime) if len(str(self.stime)) == 2 else '0' + str(self.stime)
        return d + ':' + h + ':' + m + ':' + s

    # тайминг с атакой босса
    def sleep(self):
        if t.stime == t.atak_time:
            b.taking_damage()
            t.slep = t.stime + 2
        if t.slep == t.stime:
            b.giving_damage()


t = Timer()


# взоимодействие с боссом
class Boss:
    HP = 9999999999
    armor = 9999999999
    damage = 9999999999
    first_kik = 0

    # сохранение характеристик босса в зависимости от уровня сложности
    def __init__(self, hard_of_level):
        if hard_of_level == 1:
            self.HP = 1500000
            self.armor = 500
            self.damage = 5000
        elif hard_of_level == 2:
            self.HP = 5000000
            self.armor = 2500
            self.damage = 10000
        elif hard_of_level == 3:
            self.HP = 10000000
            self.armor = 12500
            self.damage = 15000

    # получение урона от игрока
    def geting_damage(self, hard_of_level):
        global player, level_x, level_y, level_map, mapFile, sp, game_map, coords, a, all_sprites, \
            tiles_group, boss_group, player_group, fight, camera, player
        if b.first_kik == 0:
            sp = []
            fight = True
            all_sprites = None
            tiles_group = None
            boss_group = None
            player_group = None
            all_sprites = pygame.sprite.Group()
            tiles_group = pygame.sprite.Group()
            boss_group = pygame.sprite.Group()
            player_group = pygame.sprite.Group()
            game_map = []
            a = 'fight.txt'
            b.first_kik += 1
            with open('data/' + a, 'r') as mapFile:
                le = [line.strip() for line in mapFile]
                level_map = le[-1].split()
                for el in range(len(le)):
                    game_map.append(list(le[el]))
                    for ell in range(len(le[el])):
                        if le[el][ell] == '#' or le[el][ell] == 'B':
                            sp.append([ell, el])
            level_map = load_level(a)
            player, level_x, level_y = generate_level(level_map, False)
            coords = [12, 12]
            camera.update(player)
            for sprite in all_sprites:
                camera.apply(sprite)
            pygame.display.flip()
            b.giving_damage()
        else:
            if hard_of_level != 3:
                if pc.damage - (
                        b.armor - pc.physical_penetration) > 0 and \
                        b.armor - pc.physical_penetration > 0:
                    b.HP -= (pc.damage - (b.armor - pc.physical_penetration))
                elif pc.damage > (b.armor - pc.physical_penetration):
                    b.HP -= pc.damage
            else:
                if random.choice([True, False]):
                    if pc.damage - (
                            b.armor - pc.physical_penetration) > 0 and \
                            b.armor - pc.physical_penetration > 0:
                        b.HP -= (pc.damage - (b.armor - pc.physical_penetration))
            if b.HP <= 0:
                b.kill()

    # показ, где нанесёт босс
    def giving_damage(self):
        global player, level_x, level_y, tile_width, tile_height, chance, coords, all_sprites, tiles_group, boss_group, \
            player_group, level_map, mapFile, sp, game_map, atak_time, fight
        t.atak_time = t.stime + 5
        if t.atak_time >= 60:
            t.atak_time -= 60
            if t.atak_time == 0:
                t.atak_time = 1
        chance = [9, 9]
        while chance in [[9, 9], [10, 9], [9, 10], [10, 10]]:
            chance = [random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]),
                      random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])]
        sp = []
        fight = True
        all_sprites = None
        tiles_group = None
        boss_group = None
        player_group = None
        all_sprites = pygame.sprite.Group()
        tiles_group = pygame.sprite.Group()
        boss_group = pygame.sprite.Group()
        player_group = pygame.sprite.Group()
        game_map = []
        a = 'fight.txt'
        with open('data/' + a, 'r') as mapFile:
            le = [line.strip() for line in mapFile]
            level_map = le[-1].split()
            for el in range(len(le)):
                game_map.append(list(le[el]))
                for ell in range(len(le[el])):
                    if le[el][ell] == '#' or le[el][ell] == 'B':
                        sp.append([ell, el])
        level_map = load_level(a)
        player, level_x, level_y = generate_level(level_map, True)
        coords = [9, 11]
        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)
        pygame.display.flip()

    # нанесение урона игроку
    def taking_damage(self):
        global player, level_x, level_y, tile_width, tile_height, chance, coords, all_sprites, tiles_group, \
            boss_group, player_group, level_map, mapFile, sp, game_map, a, fight
        if coords != chance:
            pc.geting_damage(b)
            sp = []
            fight = True
            all_sprites = None
            tiles_group = None
            boss_group = None
            player_group = None
            all_sprites = pygame.sprite.Group()
            tiles_group = pygame.sprite.Group()
            boss_group = pygame.sprite.Group()
            player_group = pygame.sprite.Group()
            game_map = []
            a = 'fight.txt'
            with open('data/' + a, 'r') as mapFile:
                le = [line.strip() for line in mapFile]
                level_map = le[-1].split()
                for el in range(len(le)):
                    game_map.append(list(le[el]))
                    for ell in range(len(le[el])):
                        if le[el][ell] == '#' or le[el][ell] == 'B':
                            sp.append([ell, el])
            level_map = load_level(a)
            player, level_x, level_y = generate_level(level_map, False)
            coords = [9, 11]
            camera.update(player)
            for sprite in all_sprites:
                camera.apply(sprite)
            pygame.display.flip()
        else:
            sp = []
            all_sprites = None
            tiles_group = None
            boss_group = None
            player_group = None
            all_sprites = pygame.sprite.Group()
            tiles_group = pygame.sprite.Group()
            boss_group = pygame.sprite.Group()
            player_group = pygame.sprite.Group()
            game_map = []
            a = 'fight.txt'
            with open('data/' + a, 'r') as mapFile:
                le = [line.strip() for line in mapFile]
                level_map = le[-1].split()
                for el in range(len(le)):
                    game_map.append(list(le[el]))
                    for ell in range(len(le[el])):
                        if le[el][ell] == '#' or le[el][ell] == 'B':
                            sp.append([ell, el])
            level_map = load_level(a)
            player, level_x, level_y = generate_level(level_map, False)
            coords = [9, 11]
            camera.update(player)
            pygame.display.flip()
            for sprite in all_sprites:
                camera.apply(sprite)
            pygame.display.flip()

    # смерть босса, конец игры
    def kill(self):
        global sp, fight, all_sprites, tiles_group, boss_group, player_group, game_map
        sp = []
        fight = True
        all_sprites = None
        tiles_group = None
        boss_group = None
        player_group = None
        game_map = []
        fon = pygame.transform.scale(load_image('win.jpg', True), (1000, 1000))
        screen.blit(fon, (0, 0))
        name1 = ''
        while True:
            for event in pygame.event.get():
                k = pygame.key.get_pressed()
                if k[pygame.K_q] and len(name1) < 20:
                    name1 += 'q'
                if k[pygame.K_w] and len(name1) < 20:
                    name1 += 'w'
                if k[pygame.K_e] and len(name1) < 20:
                    name1 += 'e'
                if k[pygame.K_r] and len(name1) < 20:
                    name1 += 'r'
                if k[pygame.K_t] and len(name1) < 20:
                    name1 += 't'
                if k[pygame.K_y] and len(name1) < 20:
                    name1 += 'y'
                if k[pygame.K_u] and len(name1) < 20:
                    name1 += 'u'
                if k[pygame.K_i] and len(name1) < 20:
                    name1 += 'i'
                if k[pygame.K_o] and len(name1) < 20:
                    name1 += 'o'
                if k[pygame.K_p] and len(name1) < 20:
                    name1 += 'p'
                if k[pygame.K_a] and len(name1) < 20:
                    name1 += 'a'
                if k[pygame.K_s] and len(name1) < 20:
                    name1 += 's'
                if k[pygame.K_d] and len(name1) < 20:
                    name1 += 'd'
                if k[pygame.K_f] and len(name1) < 20:
                    name1 += 'f'
                if k[pygame.K_g] and len(name1) < 20:
                    name1 += 'g'
                if k[pygame.K_h] and len(name1) < 20:
                    name1 += 'h'
                if k[pygame.K_j] and len(name1) < 20:
                    name1 += 'j'
                if k[pygame.K_k] and len(name1) < 20:
                    name1 += 'k'
                if k[pygame.K_l] and len(name1) < 20:
                    name1 += 'l'
                if k[pygame.K_z] and len(name1) < 20:
                    name1 += 'z'
                if k[pygame.K_x] and len(name1) < 20:
                    name1 += 'x'
                if k[pygame.K_c] and len(name1) < 20:
                    name1 += 'c'
                if k[pygame.K_v] and len(name1) < 20:
                    name1 += 'v'
                if k[pygame.K_b] and len(name1) < 20:
                    name1 += 'b'
                if k[pygame.K_n] and len(name1) < 20:
                    name1 += 'n'
                if k[pygame.K_m] and len(name1) < 20:
                    name1 += 'm'
                if k[pygame.K_BACKSPACE] and len(name1) > 0:
                    name1 = name1[: -1: 1]
                if k[pygame.K_KP_ENTER]:
                    sq(name1, t.dtime * 24 * 60 * 60 + t.htime * 60 * 60 + t.mtime * 60 + t.stime, hard_of_level)
            pygame.draw.rect(screen, [200, 0, 0], [300, 450, 450, 100])
            f1 = pygame.font.Font(None, 24)
            text1 = f1.render('Put your name:', 0, (0, 0, 0))
            screen.blit(text1, (350, 500))
            pygame.draw.rect(screen, [255, 255, 255], [480, 500, 220, 24])
            text1 = f1.render(name1, 0, (0, 0, 0))
            screen.blit(text1, (480, 500))
            pygame.display.flip()
            clock.tick(FPS)


atak_time = 0


# действия с игроком
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
    cash = 0

    # сохранение характеристик игрока
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

    # получение урона от босса
    def geting_damage(self, hero):
        if hero.damage - pc.armor > 0:
            pc.HP -= (hero.damage - pc.armor)
        if pc.HP <= 0:
            pc.kill()

    # нанесение урона
    def giving_damage(self, hero):
        hero.geting_damage(hard_of_level)
        if (pc.damage - hero.armor > 0) and (pc.HP + ((pc.damage - hero.armor) * (pc.vampirizm / 1000)) < pc.SHP):
            pc.HP += ((pc.damage - hero.armor) * (pc.vampirizm / 1000))
            pc.HP = math.ceil(pc.HP)
        if hero.HP <= 50 and pc.dod > 0:
            pc.dod = 0
            pc.damage = math.ceil(pc.damage * 1.25)

    # либо возраждение героя, либо смерть и конец игры
    def kill(self):
        if pc.extra_life > 0:
            pc.extra_life -= 1
            pc.SHP = pc.SHP * 0.15
            pc.SHP = math.ceil(pc.SHP)
            pc.HP = pc.SHP
        else:
            animated_game_over()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        okk()
                    elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                        okk()
                pygame.display.flip()
                clock.tick(FPS)

def animated_game_over():
    global screen
    size = width, height = 600, 300
    screen = pygame.display.set_mode(size)
    running = True

    screen.fill(pygame.Color("white"))
    all_sprites = pygame.sprite.Group()
    sprite = pygame.sprite.Sprite(all_sprites)
    sprite.image = pygame.transform.scale(load_image("game_over.png"), (800, 400))
    sprite.rect = sprite.image.get_rect()
    sprite.rect.left -= 700
    fps = 50
    sprite.rect.top -= 50
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                running = False
                okk()
        pygame.display.flip()
        all_sprites.draw(screen)
        all_sprites.update()
        if sprite.rect.left < -120:
            sprite.rect.left += 5
        clock.tick(fps)

# как все предметы изменяют характеристики героя
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


def coin(h):
    if h == 1:
        pc.cash += 200
    elif h == 2:
        pc.cash += 100
    elif h == 3:
        pc.cash += 50


# определение героя
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
    elif item == 'C':
        coin(hard_of_level)


# выбор управления
def ma():
    global manage, seti
    stop = True
    fon = pygame.transform.scale(load_image('manage.jpg', True), (1000, 1000))
    screen.blit(fon, (0, 0))
    while stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 0) and (event.pos[1] > 300) and (
                    event.pos[0] < 500) and (event.pos[1] < 1000):
                manage = 1
                stop = False
                if seti:
                    return setings()
                else:
                    return start()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 500) and (event.pos[1] > 300) and (
                    event.pos[0] < 1000) and (event.pos[1] < 1000):
                manage = 2
                stop = False
                if seti:
                    return setings()
                else:
                    return start()
        pygame.display.flip()
        clock.tick(FPS)


# показ характеристик босса и игрока
def ch():
    global seti
    stop = True
    fon = pygame.transform.scale(load_image('characteristic.jpg', True), (1000, 1000))
    screen.blit(fon, (0, 0))
    while stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                stop = False
                if seti:
                    return setings()
                else:
                    return start()
        pygame.display.flip()
        clock.tick(FPS)


# выбор темы
def th():
    stop1 = True
    fon = pygame.transform.scale(load_image('theme.jpg', True), (1000, 1000))
    screen.blit(fon, (0, 0))
    while stop1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 194) and (event.pos[1] > 280) and (
                    event.pos[0] < 808) and (event.pos[1] < 382):
                tile_images['wall'] = load_image('box.png')
                tile_images['empty'] = load_image('grass.png')
                stop1 = False
                return start()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 194) and (event.pos[1] > 542) and (
                    event.pos[0] < 817) and (event.pos[1] < 651):
                tile_images['wall'] = load_image('wall.png')
                tile_images['empty'] = load_image('floor.png')
                stop1 = False
                return start()
        pygame.display.flip()
        clock.tick(FPS)


# показ рейтинга всех уровней сложности на начальном уровне сложности
def rat():
    con = sqlite3.connect('chet.db')
    # Создаём курсор
    cur = con.cursor()
    result = cur.execute("SELECT name, s FROM che1 ORDER BY s DESC, name").fetchall()
    result = [list(i) for i in result]
    result1 = cur.execute("SELECT name, s FROM che2 ORDER BY s DESC, name").fetchall()
    result1 = [list(i) for i in result1]
    result2 = cur.execute("SELECT name, s FROM che3 ORDER BY s DESC, name").fetchall()
    result2 = [list(i) for i in result2]
    result = result[:: -1]
    result1 = result1[:: -1]
    result2 = result2[:: -1]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return start()
        pygame.draw.rect(screen, [255, 0, 0], [0, 0, 1000, 1000])
        f1 = pygame.font.Font(None, 50)
        text1 = f1.render('Easy rating:', 0, (0, 0, 0))
        screen.blit(text1, (400, 0))
        t.dtime = result[0][1] // 86400
        t.htime = result[0][1] % 86400 // 3600
        t.mtime = result[0][1] % 86400 % 3600 // 60
        t.stime = result[0][1] % 86400 % 3600 % 60
        f1 = pygame.font.Font(None, 30)
        text1 = f1.render('1: ' + str(result[0][0]) + ' ' + t.print(), 0, (0, 0, 0))
        screen.blit(text1, (400, 50))
        t.dtime = result[1][1] // 86400
        t.htime = result[1][1] % 86400 // 3600
        t.mtime = result[1][1] % 86400 % 3600 // 60
        t.stime = result[1][1] % 86400 % 3600 % 60
        f1 = pygame.font.Font(None, 30)
        text1 = f1.render('2: ' + str(result[1][0]) + ' ' + t.print(), 0, (0, 0, 0))
        screen.blit(text1, (400, 100))
        t.dtime = result[2][1] // 86400
        t.htime = result[2][1] % 86400 // 3600
        t.mtime = result[2][1] % 86400 % 3600 // 60
        t.stime = result[2][1] % 86400 % 3600 % 60
        f1 = pygame.font.Font(None, 30)
        text1 = f1.render('3: ' + str(result[2][0]) + ' ' + t.print(), 0, (0, 0, 0))
        screen.blit(text1, (400, 150))
        t.dtime = result[3][1] // 86400
        t.htime = result[3][1] % 86400 // 3600
        t.mtime = result[3][1] % 86400 % 3600 // 60
        t.stime = result[3][1] % 86400 % 3600 % 60
        f1 = pygame.font.Font(None, 30)
        text1 = f1.render('4: ' + str(result[3][0]) + ' ' + t.print(), 0, (0, 0, 0))
        screen.blit(text1, (400, 200))
        t.dtime = result[4][1] // 86400
        t.htime = result[4][1] % 86400 // 3600
        t.mtime = result[4][1] % 86400 % 3600 // 60
        t.stime = result[4][1] % 86400 % 3600 % 60
        f1 = pygame.font.Font(None, 30)
        text1 = f1.render('5: ' + str(result[4][0]) + ' ' + t.print(), 0, (0, 0, 0))
        screen.blit(text1, (400, 250))
        f1 = pygame.font.Font(None, 50)
        text1 = f1.render('Medium rating:', 0, (0, 0, 0))
        screen.blit(text1, (400, 300))
        t.dtime = result1[0][1] // 86400
        t.htime = result1[0][1] % 86400 // 3600
        t.mtime = result1[0][1] % 86400 % 3600 // 60
        t.stime = result1[0][1] % 86400 % 3600 % 60
        f1 = pygame.font.Font(None, 30)
        text1 = f1.render('1: ' + str(result1[0][0]) + ' ' + t.print(), 0, (0, 0, 0))
        screen.blit(text1, (400, 350))
        t.dtime = result1[1][1] // 86400
        t.htime = result1[1][1] % 86400 // 3600
        t.mtime = result1[1][1] % 86400 % 3600 // 60
        t.stime = result1[1][1] % 86400 % 3600 % 60
        f1 = pygame.font.Font(None, 30)
        text1 = f1.render('2: ' + str(result1[1][0]) + ' ' + t.print(), 0, (0, 0, 0))
        screen.blit(text1, (400, 400))
        t.dtime = result1[2][1] // 86400
        t.htime = result1[2][1] % 86400 // 3600
        t.mtime = result1[2][1] % 86400 % 3600 // 60
        t.stime = result1[2][1] % 86400 % 3600 % 60
        f1 = pygame.font.Font(None, 30)
        text1 = f1.render('3: ' + str(result1[2][0]) + ' ' + t.print(), 0, (0, 0, 0))
        screen.blit(text1, (400, 450))
        t.dtime = result1[3][1] // 86400
        t.htime = result1[3][1] % 86400 // 3600
        t.mtime = result1[3][1] % 86400 % 3600 // 60
        t.stime = result1[3][1] % 86400 % 3600 % 60
        f1 = pygame.font.Font(None, 30)
        text1 = f1.render('4: ' + str(result1[3][0]) + ' ' + t.print(), 0, (0, 0, 0))
        screen.blit(text1, (400, 500))
        t.dtime = result1[4][1] // 86400
        t.htime = result1[4][1] % 86400 // 3600
        t.mtime = result1[4][1] % 86400 % 3600 // 60
        t.stime = result1[4][1] % 86400 % 3600 % 60
        f1 = pygame.font.Font(None, 30)
        text1 = f1.render('5: ' + str(result1[4][0]) + ' ' + t.print(), 0, (0, 0, 0))
        screen.blit(text1, (400, 550))
        f1 = pygame.font.Font(None, 50)
        text1 = f1.render('Hard rating:', 0, (0, 0, 0))
        screen.blit(text1, (400, 600))
        t.dtime = result2[0][1] // 86400
        t.htime = result2[0][1] % 86400 // 3600
        t.mtime = result2[0][1] % 86400 % 3600 // 60
        t.stime = result2[0][1] % 86400 % 3600 % 60
        f1 = pygame.font.Font(None, 30)
        text1 = f1.render('1: ' + str(result2[0][0]) + ' ' + t.print(), 0, (0, 0, 0))
        screen.blit(text1, (400, 650))
        t.dtime = result2[1][1] // 86400
        t.htime = result2[1][1] % 86400 // 3600
        t.mtime = result2[1][1] % 86400 % 3600 // 60
        t.stime = result2[1][1] % 86400 % 3600 % 60
        f1 = pygame.font.Font(None, 30)
        text1 = f1.render('2: ' + str(result2[1][0]) + ' ' + t.print(), 0, (0, 0, 0))
        screen.blit(text1, (400, 700))
        t.dtime = result2[2][1] // 86400
        t.htime = result2[2][1] % 86400 // 3600
        t.mtime = result2[2][1] % 86400 % 3600 // 60
        t.stime = result2[2][1] % 86400 % 3600 % 60
        f1 = pygame.font.Font(None, 30)
        text1 = f1.render('3: ' + str(result2[2][0]) + ' ' + t.print(), 0, (0, 0, 0))
        screen.blit(text1, (400, 750))
        t.dtime = result2[3][1] // 86400
        t.htime = result2[3][1] % 86400 // 3600
        t.mtime = result2[3][1] % 86400 % 3600 // 60
        t.stime = result2[3][1] % 86400 % 3600 % 60
        f1 = pygame.font.Font(None, 30)
        text1 = f1.render('4: ' + str(result2[3][0]) + ' ' + t.print(), 0, (0, 0, 0))
        screen.blit(text1, (400, 800))
        t.dtime = result2[4][1] // 86400
        t.htime = result2[4][1] % 86400 // 3600
        t.mtime = result2[4][1] % 86400 % 3600 // 60
        t.stime = result2[4][1] % 86400 % 3600 % 60
        f1 = pygame.font.Font(None, 30)
        text1 = f1.render('5: ' + str(result2[4][0]) + ' ' + t.print(), 0, (0, 0, 0))
        screen.blit(text1, (400, 850))
        t.dtime = 0
        t.htime = 0
        t.mtime = 0
        t.stime = 0
        pygame.display.flip()
        clock.tick(FPS)


# показ начального меню
