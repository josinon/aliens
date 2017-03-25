class Settings():
	''' Uma classe para armazenar todas as configurações da 
	Invasão alienígena.'''

	def __init__(self):
		#inicializa as configurações do jogo
		#Configurações de tela
		self.screen_width = 1200
		self.screen_height = 650
		self.bg_color = (230,230,230)
		self.ship_speed_factor = 1.5