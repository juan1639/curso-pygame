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
		pygame.mixer.init()

		self.rojo = (255, 0, 0)
		self.verde = (0, 255, 0)
		self.amarillo = (255, 255, 0)
		self.fondoGRIS = (70, 70, 70)

		self.RESOLUCION = (800, 600)
		self.FPS = 60

		self.enJuego = True
		self.GRAVEDAD = 1

		self.pantalla = pygame.display.set_mode(self.RESOLUCION)
		self.reloj = pygame.time.Clock()

		self.fondoNubes = pygame.image.load('../assets/scrollBg1.png').convert()

		self.sonido_salto = pygame.mixer.Sound('../assets/jumpbros.ogg')

		self.lista_spritesAdibujar = pygame.sprite.Group()
		self.instancias()




	def instancias(self):
		for i in range(self.RESOLUCION[0] // 80):
			suelotile = SueloTile(self, i * 80, self.RESOLUCION[1])
			self.lista_spritesAdibujar.add(suelotile)

		for i in range(80, 400, 80):
			plataforma = SueloTile(self, i, 350)
			self.lista_spritesAdibujar.add(plataforma)


		self.personaje = Personaje(self, self.RESOLUCION[0] // 2, self.RESOLUCION[1] - 220)
		self.lista_spritesAdibujar.add(self.personaje)



	def obtenerGrafico(self, nombrePng, escala):
		img = pygame.image.load('../assets/' + nombrePng).convert()
		img2 = pygame.transform.scale(img, escala)
		rect = img2.get_rect()
		image_rect = (img2, rect)

		return image_rect




	def update(self):
		self.lista_spritesAdibujar.update()

		pygame.display.flip()
		self.reloj.tick(self.FPS)



	def draw(self):
		#self.pantalla.fill(self.fondoGRIS)
		self.pantalla.blit(self.fondoNubes, (0 ,0))

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


			
