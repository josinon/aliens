import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group

def run_game():
	#inicializa o jogo e cria um objeto para a tela
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#Cria a espaçonave
	ship = Ship(ai_settings, screen)
	#Cria um grupo no qual serão armazenados os projéteis
	bullets = Group()

	#Inicia o laço principal do jogo
	while True:
		#Observa eventos de teclado e de mouse
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings, screen, ship, bullets)
		
run_game() 