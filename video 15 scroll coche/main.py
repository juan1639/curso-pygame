import pygame
import sys

from prg2 import *


# ----------------------------------------------------------------
# Codigo Principal (main.py) ... Aqui se aloja la clase Game
# 
# Funciones:
# 			instancias()
#			buclePrincipal()
#							update()
#							draw()
#							check_event()			
# ----------------------------------------------------------------
class Game:
	def __init__(self):
		pygame.init()

		self.rojo = (255, 0, 0)
		self.verde = (0, 255, 0)
		self.amarillo = (255, 255, 0)
		self.fondoGRIS = (70, 70, 70)

		self.RESOLUCION = (800, 600)
		self.FPS = 90

		self.enJuego = True
		self.velocidad = 0.0

		self.pantalla = pygame.display.set_mode(self.RESOLUCION)
		self.reloj = pygame.time.Clock()

		self.lista_spritesAdibujar = pygame.sprite.Group()
		self.lista_scroll = pygame.sprite.Group()
		self.instancias()


	def instancias(self):
		coche = Coche(self, self.RESOLUCION[0] // 2, self.RESOLUCION[1] // 1.5)
		self.lista_spritesAdibujar.add(coche)

		scrollroad = scrollRoad(self, 0, -600)
		self.lista_scroll.add(scrollroad)

		velocimetro = Textos(self, str(int(self.velocidad)), 40, self.RESOLUCION[0] // 1.25, 
			self.RESOLUCION[1] // 1.1, self.amarillo, self.fondoGRIS)
		self.lista_spritesAdibujar.add(velocimetro)


	def update(self):
		self.lista_scroll.update()
		self.lista_spritesAdibujar.update()

		pygame.display.flip()
		self.reloj.tick(self.FPS)


	def draw(self):
		self.pantalla.fill(self.fondoGRIS)
		self.lista_scroll.draw(self.pantalla)
		pygame.draw.rect(self.pantalla, self.fondoGRIS, (self.RESOLUCION[0] - 175, 
			self.RESOLUCION[1] - 100, 175, 100))

		self.lista_spritesAdibujar.draw(self.pantalla)


	def check_event(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()


	def buclePrincipal(self):
		while self.enJuego:
			self.check_event()
			self.update()
			self.draw()


if __name__ == '__main__':
    game = Game()
    game.buclePrincipal()


			
