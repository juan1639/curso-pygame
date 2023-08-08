import pygame
import random

# -------------------------------------------------------------
# Codigo prg2.py (1er codigo auxiliar)
# 
# En estos codigos, crearemos las clases que necesitemos
# -------------------------------------------------------------
class Personaje(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game

        self.lista_imagenes = []
        self.anima = 9

        image_rect = self.game.obtenerGrafico('sSheet1.png', (720, 330))
        self.image = image_rect[0]
        self.rect = image_rect[1]

        for i in range(3):
            for ii in range(9):
                img = pygame.Surface((80, 110))
                img.blit(self.image, (0, 0), (ii * 80, i * 110, 80, 110))
                img.set_colorkey((0, 0, 0))
                self.lista_imagenes.append(img)

        self.image = self.lista_imagenes[self.anima]
        self.rect = self.image.get_rect()
        self.rect.topleft = (400, 400)

        self.ultimoUpdate = pygame.time.get_ticks()




    def update(self):
        self.leerTeclado()

        calculo = pygame.time.get_ticks()
        if calculo - self.ultimoUpdate > 200:
            self.ultimoUpdate = calculo

            if self.anima == 9:
                self.anima = 10 
            else:
                self.anima = 9

            x = self.rect.x
            y = self.rect.y 
            self.image = self.lista_imagenes[self.anima]
            self.image.get_rect()
            self.rect.x = x 
            self.rect.y = y



         







    def leerTeclado(self):
        tecla = pygame.key.get_pressed()

        if tecla[pygame.K_LEFT]:
            self.rect.x -= 5

        elif tecla[pygame.K_RIGHT]:
            self.rect.x += 5


        # ------------------ Check Limites ----------------
        if self.rect.x < 0:
            self.rect.x = 0

        elif self.rect.right > self.game.RESOLUCION[0]:
            self.rect.right = self.game.RESOLUCION[0]






class SueloTile(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game 
 



    def update(self):
        pass 


