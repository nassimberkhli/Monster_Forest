import pygame
from classgame import Game
pygame.init()

screen = pygame.display.set_mode((1080, 720))

fond_ecran = pygame.image.load("fond.png")
fond_ecran = pygame.transform.scale(fond_ecran, (1080, 720))

banniere = pygame.image.load("banniere.png")
banniere = pygame.transform.scale(banniere, (1080, 720))

play_button = pygame.image.load("bouton.png")
play_button = pygame.transform.scale(play_button, (250, 225))
play_button_rect = play_button.get_rect()
play_button_rect.x = 700
play_button_rect.y = 400

clock = pygame.time.Clock()

game = Game()

continu = True
while continu:
    clock.tick(60)
    screen.blit(fond_ecran, (0, 8))

    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(banniere, (55, 90))
        screen.blit(play_button, play_button_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continu = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_RIGHT:
                game.bool_right_or_left = 2
                img = pygame.image.load("personnage.png")
                img = pygame.transform.scale(img, (60, 60))
                game.player.set_image(img)

            if event.key == pygame.K_LEFT:
                game.bool_right_or_left = 3
                img = pygame.image.load("personnage2.png")
                img = pygame.transform.scale(img, (60, 60))
                game.player.set_image(img)

            # Tir : accepter Z (AZERTY) ET W (QWERTY)
            if event.key in (pygame.K_z, pygame.K_w):
                if game.bool_right_or_left == 2:
                    game.lancer()
                elif game.bool_right_or_left == 3:
                    game.lancer2()

            # Attaque spéciale (X)
            if event.key == pygame.K_x:
                if game.kill >= 80 and game.bool_right_or_left == 3:
                    game.kill -= 80
                    if game.kill < 80:
                        game.x, game.y, game.z = 49, 5, 230
                    game.lancer_special()

                if game.kill >= 80 and game.bool_right_or_left == 2:
                    game.kill -= 80
                    if game.kill < 80:
                        game.x, game.y, game.z = 49, 5, 230
                    game.lancer_special2()

            # Saut
            if event.key == pygame.K_UP and game.player.rect.y == game.player.FLOOR_Y:
                game.player.jump()

            if event.key == pygame.K_SPACE:
                game.start()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()

    if game.kill >= 80:
        game.x, game.y, game.z = 229, 7, 7

