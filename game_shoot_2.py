import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра ТИР')
icon = pygame.image.load('img/i.jpg')
pygame.display.set_icon(icon)

original_target_img = pygame.image.load('img/target.png')
target_width = 148
target_height = 200
target_img = pygame.transform.scale(original_target_img, (target_width, target_height))

shot_sound = pygame.mixer.Sound('wav/shot.wav')
reload_sound = pygame.mixer.Sound('wav/reload.wav')
no_ammo_sound = pygame.mixer.Sound('wav/no_ammo.mp3')

target_x = random.randint(target_width // 2, SCREEN_WIDTH - target_width // 2)
target_y = random.randint(target_height // 2, SCREEN_HEIGHT - target_height // 2)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# target_speed = 0.1
# target_direction = 1 # 1 означает движение вправо, -1 влево
target_speed_x = 5
target_speed_y = 5

change_direction_time = 1000  # время в миллисекундах для смены направления
last_change_time = pygame.time.get_ticks()

score = 0
shots_fired = 0
magazine_size = 8
total_shots = 0
hit_percentage = 0.0
reloading = False
font = pygame.font.Font(None, 36)

# Таймер обратного отсчета
timer_duration = 30  # Секунды
start_time = pygame.time.get_ticks()
hits_since_last_reset = 0

running = True
while running:
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) / 1000  # Преобразование миллисекунд в секунды
    remaining_time = timer_duration - elapsed_time

    # target_x += target_speed * target_direction # Обновление позиции мишени
    # if target_x > SCREEN_WIDTH - target_width // 2 or target_x < target_width // 2:
    #     target_direction *= -1  # Изменить направление движения

    # Решение о смене направления
    if current_time - last_change_time > change_direction_time:
        target_speed_x = random.choice([-100, 100])
        target_speed_y = random.choice([-100, 100])
        last_change_time = current_time
    # Обновление позиции мишени
        target_x += target_speed_x
        target_y += target_speed_y

    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                if reloading:
                    no_ammo_sound.play()
                    continue
                if not reloading and shots_fired < magazine_size:
                    shot_sound.play()
                    shots_fired += 1
                    total_shots += 1
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if total_shots > 0:
                        hit_percentage = (score / total_shots) * 100
                    if target_x - target_width // 2 < mouse_x < target_x + target_width // 2 and target_y - target_height // 2 < mouse_y < target_y + target_height // 2:
                        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                        target_x = random.randint(target_width // 2, SCREEN_WIDTH - target_width // 2)
                        target_y = random.randint(target_height // 2, SCREEN_HEIGHT - target_height // 2)
                        score += 1
                        hits_since_last_reset += 1

                        if hits_since_last_reset >= 10:
                            hits_since_last_reset = 0
                            start_time = pygame.time.get_ticks()
                            target_width = max(20, target_width - 5)
                            target_height = max(20, target_height - 5)
                            target_img = pygame.transform.scale(original_target_img, (target_width, target_height))
                if shots_fired == magazine_size:
                    reloading = True
            elif event.button == 3:  # Правая кнопка мыши
                if reloading:
                    reload_sound.play()
                    shots_fired = 0
                    reloading = False# Отображение цели
    screen.blit(target_img, (target_x - target_width // 2, target_y - target_height // 2))

    # Отображение текста
    score_text = font.render(f'Попаданий: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    shots_text = font.render(f'Выстрелы: {shots_fired}/{magazine_size}', True, (255, 255, 255))
    screen.blit(shots_text, (10, 50))

    time_text = font.render(f'Время: {int(remaining_time)} сек', True, (255, 255, 255))
    screen.blit(time_text, (10, 90))

    hit_percentage_text = font.render(f'Точность: {hit_percentage:.2f}%', True, (255, 255, 255))
    screen.blit(hit_percentage_text, (10, 130))

    # Проверка на окончание времени
    if remaining_time <= 0:
        running = False
        final_message = f'Игра окончена! Ваш счет: {score}, точность: {hit_percentage:.2f}%'
        message_text = font.render(final_message, True, (255, 0, 0))
        screen.fill((0, 0, 0))
        screen.blit(message_text, (SCREEN_WIDTH // 2 - message_text.get_width() // 2, SCREEN_HEIGHT // 2 - message_text.get_height() // 2))
        pygame.display.update()
        pygame.time.wait(5000)  # Ожидание 5 секунд
    if reloading:
        reload_text = font.render("Для перезарядки нажмите правую клавишу мыши", True, (255, 255, 255))
        screen.blit(reload_text, (100, 550))

    pygame.display.update()

pygame.quit()