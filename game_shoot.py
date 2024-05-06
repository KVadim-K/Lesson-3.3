import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # создание экрана

pygame.display.set_caption('Игра ТИР') # название окна
icon = pygame.image.load('img/i.jpg') # иконка
pygame.display.set_icon(icon) # установка иконки

target_img = pygame.image.load('img/target.png') # картинка мишени
target_width = 50
target_height = 50

target_x = random.randint(0, SCREEN_WIDTH - target_width) # координаты мишени
target_y = random.randint(0, SCREEN_HEIGHT - target_height) # координаты мишени
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # цвет мишени

running = True
while running:
    # pass # чтобы не вылетало ошибка
    screen.fill(color) # цвет экрана (фон)
    for event in pygame.event.get(): # события
        if event.type == pygame.QUIT: # если закрыли окно
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: # если нажали мышь
            mouse_x, mouse_y = pygame.mouse.get_pos() # координаты мыши
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height: # если мышь внутри мишени
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # меняем цвет
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    screen.blit(target_img, (target_x, target_y)) # рисуем мишень
    pygame.display.update() # обновление экрана
pygame.quit() # завершение игры
