import pygame
import time
from pygame.draw import *
from random import randint

'''
"Поймай шарик"
В начале открывается окно игры. На игровом поле создается 3 шарика с рандомными цветами 
и в рандомных местах окна. Аналогично создается 3 кубика. За поподание в шарик- 1 очко, 
за кубик- 2 очка. Если кубик отразился 4 раза и по нему не попали, то на 5 отражение 
он исчезнет. После попадания будет повышаться вероятность увеличения сорости шарика и кубика.
Игра остановится, если нажать на любую клавишу. Счет игрока с его именем заносятся в файл top.txt.
'''
#Считывание имени игрока
print("Введите ваше имя: ")
name = str(input())

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 700))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
j = 0
k = 0

balls_s = []
balls_r = []
b_colours = []
balls_ds = []

class Ball():
  def __init__(self, x, y, r, color):
      self.x = x
      self.y = y
      self.r = r
      self.color = color
  def new_ball(self):
      '''
      функция создает новый шарик с рандомными координатами и цветом
      '''
      global x, y, r, color, j, k
      self.x = randint(100, 1100)
      self.y = randint(100, 600)
      self.r = randint(30, 50)
      self.color = COLORS[randint(0, 5)]
      circle(screen, color, (x, y), r)
      balls_s.append([x, y])
      balls_r.append(r)
      b_colours.append(color)
      balls_ds.append([randint(-5, 5), randint(-5, 5)])
  balls = []
  balls_s = []
  balls_r = []
  b_colours = []
  balls_ds = []

  def click_ball(event):
      '''
      функция проверяет попали ли мы по шару
      j-отвечает за количество шаров и кубов(суммарно 2*j)
      score-отвечает за количетво суммарных очков
      '''
      global j, k, score
      for i in range(j):
          if (balls_s[i][0] - event.pos[0]) ** 2 + (balls_s[i][1] - event.pos[1]) ** 2 <= (balls_r[i]) ** 2:
              score += 1
              balls_s[i] = [randint(100, 1100), randint(100, 600)]
              balls_r[i] = randint(20, 50)
              balls_ds[i] = [randint(-5, 5), randint(-5, 5)]
              b_colours[i] = COLORS[randint(0, 5)]

  def move_ball(screen):
      '''
      функция осуществляет перемещение и отражение от стенок шаров
      '''
      for i in range(j):
          if balls_s[i][0] + balls_r[i] >= 1200 or balls_s[i][0] - balls_r[i] <= 0:
              balls_ds[i][0] = -balls_ds[i][0]
          if balls_s[i][1] + balls_r[i] >= 700 or balls_s[i][1] - balls_r[i] <= 0:
              balls_ds[i][1] = -balls_ds[i][1]
          balls_s[i][0] += (1 + score / 7) * balls_ds[i][0]
          balls_s[i][1] += (1 + score / 7) * balls_ds[i][1]
          circle(screen, b_colours[i], (balls_s[i][0], balls_s[i][1]), balls_r[i])

cubes_s = []
cubes_a = []
c_colours = []
cubes_ds = []
l=[]

class Cube():
    def __init__(self):
    def new_cube():
      '''
      функция создает новый кубик с рандомными координатами и цветом
      '''
      global x, y, a, color, j, l, k
      x = randint(100, 1100)
      y = randint(100, 600)
      a = randint(40, 60)
      color = COLORS[randint(0, 5)]
      rect(screen, color, (x, y, a, a))
      cubes_s.append([x, y])
      cubes_a.append(a)
      c_colours.append(color)
      cubes_ds.append([randint(-5, 5), randint(-5, 5)])
      l.append(0)

    cubes_s = []
    cubes_a = []
    c_colours = []
    cubes_ds = []
    l = []

    def move_cube(screen):
        '''
        функция осуществляет перемещение и отражение от стенок кубов,
        а также ставит условие на количество отражений кубика
        '''
        for i in range(k):
            if cubes_s[i][0] + cubes_a[i] >= 1200 or cubes_s[i][0] <= 0:
                cubes_ds[i][0] = -cubes_ds[i][0]
                l[i] += 1
            if cubes_s[i][1] + cubes_a[i] >= 700 or cubes_s[i][1] <= 0:
                cubes_ds[i][1] = -cubes_ds[i][1]
                l[i] += 1
            # Если соударений произошло больше, чем четрыре, то кубик "удаляется"
            if l[i] > 4:
                c_colours[i] = (0, 0, 0)
                cubes_ds[i][0] = 0
                cubes_ds[i][1] = 0
                cubes_s[i][0] = 1400
                cubes_s[i][1] = 1200
            cubes_s[i][0] += (1 + score / 10) * cubes_ds[i][0]
            cubes_s[i][1] += (1 + score / 10) * cubes_ds[i][1]
            rect(screen, c_colours[i], (cubes_s[i][0], cubes_s[i][1], cubes_a[i], cubes_a[i]))

for i in range(3):
    ball = Ball(randint(30, 50), COLORS[randint(0, 5)], randint(100, 1100), randint(100, 600), randint(-5, 5), randint(-5, 5), 0)
    balls.append(ball)
for i in range(3):
    cube = Cube(COLORS[randint(0, 5)], randint(100, 1100), randint(100, 600), randint(40, 60), randint(-5, 5), randint(-5, 5), 0, 0)
    cubes.append(cube)

FONT = pygame.font.Font(None, 50)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

score = 0
for i in range(3):
    new_ball()
    j += 1
for i in range(3):
    new_cube()
    k += 1

FONT = pygame.font.Font(None, 50)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    move(screen)

    score_display = FONT.render(str(score), True, (255, 255, 255))
    screen.blit(score_display, (10, 10))
    pygame.display.update()
    screen.fill(BLACK)

f = open('top.txt', 'a', encoding='utf-8')
f.write('Игрок ' + name + ' набрал ' + str(score) + ' очков \n')
f.close()
pygame.quit()

