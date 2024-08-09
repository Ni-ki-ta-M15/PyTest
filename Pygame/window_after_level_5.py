def WAL_5():

    from game_level_1 import _game_l_1

    level_count = 0
    import pygame
    import sys
    pygame.init()
    window_size = (640, 640)
    display = pygame.display.set_mode(window_size)
    pygame.display.set_caption("ИГРА 'Метеорит'")
    font = pygame.font.Font('Minecraft Rus NEW.otf', 26)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            level_count = 0
            text_surface = font.render(f'Вы прошли уровень {5}', True, (255, 255, 255))
            text_surface2 = font.render('Хотите продолжить?', True, (255, 255, 255))
            text_surface_YES = font.render('Да', True, (55, 155, 255))
            text_surfaceNO = font.render('Нет', True, (255, 155, 55))
            text_surface3 = font.render('You won this game!', True, 'green')
            text_rect = text_surface.get_rect(topleft=(270, 100))
            text_rect2 = text_surface2.get_rect(topleft=(270, 160))
            text_rect_YES = text_surface_YES.get_rect(topleft=(270, 220))
            text_rect_NO = text_surfaceNO.get_rect(center=(270, 320))
            display.fill((222, 184, 135, 0.71))
            display.blit(text_surface, text_rect)
            display.blit(text_surface2, text_rect2)
            display.blit(text_surface_YES, text_rect_YES)
            display.blit(text_surfaceNO, text_rect_NO)
            display.blit(text_surface3, text_rect)

            mouse_yes_no = pygame.mouse.get_pos()
            if text_rect_YES.collidepoint(mouse_yes_no) and pygame.mouse.get_pressed()[0]:
                _game_l_1()

                pygame.quit()
                sys.exit()

            if text_rect_YES.collidepoint(mouse_yes_no) and pygame.mouse.get_pressed()[1] or \
                    pygame.mouse.get_pressed()[2]:
                display.fill((255, 34, 34, 0.85))
            elif text_rect_NO.collidepoint(mouse_yes_no) and pygame.mouse.get_pressed()[0]:
                pygame.quit()
                sys.exit()
            level_count += 1
        pygame.display.flip()

WAL_5()