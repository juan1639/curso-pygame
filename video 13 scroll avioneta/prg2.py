import pygame
import random

# -------------------------------------------------------------
# Codigo prg2.py (1er codigo auxiliar)
# 
# En estos codigos, crearemos las clases que necesitemos
# -------------------------------------------------------------
class Avioneta(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game 

        self.lista_imagenes = []

        for i in range(3):
            img = pygame.image.load('../assets/planeRed{}.png'.format(i + 1)).convert()
            img.set_colorkey((0, 0, 0))
            self.lista_imagenes.append(img)

        self.imgPd = 0
        self.image = self.lista_imagenes[self.imgPd]
        self.rect = self.image.get_rect()
        #print(self.image, self.rect)

        self.rect.centerx = self.game.RESOLUCION[0] // 2
        self.rect.bottom = self.game.RESOLUCION[1] // 2

        self.ultimoUpdate = pygame.time.get_ticks()
        self.ultimoUpdateHelice = pygame.time.get_ticks()


        


    def update(self):
        self.leerRaton()
        self.leerTeclado()

        calculo = pygame.time.get_ticks()

        if calculo - self.ultimoUpdateHelice > 60:
            self.ultimoUpdateHelice = calculo 

            self.imgPd += 1

            if self.imgPd >= 3:
                self.imgPd = 0

            self.image = self.lista_imagenes[self.imgPd]






    def leerTeclado(self):
        tecla = pygame.key.get_pressed()

        if tecla[pygame.K_LEFT]:
            self.rect.x -= 5

        elif tecla[pygame.K_RIGHT]:
            self.rect.x += 5

        if tecla[pygame.K_SPACE]:
            calculo = pygame.time.get_ticks()

            if calculo - self.ultimoUpdate > 150:
                self.ultimoUpdate = calculo
                self.game.instanciaDisparo()


        if self.rect.x < 0:
            self.rect.x = 0

        elif self.rect.right > self.game.RESOLUCION[0]:
            self.rect.right = self.game.RESOLUCION[0]



    def leerRaton(self):
        posXY = pygame.mouse.get_pos()

        self.rect.x = posXY[0]
        self.rect.y = posXY[1]





class Disparo(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game 

        self.image = pygame.image.load('../assets/disparoAv1.png').convert()
        self.image.set_colorkey((255, 255, 255))

        self.rect = self.image.get_rect()
        self.height = self.image.get_height()

        self.rect.x = x 
        self.rect.y = y


    def update(self):
        self.rect.x += 9

        if self.rect.x > self.game.RESOLUCION[0]:
            print(self.game.lista_spritesAdibujar)
            self.kill()







class ScrollParallax:
    def __init__(self, game, x, y, velX, img):
        self.game = game 

        imagen = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(imagen, (self.game.RESOLUCION[0], self.game.RESOLUCION[1] // 2))
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








