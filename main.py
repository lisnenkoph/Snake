import pygame
import random
import time

pygame.init()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 25)

BLACK = (0, 0, 0)
RED = (209, 3, 3)
GREEN = (0, 255, 0)
YELLOW = (255, 200, 57)
CYAN = (110, 157, 64)
ORANGE = (239, 79, 79)
GOLD = (255, 215, 0)

dis = pygame.display.set_mode((540, 360))
pygame.display.set_caption('Dream team')

clock = pygame.time.Clock()

snake = 10
snake_speed = 12
accelerated_speed = 20

font_style = pygame.font.SysFont(None, 30)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [540 / 4, 360 / 4])

def scores(score):
    value = score_font.render(str(score), True, BLACK)
    dis.blit(value, [0, 0])

def snakes(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, ORANGE, [x[0], x[1], snake_block, snake_block])

def gameLoop():
    close = False
    over = False

    x = 270
    y = 180

    foodx = round(random.randrange(0, 540 - snake) / 10) * 10
    foody = round(random.randrange(0, 360 - snake) / 10) * 10
    gold_apple_x = -1
    gold_apple_y = -1
    gold_apple_timer = time.time()

    xc = 0
    yc = 0
    snake_list = []
    snake_len = 1
    lives = 1
    is_accelerated = False

    while not over:      # Проверка, закончилась ли игра

        while close == True:
            dis.fill(CYAN)       # Заполнение экрана цветом CYAN
            message("Game over! 'r' - restart, q - 'quit'", BLACK) # Отображение сообщения игроку
            pygame.display.update()     # Обновление дисплея

            for event in pygame.event.get():        # Проверка событий, таких как нажатия клавиш
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:     # Если пользователь нажимает 'q', завершить игру
                        over = True
                        close = False
                    if event.key == pygame.K_r:     # Если пользователь нажимает 'r', перезапустить игру
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:        # Двигать змейку вверх, если пользователь нажимает стрелку вверх
                    yc = -snake
                    xc = 0
                elif event.key == pygame.K_DOWN:    # Двигать змейку вниз, если пользователь нажимает стрелку вниз
                    yc = snake
                    xc = 0
                elif event.key == pygame.K_LEFT:    # Двигать змейку влево, если пользователь нажимает стрелку влево
                    xc = -snake
                    yc = 0
                elif event.key == pygame.K_RIGHT:   # Двигать змейку вправо, если пользователь нажимает стрелку вправо
                    xc = snake
                    yc = 0
                elif event.key == pygame.K_LSHIFT:  # Ускорить змейку, если пользователь удерживает клавишу левого shift
                    is_accelerated = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    is_accelerated = False

        if x >= 540 or x < 0 or y >= 360 or y < 0:  # Проверка столкновения змейки со стенами игровой области
            close = True
        x += xc     # Обновление позиции змейки на основе текущего направления движения
        y += yc

        if x >= 540 or x < 0 or y >= 360 or y < 0:  # Повторная проверка столкновения змейки со стенами игровой области
            close = True

        dis.fill(CYAN)
        
        if gold_apple_x == -1 and gold_apple_y == -1 and time.time() - gold_apple_timer >= 8:
            if random.randrange(150) == 0:
                gold_apple_x = round(random.randrange(0, 540 - snake) / 10) * 10
                gold_apple_y = round(random.randrange(0, 360 - snake) / 10) * 10
                gold_apple_timer = time.time()

        if x == foodx and y == foody:
            snake_len += 1
            foodx = round(random.randrange(0, 540 - snake) / 10) * 10
            foody = round(random.randrange(0, 360 - snake) / 10) * 10

        if x == gold_apple_x and y == gold_apple_y:
            snake_len += 3
            gold_apple_x = -1
            gold_apple_y = -1

        if gold_apple_x != -1 and gold_apple_y != -1:
            pygame.draw.rect(dis, GOLD, [gold_apple_x, gold_apple_y, snake, snake])
            if time.time() - gold_apple_timer >= 5:
                gold_apple_x = -1
                gold_apple_y = -1
                
       pygame.draw.rect(dis, RED, [foodx, foody, snake, snake])
        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_list.append(snake_Head)
        if len(snake_list) > snake_len:
            del snake_list[0]

        for i in snake_list[:-1]:
            if i == snake_Head:
                if lives > 0:
                    lives -= 1
                    snake_len = 1
                else:
                    close = True

        snakes(snake, snake_list)
        scores(snake_len - 1)
        pygame.draw.rect(dis, YELLOW, [x, y, snake, snake])
        pygame.display.update()

        if is_accelerated:
            clock.tick(accelerated_speed)
        else:
            clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
