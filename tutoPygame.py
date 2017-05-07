"""
Memory Simulator
04 - TP Final
3253.1 - Conception OS
RODRIGUES L. Daniel & RUEDIN Cyril
mai 2017
"""
import pygame
import sys
import os

from enum import Enum
from pygame.locals import *


# ------------------------------------------------------------
# Enum des type de case memoire
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

    def remove_text(self):
        pass


# ------------------------------------------------------------
# Affichage initial
# ------------------------------------------------------------
def display_interface(pygame, window, font):
    """Initialise l'affichage de la fenêtre"""
    global COLORS

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
        memory.append(MemoryCase(pygame.Rect(500, 30 + i * 50, 200, 50), COLORS[type.value], type))

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
    TextCode("* Stack Area", TypeMemory.STACK, COLORS[TypeMemory.STACK.value]).display_text(window, font, 500, 535)
    TextCode("* Heap Area", TypeMemory.STACK, COLORS[TypeMemory.HEAP.value]).display_text(window, font, 500, 555)
    TextCode("CODE", None, Color(236, 240, 241, 255)).display_text(window, font, 50, 10)
    TextCode("MEMORY", None, Color(236, 240, 241, 255)).display_text(window, font, 500, 10)
    TextCode("Press ESPACE to execute one line", None, Color(236, 240, 241, 255)).display_text(window, font, 50, 535)
    TextCode("Press r to restart the application", None, Color(236, 240, 241, 255)).display_text(window, font, 50, 555)
    TextCode("Press ESC to quit the application", None, Color(236, 240, 241, 255)).display_text(window, font, 50, 575)

    i = 0
    for c in CODE:
        c.display_text(window, font, 85, 85 + i * 45)
        i += 1

    pygame.display.update()


# ------------------------------------------------------------
# Action de la Touche Espace
# ------------------------------------------------------------
def step(pygame, window, font):
    """Fonction appelee a chaque fois que l'utilisateur appuie sur ESPACE"""
    global CODE_POINT
    global CODE_PTR
    global STACK_PTR
    global STACK_MEM_PTR
    global HEAP_PTR
    global HEAP_MEM_PTR
    CODE_POINT.move_ip(0, 45)
    pygame.draw.rect(window, Color(231, 76, 60, 255), CODE_POINT, 0)
    if CODE[CODE_PTR].type is TypeMemory.STACK:
        STACK_ACTIONS[STACK_PTR][1].display_text(window, font, 545, 45 + STACK_MEM_PTR * 50)
        tmp_stack = STACK_ACTIONS[STACK_PTR]
        STACK_PTR += 1
        while STACK_PTR < len(STACK_ACTIONS) and STACK_ACTIONS[STACK_PTR][0] == tmp_stack[0]:
            STACK_MEM_PTR += STACK_ACTIONS[STACK_PTR][2]
            STACK_ACTIONS[STACK_PTR][1].display_text(window, font, 545, 45 + STACK_MEM_PTR * 50)
            STACK_PTR += 1
    elif CODE[CODE_PTR].type is TypeMemory.HEAP:
        HEAP_ACTIONS[HEAP_PTR][1].display_text(window, font, 545, 445 - HEAP_MEM_PTR * 50)
        tmp_heap = HEAP_ACTIONS[HEAP_PTR]
        HEAP_PTR += 1
        while HEAP_PTR < len(HEAP_ACTIONS) and HEAP_ACTIONS[HEAP_PTR][0] == tmp_heap[0]:
            HEAP_MEM_PTR += HEAP_ACTIONS[HEAP_PTR][2]
            HEAP_ACTIONS[HEAP_PTR][1].display_text(window, font, 545, 445 - HEAP_MEM_PTR * 50)
            HEAP_PTR += 1
    CODE_PTR += 1


# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------
def main():
    """Fonction principale
        - Initialisation de la fenêtre
        - Boucle d'animation
    """
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

    CODE_PTR = 0

    # Boucle d'animation
    animation = True
    while animation:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE and CODE_PTR < len(CODE):
                    step(pygame, window, font)
                if event.key == K_r:
                    restart_program()
                if event.key == K_ESCAPE:
                    animation = False
            if event.type == QUIT:
                animation = False

        pygame.display.update()

# ------------------------------------------------------------
# Variables globales
# ------------------------------------------------------------
# Couleurs
COLORS = [Color(241, 196, 15, 255),
          Color(230, 126, 34, 255),
          Color(52, 152, 219, 255)]

# Code à afficher
CODE = [TextCode('char c = \'a\';', TypeMemory.STACK),
        TextCode('// User object is 3 bytes', None),
        TextCode('User user = new User();', TypeMemory.HEAP),
        TextCode('c = \'b\';', TypeMemory.STACK),
        TextCode('delete user;', TypeMemory.HEAP),
        TextCode('char[] cs = malloc(2*sizeof(char));', TypeMemory.HEAP),
        TextCode('strcpy(cs, "LE");', TypeMemory.HEAP),
        TextCode('// free(cs);', None)]

# 1e element :
#   Numero groupe (permet de regrouper les commandes a "executer" en meme temps)
# 2e element :
#   Texte a afficher dans les cases memoire
# 3e element :
#   1  => Ajout
#   -1 => Suppression

STACK_ACTIONS = [(1, TextCode('c = a', None), 1),
                 (2, TextCode('c = a', None, COLORS[TypeMemory.STACK.value]), -1),
                 (2, TextCode('c = b', None), 1)]
HEAP_ACTIONS = [(1, TextCode('user', None), 1),
                (1, TextCode('user', None), 1),
                (1, TextCode('user', None), 1),
                (2, TextCode('user', None, COLORS[TypeMemory.HEAP.value]), -1),
                (2, TextCode('user', None, COLORS[TypeMemory.HEAP.value]), -1),
                (2, TextCode('user', None, COLORS[TypeMemory.HEAP.value]), -1),
                (3, TextCode('c = ', None), 1),
                (3, TextCode('c = ', None), 1),
                (4, TextCode('c = ', None, COLORS[TypeMemory.HEAP.value]), -1),
                (4, TextCode('c = ', None, COLORS[TypeMemory.HEAP.value]), -1),
                (4, TextCode('c = L', None), 1),
                (4, TextCode('c = E', None), 1)]

# Pointeurs
STACK_PTR = 0
STACK_MEM_PTR = 0
HEAP_PTR = 0
HEAP_MEM_PTR = 0
CODE_PTR = 0

# Point d'arret dans le code
CODE_POINT = None


def restart_program():
    """Redemarrer le programme courant"""
    python = sys.executable
    os.execl(python, python, * sys.argv)

# ------------------------------------------------------------
# POINT D'ENTREE
# ------------------------------------------------------------
if __name__ == '__main__':
    main()
