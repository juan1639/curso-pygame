import pygame
import random

# -------------------------------------------------------------
# Codigo prg2.py (1er codigo auxiliar)
# 
# En estos codigos, crearemos las clases que necesitemos
# -------------------------------------------------------------
class Coche(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game 

        self.image = pygame.image.load('../assets/coche2.png').convert()
        self.image.set_colorkey((255, 255, 255))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.ultimo_update_sonidoFreno = pygame.time.get_ticks()

        self.aceleracion = 0.2 
        self.deceleracion = 0.05
        self.frenar = 0.4
        self.max_velocidad = 30


    def update(self):
        self.leerTeclado()
        self.checkLimites()


    def leerTeclado(self):
        tecla = pygame.key.get_pressed()
        offSetX = 0

        if tecla[pygame.K_LEFT]:
            offSetX = -5

        elif tecla[pygame.K_RIGHT]:
            offSetX = 5

        if tecla[pygame.K_UP]:
            if self.game.velocidad + self.aceleracion > self.max_velocidad:
                self.game.velocidad += 0.0
            else:
                self.game.velocidad += self.aceleracion

        elif tecla[pygame.K_DOWN]:
            self.sonidoFreno()
            if self.game.velocidad - self.frenar < 0:
                self.game.velocidad -= 0.0
            else:
                self.game.velocidad -= self.frenar

        else:
            if self.game.velocidad - self.deceleracion < 0:
                self.game.velocidad -= 0.0
            else:
                self.game.velocidad -= self.deceleracion

        if tecla[pygame.K_SPACE]:
            self.game.sonido_claxon.play()

        # GIRAR direccion (si hemos pulsado Izda o Dcha)
        self.rect.x += offSetX


    def checkLimites(self):
        zonaVerde = 180
        if self.rect.x < zonaVerde:
            self.rect.x = zonaVerde

        elif self.rect.right > self.game.RESOLUCION[0] - zonaVerde:
            self.rect.right = self.game.RESOLUCION[0] - zonaVerde


    def sonidoFreno(self):
        calculo = pygame.time.get_ticks()
        if calculo - self.ultimo_update_sonidoFreno > 3000:
            self.ultimo_update_sonidoFreno = calculo
            self.game.sonido_frenar.play()


class scrollRoad(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game 

        self.image = pygame.image.load('../assets/carretera.png').convert()

        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y


    def update(self):
        self.checkLimites()
        self.rect.y += self.game.velocidad


    def checkLimites(self):
        if self.rect.y + self.game.velocidad > 0:
            self.rect.y = -600


class cochesEnemigos(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game

        self.image = pygame.image.load('../assets/coche_enemigo.png').convert()
        self.image.set_colorkey((255, 255, 255))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.velocidad = 10


    def update(self):
        self.rect.y += self.calcularOffSetY()


    def calcularOffSetY(self):
        return self.game.velocidad - self.velocidad


class Textos(pygame.sprite.Sprite):
    def __init__(self, game, texto, size, x, y, qcolor, background):
        super().__init__()
        self.game = game 

        self.qcolor = qcolor
        self.background = background

        self.font = pygame.font.SysFont('serif', size)
        self.image = self.font.render(texto, True, self.qcolor, self.background)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        km_h = int(self.game.velocidad * 9)
        self.image = self.font.render(f'{km_h} km/h', True, self.qcolor, self.background)

