import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # создание экрана

pygame.display.set_caption('Игра ТИР') # название окна
icon = pygame.image.load('')


running = True
while running:
    pass # чтобы не вылетало ошибка

pygame.quit()