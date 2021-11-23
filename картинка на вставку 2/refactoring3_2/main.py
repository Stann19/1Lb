import pygame
from pygame.draw import *

pygame.init()
FPS = 30
large = 1258
height = 500
screen = pygame.display.set_mode((large, height))

def background(screen, x, y, large, height, grass_color, sky_color):
    '''
    color-цвета прямоугольников
    large-ширина
    height-высота прямоугольников
    x, y-координаты верхнего левого угла изображения
    '''
    grass(screen, x, y+height/2, large, height/2, grass_color)
    sky(screen, x, y, large, height/2, sky_color)

def grass(screen, x, y, large, height, color):
    '''
     рисует траву
     высотой height
     шириной large
     x,y-координаты верхнего левого угла изображения
    '''
    rect(screen, color, (x, y, large, height))

def sky(screen, x, y, large, height, color):
    '''
    рисует небо
    высотой height
    шириной large
    x,y-координаты верхнего левого угла изображения
    '''
    rect(screen, color, (x, y, large, height))

def boy(screen, head_color, body_color, arm_color, leg_color, h1, h2, r):
    '''
    рисует симметрично мальчиков
    высота прямоугольника, вписанного в эллипс h2
    от верхнего края прямоугольника до верхней точки руки h1
    радиус головы r
    '''
    a = (-1) ** boy_number
    b = boy_number * large
    boy_body(screen, body_color, a, b, h1, h2)
    boy_head(screen, head_color, a, b, h1, r)
    boy_arm(screen, arm_color, a, b, h1, h2)
    boy_leg(screen, leg_color, a, b, h1, h2)

def boy_body(screen, body_color, a, b, h1, h2):
    '''
    функция, отвечает за рисование туловища
    a * 200 + b,h1 - 20-координаты верхней левой вершины прямоугольника
    a * 100, h2-длина сторон прямоугольника
    '''
    ellipse(screen, body_color, (a * 200 + b, h1 - 20, a * 100, h2))

def boy_head(screen, head_color, a, b, h1, r):
    '''
    функция, отвечает за рисование головы
    a * 250 + b, h1 - 50-координаты центра окружности
    r-ее радиус
    '''
    circle(screen, head_color, (a * 250 + b, h1 - 50), r)

def boy_arm(screen, arm_color, a, b, h1, h2):
    '''
    функция, отвечает за рисование рук
    a,b,h1,h2-отвечают за положение точек, через которые проходят руки
    '''
    line(screen, arm_color, (a * 220 + b, h1), (a * 130 + b, h2 + 60))
    line(screen, arm_color, (a * 280 + b, h1), (a * 370 + b, h2 + 60))

def boy_leg(screen, leg_color, a, b, h1, h2):
    '''
    функция отвечает за рисование ног
    a,b,h1,h2-отвечает за положение, точек через которые проходят ноги
    '''
    lines(screen, (0, 0, 0), False, [(a * 220 + b, h2 + 130), (a * 180 + b, h2 + 240), (a * 150 + b, h2 + 245)])
    lines(screen, (0, 0, 0), False, [(a * 280 + b, h2 + 125), (a * 300 + b, h2 + 240), (a * 330 + b, h2 + 240)])

def girl(screen, head_color, body_color, arm_color, leg_color, h1, h2, r):
    '''
    рисует симметрично мальчиков
    высота прямоугольника, вписанного в эллипс h2
    от верхнего края прямоугольника до верхней точки руки h1
    радиус головы r
    '''
    a = (-1) ** girl_number
    b = girl_number * large
    girl_body(screen, body_color, a, b, h1, h2)
    girl_head(screen, head_color, a, b, h1, r)
    girl_arm(screen, arm_color, a, b, h1, h2)
    girl_leg(screen, leg_color, a, b, h1, h2)

def girl_body(screen, body_color, a, b, h1, h2):
    '''
    функция, отвечает за рисование туловища
    (a * 500 + b, h1 - 20), (a * 430 + b, h2), (a * 570 + b, h2)-координаты вершин треугольника
    '''
    polygon(screen, body_color, [(a * 500 + b, h1 - 20), (a * 430 + b, h2), (a * 570 + b, h2)])

def girl_head(screen, head_color, a, b, h1, r):
    '''
    функция, отвечает за рисование головы
    a * 250 + b, h1 - 50-координаты центра окружности
    r-ее радиус
    '''
    circle(screen, head_color, (a * 500 + b, h1 - 30), r)

def girl_arm(screen, arm_color, a, b, h1, h2):
    '''
    функция, отвечает за рисование рук
    a,b,h1,h2-отвечают за положение точек, через которые проходят руки
    '''
    line(screen, arm_color, (a * 490 + b, h1 + 15), (a * 370 + b, h1 + 110))
    lines(screen, arm_color, False, [(a * 510 + b, h1 + 15), (a * 570 + b, h1 + 45), (a * 630 + b, h1 + 20)])

