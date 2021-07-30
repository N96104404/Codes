import pygame
import os
import math

TOWER_IMAGE = pygame.image.load(os.path.join("images", "rapid_test.png"))

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def collide(self, enemy):
        """
        Q2.2)check whether the enemy is in the circle (attack range), if the enemy is in range return True
        :param enemy: Enemy() object
        :return: Bool

        Hint:
        x1, y1 = enemy.get_pos()

        """
        en_x, en_y = enemy.get_pos()  #enemy座標
        x, y = self.center            #圓的中心座標 
        if ((en_x-x)**2) + ((en_y-y)**2) <= ((self.radius)**2): # 圓的方程式
            return True
        else:
            return False

    def draw_transparent(self, win):
        """
        Q1) draw the tower effect range, which is a transparent circle.
        :param win: window surface
        :return: None
        """
        transparent_surface = pygame.Surface((300, 300), pygame.SRCALPHA)  
        transparency = 80  # define transparency: 0~255, 0 is fully transparent  透明度
        # draw the rectangle on the transparent surface
        pygame.draw.circle(transparent_surface, (230, 250, 230, transparency), (self.radius,self.radius), self.radius) #圓圈的位置
        x , y = self.center
        win.blit(transparent_surface, (x-self.radius, y-self.radius))

class Tower:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(TOWER_IMAGE, (70, 70))  # image of the tower
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # center of the tower
        self.range = 150  # tower attack range
        self.damage = 2   # tower damage
        self.range_circle = Circle(self.rect.center, self.range)  # attack range circle (class Circle())
        self.cd_count = 0  # used in self.is_cool_down()
        self.cd_max_count = 60  # used in self.is_cool_down()
        self.is_selected = True  # the state of whether the tower is selected
        self.type = "tower"

    def is_cool_down(self):
        """
        Q2.1) Return whether the tower is cooling down
        (1) Use a counter to computer whether the tower is cooling down (( self.cd_count
        :return: Bool

        Hint:
        let counter be 0
        if the counter < max counter then
            set counter to counter + 1
        else 
            counter return to zero
        end if
        """
        if self.cd_count < self.cd_max_count :
            self.cd_count += 1
            return False
        else :
            self.cd_count = 0
            return True 

    def attack(self, enemy_group):
        """
        Q2.3) Attack the enemy.
        (1) check the the tower is cool down ((self.is_cool_down()
        (2) if the enemy is in attack range, then enemy get hurt. ((Circle.collide(), enemy.get_hurt()
        :param enemy_group: EnemyGroup()
        :return: None
        """ 
        #把enemy_group的enemy拿出來,如果冷卻和enemy進到圓圈內都為真,那就進行攻擊
        for en in enemy_group.get():
            if self.is_cool_down() == True and self.range_circle.collide(en)== True:
                en.get_hurt(self.damage)
                return True
       
    def is_clicked(self, x, y):
        """
        Bonus) Return whether the tower is clicked
        (1) if the mouse position is on the tower image, return True
        :param x: mouse pos x
        :param y: mouse pos y
        :return: Bool
        """
        # 塔矩形的四個點用座標表示,及(矩形x,y) & (矩形x+w(寬)),y & (矩形x+w,y+h(高)) & (矩形x,y+h) 
        # 如果滑鼠座標(x,y)在這個範圍內,則為真, 不在則為否
        if self.rect.x < x < self.rect.x + self.rect.w  and self.rect.y < y < self.rect.y + self.rect.h:
            return True
        else:
            return False
            
    def get_selected(self, is_selected):
        """
        Bonus) Change the attribute self.is_selected
        :param is_selected: Bool
        :return: None

        """      
        self.is_selected = is_selected

    def draw(self, win):
        """
        Draw the tower and the range circle
        :param win:
        :return:
        """
        # draw range circle
        if self.is_selected:
            self.range_circle.draw_transparent(win)
        # draw tower
        win.blit(self.image, self.rect)


class TowerGroup:
    def __init__(self):
        self.constructed_tower = [Tower(250, 380), Tower(420, 400), Tower(600, 400)]

    def get(self):
        return self.constructed_tower

