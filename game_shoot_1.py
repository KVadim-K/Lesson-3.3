import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра ТИР')
icon = pygame.image.load('img/i.jpg')
pygame.display.set_icon(icon)
# Загрузка оригинального изображения мишени
original_target_img = pygame.image.load('img/target.png')
target_width = 148
target_height = 200
# Создаем копию изображения с начальным размером
target_img = pygame.transform.scale(original_target_img, (target_width, target_height))
# Загрузка звукового файла
shot_sound = pygame.mixer.Sound('wav/shot.wav')
reload_sound = pygame.mixer.Sound('wav/reload.wav')
no_ammo_sound = pygame.mixer.Sound('wav/no_ammo.mp3')
# Позиция центра мишени
target_x = random.randint(target_width // 2, SCREEN_WIDTH - target_width // 2)
target_y = random.randint(target_height // 2, SCREEN_HEIGHT - target_height // 2)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
score = 0
shots_fired = 0
magazine_size = 8
total_shots = 0
hit_percentage = 0.0
reloading = False
font = pygame.font.Font(None, 36)
running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                if reloading:
                    no_ammo_sound.play()  # Воспроизвести звук, если игрок пытается стрелять без патронов
                    continue
                if not reloading and shots_fired < magazine_size:
                    shot_sound.play()
                    shots_fired += 1
                    total_shots += 1  # Увеличиваем общее количество выстрелов
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if total_shots > 0:
                        hit_percentage = (score / total_shots) * 100  # Обновляем процент попаданий
                    if target_x - target_width // 2 < mouse_x < target_x + target_width // 2 and target_y - target_height // 2 < mouse_y < target_y + target_height // 2:
                        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                        target_x = random.randint(target_width // 2, SCREEN_WIDTH - target_width // 2)
                        target_y = random.randint(target_height // 2, SCREEN_HEIGHT - target_height // 2)
                        score += 1
                        if score % 10 == 0:
                            target_width = max(20, target_width - 5)
                            target_height = max(20, target_height - 5)
                            target_img = pygame.transform.scale(original_target_img, (target_width, target_height))
                if shots_fired == magazine_size:
                    reloading = True
            elif event.button == 3:  # Правая кнопка мыши
                if reloading:
                    reload_sound.play()
                    shots_fired = 0
                    reloading = False

    screen.blit(target_img, (target_x - target_width // 2, target_y - target_height // 2))
    score_text = font.render(f"Очки: {score}", True, (255, 255, 255))
    ammo_text = font.render(f"Патроны: {magazine_size - shots_fired}", True, (255, 255, 255))
    total_shots_text = font.render(f"Всего выстрелов: {total_shots}", True, (255, 255, 255))
    hit_percentage_text = font.render(f"Точность: {hit_percentage:.2f}%", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(ammo_text, (10, 50))
    screen.blit(total_shots_text, (530, 10))
    screen.blit(hit_percentage_text, (590, 50))

    if reloading:
        reload_text = font.render("Для перезарядки нажмите правую клавишу мыши", True, (255, 255, 255))
        screen.blit(reload_text, (100, 550))

    pygame.display.update()

pygame.quit()