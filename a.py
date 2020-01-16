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
            fon = pygame.transform.scale(load_image('game_over.jpg', True), (1000, 1000))
            screen.blit(fon, (0, 0))
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        okk()
                    elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                        okk()
                pygame.display.flip()
                clock.tick(FPS)


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
def start():
    global hard_of_level, manage, ok
    stop = True
    fon = pygame.transform.scale(load_image('first_fon.jpg', True), (1000, 1000))
    screen.blit(fon, (0, 0))
    while stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 800) and (event.pos[1] > 0) and (
                    event.pos[0] < 1000) and (event.pos[1] < 100):
                return start_screen()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 800) and (event.pos[1] > 150) and (
                    event.pos[0] < 1000) and (event.pos[1] < 250):
                return th()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 800) and (event.pos[1] > 300) and (
                    event.pos[0] < 1000) and (event.pos[1] < 400):
                return ma()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 800) and (event.pos[1] > 450) and (
                    event.pos[0] < 1000) and (event.pos[1] < 550):
                return ch()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 800) and (event.pos[1] > 600) and (
                    event.pos[0] < 1000) and (event.pos[1] < 700):
                return rat()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 800) and (event.pos[1] > 750) and (
                    event.pos[0] < 1000) and (event.pos[1] < 850):
                terminate()
        if ok:
            return
        pygame.display.flip()
        clock.tick(FPS)


# три точки в паузе
def setings():
    global hard_of_level, manage, ok, seti
    stop = True
    seti = True
    fon = pygame.transform.scale(load_image('settings.jpg', True), (1000, 1000))
    screen.blit(fon, (0, 0))
    while stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 0) and (event.pos[1] > 0) and (
                    event.pos[0] < 150) and (event.pos[1] < 200):
                seti = False
                return menu()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 400) and (event.pos[1] > 300) and (
                    event.pos[0] < 600) and (event.pos[1] < 400):
                return ma()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 400) and (event.pos[1] > 450) and (
                    event.pos[0] < 600) and (event.pos[1] < 550):
                return ch()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 400) and (event.pos[1] > 600) and (
                    event.pos[0] < 600) and (event.pos[1] < 700):
                return rt(hard_of_level)
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 400) and (event.pos[1] > 750) and (
                    event.pos[0] < 600) and (event.pos[1] < 850):
                terminate()
        pygame.display.flip()
        clock.tick(FPS)


# выбор уровня сложности, начало игры
def start_screen():
    global hard_of_level, manage, ok
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
                ok = True
                return start()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 208) and (event.pos[1] > 570) and (
                    event.pos[0] < 776) and (event.pos[1] < 728):
                hard_of_level = 2
                stop = False
                ok = True
                return start()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 208) and (event.pos[1] > 745) and (
                    event.pos[0] < 774) and (event.pos[1] < 902):
                hard_of_level = 3
                stop = False
                ok = True
                return start()
        pygame.display.flip()
        clock.tick(FPS)


