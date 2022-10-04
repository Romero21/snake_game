
import pygame
pygame.init()

BODY_COLOR = pygame.Color(51, 204, 51)
BODY_COLOR_2 = pygame.Color(0, 255, 0)
BACKGROUND_COLOR = pygame.Color(255, 199, 130)
BG_SQUARE_COLOR = [0, 0, 0]
APPLE_COLOR = pygame.Color(255, 0, 0)
APPLE_COLOR_2 = pygame.Color(200, 0, 0)

GAME_RES = (751, 501)
GAME_FPS = 10
GAME_SCORE = 0

SCORE_COLOR = pygame.Color(0, 0, 240)
SCORE_COLOR_2 = pygame.Color(255, 255, 255)
SCORE_FONT = pygame.font.Font('freesansbold.ttf', 26)
SCORE_FONT_2 = pygame.font.Font('freesansbold.ttf', 28)
SCORE_POSITION = (GAME_RES[0]//2, 30)
SCORE_POSITION_2 = (GAME_RES[0]//2, 29)


GAME_OVER_COLOR = pygame.Color(255, 0, 0)
GAME_OVER_FONT = pygame.font.Font('freesansbold.ttf', 36)
GAME_OVER_POSITION = (GAME_RES[0]//2, GAME_RES[1]//2)

SNAKE_SIZE = 25
SNAKE_SIZE_2 = 21