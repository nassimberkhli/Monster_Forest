import pygame
from classplayer import Player
from classprojectile import Projectile
from classprojectile2 import Projectile2
from classmonstre import Monstre
from classcomet_event import CometFallEvent
from classsuper_projectile import Super_projectile
from classsuper_projectile2 import Super_projectile2

class Game:
    def __init__(self):
        self.is_playing = False
        self.first_game = True

        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)

        self.comet_event = CometFallEvent(self)

        self.all_monstre = pygame.sprite.Group()
        self.all_monstre2 = pygame.sprite.Group()
        self.pressed = {}

        self.all_projectile = pygame.sprite.Group()
        self.all_projectile2 = pygame.sprite.Group()
        self.all_super_projectile = pygame.sprite.Group()
        self.all_super_projectile2 = pygame.sprite.Group()

        self.score = 0
        self.kill = 0
        self.bool_right_or_left = 2

        # couleur de la jauge special (rouge)
        self.x, self.y, self.z = 49, 5, 230
        # couleur de la jauge special (vert)
        self.x1, self.y1, self.z1 = 123, 40, 133

    def start(self):
        self.is_playing = True
        if self.first_game:
            self.spawn_monstre()
            self.spawn_monstre()
            self.first_game = False

    def game_over(self):
        self.all_monstre = pygame.sprite.Group()
        self.player.barre_vie = self.player.barre_vie_max
        self.comet_event.all_comet = pygame.sprite.Group()
        self.comet_event.percent = 0
        self.score = 0
        self.kill = 0
        self.is_playing = False
        self.first_game = True

    def update(self, screen):
        # score
        font = pygame.font.SysFont("monospace", 25)
        score_text = font.render(f"Score : {self.score}", 1, (255, 255, 255))
        screen.blit(score_text, (20, 20))

        # gravité / physique du joueur
        self.player.apply_gravity()

        # joueur
        screen.blit(self.player.image, self.player.rect)
        self.player.barre(screen)

        # barres événementielles
        self.comet_event.update_bar(screen)

        # projectiles
        for p in list(self.all_projectile):
            p.move()
            if p.rect.x > 1100:
                self.all_projectile.remove(p)

        for p2 in list(self.all_projectile2):
            p2.move()
            if p2.rect.x < -100:
                self.all_projectile2.remove(p2)

        for sp in list(self.all_super_projectile):
            sp.move()
            if sp.rect.x < -100:
                self.all_super_projectile.remove(sp)

        for sp2 in list(self.all_super_projectile2):
            sp2.move()
            if sp2.rect.x > 1100:
                self.all_super_projectile2.remove(sp2)

        # monstres
        for monstre in list(self.all_monstre):
            monstre.move_monstre()
            monstre.barre_slime(screen)
            if monstre.rect.x < -300:
                self.player.damage(10)
                self.all_monstre.remove(monstre)
                self.spawn_monstre()

        # comètes
        for comet in list(self.comet_event.all_comet):
            comet.fall()

        # draw groups
        self.all_projectile.draw(screen)
        self.all_projectile2.draw(screen)
        self.all_super_projectile.draw(screen)
        self.all_super_projectile2.draw(screen)
        self.all_monstre.draw(screen)
        self.comet_event.all_comet.draw(screen)

        # barre spéciale
        pygame.draw.rect(screen, (60, 63, 60), [850, 30, 160, 10])
        pygame.draw.rect(screen, (self.x, self.y, self.z), [850, 30, self.kill, 10])

        # déplacements horizontaux (au sol ou en l'air)
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x <= 1026:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x >= -2:
            self.player.move_left()

    # lancements
    def lancer(self):
        self.all_projectile.add(Projectile(self))

    def lancer2(self):
        self.all_projectile2.add(Projectile2(self))

    def lancer_special(self):
        self.all_super_projectile.add(Super_projectile(self))

    def lancer_special2(self):
        self.all_super_projectile2.add(Super_projectile2(self))

    def spawn_monstre(self):
        self.all_monstre.add(Monstre(self))

    def collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

