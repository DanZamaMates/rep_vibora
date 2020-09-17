"""
Intituto Tecnologico de Estudios Superiores de Monterrey
Equipo "Default":
Daniel de Zamacona Madero - A01570576
Elmer Osiel Avila Vargas - A00826359
El programa despliega un juego de snake con variantes de colores y movimientos de la comida
Fecha de Modificacion: 16/9/2020
"""

from turtle import *
from random import randrange
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


'''
Se cambia la direccion de la serpiente de acorde a la entrada del usuario
Entrada: (x,y) posicion vectorial que da el usuario
Salida: ninguna
'''
def change(x, y):
    aim.x = x
    aim.y = y

'''
Regresa que los parametros esten dentro de los limites de la pantalla del juego
Entrada: posicion vectorial de un elemento
Salida: valor verdadero o falso
'''

def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190


'''
Se genera un valor de decision que se asigna color ya sea de la serpiente o la comida, y se asegura que no sean iguales entre ellos
'''

colores =['yellow','violet','blue','purple','orange']
rand_colores = [random.choice(colores)]

rand_colores_comida = [random.choice(colores)]

while rand_colores_comida == rand_colores:
    rand_colores_comida = [random.choice(colores)]

def move():
    head = snake[-1].copy()
    head.move(aim)

   
    
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, rand_colores)

    square(food.x, food.y, 9, rand_colores_comida)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()