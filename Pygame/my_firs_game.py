import random
import pygame

clock = pygame.time.Clock()

player_speed = 20
pygame.init()
display = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Jump")
pygame.display.set_icon(pygame.image.load("game.png").convert_alpha())

music = pygame.mixer.Sound('music_for_game.mp3')

bg = pygame.image.load('big_dipper_little_dipper_by_jonreytrevino_dff5flg-fullview.png')
meteorite = pygame.image.load("meteorite.png")

money = pygame.image.load('dollar.png')
money_x = random.randint(10, 610)
money_y = -30
money_list = []
money_count = 0




meteorite_y = 660
meteorite_x = random.randint(10, 610)
meteorite_list = []

player_right = [pygame.image.load('player.png'),
                pygame.image.load('player.png')
                ]
player_left = [pygame.image.load('player.png'),
               pygame.image.load('player.png')
               ]

player_count = 0

skip_metior = 0
skip_metior_cor = (90, 90)

missile = pygame.image.load('missile.png')
missile_list = []


player_x = 20
player_y = 580
bg_y = 0

meteorite_timer = pygame.USEREVENT + 1
pygame.time.set_timer(meteorite_timer, 1000)

money_timer = pygame.USEREVENT + 2
pygame.time.set_timer(meteorite_timer, 4000)

gameplay = True

label_lose_x = 150
label_lose_y = 250
label_lose_try_x = 200
label_lose_try_y = 400

label = pygame.font.Font('Thirt.ttf', 50)
label_lose = label.render('You are lose !', False, (190, 60, 250))
label_lose_try = label.render('Click to try again!', False, (190, 60, 250))
label_lose_rect = label_lose.get_rect(topleft=(label_lose_try_x, label_lose_try_y))

while True:
    display.blit(bg, (0, bg_y))
    display.blit(bg, (0, bg_y - 640))

    if gameplay == True:
        music.set_volume(0.1)
        music.play()
        keys = pygame.key.get_pressed()

        counter_text = label.render(f"Skip: {skip_metior}", True, (255, 255, 255))
        display.blit(counter_text, (10, 10))

        money_counter_text = label.render(f"Money: {money_counter}", True, (255, 255, 255))
        display.blit(money_counter_text, (10, 50))  # Отображаем счетчик монеток под счетчиком метеоритов

        if keys[pygame.K_LEFT] and player_x >= 10:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x <= 595:
            player_x += player_speed
        player_rect = player_left[0].get_rect(topleft=(player_x, player_y))

        if meteorite_list:
            for (last, (el, speed)) in enumerate(meteorite_list):
                display.blit(meteorite, el)
                el.y += speed

                if player_rect.colliderect(el):
                    gameplay = False
                    meteorite_list.clear()
                    skip_metior = 0
                elif el.y > 650:
                    meteorite_list = [(el, speed) for el, speed in meteorite_list if el.y <= 650]
                    skip_metior += 1

        if money_list:
            money_list = [el for el in money_list if el.y <= 650]
            for el in money_list:
                display.blit(money, el)
                el.y += 10  # Используем одинаковую скорость для всех монеток

                if player_rect.colliderect(el):
                    money_list.remove(el)  # Удаляем монетку, если игрок ее собрал
                    money_counter += 1  # Увеличиваем счетчик монеток

        display.blit(player_left[player_count], (player_x, player_y))
        if player_count == 1:
            player_count = 0
        elif player_count < 2:
            player_count += 1

        bg_y += 5
        if bg_y == 640:
            bg_y = 0
        meteorite_y += 10

        if keys[pygame.K_SPACE]:
            missile_list.append(missile.get_rect(topleft=(player_x, player_y + 30)))

        if missile_list:
            for (i, el) in enumerate(missile_list):
                display.blit(missile, (el.x, el.y))
                el.y -= 10

                if el.y < 0:
                    missile_list.pop(i)

                if meteorite_list:
                    for (index, (meteorite_el, speed)) in enumerate(meteorite_list):
                        if el.colliderect(meteorite_el):
                            meteorite_list.pop(index)
                            missile_list.pop(i)
                            skip_metior += 1
                            break

    else:
        display.fill((25, 78, 90))
        display.blit(label_lose, (label_lose_x, label_lose_y))
        display.blit(label_lose_try, label_lose_rect)

        mouse = pygame.mouse.get_pos()
        if label_lose_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            meteorite_list.clear()
            missile_list.clear()
            money_list.clear()
            gameplay = True

        music.stop()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == money_timer:
            money_x = random.randint(10, 610)
            money_y = 0
            money_list.append(money.get_rect(topleft=(money_x, money_y)))
        if event.type == meteorite_timer:
            meteorite_x = random.randint(10, 610)
            meteorite_y = 0
            meteorite_speed = random.randint(10, 25)
            meteorite_list.append((meteorite.get_rect(topleft=(meteorite_x, meteorite_y)), meteorite_speed))

        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            missile_list.append(missile.get_rect(topleft=(player_x + 14, player_y - 28)))

    clock.tick(25)