#
class Bosss(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(boss_group, all_sprites)
        self.image = tile_images['boss']
        self.x = pos_x
        self.y = pos_y
        self.rect = self.image.get_rect().move(tile_width * self.x, tile_height * self.y)

    def draw(self):
        self.rect = self.image.get_rect().move(tile_width * self.x, tile_height * self.y)


# загрузка картинок
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


#
def generate_level(level, atak):
    global bx, by, chance
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if [y, x] in sp_of_gotten_things:
                Tile('empty', x, y)
            elif level[y][x] == '.' and chance != [x, y] and atak:
                Tile('empty1', x, y)
            elif level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
                sp.append((x * 50 + 15, y * 50 + 5))
            elif level[y][x] == '@' and chance != [x, y] and atak:
                Tile('empty1', x, y)
                new_player = Player(x, y)
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
            elif level[y][x] == 'C':
                Tile('coin', x, y)
            dikt[(y, x)] = level[y][x]
    return new_player, x, y


#
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


#
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * pos_x + 15, tile_height * pos_y + 5)

    def rect(self):
        return self.rect.topleft

    def movel(self):
        global coords
        if (self.rect.left - 50 > 0) and (self.rect.left - 50 < 1000) and [coords[0] - 1, coords[1]] not in sp and \
                coords[0] - 1 != -1:
            if fight and coords in [[11, 9], [11, 10]]:
                return
            else:
                self.rect.topleft = (self.rect.left - 50, self.rect.top)
                game_map[coords[1]][coords[0]] = '.'
                coords = [coords[0] - 1, coords[1]]
                game_map[coords[1]][coords[0]] = '@'

    def mover(self):
        global coords, fight
        if fight:
            if (self.rect.left + 50 > 0) and (self.rect.left + 50 < 1000) and [coords[0] + 1, coords[1]] not in sp and \
                    coords[0] + 1 != 20:
                if coords == [8, 10]:
                    return
                else:
                    self.rect.topleft = (self.rect.left + 50, self.rect.top)
                    game_map[coords[1]][coords[0]] = '.'
                    coords = [coords[0] + 1, coords[1]]
                    game_map[coords[1]][coords[0]] = '@'
        else:
            if (self.rect.left + 50 > 0) and (self.rect.left + 50 < 1000) and [coords[0] + 1, coords[1]] not in sp and \
                    coords[0] + 1 != 300:
                self.rect.topleft = (self.rect.left + 50, self.rect.top)
                game_map[coords[1]][coords[0]] = '.'
                coords = [coords[0] + 1, coords[1]]
                game_map[coords[1]][coords[0]] = '@'

    def moveu(self):
        global coords
        if (self.rect.top - 50 > 0) and (self.rect.top - 50 < 1000) and [coords[0], coords[1] - 1] not in sp and \
                coords[1] - 1 != -1:
            if fight and coords in [[9, 11], [10, 11]]:
                return
            else:
                self.rect.topleft = (self.rect.left, self.rect.top - 50)
                game_map[coords[1]][coords[0]] = '.'
                coords = [coords[0], coords[1] - 1]
                game_map[coords[1]][coords[0]] = '@'

    def moved(self):
        global coords, fight
        if fight:
            if (self.rect.top + 50 > 0) and (self.rect.top + 50 < 1000) and [coords[0], coords[1] + 1] not in sp and \
                    coords[1] + 1 != 20:
                if coords == [10, 8]:
                    return
                else:
                    self.rect.topleft = (self.rect.left, self.rect.top + 50)
                    game_map[coords[1]][coords[0]] = '.'
                    coords = [coords[0], coords[1] + 1]
                    game_map[coords[1]][coords[0]] = '@'
        else:
            if (self.rect.top + 50 > 0) and (self.rect.top + 50 < 1000) and [coords[0], coords[1] + 1] not in sp and \
                    coords[1] + 1 != 300:
                self.rect.topleft = (self.rect.left, self.rect.top + 50)
                game_map[coords[1]][coords[0]] = '.'
                coords = [coords[0], coords[1] + 1]
                game_map[coords[1]][coords[0]] = '@'


#
def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


# выход из игры
def terminate():
    pygame.quit()
    sys.exit()


#
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


