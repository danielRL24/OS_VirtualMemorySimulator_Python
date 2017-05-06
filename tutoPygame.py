import pygame
import sys

from enum import Enum
from pygame.locals import *


# ------------------------------------------------------------
# MemoryCase class
# ------------------------------------------------------------
class TypeMemory(Enum):
    STACK = 0
    HEAP = 1
    HEAP_ALLOCATE = 2


# ------------------------------------------------------------
# Classe MemoryCase
# ------------------------------------------------------------
class MemoryCase:

    border_color = (189, 195, 199, 255)

    def __init__(self, rect, color, type):
        self.rect = rect
        self.color = color
        self.type = type

    def draw(self, window):
        window.fill(self.color, self.rect)
        pygame.draw.rect(window, self.border_color, self.rect, 3)


# ------------------------------------------------------------
# Classe TextCode
# ------------------------------------------------------------
class TextCode:
    def __init__(self, text, type, color=(0, 0, 0)):
        self.text = text
        self.color = color
        self.type = type

    def display_text(self, window, font, x, y):
        window.blit(font.render(self.text, 1, self.color), (x, y))


# ------------------------------------------------------------
# Affichage initial
# ------------------------------------------------------------
def display_interface(pygame, window, font):
    colors = [Color(241, 196, 15, 255),
              Color(230, 126, 34, 255),
              Color(52, 152, 219, 255)]

    # Preparation
    memory = []
    code = []

    for i in range(0, 10):
        type = TypeMemory.STACK
        if i < 5:
            type = TypeMemory.STACK
        elif i < 9:
            type = TypeMemory.HEAP
        else:
            type = TypeMemory.HEAP_ALLOCATE
        memory.append(MemoryCase(pygame.Rect(500, 30 + i * 50, 200, 50), colors[type.value], type))

    # Pointeurs
    stack_ptr = 0
    heap_ptr = 0
    code_ptr = 0

    # Affichage initial
    window.fill((44, 62, 80, 255))

    i = 0
    for m in memory:
        m.draw(window)
        i += 1

    i = 0
    for c in code:
        c.display_text(window, font, i)
        i += 1

    # Display Code Area
    code_area = pygame.Rect(50, 30, 300, 500)
    window.fill(Color(236, 240, 241, 255), code_area)
    pygame.draw.rect(window, (189, 195, 199, 255), code_area, 3)

    TextCode("Permanent Storage Area", TypeMemory.HEAP_ALLOCATE).display_text(window, font, 501, 495)
    TextCode("* Stack Area", TypeMemory.STACK, colors[TypeMemory.STACK.value]).display_text(window, font, 500, 535)
    TextCode("* Heap Area", TypeMemory.STACK, colors[TypeMemory.HEAP.value]).display_text(window, font, 500, 555)
    TextCode("CODE", None, Color(236, 240, 241, 255)).display_text(window, font, 50, 10)
    TextCode("MEMORY", None, Color(236, 240, 241, 255)).display_text(window, font, 500, 10)


    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------
def main():
    pygame.init()
    # Ouverture de la fenêtre Pygame
    window = pygame.display.set_mode((800, 600))
    font = pygame.font.SysFont("monospace", 15)

    display_interface(pygame, window, font)

    # Boucle d'animation
    animation = True
    while animation:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    print("Espace")
            if event.type == QUIT:
                animation = False


# ------------------------------------------------------------
# POINT D'ENTREE
# ------------------------------------------------------------
if __name__ == '__main__':
    main()
