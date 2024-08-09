import pygame, random


clock = pygame.time.Clock()

pygame.init()
screen_info = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Second Game")
pygame.display.set_icon(pygame.image.load("game.png").convert_alpha())



#Settings player

bg = pygame.image.load("BG.png").convert_alpha()
player = pygame.image.load('right_go.png').convert_alpha()
enemy = pygame.image.load('monster.png').convert_alpha()


walk_right = [
    pygame.image.load('right_stop.png').convert_alpha(),
    pygame.image.load('right_go.png').convert_alpha(),
    pygame.image.load('right_stop.png').convert_alpha(),
    pygame.image.load('right_go_1.png').convert_alpha()
]
walk_left = [
    pygame.image.load('left_stop.png').convert_alpha(),
    pygame.image.load('left_go.png').convert_alpha(),
    pygame.image.load('left_stop.png').convert_alpha(),
    pygame.image.load('left_go_1.png').convert_alpha()
]



player_count = 0
running = True

player_speed = 10
player_x = 90
player_y = 570


enemy_list = []

is_jump = False
jump_count = 8

#Settings game
bg_x = 0
music = pygame.mixer.Sound('music_for_game.mp3')

music.play()

enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, random.randint(1200, 4000))

gameplay = True

label = pygame.font.Font('Second.ttf', 50)
lose_label = label.render('You are lose in this time', False, (250, 70, 10))
restart_label = label.render('Try again? ', False, (10, 70, 250))
restart_label_rect = restart_label.get_rect(topleft=(320, 340))


fireball_amount = 5
fireball = pygame.image.load('fireball.png').convert_alpha()
fireballs_list = []

while running:

    screen_info.blit(bg, (bg_x, 0))
    screen_info.blit(bg, (bg_x + 1280, 0))

    if gameplay == True:

        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
        if enemy_list:
            for (i, el) in enumerate(enemy_list):
                screen_info.blit(enemy, el)
                el.x -= 10


                if el.x < -2:
                    enemy_list.pop(i)
                if player_rect.colliderect(el):
                    gameplay = False


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            screen_info.blit(walk_left[player_count], (player_x, player_y)) # y = 570
        else:
            screen_info.blit(walk_right[player_count], (player_x, player_y))



        if keys[pygame.K_LEFT] and player_x > 10:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 1190:
            player_x += player_speed


        if not is_jump:
            if keys[pygame.K_UP]:
                is_jump = True
        else:
            if jump_count >= -8:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2

                jump_count -= 1
            else:
                is_jump = False
                jump_count = 8

        if player_count == 3:
            player_count = 0
        else:
            player_count += 1


        bg_x -= 5
        if bg_x == -1280:
            bg_x = 0

        if fireballs_list:
            for (i, el) in enumerate(fireballs_list):
                screen_info.blit(fireball, (el.x, el.y))
                el.x += 5

                if el.x > 1282:
                    fireballs_list.pop(i)

                if enemy_list:
                    for (index, ghost) in enumerate(enemy_list):
                        if el.colliderect(ghost):
                            enemy_list.pop(index)
                            fireballs_list.pop(i)

    else:
        screen_info.fill((107, 108, 109))
        screen_info.blit(lose_label, (320, 240))
        screen_info.blit(restart_label, (restart_label_rect))


        mouse = pygame.mouse.get_pos()

        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 90
            enemy_list.clear()
            fireballs_list.clear()



    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == enemy_timer:
            enemy_list.append(enemy.get_rect(topleft=(1290, 562)))

        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_SPACE and fireball_amount > 0:
            fireballs_list.append(fireball.get_rect(topleft=(player_x + 25, player_y - 15)))
            fireball_amount -= 1

    clock.tick(20)

