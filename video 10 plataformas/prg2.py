import pygame
import random

# -------------------------------------------------------------
# Codigo prg2.py (1er codigo auxiliar)
# 
# En estos codigos, crearemos las clases que necesitemos
# -------------------------------------------------------------
class Personaje(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
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
        self.rect.topleft = (x, y)

        self.flip = False
        self.saltar = False

        self.dx = 0
        self.dy = 0

        self.ultimoUpdate = pygame.time.get_ticks()




    def update(self):
        if self.saltar:
            self.mientrasSaltandoNoLeerTeclado()
        else:
            self.leerTeclado()

        calculo = pygame.time.get_ticks()
        if calculo - self.ultimoUpdate > 100:
            self.ultimoUpdate = calculo

            if self.anima == 9:
                self.anima = 10 
            else:
                self.anima = 9

        if self.dx != 0:
            self.image = self.lista_imagenes[self.anima]
            self.image = pygame.transform.flip(self.image, self.flip, False)
        else:
            self.image = self.lista_imagenes[0]
            self.image = pygame.transform.flip(self.image, self.flip, False)





    def leerTeclado(self):
        tecla = pygame.key.get_pressed()
        self.dx = 0

        if tecla[pygame.K_LEFT]:
            self.dx = -5
            self.flip = True

        elif tecla[pygame.K_RIGHT]:
            self.dx = 5
            self.flip = False

        if tecla[pygame.K_SPACE] or tecla[pygame.K_UP]:
            if not self.saltar:
                self.saltar = True
                self.dy = -20
                self.game.sonido_salto.play()


        self.rect.x += self.dx


        # ------------------ Check Limites ----------------
        if self.rect.x < 0:
            self.rect.x = 0

        elif self.rect.right > self.game.RESOLUCION[0]:
            self.rect.right = self.game.RESOLUCION[0]



    def mientrasSaltandoNoLeerTeclado(self):
        self.dy += self.game.GRAVEDAD

        self.rect.y += self.dy
        self.rect.x += self.dx

        if self.rect.bottom + self.dy >= self.game.RESOLUCION[1] - 55:
            self.rect.bottom = self.game.RESOLUCION[1] - 55
            self.saltar = False
            self.dy = 0








class Plataforma(pygame.sprite.Sprite):
    def __init__(self, game, x, y, numero):
        super().__init__()
        self.game = game

        image_rect = self.game.obtenerGrafico('SueloTile.png', (self.game.TX, self.game.TY))

        if numero == 0:
            longitudRND = 10
            x = 0
        else:
            longitudRND = random.randrange(7) + 1

        self.image = pygame.Surface((longitudRND * self.game.TX, self.game.TY))

        for i in range(longitudRND):
            self.image.blit(image_rect[0], (i * self.game.TX, 0))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)



    def update(self):
        pass 


