import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # создание экрана

pygame.display.set_caption('Игра ТИР') # название окна
icon = pygame.image.load('img/i.jpg') # иконка
pygame.display.set_icon(icon) # установка иконки

target_img = pygame.image.load('target.png') # картинка мишени
target_width = 50
target_height = 50

target_x = random.randint(0, SCREEN_WIDTH - target_width) # координаты мишени
target_y = random.randint(0, SCREEN_HEIGHT - target_height) # координаты мишени
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # цвет мишени

running = True
while running:
    pass # чтобы не вылетало ошибка

pygame.quit()