#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame

from Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))

    def run(self, ):

        print('Setup Start')
        print('Setup End')
        print('Loop Start')
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


