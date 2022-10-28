import pygame as pg
import sys
from pygame.draw import *

clock = pg.time.Clock()
frames_per_second = 144

pg.display.init()
screen = pg.display.set_mode((1000, 1000)) # размеры экрана задаем
circ_kor = (500, 500)
circ_r = 300
circle(screen, (200, 200, 0), circ_kor, circ_r, 0)
circle(screen, (0, 0, 0), circ_kor, circ_r, 5)
pg.display.update()
while True:
    clock.tick(frames_per_second)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


#pg.display.flip()
