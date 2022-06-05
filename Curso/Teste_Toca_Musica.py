
import pygame
from time import sleep
#import os
#print(os.getcwd())

pygame.init()
pygame.mixer.music.load('house_lo.mp3')
pygame.mixer.music.play(loops=2)
pygame.event.wait()
sleep(360)
#input()