# открытие магазина
def shop():
    global item1, item2, item3, item4, player_image, player_group, all_sprites, tiles_group, tile_height, tile_width, \
        player, level_y, level_x
    stop = True
    fon = pygame.transform.scale(load_image('shop.jpg', True), (1000, 1000))
    screen.blit(fon, (0, 0))
    if not item1:
        pygame.draw.rect(screen, [200, 0, 0], [59, 179, 451, 390])
    if not item2:
        pygame.draw.rect(screen, [200, 0, 0], [559, 179, 951, 391])
    if not item3:
        pygame.draw.rect(screen, [200, 0, 0], [59, 579, 451, 1000])
    if not item4:
        pygame.draw.rect(screen, [200, 0, 0], [559, 579, 951, 1000])
    while stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 100) and (event.pos[1] > 200) and (
                    event.pos[0] < 400) and (event.pos[1] < 500) and item1 and pc.cash >= 1500:
                item1 = False
                pc.cash -= 1500
                pc.SHP = pc.SHP * 2
                pygame.draw.rect(screen, [200, 0, 0], [59, 179, 451, 390])
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 600) and (event.pos[1] > 200) and (
                    event.pos[0] < 900) and (event.pos[1] < 500) and item2 and pc.cash >= 1500:
                item2 = False
                pc.cash -= 1500
                pc.physical_penetration += 1000
                pygame.draw.rect(screen, [200, 0, 0], [559, 179, 951, 391])
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 100) and (event.pos[1] > 600) and (
                    event.pos[0] < 400) and (event.pos[1] < 900) and item3 and pc.cash >= 1500:
                item3 = False
                pc.cash -= 1500
                pc.damage = pc.damage * 2
                pygame.draw.rect(screen, [200, 0, 0], [59, 579, 451, 1000])
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 600) and (event.pos[1] > 600) and (
                    event.pos[0] < 900) and (event.pos[1] < 900) and item4 and pc.cash >= 1500:
                item4 = False
                pc.cash -= 1500
                pc.armor *= 2
                pygame.draw.rect(screen, [200, 0, 0], [559, 579, 951, 1000])
                player_image = load_image('armorx2.png', -1)
                all_sprites = pygame.sprite.Group()
                tiles_group = pygame.sprite.Group()
                player_group = pygame.sprite.Group()
                player, level_x, level_y = generate_level(game_map, False)
                tile_width = tile_height = 50
                camera.update(player)
                for sprite in all_sprites:
                    camera.apply(sprite)
                pygame.display.flip()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 5) and (event.pos[1] > 10) and (
                    event.pos[0] < 210) and (event.pos[1] < 125):
                return menu()
        pygame.draw.rect(screen, [200, 0, 0], [800, 0, 1000, 100])
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render('cash: ' + str(pc.cash), 0, (0, 0, 0))
        screen.blit(text1, (810, 10))
        pygame.display.flip()
        clock.tick(FPS)


# возращает строку времени
def clockprint(d, h, m, s):
    d = str(d) if len(str(d)) == 2 else '0' + str(d)
    h = str(h) if len(str(h)) == 2 else '0' + str(h)
    m = str(m) if len(str(m)) == 2 else '0' + str(m)
    s = str(s) if len(str(s)) == 2 else '0' + str(s)
    return d + ':' + h + ':' + m + ':' + s


