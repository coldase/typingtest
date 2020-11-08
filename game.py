import pygame
import string
import random
WHITE = (255,255,255)
BLACK = (0,0,0)

class Game:
	def __init__(self):
		pygame.init()
		pygame.font.init()

		self.key = ""
		self.clock = pygame.time.Clock()
		self.myfont = pygame.font.SysFont("Calibri", 50)
		self.screen = pygame.display.set_mode((400,400))
		self.FPS = 20
		self.run = True
		self.current_word = ""
		self.rand_word = self.random_word()

	def start(self):
		while self.run:
			self.clock.tick(self.FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.run = False
				if event.type == pygame.KEYDOWN:
					self.key = pygame.key.name(event.key)
					self.draw_keypress()
					if self.current_word == self.random_word:
						self.rand_word = self.random_word()
					else:
						self.screen.fill(BLACK)
						self.draw_word()
				

			pygame.display.flip()
		pygame.quit()

	def draw_keypress(self):
		self.screen.blit(self.myfont.render(self.key,False, WHITE), (40,40))
		self.current_word += self.key

	def draw_word(self):
		self.screen.blit(self.myfont.render(self.current_word,False, WHITE), (100,100))		

	def random_word(self):
		words = ["car", "find","green","mouse"]
		rand_word = random.choice(words)
		self.screen.blit(self.myfont.render(rand_word,False, WHITE), (50,150))
		return rand_word

app = Game()		

if __name__ == "__main__":
	app.start()