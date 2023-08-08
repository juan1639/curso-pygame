import pygame

# -------------------------------------------------------------
# Codigo prg2.py (1er codigo auxiliar)
# 
# En estos codigos, crearemos las clases que necesitemos
# -------------------------------------------------------------
class Nave(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game 

        self.image = pygame.image.load('../assets/nave1.png').convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        print(self.image, self.rect)
        self.rect.centerx = self.game.RESOLUCION[0] // 2
        self.rect.bottom = self.game.RESOLUCION[1]

        


    def update(self):
        pass


