import pygame
import random
import sqlite3

# DB en mémoire
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Monstre(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     barre_vie_slime INTEGER,
     attaque REAL,
     vitesse INTEGER
)
""")
conn.commit()

cursor.execute("""
INSERT INTO Monstre (barre_vie_slime, attaque, vitesse)
VALUES (?, ?, ?)
""", (100, 0.3, 2))
conn.commit()

cursor.execute("""SELECT barre_vie_slime, attaque, vitesse FROM Monstre""")
base_donnee_monstre = cursor.fetchone()


class Monstre(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game

        self.barre_vie_slime = base_donnee_monstre[0]
        self.barre_vie_slime_max = base_donnee_monstre[0]
        self.attaque = base_donnee_monstre[1]
        self.vitesse = base_donnee_monstre[2]

        self.image = pygame.image.load("slime2.png")
        self.image = pygame.transform.scale(self.image, (240, 120))
        self.rect = self.image.get_rect()
        self.rect.x = 800 + random.randint(20, 200)
        self.rect.y = 609

        self.mask = pygame.mask.from_surface(self.image)

    def damage(self, degat):
        self.barre_vie_slime -= degat
        if self.barre_vie_slime <= 0:
            self.rect.x = 1000 + random.randint(0, 500)
            self.vitesse = random.randint(1, 3)
            self.barre_vie_slime = self.barre_vie_slime_max
            self.game.score += 1

            if self.game.kill < 160:
                self.game.kill += 20

            if self.game.kill >= 80:
                self.game.x, self.game.y, self.game.z = 230, 131, 5

    def barre_slime(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 140, self.rect.y - 2, self.barre_vie_slime_max, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 140, self.rect.y - 2, max(0, self.barre_vie_slime), 5])

    def move_monstre(self):
        if not self.game.collision(self, self.game.all_player):
            self.rect.x -= self.vitesse
        else:
            self.game.player.damage(self.attaque)