def girl_leg(screen, leg_color, a, b, h1, h2):
    '''
    функция отвечает за рисование ног
    a,b,h1,h2-отвечает за положение, точек через которые проходят ноги
    '''
    lines(screen, leg_color, False, [(a * 480 + b, h2), (a * 480 + b, h2 + 80), (a * 450 + b, h2 + 85)])
    lines(screen, leg_color, False, [(a * 520 + b, h2), (a * 520 + b, h2 + 80), (a * 550 + b, h2 + 80)])

def balloon(screen, line1_color, heart_color, x1, y1):
    '''
    рисует надувной шарик с ниткой
    heart_color, line_heart- их цвета соответственно
    x1, y1- координаты для нитки и шара
    '''
    line1(screen, line1_color, x1, y1)
    heart(screen, heart_color, x1, y1)

def line1(screen, line1_color, x1, y1):
    '''
    функция рисует нить шара
    x1,y1-координаты нижнего конца нити
    x1+40, y1+105-координаты верхнего конца нити
    '''
    line(screen, line1_color, (x1, y1), (x1 + 40, y1 + 105))

def heart(screen, heart_color, x1, y1):
    '''
    функция рисует воздушный шар ввиде сердечка
    x1,y1-координаты точки, соединяющий шарик и нитку
    '''
    polygon(screen, heart_color, [(x1, y1), (x1 - 55, y1 - 35), (x1 - 10, y1 - 70)])
    circle(screen, heart_color, (x1 - 30, y1 - 75), 20)
    circle(screen, heart_color, (x1 - 50, y1 - 55), 20)

def icecream1(screen, y1, horn_color, red_color, brown_color, white_color):
    '''
    рисует мороженое
    horn_color-цвет рожка
    red_color,brown_color,white_color-цвет шариков мороженого
    x2,y2-координата конца руки держащего мороженое
    '''
    horn1(screen, y1, horn_color, red_color, brown_color, white_color)
    ball1(screen, y1, horn_color, red_color, brown_color, white_color)


def horn1(screen, y1, horn_color, red_color, brown_color, white_color):
    '''
    функция рисует стаканчик от мороженого
    '''
    polygon(screen, horn_color, [(large-140, y1), (large-85, y1 - 35), (large-130, y1 - 70)])


def ball1(screen, y1, horn_color, red_color, brown_color, white_color):
    '''
    функция рисует шарики мороженогое
    '''
    circle(screen, white_color, (large-90, y1 - 85), 20)
    circle(screen, red_color, (large-110, y1 - 75), 20)
    circle(screen, brown_color, [large - 90, y1 - 55], 20)

def icecream2(screen, x1, y1, line2_color, horn_color, red_color, brown_color, white_color):
    '''
    рисует центральное мороженное и часть руки
    red_color, brown_color, white_color-цвет шариков мороженного
    line2_color-цвет части руки
    horn_color-цвет рожка мороженного
    x1, y1-координаты конца части руки, которое держит мороженное
    '''
    line2(screen, x1, y1, line2_color, horn_color, red_color, brown_color, white_color)
    horn2(screen, x1, y1, line2_color, horn_color, red_color, brown_color, white_color)
    ball2(screen, x1, y1, line2_color, horn_color, red_color, brown_color, white_color)

def line2(screen, x1, y1, line2_color, horn_color, red_color, brown_color, white_color):
    '''
    функция рисует часть руки
    '''
    line(screen, line2_color, (x1, y1), (x1 - 10, y1+80))

def horn2(screen, x1, y1, line2_color, horn_color, red_color, brown_color, white_color):
    '''
    функция рисует рожок мороженного
    '''
    polygon(screen, horn_color, [(x1, y1), (x1+20, y1-60), (x1-20, y1-60)])

def ball2(screen, x1, y1, line2_color, horn_color, red_color, brown_color, white_color):
    '''
    функция рисует шарики мороженного
    '''
    circle(screen, red_color, (x1 + 10, y1 - 75), 20)
    circle(screen, brown_color, (x1-10, y1 - 75), 20)
    circle(screen, white_color, (x1, y1 - 90), 20)

background(screen, 0, 0, large, height, (60, 179, 113), (135, 206, 235))

for boy_number in range(2):
  boy(screen, (255, 228, 196), (119, 136, 153), (0, 0, 0), (0, 0, 0), 170, 220, 40)

for girl_number in range(2):
  girl(screen, (255, 228, 196), (255, 20, 147), (0, 0, 0), (0, 0, 0), 170, 370, 40)

balloon(screen, (0, 0, 0), (255, 0, 0), 100, 175)

icecream1(screen, 290, (255, 165, 0), (255, 0, 0), (160, 82, 45), (255, 245, 238))

icecream2(screen, 640, 110, (0, 0, 0), (255, 165, 0), (255, 0, 0), (160, 82, 45), (255, 245, 238))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()




