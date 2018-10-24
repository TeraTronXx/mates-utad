import pygame # necesito instalarlo: desde una linea de comandos -> pip install pygame
import time
from punto import Point
from punto import Poligono

"""
a = Point (100, 200)
b = Point (500, 200)
c = Point (200, 300)
d = Point (200, 400)
e = Point (200, 100)
f = Point (300, 200)
g = Point (400, 100)
h = Point (150, 350)

p=Poligono()
p.anadir(a)
p.anadir(b)
p.anadir(c)
p.anadir(d)
p.anadir(e)
p.anadir(f)
p.anadir(g)
p.anadir(h)
"""
"""
p1 = Point(500,200)
p2 = Point(200,100)
p3 = Point(000,300)
p4 = Point(400,400)
p5 = Point(300,700)
p6 = Point(700,600)
p7 = Point(1000,400)
p8 = Point(700,200)
p9 = Point(1000,300)
p10 = Point(800,300)
p11 = Point(900,100)
p12 = Point(800,000)
p13 = Point(1000,200)

p=Poligono()
p.anadir(p1)
p.anadir(p2)
p.anadir(p3)
p.anadir(p4)
p.anadir(p5)
p.anadir(p6)
p.anadir(p7)
p.anadir(p8)
p.anadir(p9)
p.anadir(p10)
p.anadir(p11)
p.anadir(p12)
p.anadir(p13)
"""

p1 = Point(400,300)
p2 = Point(200,100)
p3 = Point(100,500)
p4 = Point(500,400)
p5 = Point(800,600)
p6 = Point(000,300)
p7 = Point(700,200)
p8 = Point(800,500)

p=Poligono()
p.anadir(p1)
p.anadir(p2)
p.anadir(p3)
p.anadir(p4)
p.anadir(p5)
p.anadir(p6)
p.anadir(p7)
p.anadir(p8)


polig = []

fin = p.total()
#print(fin)
longitud = len(fin)
pint = p.pintar(fin)
print(pint)
pygame.init()


for i in pint:
    i= [i.x, i.y]
    polig.append(i)

size = [1500, 1500]
screen = pygame.display.set_mode(size)

GREEN = (  0, 255,   0 )
RED = (  255, 0,   0 )
PURPLE = ( 208, 157, 255 )



for i in range(0,len(pint)):
    if (i==((len(pint))-1)):#con lines en lugar de line, puedo meter el poligono completo.
        pygame.draw.line(screen, PURPLE, [pint[i-1].x, pint[i-1].y], [pint[i].x,pint[i].y], 1)
        pygame.display.flip()
        time.sleep(1)
        pygame.draw.line(screen, PURPLE, [pint[i].x, pint[i].y], [pint[0].x,pint[0].y], 1)
        pygame.display.flip()
        time.sleep(1)
    else:
        pygame.draw.line(screen, PURPLE, [pint[i-1].x, pint[i-1].y], [pint[i].x,pint[i].y], 1)
        pygame.display.flip()
        time.sleep(1)
    i=i+1


pygame.draw.lines(screen, PURPLE, True, polig, 1)


pygame.display.flip()

time.sleep(1.5) #necesario para no cerrar la pantalla inmediatamente
pygame.quit()
