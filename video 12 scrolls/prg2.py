import pygame
import random

# -------------------------------------------------------------
# Codigo prg2.py (1er codigo auxiliar)
# 
# En estos codigos, crearemos las clases que necesitemos
# -------------------------------------------------------------
class Nave(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game 

        self.invisible = 255

        self.image = pygame.image.load('../assets/nave1.png').convert()
        self.image.set_colorkey((0, 0, 0))
        self.image.set_alpha(self.invisible)
        self.rect = self.image.get_rect()
        #print(self.image, self.rect)
        self.rect.centerx = self.game.RESOLUCION[0] // 2
        self.rect.bottom = self.game.RESOLUCION[1]


        


    def update(self):
        self.leerTeclado()

        self.invisible -= 0
        self.image.set_alpha(self.invisible)

        if self.invisible <= 0:
            self.invisible = 255





    def leerTeclado(self):
        tecla = pygame.key.get_pressed()

        if tecla[pygame.K_LEFT]:
            self.rect.x -= 5

        elif tecla[pygame.K_RIGHT]:
            self.rect.x += 5

        if tecla[pygame.K_SPACE]:
            self.game.instanciaDisparo()

        if self.rect.x < 0:
            self.rect.x = 0

        elif self.rect.right > self.game.RESOLUCION[0]:
            self.rect.right = self.game.RESOLUCION[0]





class ScrollParallax:
    def __init__(self, game, x, y, velX, img):
        self.game = game 

        imagen = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(imagen, (self.game.RESOLUCION[0], self.game.RESOLUCION[1]))
        self.rect = self.image.get_rect()

        self.posInicial = x 
        self.rect.x = x 
        self.rect.y = y

        self.velX = velX


    def dibuja(self):
        self.rect.x -= self.velX

        if self.rect.x <= -self.game.RESOLUCION[0]:
            self.rect.x = self.posInicial

        self.game.pantalla.blit(self.image, (self.rect.x, self.rect.y))
        self.game.pantalla.blit(self.image, (self.rect.x + self.game.RESOLUCION[0], self.rect.y))








class EstrellasRetro:
    def __init__(self, game):
        self.game = game 

        self.color = (random.randrange(255), random.randrange(255),random.randrange(255))

        self.x = random.randrange(self.game.RESOLUCION[0])
        self.y = random.randrange(self.game.RESOLUCION[1])

        self.size = random.randrange(2) + 1



    def dibuja(self):
        self.actualiza()

        pygame.draw.rect(self.game.pantalla, self.color, (self.x, self.y, self.size, self.size))


    def actualiza(self):
        self.y += 1

        if self.y > self.game.RESOLUCION[1]:
            self.y = 0








