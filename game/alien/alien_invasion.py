import sys
import pygame

def run_game():
	pygame.init()
	screen = pygame.display.set_mode((800, 600))
	pygame.display.set_caption('Alien Invasion')
	# 设置背景色
	bg_color = (230, 230, 230)
	# 开始游戏的主循环
	while True:
		# 监视键盘和鼠标事件:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		# 每次循环时都会重绘屏幕
		screen.fill(bg_color)
		# 让最近绘制的屏幕可见
		pygame.display.flip()

run_game()