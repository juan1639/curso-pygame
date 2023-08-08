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

        self.velY = 10



    def update(self):
        self.rect.y -= self.velY

        if self.rect.bottom < 0:
            self.kill()
            print(len(self.game.lista_spritesAdibujar))














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


