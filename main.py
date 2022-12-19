import pygame
from random import randrange
# окно игры
RES = 800
SIZE = 50
pygame.init()
sc=pygame.display.set_mode([RES,RES])
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
front_x = pygame.font.SysFont('Arial', 48, bold=True)
front_n = pygame.font.SysFont('Arial', 48, bold=True)
img = pygame.image.load('228.jpg').convert()
# рассположение змеи и яблока
x = randrange(SIZE, RES - SIZE, SIZE)
y = randrange(SIZE, RES - SIZE, SIZE)
apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
# доп параметры
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 60
dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
score = 0
speed_count = 0
snake_speed = 10
def close_game():
	"""
	Функция закрытия игры
	используютс методы получения события из очереди
	В них определяеться, кода окно закрываеться
	:return:
	"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

def func1():
	"""
	Функция появления текста на экране в случаее проражения
	:return:
	"""
	render_end = font_end.render('GAME OVER', 1, pygame.Color('black'))
	sc.blit(render_end, (RES // 2 - 200, RES // 3))
	render_n = front_n.render('нажмите    для закрытия', 1, pygame.Color('black'))
	sc.blit(render_n, (105, RES // 2-50))
	render_x = front_x.render('X', 1, pygame.Color('red'))
	sc.blit(render_x, (320, RES // 2-45))
	pygame.display.flip()

def func2():
	"""
	Функция появления текста на экране в случаее пробеды
	:return:
	"""
	render_end = font_end.render('WIN', 1, pygame.Color('black'))
	sc.blit(render_end, (RES // 2 - 70, RES // 3))
	render_n = front_n.render('нажмите    для закрытия', 1, pygame.Color('black'))
	sc.blit(render_n, (105, RES // 2 - 50))
	render_x = front_x.render('X', 1, pygame.Color('red'))
	sc.blit(render_x, (320, RES // 2 - 45))
	pygame.display.flip()

if __name__ == '__main__':
	while True:
		sc.blit(img, (0, 0))
	# цвета и отбражения змейки и яблока
		[pygame.draw.rect(sc, pygame.Color('dark green'), (i, j, SIZE - 1, SIZE - 1)) for i, j in snake]
		pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))
	# очки
		render_score = font_score.render(f'SCORE: {score}',1, pygame.Color('black'))
		sc.blit(render_score, (RES // 2 - 75,0))
	# передвежение змейки
		speed_count += 1
		if not speed_count % snake_speed:
			x += dx * SIZE
			y += dy * SIZE
			snake.append((x, y))
			snake = snake[-length:]
	# поедание яблок
		if snake[-1] == apple:
			apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
			length += 1
			score += 1
			snake_speed -= 1
			snake_speed = max(snake_speed, 8)
	# проиграшный вариант
		if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)) :
			while True:
				func1()
				close_game()
		pygame.display.flip()
		clock.tick(fps)
		close_game()
	# выйграшный вариант
		if score == 256:
			while True:
				func2()
				close_game()
	# управление
		key = pygame.key.get_pressed()
		if key[pygame.K_w]:
			if dirs['W']:
				dx, dy = 0, -1
				dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
		elif key[pygame.K_s]:
			if dirs['S']:
				dx, dy = 0, 1
				dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
		elif key[pygame.K_a]:
			if dirs['A']:
				dx, dy = -1, 0
				dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
		elif key[pygame.K_d]:
			if dirs['D']:
				dx, dy = 1, 0
				dirs = {'W': True, 'S': True, 'A': False, 'D': True, }