# вывод рейтинга в паузе
def rt(hard):
    fon = pygame.transform.scale(load_image('rt.jpg', True), (1000, 1000))
    screen.blit(fon, (0, 0))
    con = sqlite3.connect('chet.db')
    # Создаём курсор
    cur = con.cursor()
    result = None
    if hard == 1:
        result = cur.execute("SELECT name, s FROM che1 ORDER BY s DESC, name").fetchall()
        result = [list(i) for i in result]
    elif hard == 2:
        result = cur.execute("SELECT name, s FROM che2 ORDER BY s DESC, name").fetchall()
        result = [list(i) for i in result]
    elif hard == 3:
        result = cur.execute("SELECT name, s FROM che3 ORDER BY s DESC, name").fetchall()
        result = [list(i) for i in result]
    result = result[:: -1]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 0) and (event.pos[1] > 0) and (
                    event.pos[0] < 205) and (event.pos[1] < 203):
                return setings()
        f1 = pygame.font.Font(None, 50)
        text1 = f1.render('Rating:', 0, (0, 0, 0))
        screen.blit(text1, (400, 200))
        d = result[0][1] // 86400
        h = result[0][1] % 86400 // 3600
        m = result[0][1] % 86400 % 3600 // 60
        s = result[0][1] % 86400 % 3600 % 60
        f1 = pygame.font.Font(None, 50)
        text1 = f1.render('1: ' + str(result[0][0]) + ' ' + clockprint(d, h, m, s), 0, (0, 0, 0))
        screen.blit(text1, (400, 300))
        d = result[1][1] // 86400
        h = result[1][1] % 86400 // 3600
        m = result[1][1] % 86400 % 3600 // 60
        s = result[1][1] % 86400 % 3600 % 60
        f1 = pygame.font.Font(None, 50)
        text1 = f1.render('2: ' + str(result[1][0]) + ' ' + clockprint(d, h, m, s), 0, (0, 0, 0))
        screen.blit(text1, (400, 400))
        d = result[2][1] // 86400
        h = result[2][1] % 86400 // 3600
        m = result[2][1] % 86400 % 3600 // 60
        s = result[2][1] % 86400 % 3600 % 60
        f1 = pygame.font.Font(None, 50)
        text1 = f1.render('3: ' + str(result[2][0]) + ' ' + clockprint(d, h, m, s), 0, (0, 0, 0))
        screen.blit(text1, (400, 500))
        d = result[3][1] // 86400
        h = result[3][1] % 86400 // 3600
        m = result[3][1] % 86400 % 3600 // 60
        s = result[3][1] % 86400 % 3600 % 60
        f1 = pygame.font.Font(None, 50)
        text1 = f1.render('4: ' + str(result[3][0]) + ' ' + clockprint(d, h, m, s), 0, (0, 0, 0))
        screen.blit(text1, (400, 600))
        d = result[4][1] // 86400
        h = result[4][1] % 86400 // 3600
        m = result[4][1] % 86400 % 3600 // 60
        s = result[4][1] % 86400 % 3600 % 60
        f1 = pygame.font.Font(None, 50)
        text1 = f1.render('5: ' + str(result[4][0]) + ' ' + clockprint(d, h, m, s), 0, (0, 0, 0))
        screen.blit(text1, (400, 700))
        pygame.display.flip()
        clock.tick(FPS)


# пауза
def menu():
    fon = pygame.transform.scale(load_image('menu.jpg', True), (1000, 1000))
    screen.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 185) and (event.pos[1] > 99) and (
                    event.pos[0] < 814) and (event.pos[1] < 273):
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 185) and (event.pos[1] > 290) and (
                    event.pos[0] < 814) and (event.pos[1] < 460):
                return shop()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 185) and (event.pos[1] > 476) and (
                    event.pos[0] < 814) and (event.pos[1] < 688):
                okk()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 185) and (event.pos[1] > 705) and (
                    event.pos[0] < 814) and (event.pos[1] < 900):
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN and (event.pos[0] > 895) and (event.pos[1] > 0) and (
                    event.pos[0] < 1000) and (event.pos[1] < 100):
                return setings()
        pygame.display.flip()
        clock.tick(FPS)


