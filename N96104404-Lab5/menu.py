import pygame
import os

UpgradeMenu_IMAGE = pygame.image.load(os.path.join("images", "upgrade_menu.png"))
sell_IMAGE = pygame.image.load(os.path.join("images", "sell.png"))
upgrade_IMAGE = pygame.image.load(os.path.join("images", "upgrade.png"))

class UpgradeMenu:
    def __init__(self, x, y):        
        self.image = pygame.transform.scale(UpgradeMenu_IMAGE, (180, 180))  # image of the menu
        self.sell_image = pygame.transform.scale(sell_IMAGE, (35, 35))  # image of the sell
        self.upgrade_image = pygame.transform.scale(upgrade_IMAGE, (55, 30))  # image of the upgrade
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)  # center of the menu
        self.__buttons = [Button(self.upgrade_image,"upgrade",self.rect.centerx,self.rect.centery-65),  #button位置
                          Button(self.sell_image,"sell",self.rect.centerx,self.rect.centery+66)]  # (Q2) Add buttons here

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.image, (self.rect.x, self.rect.y))
        # (Q2) Draw buttons here
        #win.blit(self.sell_image, (self.rect.x+72, self.rect.y+140))     #可用#這兩行各自顯示sell & upgrade也可以使用另一個直接顯示2個
        #win.blit(self.upgrade_image, (self.rect.x+62, self.rect.y+10))  
        for btn in self.__buttons:
            win.blit(btn.image, btn.rect)
            
    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons

class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        if self.rect.collidepoint(x, y):
            return True
        else:
            return False

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name

