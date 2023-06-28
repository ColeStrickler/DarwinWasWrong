from genetic_algo import Darwin
import pygame as p


BOARD_WIDTH = 1000
BOARD_HEIGHT = 800


p.init()
screen = p.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
clock = p.time.Clock()
d = Darwin(BOARD_WIDTH, BOARD_HEIGHT, 0.15, p, screen, 1000, 150, 50, trapper_count=10)


while True:
    screen.fill(p.Color("Gray"))



    for e in p.event.get():
        if e.type == p.QUIT:
            break



    d.runCycle()
    clock.tick(250)
    p.display.flip()
