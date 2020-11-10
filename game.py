import pygame
import string
import random

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)

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
		self.points = 0
		self.color = WHITE
		
	def start(self):
		while self.run:
			self.clock.tick(self.FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.run = False
				if event.type == pygame.KEYDOWN:
					self.key = pygame.key.name(event.key)
					self.draw_keypress()
					self.screen.fill(BLACK)
					self.draw_words()

			self.check()
			self.check_keyboard()
			pygame.display.flip()
		pygame.quit()

	def check_keyboard(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_BACKSPACE]:
			self.reset()
			self.points -= 1

	def reset(self):		
		self.current_word = ""
		self.rand_word = self.random_word()

	def check(self):
		if len(self.current_word) == len(self.rand_word):

			#right word
			if self.current_word == self.rand_word:
				self.points += 1
				self.current_word = ""
				self.rand_word = self.random_word()

			#wrong word
			if len(self.current_word) == len(self.rand_word):
				self.points -= 1
				self.current_word = ""
				self.rand_word = self.random_word()

	def draw_keypress(self):
		self.screen.blit(self.myfont.render(self.key,False, WHITE), (40,40))
		if self.key in string.ascii_lowercase:
			self.current_word += self.key
		else:
			pass

	def draw_words(self):
		self.screen.blit(self.myfont.render(self.current_word,False, self.color), (100,300))		
		self.screen.blit(self.myfont.render(str(self.points),False, WHITE), (200,15))

	def random_word(self):
		words = ["car", "find","green","mouse"]
		rand_word = random.choice(words)
		self.screen.blit(self.myfont.render(rand_word,False, WHITE), (150,150))
		return rand_word

app = Game()		

if __name__ == "__main__":
	app.start()