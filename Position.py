import pygame
import string
import keyboard
import time
import pyautogui

pygame.init()
pygame.font.init()

string = 'feitoria'

size = 500,300
screen = pygame.display.set_mode(size)

myfont = pygame.font.SysFont('Arial', 35)
black = 0,0,0
number = ''
while True:

    position = str(pyautogui.position())

    screen.fill((black))
    textsurface = myfont.render(position, False, (255, 255, 255))
        
    screen.blit(textsurface,(0,0))
    pygame.display.flip()



    if keyboard.is_pressed('esc'):
        break

