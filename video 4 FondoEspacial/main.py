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
		self.FPS = 60

		self.enJuego = True
		self.arrayEstrellasRetro = []

		self.pantalla = pygame.display.set_mode(self.RESOLUCION)
		self.reloj = pygame.time.Clock()

		self.fondoEstrellas = pygame.image.load('../assets/fondo_estrellas_jon.png').convert()
		self.saturno = pygame.image.load('../assets/saturno_moonpatrol.png').convert_alpha()

		self.lista_spritesAdibujar = pygame.sprite.Group()
		self.instancias()




	def instancias(self):
		self.nave = Nave(self)
		self.lista_spritesAdibujar.add(self.nave)

		# for i in range(900):
		# 	estrella = EstrellasRetro(self)
		# 	self.arrayEstrellasRetro.append(estrella)




	def update(self):
		self.lista_spritesAdibujar.update()

		pygame.display.flip()
		self.reloj.tick(self.FPS)



	def draw(self):
		self.pantalla.blit(self.fondoEstrellas, (0, 0))
		# self.pantalla.blit(self.saturno, (500, 200))
		# self.pantalla.fill((0, 0, 40))
		
		# for i in range(900):
		# 	self.arrayEstrellasRetro[i].dibuja()

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


			
