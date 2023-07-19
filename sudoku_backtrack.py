import copy
import sys

import numpy as np
import pygame as p
import pygame.display

p.init()


WIDTH, HEIGHT = 900, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = p.time.Clock()

class Board():
    def __init__(self, pygame, screen):
        self.board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
                      [5, 2, 0, 0, 0, 0, 0, 0, 0],
                      [0, 8, 7, 0, 0, 0, 0, 3, 1],
                      [0, 0, 3, 0, 1, 0, 0, 8, 0],
                      [9, 0, 0, 8, 6, 3, 0, 0, 5],
                      [0, 5, 0, 0, 9, 0, 6, 0, 0],
                      [1, 3, 0, 0, 0, 0, 2, 5, 0],
                      [0, 0, 0, 0, 0, 0, 0, 7, 4],
                      [0, 0, 5, 2, 0, 6, 3, 0, 0]]
        self.pygame = pygame
        self.screen = screen
        self.sq_color = self.pygame.Color("White")
        self.sq_size = 95
        self.border_size = 5

        self.number_font = self.pygame.font.SysFont('Times New Roman', 75)
        self.move_queue = []
        self.getSolvedBoard()



    def draw_board(self):
        x, y = 0, 0
        for m in range(len(self.board)):
            for n in range(len(self.board[0])):
                self.pygame.draw.rect(self.screen, self.sq_color, (x, y, self.sq_size, self.sq_size))
                self.pygame.draw.rect(self.screen, self.border_size, (x, y, self.sq_size, self.sq_size), self.border_size)
                self.drawNumber(m, n)
                x += (self.sq_size + self.border_size)
            x = 0
            y += (self.sq_size + self.border_size)


    def drawNumber(self, m, n):
        number = str(self.board[m][n])
        text = self.number_font.render(number, False, (0, 0, 0))
        self.screen.blit(text, self.GetNumberLocation(m,n))


    def GetNumberLocation(self, m, n):
        new_m = m * (self.sq_size + self.border_size) + int((self.sq_size/8))
        new_n = n * (self.sq_size + self.border_size) + int((self.sq_size/3))
        return (new_n, new_m)

    def isSafe(self, board, m, n, insert_num):
        for i in range(9):  # check row
            if board[i][n] == insert_num:
                return False

        for i in range(9):  # check column
            if board[m][i] == insert_num:
                return False

        start_row = m - (m % 3)
        start_col = n - (n % 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == insert_num:
                    return False
        return True

    def solve(self, board, m, n):
        if m == 8 and n == 9:
            return True

        if n == 9:
            m += 1
            n = 0

        if board[m][n] != 0:
            return self.solve(board, m, n + 1)

        for i in range(1, 10):
            if self.isSafe(board, m, n, i):
                board[m][n] = i
                self.move_queue.append([(m,n), i])
                if self.solve(board, m, n + 1):
                    return True
                self.move_queue.append([(m, n), 0])
            board[m][n] = 0
        return False


    def getSolvedBoard(self):
        board = copy.deepcopy(self.board)
        self.solve(board, 0, 0)


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

    board.draw_board()
    board.doSolveStep()
    clock.tick(15)
    p.display.flip()


