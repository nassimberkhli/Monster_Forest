import pygame
import random

class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super().__init__()
        self.comet_event = comet_event

        # Charger, mettre à l'échelle, puis récupérer le rect (cet ordre est important)
        img = pygame.image.load("comet.png")
        self.image = pygame.transform.scale(img, (120, 90))
        self.rect = self.image.get_rect()

        # spawn au-dessus de l'écran, x aléatoire
        self.rect.x = random.randint(0, 1080 - self.rect.width)
        self.rect.y = random.randint(-200, -60)

        # vitesse plus lente
        self.vitesse = random.randint(2, 4)

        # mask pour collide_mask
        self.mask = pygame.mask.from_surface(self.image)

    def fall(self):
        self.rect.y += self.vitesse

        # hors écran
        if self.rect.y >= 720:
            self.comet_event.all_comet.remove(self)
            return

        # collision joueur
        if self.comet_event.game.collision(self, self.comet_event.game.all_player):
            self.comet_event.all_comet.remove(self)
            self.comet_event.game.player.damage(20)

