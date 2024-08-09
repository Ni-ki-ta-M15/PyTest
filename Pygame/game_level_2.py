
def _game_l_2():

    import sys
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
    ammo = pygame.image.load('ammunitionссссссссс1.png')

    detect = pygame.image.load('defence.png')
    detect_x = random.randint(5, 620)
    detect_y = -2
    detect_list = []

    ammo_x = random.randint(5, 620)
    ammo_y = -2
    ammo_list = []
    ammo_rem = 2

    money = pygame.image.load('dollar.png')
    money_x = random.randint(10, 610)
    money_y = -30
    money_list = []
    money_counter = 0

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
    pygame.time.set_timer(money_timer, random.randint(3000, 8000))

    ammo_timer = pygame.USEREVENT + 3
    pygame.time.set_timer(ammo_timer, random.randint(10000, 20000))

    detec_timer = pygame.USEREVENT + 4
    pygame.time.set_timer(detec_timer, 10000)

    detec_timer_line = pygame.USEREVENT + 5
    pygame.time.set_timer(detec_timer_line, 5000)

    gameplay = True

    label_lose_x = 150
    label_lose_y = 50

    label_lose_try_x = 90
    label_lose_try_y = 470

    label_to_try = pygame.font.Font('Minecraft Rus NEW.otf', 50)
    label = pygame.font.Font('Thirt.ttf', 50)
    label_lose = label_to_try.render('You lose !', False, (190, 60, 250))
    label_lose_try = label_to_try.render('Click to try again!', False, (190, 60, 250))
    label_lose_rect = label_lose.get_rect(topleft=(label_lose_try_x, label_lose_try_y))

    while True:
        display.blit(bg, (0, bg_y))
        display.blit(bg, (0, bg_y - 640))

        if gameplay:
            music.set_volume(0.1)
            music.play()
            keys = pygame.key.get_pressed()

            meteorite_counter_text = label.render(f"Skip: {skip_metior}", True, (255, 255, 255))
            display.blit(meteorite_counter_text, (10, 10))

            money_counter_text = label.render(f"Money: {money_counter}", True, (255, 255, 255))
            display.blit(money_counter_text, (10, 50))

            ammo_counter_text = label.render(f"A: {ammo_rem}", True, (255, 255, 255))
            display.blit(ammo_counter_text, (10, 90))

            meteorite_counter_text_lose = label.render(f"Skipped meteorite: {skip_metior}", False, (255, 40, 0))

            money_counter_text_lose = label.render(f"Money: {money_counter}", False, (255, 140, 0))

            if keys[pygame.K_LEFT] and player_x >= 10:
                player_x -= player_speed
            elif keys[pygame.K_RIGHT] and player_x <= 595:
                player_x += player_speed
            player_rect = player_left[0].get_rect(topleft=(player_x, player_y))

            if meteorite_list:
                for (last, (el_met, speed)) in enumerate(meteorite_list):
                    display.blit(meteorite, el_met)
                    el_met.y += speed

                    if player_rect.colliderect(el_met):
                        gameplay = False
                        meteorite_list.clear()
                        skip_metior = 0
                    elif el_met.y > 650:
                        meteorite_list = [(el, speed) for el, speed in meteorite_list if el.y <= 650]
                        skip_metior += 1

            if detect_list:
                detect_list = [el for el in detect_list if el.y <= 650]
                for el in detect_list:
                    display.blit(detect, el)
                    el.y += 10

            if money_list:
                money_list = [el for el in money_list if el.y <= 650]
                for el in money_list:
                    display.blit(money, el)
                    el.y += 10

                    if player_rect.colliderect(el):
                        money_list.remove(el)
                        money_counter += 1

            if ammo_list:
                ammo_list = [al for al in ammo_list if al.y <= 650]
                for al in ammo_list:
                    display.blit(ammo, al)
                    al.y += 10

                    if player_rect.colliderect(al):
                        ammo_list.remove(al)
                        ammo_rem += random.randint(1, 4)
            display.blit(player_left[player_count], (player_x, player_y))
            if player_count == 1:
                player_count = 0
            elif player_count < 2:
                player_count += 1
            bg_y += 5
            if bg_y == 640:
                bg_y = 0
            meteorite_y += 10
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
            display.blit(meteorite_counter_text_lose, (150, 140))
            display.blit(money_counter_text_lose, (120, 270))

            mouse = pygame.mouse.get_pos()
            if label_lose_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                meteorite_list.clear()
                missile_list.clear()
                money_list.clear()
                money_counter = 0
                ammo_list.clear()
                ammo_rem = 5
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
            if event.type == ammo_timer:
                ammo_x = random.randint(10, 610)
                ammo_y = 0
                ammo_list.append(ammo.get_rect(topleft=(ammo_x, ammo_y)))

            if event.type == detec_timer:
                detect_x = random.randint(10, 610)
                detect_y = 0
                detect_list.append(detect.get_rect(topleft=(detect_x, detect_y)))

                detect_list.append(detect.get_rect(topleft=(detect_x, detect_y)))
            if event.type == detec_timer_line:
                detect_x = 100
                detect_y = 100
                pygame.draw.line(display, (255, 0, 0), (100, 100), (150, 100), 20)

            if event.type == meteorite_timer:
                meteorite_x = random.randint(10, 610)
                meteorite_y = 0
                if skip_metior < 25:
                    meteorite_speed = random.randint(15, 25)
                    meteorite_list.append((meteorite.get_rect(topleft=(meteorite_x, meteorite_y)), meteorite_speed))
                elif skip_metior == 25:
                    from window_after_level_2 import WAL_2
                    WAL_2()
                    sys.exit()

            if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_SPACE and ammo_rem > 0:
                missile_list.append(missile.get_rect(topleft=(player_x + 14, player_y - 28)))
                ammo_rem -= 1

        clock.tick(25)
_game_l_2()