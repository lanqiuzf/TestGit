import sys
import pygame

def check_events():
	# ��Ӧ����������¼�
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()