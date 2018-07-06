# Add your Python code here. E.g.
from microbit import *
contador = 1
minimo = 2
top = 5
icons = [Image.HEART,Image.HEART_SMALL]

def mensaje5():
    display.show(icons, delay=150)

def switch_demo(argument):
    dic = {
        1: 'Yo apoyo la lucha docente en Chubut',
        2: 'Luche, luche y que se escuche',
        3: 'MMLPQTP',
        4: 'Unidad de los trabajadores, el que no le gusta, se jode, se jode',
    }
    valor = dic.get(argument)
    display.scroll(valor)

while True:
    if button_a.is_pressed():
        contador = contador + 1
        
    elif button_b.is_pressed():
        contador = contador - 1

    if contador < minimo:
        contador = top
    
    if contador > top:
        contador = 1
    
    if contador == top:
        mensaje5()
    
    if contador < top:
        switch_demo(contador)
 

