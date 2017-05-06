import pygame
import sys

from pygame.locals import *


class MemoryCase:

    border_color = Color(255, 255, 255, 255)

    def __init__(self, rect, color, text):
        self.rect = rect
        self.color = color
        self.text = text

    def draw(self, window):
        window.fill(m.color, m.rect)
        pygame.draw.rect(window, self.border_color, self.rect, 3)

    def display_text(self, window, font, offset):
        window.blit(font.render(m.text, 1, (0, 0, 0)), (390, 120 + offset * 50))

if __name__ == '__main__':
    pygame.init()

    # Ouverture de la fenêtre Pygame
    window = pygame.display.set_mode((800, 600))
    colors = [Color(0, 255, 0, 255), Color(255, 0, 0, 255), Color(0, 0, 255, 255)]
    heap = []
    stack = []
    other = []

    for i in range(0, 4):
        heap.append(MemoryCase(pygame.Rect(300, 100 + i * 50, 200, 50), colors[0], str(i)))
    for i in range(4, 8):
        stack.append(MemoryCase(pygame.Rect(300, 100 + i * 50, 200, 50), colors[1], str(i)))

    other.append(MemoryCase(pygame.Rect(300, 100 + 8 * 50, 200, 50), colors[2], "BSS"))
    other.append(MemoryCase(pygame.Rect(300, 100 + 9 * 50, 200, 50), colors[2], "DATA"))
    other.append(MemoryCase(pygame.Rect(300, 100 + 10 * 50, 200, 50), colors[2], "CODE"))

    window.fill((0, 0, 0))

    font = pygame.font.SysFont("monospace", 15)

    memory = heap
    memory.extend(stack)
    memory.extend(other)

    while True:
        i = 0
        for m in memory:
            m.draw(window)
            m.display_text(window, font, i)
            i += 1

        # caseMem.move_ip(a,a)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
