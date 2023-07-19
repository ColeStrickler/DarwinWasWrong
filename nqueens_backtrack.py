import copy
import sys

import numpy as np
import pygame as p
import pygame.display

p.init()


WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = p.time.Clock()


def isSafe(board, m, n):
    conflicts = 0
    for i in range(8):
        if i != n and board[m][i] == 1:
            return False

    for i in range(8):
        if i != m and board[i][n] == 1:
            return False

    dir = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for d in dir:
        y = m + d[1]
        x = n + d[0]
        while y < 8 and x < 8 and y >= 0 and x >= 0:
            if board[y][x] == 1:
                return False
            y += d[1]
            x += d[0]

    return True

def validBoard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                if not isSafe(board, i, j):
                    return False
    return True








class Board():
    def __init__(self, pygame, screen):
        self.board = [[0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0]]
        self.pygame = pygame
        self.screen = screen
        self.c1 = (227, 213, 179)
        self.c2 = (194, 147, 29)
        self.sq_size = 100
        self.queenImage = p.transform.scale(p.image.load("assets/wQ.png"), (self.sq_size, self.sq_size))
        self.move_queue = []
        self.getSolvedBoard()


    def drawBoard(self):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    p.draw.rect(self.screen, self.c1, p.Rect(i * self.sq_size, j * self.sq_size, self.sq_size, self.sq_size))
                else:
                    p.draw.rect(self.screen, self.c2, p.Rect(i * self.sq_size, j * self.sq_size, self.sq_size, self.sq_size))
                if self.board[j][i] == 1:
                    rect = p.Rect(i * self.sq_size, j * self.sq_size,self.sq_size, self.sq_size)
                    self.screen.blit(self.queenImage, rect)



    def getSolvedBoard(self):
        board = copy.deepcopy(self.board)
        self.solve(board, 0)

    def isSafe(self, board, m, n):
        conflicts = 0
        for i in range(8):
            if i != n and board[m][i] == 1:
                return False

        for i in range(8):
            if i != m and board[i][n] == 1:
                return False

        dir = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for d in dir:
            y = m + d[1]
            x = n + d[0]
            while y < 8 and x < 8 and y >= 0 and x >= 0:
                if board[y][x] == 1:
                    return False
                y += d[1]
                x += d[0]

        return True



    def solve(self, board, n):
        if n == 8:
            return True

        for m in range(len(board)):
            if isSafe(board, m, n):
                board[m][n] = 1
                self.move_queue.append([(m, n), 1])
                if self.solve(board, n + 1):
                    return True
                self.move_queue.append([(m, n), 0])
            board[m][n] = 0
        return False

    def isSafe(self, board, m, n):
        conflicts = 0
        for i in range(8):
            if i != n and board[m][i] == 1:
                return False

        for i in range(8):
            if i != m and board[i][n] == 1:
                return False

        dir = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for d in dir:
            y = m + d[1]
            x = n + d[0]
            while y < 8 and x < 8 and y >= 0 and x >= 0:
                if board[y][x] == 1:
                    return False
                y += d[1]
                x += d[0]

        return True

    def doSolveStep(self):
        if len(self.move_queue):
            step = self.move_queue.pop(0)
            m,n = step[0]
            num = step[1]
            self.board[m][n] = num






board = Board(p, screen)
while True:

    for event in p.event.get():
        if event.type == p.QUIT:
            sys.exit()

    board.drawBoard()
    board.doSolveStep()
    clock.tick(5)
    p.display.flip()


