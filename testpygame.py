import pygame

from pygame.locals import *

if __name__ == '__main__':
    pygame.init()

    window = pygame.display.set_mode((800, 600))
    
    caseMem = pygame.Rect(500,200,200,50)

    heap = []
    stack = []

    heap.append(50)
    heap.append(30)
    heap.append(120)

    stack.append(60)
    stack.append(80)
    
    t_mem = 8

    a=1
    b=0

    myfont = pygame.font.SysFont("monospace", 15)

    while True:
        window.fill((0,0,0))
        for i in range(t_mem):
            value = "null"
            color = Color(255,255,255,255)           

            if(i < len(heap)):
                color = Color(0,255,0,255)
                value = str(heap[i])
                
            if(t_mem-i-1 < len(stack)):
                color = Color(0,0,255,255)
                value = str(stack[t_mem-i-1])
            
            rect = pygame.Rect(500,100+i*50,200,50)
            window.fill(color, rect)
            pygame.draw.rect(window, Color(240,240,240, 255),rect, 3)
            window.blit(myfont.render(value, 1, (0,0,0)), (550,125+i*50))
            
        # caseMem.move_ip(a,a)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()