# обозначение всех переменных
def okk():
    global seti, kick_boss, fight, chance, ok, size, width, height, screen, running, a, sp, clock, game_map, dikt, \
        hard_of_level, sp_of_gotten_things, bx, by, tile_images, tile_width, tile_height, tiles_group, player_group, \
        player, player_group, player_image, boss_group, item4, item3, item2, item1, name, pc, heal_pc, running, \
        level_y, all_sprites, dikt, coords, fight, game_map, atak_time, le, level_x, chance, camera, manage, level_map,\
        b, FPS
    seti = False
    kick_boss = [[149, 148], [150, 148], [151, 149], [151, 150], [150, 151], [149, 151], [148, 150], [148, 149]]
    pygame.init()
    fight = False
    chance = None
    ok = False
    size = width, height = 1000, 1000
    screen = pygame.display.set_mode(size)
    running = True
    create_file()
    a = 'map.txt'
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
    bx, by = 0, 0
    tile_images = {'coin': load_image('coin.jpg'), 'empty1': load_image('atak_floor.png'),
                   'boss': pygame.transform.scale(load_image('boss.png', -1), (100, 100)),
                   'wall': load_image('box.png'),
                   'empty': load_image('grass.png'), 'axe_of_bloodlust': load_image('axe_of_bloodlust.png'),
                   'berserker_rage': load_image('berserker_rage.png'),
                   'blade_of_despair': load_image('blade_of_despair.png'),
                   'blade_of_seven_seas': load_image('blade_of_the_seven_seas.png'),
                   'claws_of_chaos': load_image('claws_of_chaos.png'),
                   'endless_battle': load_image('endless_battle.png'),
                   'Wind_of_Nature': load_image('Wind_of_Nature.png'),
                   'the_sword_of_the_legionnaire': load_image('the_sword_of_the_legionnaire.png'),
                   'the_giants_axe': load_image('the_giants_axe.png'),
                   'the_belt_of_ares': load_image('the_belt_of_ares.png'),
                   'the Golden stick': load_image('the Golden stick.png'),
                   'studded_armor': load_image('studded_armor.png'),
                   'storm_belt': load_image('storm_belt.png'), 'queens_wings': load_image('queens_wings.png'),
                   'leather_armor': load_image('leather_armor.png'), 'health_crystal': load_image('health_crystal.png'),
                   'healing_necklace': load_image('healing_necklace.png'),
                   'hammer_of_wrath': load_image('hammer_of_wrath.png'),
                   'Golden meteor': load_image('Golden meteor.png'),
                   'dagger': load_image('dagger.png'), 'caller_of_the_devil': load_image('caller_of_the_devil.png'),
                   'benefit_of_courage': load_image('benefit_of_courage.png'),
                   'armor_blade': load_image('armor_blade.png'),
                   'an_ordinary_spear': load_image('an_ordinary_spear.png'),
                   'a_shot_of_the_hunter': load_image('a_shot_of_the_hunter.png'), 'trident': load_image('trident.png'),
                   'protective_helmet': load_image('protective_helmet.png'),
                   'immortality': load_image('immortality.png')}
    player_image = load_image('mar.png', -1)
    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    boss_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    tile_width = tile_height = 50
    manage = 2
    FPS = 50
    start()
    level_map = load_level(a)
    player, level_x, level_y = generate_level(level_map, False)
    item1 = True
    item2 = True
    item3 = True
    item4 = True
    b = Boss(hard_of_level)
    heal_pc = 0
    pc = Player_characters(hard_of_level)
    camera = Camera()
    how_much = 1
    camera.update(player)
    name = ''
    t.dtime = 0
    t.htime = 0
    t.mtime = 0
    t.stime = 0
    for sprite in all_sprites:
        camera.apply(sprite)
    # сама игра
    while True:
        for event in pygame.event.get():
            k = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                terminate()
            if k[pygame.K_LEFT] and manage == 2:
                heal_pc += 1
                if heal_pc == 25:
                    t.tick(1, how_much)
                    heal_pc = 0
                if coords[0] - 1 > -1:
                    if dikt[(coords[1]), coords[0] - 1].isalpha():
                        what_the_item(dikt[(coords[1]), coords[0] - 1])
                        Player.movel(player)
                        camera.update(player)
                        if not item4:
                            player_image = load_image('armorx2.png', -1)
                        else:
                            player_image = load_image('mar.png', -1)
                        all_sprites = pygame.sprite.Group()
                        tiles_group = pygame.sprite.Group()
                        player_group = pygame.sprite.Group()
                        player, level_x, level_y = generate_level(game_map, False)
                        tile_width = tile_height = 50
                        camera.update(player)
                    else:
                        Player.movel(player)
                        camera.update(player)
                    for sprite in all_sprites:
                        camera.apply(sprite)
            elif k[pygame.K_RIGHT] and manage == 2:
                heal_pc += 1
                if heal_pc == 25:
                    t.tick(1, how_much)
                    heal_pc = 0
                if coords[0] + 1 < 300:
                    if dikt[(coords[1]), coords[0] + 1].isalpha():
                        what_the_item(dikt[(coords[1]), coords[0] + 1])
                        Player.mover(player)
                        camera.update(player)
                        if not item4:
                            player_image = load_image('armorx2.png', -1)
                        else:
                            player_image = load_image('mar.png', -1)
                        all_sprites = pygame.sprite.Group()
                        tiles_group = pygame.sprite.Group()
                        player_group = pygame.sprite.Group()
                        player, level_x, level_y = generate_level(game_map, False)
                        tile_width = tile_height = 50
                        camera.update(player)
                    else:
                        Player.mover(player)
                        camera.update(player)
                    for sprite in all_sprites:
                        camera.apply(sprite)
            elif k[pygame.K_UP] and manage == 2:
                heal_pc += 1
                if heal_pc == 25:
                    t.tick(1, how_much)
                    heal_pc = 0
                if coords[1] - 1 > -1:
                    if dikt[(coords[1] - 1), coords[0]].isalpha():
                        what_the_item(dikt[(coords[1] - 1), coords[0]])
                        Player.moveu(player)
                        camera.update(player)
                        if not item4:
                            player_image = load_image('armorx2.png', -1)
                        else:
                            player_image = load_image('mar.png', -1)
                        all_sprites = pygame.sprite.Group()
                        tiles_group = pygame.sprite.Group()
                        player_group = pygame.sprite.Group()
                        player, level_x, level_y = generate_level(game_map, False)
                        tile_width = tile_height = 50
                        camera.update(player)
                    else:
                        Player.moveu(player)
                        camera.update(player)
                    for sprite in all_sprites:
                        camera.apply(sprite)
            elif k[pygame.K_DOWN] and manage == 2:
                heal_pc += 1
                if heal_pc == 25:
                    t.tick(1, how_much)
                    heal_pc = 0
                if coords[1] + 1 < 300:
                    if dikt[(coords[1] + 1), coords[0]].isalpha():
                        what_the_item(dikt[(coords[1] + 1), coords[0]])
                        Player.moved(player)
                        camera.update(player)
                        if not item4:
                            player_image = load_image('armorx2.png', -1)
                        else:
                            player_image = load_image('mar.png', -1)
                        all_sprites = pygame.sprite.Group()
                        tiles_group = pygame.sprite.Group()
                        player_group = pygame.sprite.Group()
                        player, level_x, level_y = generate_level(game_map, False)
                        tile_width = tile_height = 50
                        camera.update(player)
                    else:
                        Player.moved(player)
                        camera.update(player)
                    for sprite in all_sprites:
                        camera.apply(sprite)
            elif k[pygame.K_a] and manage == 1:
                heal_pc += 1
                if heal_pc == 25:
                    t.tick(1, how_much)
                    heal_pc = 0
                if coords[0] - 1 > -1:
                    if dikt[(coords[1]), coords[0] - 1].isalpha():
                        what_the_item(dikt[(coords[1]), coords[0] - 1])
                        Player.movel(player)
                        camera.update(player)
                        if not item4:
                            player_image = load_image('armorx2.png', -1)
                        else:
                            player_image = load_image('mar.png', -1)
                        all_sprites = pygame.sprite.Group()
                        tiles_group = pygame.sprite.Group()
                        player_group = pygame.sprite.Group()
                        player, level_x, level_y = generate_level(game_map, False)
                        tile_width = tile_height = 50
                        camera.update(player)
                    else:
                        Player.movel(player)
                        camera.update(player)
                    for sprite in all_sprites:
                        camera.apply(sprite)
            elif k[pygame.K_d] and manage == 1:
                heal_pc += 1
                if heal_pc == 25:
                    t.tick(1, how_much)
                    heal_pc = 0
                if coords[0] + 1 < 300:
                    if dikt[(coords[1]), coords[0] + 1].isalpha():
                        what_the_item(dikt[(coords[1]), coords[0] + 1])
                        Player.mover(player)
                        camera.update(player)
                        if not item4:
                            player_image = load_image('armorx2.png', -1)
                        else:
                            player_image = load_image('mar.png', -1)
                        all_sprites = pygame.sprite.Group()
                        tiles_group = pygame.sprite.Group()
                        player_group = pygame.sprite.Group()
                        player, level_x, level_y = generate_level(game_map, False)
                        tile_width = tile_height = 50
                        camera.update(player)
                    else:
                        Player.mover(player)
                        camera.update(player)
                    for sprite in all_sprites:
                        camera.apply(sprite)
            elif k[pygame.K_w] and manage == 1:
                heal_pc += 1
                if heal_pc == 25:
                    t.tick(1, how_much)
                    heal_pc = 0
                if coords[1] - 1 > -1:
                    if dikt[(coords[1] - 1), coords[0]].isalpha():
                        what_the_item(dikt[(coords[1] - 1), coords[0]])
                        Player.moveu(player)
                        camera.update(player)
                        if not item4:
                            player_image = load_image('armorx2.png', -1)
                        else:
                            player_image = load_image('mar.png', -1)
                        all_sprites = pygame.sprite.Group()
                        tiles_group = pygame.sprite.Group()
                        player_group = pygame.sprite.Group()
                        player, level_x, level_y = generate_level(game_map, False)
                        tile_width = tile_height = 50
                        camera.update(player)
                    else:
                        Player.moveu(player)
                        camera.update(player)
                    for sprite in all_sprites:
                        camera.apply(sprite)
            elif k[pygame.K_s] and manage == 1:
                heal_pc += 1
                if heal_pc == 25:
                    t.tick(1, how_much)
                    heal_pc = 0
                if coords[1] + 1 < 300:
                    if dikt[(coords[1] + 1), coords[0]].isalpha():
                        what_the_item(dikt[(coords[1] + 1), coords[0]])
                        Player.moved(player)
                        camera.update(player)
                        if not item4:
                            player_image = load_image('armorx2.png', -1)
                        else:
                            player_image = load_image('mar.png', -1)
                        all_sprites = pygame.sprite.Group()
                        tiles_group = pygame.sprite.Group()
                        player_group = pygame.sprite.Group()
                        player, level_x, level_y = generate_level(game_map, False)
                        tile_width = tile_height = 50
                        camera.update(player)
                    else:
                        Player.moved(player)
                        camera.update(player)
                    for sprite in all_sprites:
                        camera.apply(sprite)
            elif k[pygame.K_SPACE]:
                heal_pc += 1
                if heal_pc == 25:
                    t.tick(1, how_much)
                    heal_pc = 0
                if coords in kick_boss:
                    pc.giving_damage(b)
                elif coords in [[8, 8], [9, 8], [10, 8], [11, 8],
                                [8, 9], [8, 10], [11, 9], [11, 10],
                                [8, 11], [9, 11], [10, 11], [11, 11]] and fight:
                    pc.giving_damage(b)
            elif k[pygame.K_t]:
                heal_pc += 1
                if heal_pc == 25:
                    t.tick(1, how_much)
                    heal_pc = 0
                t.tick(10, how_much)
            elif k[pygame.K_ESCAPE]:
                heal_pc += 1
                if heal_pc == 25:
                    t.tick(1, how_much)
                    heal_pc = 0
                menu()
            elif k[pygame.K_m]:
                heal_pc += 1
                if heal_pc == 25:
                    t.tick(1, how_much)
                    heal_pc = 0
                how_much = 10
        heal_pc += 1
        if heal_pc == 25:
            t.tick(1, how_much)
            heal_pc = 0
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        tiles_group.draw(screen)
        player_group.draw(screen)
        pygame.draw.rect(screen, [0, 0, 200], [750, 0, 1000, 110])
        pygame.draw.rect(screen, [200, 0, 0], [750, 110, 1000, 354])
        f1 = pygame.font.Font(None, 24)
        text1 = f1.render(str(b.HP) + 'HP', 0, (0, 0, 0))
        screen.blit(text1, (760, 10))
        f1 = pygame.font.Font(None, 24)
        text1 = f1.render('armor: ' + str(b.armor), 0, (0, 0, 0))
        screen.blit(text1, (760, 44))
        f1 = pygame.font.Font(None, 24)
        text1 = f1.render('damage: ' + str(b.damage), 0, (0, 0, 0))
        screen.blit(text1, (760, 78))
        f1 = pygame.font.Font(None, 24)
        text1 = f1.render('Time: ' + t.print(), 0, (0, 0, 0))
        screen.blit(text1, (760, 120))
        f1 = pygame.font.Font(None, 24)
        text1 = f1.render(str(pc.HP) + '/' + str(pc.SHP) + 'HP', 0, (0, 0, 0))
        screen.blit(text1, (760, 154))
        f1 = pygame.font.Font(None, 24)
        text1 = f1.render('armor: ' + str(pc.armor), 0, (0, 0, 0))
        screen.blit(text1, (760, 188))
        f1 = pygame.font.Font(None, 24)
        text1 = f1.render('damage: ' + str(pc.damage), 0, (0, 0, 0))
        screen.blit(text1, (760, 223))
        f1 = pygame.font.Font(None, 24)
        text1 = f1.render('vampirizm: ' + str(pc.vampirizm), 0, (0, 0, 0))
        screen.blit(text1, (760, 256))
        f1 = pygame.font.Font(None, 24)
        text1 = f1.render('regen: ' + str(pc.regen), 0, (0, 0, 0))
        screen.blit(text1, (760, 290))
        f1 = pygame.font.Font(None, 24)
        text1 = f1.render('extra life: ' + str(pc.extra_life), 0, (0, 0, 0))
        screen.blit(text1, (760, 324))
        f1 = pygame.font.Font(None, 24)
        text1 = f1.render('physical penetration: ' + str(pc.physical_penetration), 0, (0, 0, 0))
        screen.blit(text1, (760, 358))
        f1 = pygame.font.Font(None, 24)
        text1 = f1.render('coords: ' + str(coords[0] + 1) + ',' + str(coords[1] + 1), 0, (0, 0, 0))
        screen.blit(text1, (760, 392))
        f1 = pygame.font.Font(None, 24)
        text1 = f1.render('cash: ' + str(pc.cash) + ' $', 0, (0, 0, 0))
        screen.blit(text1, (760, 426))
        pygame.display.flip()
        clock.tick(FPS)


seti = False
kick_boss = [[149, 148], [150, 148], [151, 149], [151, 150], [150, 151], [149, 151], [148, 150], [148, 149]]
pygame.init()
fight = False
chance = None
ok = False
size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
running = True
create_file()
a = 'map.txt'
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
bx, by = 0, 0
tile_images = {'coin': load_image('coin.jpg'), 'empty1': load_image('atak_floor.png'),
               'boss': pygame.transform.scale(load_image('boss.png', -1), (100, 100)), 'wall': load_image('box.png'),
               'empty': load_image('grass.png'), 'axe_of_bloodlust': load_image('axe_of_bloodlust.png'),
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
manage = 2
FPS = 50
level_map = load_level(a)
player, level_x, level_y = generate_level(level_map, False)
item1 = True
item2 = True
item3 = True
item4 = True
b = Boss(hard_of_level)
heal_pc = 0
pc = Player_characters(hard_of_level)
camera = Camera()
how_much = 1
camera.update(player)
name = ''
okk()
