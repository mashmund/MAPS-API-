import sys
import requests
import pygame
import os

coords = [37.629331, 55.816546]
spn = [0.005, 0.005]
geocoder = "http://static-maps.yandex.ru/1.x/"
params = {
    'll': str(coords[0]) + ',' + str(coords[1]),
    'spn': str(spn[0]) + ',' + str(spn[1]),
    'l': 'map'}
response = requests.get(geocoder, params=params)
with open('map.png', 'wb') as f:
    f.write(response.content)
im = pygame.image.load('map.png')
os.remove('map.png')
pygame.init()
screen = pygame.display.set_mode((600, 400))
running = True
now = 0
while running:
    screen.blit(im, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()