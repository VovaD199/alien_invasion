import pygame
pygame.init()
dis = pygame.display.set_mode((1280, 720))
dis.fill((255, 255, 255))
class Bullet:
    Bullets = set()
    def __init__(self, display, x, y, width, height, sprite, directionY = -2, directionX = 0):
        self.sprite = sprite
        self.display = display
        self.directionY = directionY  #Использовать при именении координат пули по Y
        self.directionX = directionX  #Использовать при именении координат пули по X
        self.instance = pygame.Rect(x, y, x + width, y + height)
        display.blit(sprite, self.instance)  #Должно быть в главном цикле
    def move(self):    #Должно быть в главном цикле
        self.display.move(self.instance, self.directionX, self.directionY)
class Player:
    def __init__(self, display, x1, y1, x2, y2, sprite):
        self.sprite = sprite
        self.display = display
        self.instance = pygame.Rect(x1, y1, x2, y2)
        display.blit(sprite, self.instance)  #Должно быть в главном цикле
    def shoot(self, sprite):
        Bullet.Bullets.add(Bullet(self.display, self.instance.centerx - 7, self.instance.y, 5, 5, sprite))
class EnemyLevelOne(Player):
    def __init__(self, *args, **kwargs):
        Player.__init__(*args, **kwargs)
    def shoot(self, sprite):
        Bullet.Bullets.add(Bullet(self.display, self.instance.centerx - 7, self.instance.bottomleft[1], 5, 5, sprite, 2))
class EnemyLevelTwo(EnemyLevelOne):
    def __init__(self, *args, **kwargs):
        EnemyLevelOne.__init__(*args, **kwargs)
        self.is_active = False  #Для проверки активности ряда врагов
    def shoot(self, sprite):
        Bullet.Bullets.add(Bullet(self.display, self.instance.centerx - 7, self.instance.bottomleft[1], 5, 5, sprite, 2, -1))
        Bullet.Bullets.add(Bullet(self.display, self.instance.centerx - 7, self.instance.bottomleft[1], 5, 5, sprite, 2, 1))
class EnemyLevelThree(EnemyLevelTwo):
    def __init__(self, *args, **kwargs):
        EnemyLevelTwo.__init__(*args, **kwargs)
    def shoot(self, sprite):
        Bullet.Bullets.add(Bullet(self.display, self.instance.centerx - 7, self.instance.bottomleft[1], 5, 5, sprite, 2))
        Bullet.Bullets.add(Bullet(self.display, self.instance.centerx - 7, self.instance.bottomleft[1], 5, 5, sprite, 2, -1))
        Bullet.Bullets.add(Bullet(self.display, self.instance.centerx - 7, self.instance.bottomleft[1], 5, 5, sprite, 2, 1))