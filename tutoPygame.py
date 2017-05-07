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

    for i in range(0, 10):
        type = TypeMemory.STACK
        if i < 5:
            type = TypeMemory.STACK
        elif i < 9:
            type = TypeMemory.HEAP
        else:
            type = TypeMemory.HEAP_ALLOCATE
        memory.append(MemoryCase(pygame.Rect(500, 30 + i * 50, 200, 50), colors[type.value], type))

    # Affichage initial
    window.fill((44, 62, 80, 255))

    i = 0
    for m in memory:
        m.draw(window)
        i += 1

    # Affichage du rectangle contenant le code
    code_area = pygame.Rect(50, 30, 350, 500)
    window.fill(Color(236, 240, 241, 255), code_area)
    pygame.draw.rect(window, (189, 195, 199, 255), code_area, 3)

    # Quelques textes
    TextCode("Permanent Storage Area", TypeMemory.HEAP_ALLOCATE).display_text(window, font, 501, 495)
    TextCode("* Stack Area", TypeMemory.STACK, colors[TypeMemory.STACK.value]).display_text(window, font, 500, 535)
    TextCode("* Heap Area", TypeMemory.STACK, colors[TypeMemory.HEAP.value]).display_text(window, font, 500, 555)
    TextCode("CODE", None, Color(236, 240, 241, 255)).display_text(window, font, 50, 10)
    TextCode("MEMORY", None, Color(236, 240, 241, 255)).display_text(window, font, 500, 10)
    TextCode("Press ESPACE to execute one line", None, Color(236, 240, 241, 255)).display_text(window, font, 50, 535)

    i = 0
    for c in CODE:
        c.display_text(window, font, 85, 85 + i * 45)
        i += 1

    pygame.display.update()


# ------------------------------------------------------------
# Action de la Touche Espace
# ------------------------------------------------------------
def step(pygame, window):
    global CODE_POINT
    global CODE_PTR
    global STACK_PTR
    global HEAP_STR
    CODE_POINT.move_ip(0, 45)
    pygame.draw.rect(window, Color(231, 76, 60, 255), CODE_POINT, 0)
    CODE_PTR += 1

# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------
def main():
    global CODE_POINT
    global CODE_PTR
    pygame.init()
    pygame.display.set_caption('Memory Simulator')
    # Ouverture de la fenêtre Pygame
    window = pygame.display.set_mode((800, 600))
    font = pygame.font.SysFont("monospace", 15)

    display_interface(pygame, window, font)

    CODE_POINT = pygame.Rect(60, 85, 15, 15)
    window.fill(Color(231, 76, 60, 255), CODE_POINT)

    CODE_PTR = 1

    # Boucle d'animation
    animation = True
    while animation:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE and CODE_PTR < len(CODE):
                    step(pygame, window)
            if event.type == QUIT:
                animation = False

        pygame.display.update()

# ------------------------------------------------------------
# Variables globales
# ------------------------------------------------------------
# Code à afficher
CODE = [TextCode('int i = 10;', TypeMemory.STACK),
        TextCode('User user = new User();', TypeMemory.HEAP),
        TextCode('i = 25 + 6;', TypeMemory.STACK),
        TextCode('delete user;', TypeMemory.HEAP),
        TextCode('char[] c = malloc(2*sizeof(char));', TypeMemory.HEAP),
        TextCode('strcpy(c, "LE");', TypeMemory.HEAP),
        TextCode('free(c);', TypeMemory.HEAP)]

# Pointeurs
STACK_PTR = 0
HEAP_STR = 0
CODE_PTR = 0

# Point d'arret
CODE_POINT = None

# ------------------------------------------------------------
# POINT D'ENTREE
# ------------------------------------------------------------
if __name__ == '__main__':
    main()
