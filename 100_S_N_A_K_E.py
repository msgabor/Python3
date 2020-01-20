import pygame
import random                                                           # 13.a import random library for another cubes
pygame.init()

screen = pygame.display.set_mode((800, 600))                            # 1. create display
done = False                                                            # 2. done variable boolean

x_coordinate = 400                                                      # cube starting position
y_coordinate = 300
x_new_coordinate = random.randint(50, 750)                              # 13.b random generate position for new cube
y_new_coordinate = random.randint(50, 550)

background_image = pygame.image.load("snake_background.jpg")            # 12. create var for image

timing = 0                                                              # 10.a create var for timing

font = pygame.font.SysFont("Arial Narrow", 48)                          # 10.c create font
font_text = font.render("Time: ", True, (0, 255, 0))
result_text = font.render("Result: ", True, (0, 255, 0))
new_game_text = font.render("Start New Game..", True, (204, 255, 255))
save_time_text = font.render("Time: ", True, (204, 255, 255))
record_time = font.render("Record: ", True, (204, 255, 255))

result = 0                                                              # 15.a create var for result

while not done:                                                         # 3. for loop listen all activity in window
    for event in pygame.event.get():                                    # window are able to click X
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()                                  # 4. create variable for pressed button
    if pressed[pygame.K_UP] and y_coordinate > 0:                       # 9.a y_coordinate not bigger than 0.
        y_coordinate -= 5                                               # if moving up, need to decrease the amount of Y axel
    if pressed[pygame.K_DOWN] and y_coordinate < 600 - 30:              # 9.b down - less sze with cube pixel size
        y_coordinate += 5                                               # when moving down, increase the value of Y axel
    if pressed[pygame.K_LEFT] and x_coordinate > 0:
        x_coordinate -= 5
    if pressed[pygame.K_RIGHT] and x_coordinate < 800 - 30:
        x_coordinate += 5

    screen.blit(background_image, [0, 0])                               # 7. upload with black box previous area + # 12. fill with background

    if result < 5:                                                         # 17. running only if result < then 15 cube
        original_rect = pygame.draw.rect(screen, (0, 128, 255), (x_coordinate, y_coordinate, 30, 30))           # 5. draw blue rectangle
        new_rect = pygame.draw.rect(screen, (0, 255, 0), (x_new_coordinate, y_new_coordinate, 30, 30))          # 13.c draw new cube

        if original_rect.colliderect(new_rect):                             # 14. if collided orig cube with new,
            result += 1                                                     # 15.b if collide happen, increase result var
            x_new_coordinate = random.randint(50, 750)                      # 14. get immediate new coordinates
            y_new_coordinate = random.randint(50, 550)
            pygame.display.update(new_rect)                                 # 14. and refresh display

        timing += 1 / 60                                                    # 10.b 1/60 bc loop running 60x per min
        timing_text = font.render(str(int(timing)), True, (255, 255, 0))    # 10.d writing out into a variable the text
        screen.blit(timing_text, (770 - timing_text.get_width(), 0))        # 11. write out timing and right
        screen.blit(result_text, (10, 0))                                   # 15.c draw res text
        screen.blit(font_text, (645, 0))

        result_text2 = font.render(str(result), True, (255, 255, 0))          # 16.a create var for result text
        screen.blit(result_text2, (result_text.get_width() + 10, 0))        # 16.b print result

    else:
        screen.blit(new_game_text, (300, 250))
        screen.blit(save_time_text, (300, 400))
        save_time_text2 = font.render(str(int(timing)), True, (255, 255, 0))
        screen.blit(save_time_text2, (300 + save_time_text.get_width() + 10, 400))
        screen.blit(record_time, (300, 450))

    pygame.display.flip()                                               # 6. refresh display
    pygame.time.Clock().tick(60)                                        # 8. slowing with 60 fps, while loop running 60x per minute