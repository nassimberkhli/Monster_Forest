import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.degat = 7
        self.vitesse = 8

        img = pygame.image.load("projectile.png")
        self.image = pygame.transform.scale(img, (160, 64))
        self.rect = self.image.get_rect()
        self.rect.x = self.game.player.rect.x + 20
        self.rect.y = self.game.player.rect.y + 20

        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.x += self.vitesse

        for monstre in self.game.collision(self, self.game.all_monstre):
            self.game.all_projectile.remove(self)
            monstre.damage(self.degat)

