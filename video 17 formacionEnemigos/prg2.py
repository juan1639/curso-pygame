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

        self.ultimoUpdate = pygame.time.get_ticks()


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
            calculo = pygame.time.get_ticks()

            if calculo - self.ultimoUpdate > 200:
                self.ultimoUpdate = calculo
                self.game.instanciaDisparo()


        # ------------------ Check Limites ----------------
        if self.rect.x < 0:
            self.rect.x = 0

        elif self.rect.right > self.game.RESOLUCION[0]:
            self.rect.right = self.game.RESOLUCION[0]


class Disparo(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game 

        self.image = pygame.image.load('../assets/laserBlue16.png').convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        #print(self.image, self.rect)
        
        self.rect.centerx = x 
        self.rect.bottom = y 

        self.velY = 15


    def update(self):
        self.rect.y -= self.velY
        # mouse = pygame.mouse.get_pos()

        # self.rect.y = mouse[1]
        # self.rect.x = mouse[0]

        if self.rect.bottom < 0:
            self.kill()
            print(len(self.game.lista_spritesAdibujar))


class Formacion:
    def __init__(self, game, x, y, ancho, alto, velX, velY):
        self.game = game 

        self.x = x 
        self.y = y 
        self.ancho = ancho
        self.alto = alto

        self.velX = velX
        self.velY = velY
        self.limiteDcho = self.game.RESOLUCION[0]
        self.limiteIzq = 0 


    def actualiza(self):
        self.x += self.velX

        if self.x + self.ancho >= self.limiteDcho and self.velX > 0:
            self.velX *= -1
            self.y += self.velY

        if self.x <= self.limiteIzq and self.velX < 0:
            self.velX *= -1
            self.y += self.velY


    def dibuja(self, surface):
        self.actualiza()
        #pygame.draw.rect(surface, (20, 240, 20), (self.x, self.y, self.ancho, self.alto), 2)



class Enemigo(pygame.sprite.Sprite):
    def __init__(self, game, posX, posY, formX, formY):
        super().__init__()
        self.game = game 

        self.lista_imagenes = []
        self.anima = 0

        for i in range(5):
            img = pygame.image.load('../assets/enemyRed{}.png'.format(i + 1))
            img.set_colorkey((255, 255, 255))
            self.lista_imagenes.append(img)

        self.image = self.lista_imagenes[self.anima]
        self.rect = self.image.get_rect()

        self.ancho = 100
        self.alto = 100

        self.posX = posX
        self.posY = posY

        self.rect.x = self.posX * self.ancho + formX
        self.rect.y = self.posY * self.alto + formY

        self.ultimoUpdate = pygame.time.get_ticks()


    def update(self):
        self.check_colision()
        self.animacion()

        self.rect.x = self.posX * self.ancho + self.game.formacion.x
        self.rect.y = self.posY * self.alto + self.game.formacion.y


    def animacion(self):
        calculo = pygame.time.get_ticks()

        if calculo - self.ultimoUpdate > 500:
            self.ultimoUpdate = calculo

            self.anima += 1
            if self.anima >= 5:
                self.anima = 0

            x = self.rect.x 
            y = self.rect.y
            self.image = self.lista_imagenes[self.anima]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y


    def check_colision(self):
        colision = pygame.sprite.spritecollide(self, self.game.lista_disparos, True)
        #colision = pygame.sprite.groupcollide(self.game.lista_enemigos, self.game.lista_disparos, True, True)

        if colision:
            self.kill()

