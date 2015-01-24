#!/usr/bin/env python
"""
Created by Jan 23, 2015
@author: Cyril
"""

import pygame
import math
import numpy as np
from pygame.locals import *
from sys import exit


screen_size = (640, 480)
background_image = 'sushiplate.jpg'
mouse_image = 'fugu.png'


class DrawObj(object):

    """docstring for DrawObj"""

    def __init__(self):
        super(DrawObj, self).__init__()
        self.color = (0, 0, 0)
        self.width = 2

    def set_color(self, color):
        self.color = color

    def set_width(self, width):
        self.width = width

    def mouse_down(self, pos):
        pass

    def mouse_motion(self, pos):
        pass

    def draw(self, screen):
        pass


class Line(DrawObj):

    """docstring for Line"""

    def __init__(self):
        super(Line, self).__init__()
        self.line = []

    def append_point(self, pos):
        self.line.append(pos)

    def mouse_down(self, pos):
        self.append_point(pos)

    def mouse_motion(self, pos):
        self.append_point(pos)

    def draw(self, screen):
        if len(self.line) > 1:
            pygame.draw.lines(
                screen, self.color, False, self.line, self.width)


class Circle(DrawObj):

    """docstring for Circle"""

    def __init__(self):
        super(Circle, self).__init__()
        self.center = (0, 0)
        self.radius = 0

    def set_center(self, pos):
        self.center = pos

    def set_radius(self, radius):
        self.radius = radius

    def mouse_down(self, pos):
        self.set_center(pos)

    def mouse_motion(self, pos):
        radius = math.sqrt(abs(
            pos[0] - self.center[0]) ** 2 + abs(pos[1] - self.center[1]) ** 2)
        self.set_radius(int(radius))

    def draw(self, screen):
        if self.radius > self.width:
            pygame.draw.circle(
                screen, self.color, self.center, self.radius, self.width)


class Direct_line(DrawObj):

    """docstring for Direct_line"""

    def __init__(self):
        super(Direct_line, self).__init__()
        self.start_pos = (0, 0)
        self.end_pos = (-1, -1)

    def set_start_pos(self, pos):
        self.start_pos = pos

    def set_end_pos(self, pos):
        self.end_pos = pos

    def mouse_down(self, pos):
        self.set_start_pos(pos)

    def mouse_motion(self, pos):
        self.set_end_pos(pos)

    def draw(self, screen):
        if self.end_pos[0] >= 0:
            pygame.draw.line(
                screen, self.color, self.start_pos, self.end_pos, self.width)


class Rect_line(DrawObj):

    """docstring for Rect_line"""

    def __init__(self):
        super(Rect_line, self).__init__()
        self.start_pos = (0, 0)
        self.end_pos = (-1, -1)

    def set_start_pos(self, pos):
        self.start_pos = pos

    def set_end_pos(self, pos):
        self.end_pos = pos

    def mouse_down(self, pos):
        self.set_start_pos(pos)

    def mouse_motion(self, pos):
        end_pos = (pos[0] - self.start_pos[0], pos[1] - self.start_pos[1])
        self.set_end_pos(end_pos)

    def draw(self, screen):
        if abs(self.end_pos[0]) > self.width and abs(self.end_pos[1]) > self.width:
            pygame.draw.rect(
                screen, self.color, (self.start_pos, self.end_pos), self.width)
def main():
    pygame.init()
    screen = pygame.display.set_mode(screen_size, 0, 32)
    pygame.display.set_caption('Draw Something you want...')
    list_draw = []
    draw_tool = Line
    m_draw = draw_tool()
    mouse_flag = False
    current_color = (0, 0, 0)
    current_width = 2

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYUP:
                if event.key == K_c or K_l or K_z:
                    draw_tool = Line
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
                if event.key == K_DELETE:
                    list_draw = []
                if event.key == K_c:
                    draw_tool = Circle
                if event.key == K_l:
                    draw_tool = Direct_line
                if event.key == K_z:
                    draw_tool = Rect_line
                if event.key == K_r:
                    current_color = (255, 0, 0)
                if event.key == K_g:
                    current_color = (0, 255, 0)
                if event.key == K_b:
                    current_color = (0, 0, 255)
                if event.key == K_k:
                    current_color = (0, 0, 0)
                if event.key == K_1:
                    current_width = 1
                if event.key == K_2:
                    current_width = 2
                if event.key == K_3:
                    current_width = 3
                if event.key == K_4:
                    current_width = 4
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_flag = True
                m_draw = draw_tool()
                m_draw.set_color(current_color)
                m_draw.set_width(current_width)
                m_draw.mouse_down(event.pos)
                list_draw.append(m_draw)
            if event.type == MOUSEMOTION:
                if mouse_flag:
                    m_draw.mouse_motion(event.pos)
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_flag = False
        screen.fill((255, 255, 255))
        for draw_obj in list_draw:
            draw_obj.draw(screen)
        pygame.display.update()
if __name__ == '__main__':
	try:
		main()
	except Exception, e:
		print "There is a except:",e