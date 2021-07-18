"""
 Intrucciones para este ejercicio:
    Deben crear una función glLine(x0, y0, x1, y1) o glLine(v0, v1) que se utilice para dibujar una línea recta de (x0, y0) a (x1, y1)
    Desde el programa principal, utilizar la función de líneas para dibujar 5 polígonos diferentes (10 pts cada uno)
"""
# El que funciona como graficador
from IA import Renderer, V2

width = 880
height = 720

rend = Renderer(width, height)

rend.glColor(0, 0, 0)
rend.glClear()
rend.glColor(1, 1, 1)

# ________________________________________________
#  Comienzan las lineas

# 1.            TRIANGULO 
rend.glLine(V2(100, 300), V2(150, 300))
rend.glLine(V2(100, 300), V2(125, 350))
rend.glLine(V2(125, 350), V2(150, 300))


# 2.       CUADRILATERO IRREGULAR
rend.glLine(V2(200, 300), V2(250, 300))
rend.glLine(V2(200, 350), V2(200, 300))
rend.glLine(V2(250, 300), V2(280, 350))
rend.glLine(V2(200, 350), V2(280, 350))



# 3.            PENTAGONO
rend.glLine(V2(350, 300), V2(400, 300))
rend.glLine(V2(350, 300), V2(335, 335))
rend.glLine(V2(335, 335), V2(370, 365))
rend.glLine(V2(400, 300), V2(410, 335))
rend.glLine(V2(370, 365), V2(410, 335))



# 4.       HEXAGONO IRREGULAR
rend.glLine(V2(500, 300), V2(500, 360))
rend.glLine(V2(500, 360), V2(550, 350))
rend.glLine(V2(500, 300), V2(550, 310))
rend.glLine(V2(550, 310), V2(610, 300))
rend.glLine(V2(610, 300), V2(610, 360))
rend.glLine(V2(610, 360), V2(550, 350))



# 5.            OCTAGONO
rend.glLine(V2(700, 300), V2(750, 300))
rend.glLine(V2(750, 300), V2(770, 330))
rend.glLine(V2(770, 330), V2(770, 360))
rend.glLine(V2(770, 360), V2(750, 390))
rend.glLine(V2(700, 390), V2(750, 390))
rend.glLine(V2(700, 390), V2(680, 360))
rend.glLine(V2(680, 360), V2(680, 330))
rend.glLine(V2(680, 330), V2(700, 300))

#_________________________________________________


rend.glFinished("Ejercicio#2.bmp")