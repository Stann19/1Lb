import pygame
from pygame.draw import *
from random import randint

'''
"Поймай шарик"
В начале открывается окно игры. На игровом поле создается 3 шарика с рандомными цветами 
и в рандомных местах окна. Аналогично создается 3 кубика. За поподание в шарик- 1 очко, 
за кубик- 2 очка. Если кубик отразился 4 раза и по нему не попали, то на 5 отражение 
он исчезнет. Счет игрока с его именем заносятся в файл top.txt.
'''
#Считывание имени игрока
print("Введите ваше имя: ")
name = str(input())

pygame.init()

FPS = 50
screen = pygame.display.set_mode((1200, 700))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
j = 1
i = 1

class Ball:
   def __init__(self, x, y, r, color):
      self.x = x
      self.y = y
      self.r = r
      self.color = color
      self.vx = randint(-5, 5)
      self.vy = randint(-5, 5)
   def new_ball(self, screen):
      '''
      функция создает новый шарик с рандомными координатами и цветом
      '''
      circle(screen, self.color, (self.x, self.y), self.r)

   def click_ball(self, event):
      '''
      функция проверяет попали ли мы по шару
      j-отвечает за количество шаров(суммарно 2*j)
      score-отвечает за количетво суммарных очков
      '''
      global score
      b = event.pos[0]
      c = event.pos[1]
      if (self.x - b) ** 2 + (self.y - c) ** 2 <= (self.r) ** 2:
         score += 1
         self.x = randint(100, 1100)
         self.y = randint(100, 600)
         self.r = randint(20, 50)
         self.vx = randint(-5, 5)
         self.vy = randint(-5, 5)
         self.color = COLORS[randint(0, 5)]

   def move_ball(self):
       '''
       функция осуществляет перемещение и отражение от стенок шаров
       '''
       global score
       self.x += 1.5*self.vx
       self.y += 1.5*self.vy
       if self.x + self.r >= 1200 or self.x - self.r <= 0:
           self.vx = -self.vx
           self.x += self.vx
           self.y += self.vy
       if self.y + self.r >= 700 or self.y - self.r <= 0:
           self.vy = -self.vy
           self.x += self.vx
           self.y += self.vy
       ball1.new_ball(screen)
       ball2.new_ball(screen)
       ball3.new_ball(screen)


class Cube:
    def __init__(self, x, y, a, color):
        self.x = x
        self.y = y
        self.a = a
        self.vx = randint(-5, 5)
        self.vy = randint(-5, 5)
        self.color = color
        self.l = 0
    def new_cube(self, screen):
       '''
       функция создает новый кубик с рандомными координатами и цветом
       '''
       rect(screen, self.color, (self.x, self.y, self.a, self.a))

    def click_cube(self, event):
        '''
        функция проверяет попали ли мы по кубу
        2*j-отвечает за количество кубов
        score-отвечает за количетво суммарных очков
        '''
        global score
        b = event.pos[0]
        c = event.pos[1]
        if (self.x - b) ** 2 + (self.y - c) ** 2 <= (self.a) ** 2:
            score += 2
            self.x = randint(100, 1100)
            self.y = randint(100, 600)
            self.a = randint(30, 60)
            self.vx = randint(-5, 5)
            self.vy = randint(-5, 5)
            self.l = 0
            self.color = COLORS[randint(0, 5)]

    def move_cube(self):
        '''
        функция осуществляет перемещение и отражение от стенок кубов,
        а также ставит условие на количество отражений кубика
        '''
        self.x += 1.5*self.vx
        self.y += 1.5*self.vy
        if self.x + self.a >= 1200 or self.x <= 0:
            self.vx = -self.vx
            self.l += 1
            self.x += self.vx
            self.y += self.vy
        if self.y + self.a >= 700 or self.y <= 0:
            self.vy = -self.vy
            self.l += 1
            self.x += self.vx
            self.y += self.vy
        # Если соударений произошло больше, чем четрыре, то кубик "удаляется"
        if self.l > 4:
            self.color = (0, 0, 0)
            self.vx = 0
            self.vy = 0
            self.x = 1400
            self.y = 1200
        cube1.new_cube(screen)
        cube2.new_cube(screen)
        cube3.new_cube(screen)

score = 0
ball1 = Ball(randint(100, 1100), randint(100, 600), randint(30, 50), COLORS[randint(0, 5)])
cube1 = Cube(randint(100, 1100), randint(100, 600), randint(40, 60), COLORS[randint(0, 5)])
ball2 = Ball(randint(100, 1100), randint(100, 600), randint(30, 50), COLORS[randint(0, 5)])
cube2 = Cube(randint(100, 1100), randint(100, 600), randint(40, 60), COLORS[randint(0, 5)])
ball3 = Ball(randint(100, 1100), randint(100, 600), randint(30, 50), COLORS[randint(0, 5)])
cube3 = Cube(randint(100, 1100), randint(100, 600), randint(40, 60), COLORS[randint(0, 5)])
ball1.new_ball(screen)
cube1.new_cube(screen)
ball2.new_ball(screen)
cube2.new_cube(screen)
ball3.new_ball(screen)
cube3.new_cube(screen)

FONT = pygame.font.Font(None, 50)

pygame.display.update()
clock = pygame.time.Clock()
finished = False


FONT = pygame.font.Font(None, 50)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cube1.click_cube(event)
            cube2.click_cube(event)
            cube3.click_cube(event)
            ball1.click_ball(event)
            ball2.click_ball(event)
            ball3.click_ball(event)

    cube1.move_cube()
    cube2.move_cube()
    cube3.move_cube()
    ball1.move_ball()
    ball2.move_ball()
    ball3.move_ball()

    score_display = FONT.render(str(score), True, (255, 255, 255))
    screen.blit(score_display, (10, 10))
    pygame.display.update()
    screen.fill(BLACK)

f = open('top.txt', 'a', encoding='utf-8')
f.write('Игрок ' + name + ' набрал ' + str(score) + ' очков \n')
f.close()
pygame.quit()

