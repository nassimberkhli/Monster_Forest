# Monster_Forest
my first project : un personnage peut se déplacer, sauter, tirer et utiliser une attaque spéciale. Des slimes apparaissent et une pluie de comètes peut tomber.
---

## ⚙️ Installation

1. Installer Python (3.9+ recommandé)
2. Installer Pygame :

   ```bash
   pip install pygame
   ```

---

## ▶️ Lancer le jeu

```bash
python jeux.py
```

---

## 🎮 Commandes

* **Flèches gauche/droite** : déplacement
* **Flèche haut** : saut
* **Z ou W** : tir normal
* **X** : attaque spéciale (quand la jauge est remplie)
* **Espace** ou clic sur le bouton Play : démarrer

---

## 📖 Règles

* Tuer des slimes augmente le score et remplit la jauge spéciale.
* Quand la jauge est pleine, tu peux lancer une attaque spéciale.
* Des comètes tombent régulièrement et doivent être évitées.
* Si ta vie tombe à 0, la partie recommence.

---

## 📁 Structure

* `jeux.py` : point d’entrée
* `classgame.py`, `classplayer.py`, `classmonstre.py`, `classcomet*.py` : logique du jeu
* `classprojectile*.py`, `projectile_base.py` : projectiles
<img width="1073" height="718" alt="image" src="https://github.com/user-attachments/assets/479a3716-e6c9-4ce6-b01b-879c52afea70" />



Projet basé sur **Pygame**. Have fun 🎯
