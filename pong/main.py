import pygame, sys

pygame.init()
display = pygame.display
screen_width, screen_height = 600, 400
display.set_caption("Game")
screen = display.set_mode((screen_width, screen_height))

load_image = pygame.image.load
player_image = load_image('player.png')
player_image = pygame.transform.scale(player_image, (80, 10))
player_image.set_colorkey((255, 255, 255))
player = player_image.get_rect()
tło_image = load_image('tło.png')
tło_image = pygame.transform.scale(tło_image, (screen_width, screen_height))
ball_image = load_image('ball.png')
ball_image = pygame.transform.scale(ball_image, (40, 40))
ball_image.set_colorkey((255, 255, 255))
odbice_sound = pygame.mixer.Sound('odbicie.wav')
pygame.mixer.Sound.set_volume(odbice_sound,0.1)
music = pygame.mixer.music.load('music.wav')
pygame.mixer.music.set_volume(0.03)
pygame.mixer.music.play(-1)
display.set_icon(ball_image)
ball = ball_image.get_rect()
score = -1
score_text = pygame.font.SysFont(None, 25).render(f'score:{score}',True,(255,255,255))
preskey_text = pygame.font.SysFont(None, 40).render(f'Press any key',True,(0,0,0))

clock = pygame.time.Clock()
x_speed,y_speed = 5,5
score = 0
def game():
    ball.x = 200
    ball.y = 0
    score = 0

    game_run = True
    x_speed, y_speed = 5, 5

    while game_run:

        score_text = pygame.font.SysFont(None, 100).render(f'{score}', True, (0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ball.x += x_speed
        ball.y += y_speed
        if ball.bottom >= screen_height:
            game_run = False
            score = 0
        if ball.top <= 0 :
            pygame.mixer.Sound.play(odbice_sound)
            y_speed *= -1
        if ball.left <= 0 or ball.right >= screen_width:
            pygame.mixer.Sound.play(odbice_sound)
            x_speed *= - 1
        if ball.colliderect(player):
            pygame.mixer.Sound.play(odbice_sound)
            score += 1

            y_speed *= -1
        screen.blit(tło_image, (0, 0))
        screen.blit(score_text, (275, 180))
        # drawing ball

        screen.blit(ball_image, (ball))

        # drawindg player

        player.y = 350
        player.x = pygame.mouse.get_pos()[0]
        screen.blit(player_image, (player.x,player.y))
        #bliting text

        display.update()
        clock.tick(60)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN :
            game_run = True
            game()
    
    ball.x += x_speed
    ball.y += y_speed
    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(odbice_sound)
        y_speed *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        pygame.mixer.Sound.play(odbice_sound)
        x_speed *= - 1
    screen.blit(tło_image,(0,0))
    screen.blit(preskey_text,(200,200))
    screen.blit(ball_image,ball)
    clock.tick(60)
    display.update()




