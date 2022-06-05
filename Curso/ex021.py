import pygame
pygame.init()
pygame.mixer.music.load('ex01.mp3')
pygame.mixer.music.play(loops=3)
pygame.event.wait()
input('Pressione [Enter] para parar')