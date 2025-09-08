import pygame
from classmonstre import Monstre
import sqlite3

# Base "temporaire" en mémoire (évite sqlite3.connect("") qui peut planter)
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Player(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     barre_vie INTEGER,
     attaque INTEGER,
     vitesse INTEGER
)
""")
conn.commit()

# Valeurs de base
cursor.execute("""
INSERT INTO Player (barre_vie, attaque, vitesse) VALUES (?, ?, ?)
""", (100, 25, 3))  # vitesse de déplacement horizontale = 3 (moins “rapide”)
conn.commit()

cursor.execute("""SELECT barre_vie, attaque, vitesse FROM Player """)
base_donnee_player = cursor.fetchone()


class Player(pygame.sprite.Sprite):
    FLOOR_Y = 625        # hauteur du sol (cohérent avec ton code)
    GRAVITY = 0.6        # gravité plus douce
    JUMP_STRENGTH = -12  # impulsion de saut

    def __init__(self, game):
        super().__init__()
        self.game = game

        # paramètres
        self.barre_vie = base_donnee_player[0]
        self.barre_vie_max = base_donnee_player[0]
        self.attaque = base_donnee_player[1]

        # vitesse horizontale fixe (ne jamais toucher pendant le saut)
        self.speed = base_donnee_player[2]

        # physique verticale
        self.vy = 0

        # sprite
        self.image = pygame.image.load("personnage.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = Player.FLOOR_Y

        # mask pour collide_mask
        self.mask = pygame.mask.from_surface(self.image)

    # Déplacements horizontaux
    def move_right(self):
        if not self.game.collision(self, self.game.all_monstre):
            self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed

    # Barre de vie
    def barre(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 20, self.rect.y - 20, self.barre_vie_max, 5])
        pygame.draw.rect(surface, (201, 73, 207), [self.rect.x - 20, self.rect.y - 20, max(0, self.barre_vie), 5])

    def damage(self, degat):
        self.barre_vie -= degat
        if self.barre_vie <= 0:
            self.game.game_over()

    # Saut & gravité
    def jump(self):
        # saute uniquement si sur le sol
        if self.rect.y >= Player.FLOOR_Y and self.vy == 0:
            self.vy = Player.JUMP_STRENGTH

    def apply_gravity(self):
        self.vy += Player.GRAVITY
        self.rect.y += self.vy

        # collision avec le “sol”
        if self.rect.y >= Player.FLOOR_Y:
            self.rect.y = Player.FLOOR_Y
            self.vy = 0

    # mettre à jour le mask si l'image change (quand tu tournes le perso)
    def set_image(self, surface):
        self.image = surface
        self.mask = pygame.mask.from_surface(self.image)

