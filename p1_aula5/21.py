import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('nerdcast_702_muro_de_berlim.mp3')
pygame.mixer.music.play()
pygame.event.wait()