# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 13:25:37 2022

@author: Mathieu
"""

import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self,x,y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('asset/perso.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()
        self.position =[x,y]
        self.images = {
                'down' : self.get_image(0, 0),
                'left' : self.get_image(0, 32),
                'right': self.get_image(0, 64),
                'up'   : self.get_image(0, 96),
                'down1' : self.get_image(32, 0),
                'left1' : self.get_image(32, 32),
                'right1': self.get_image(32, 64),
                'up1'   : self.get_image(32, 96),
                'down2' : self.get_image(64, 0),
                'left2' : self.get_image(64, 32),
                'right2': self.get_image(64, 64),
                'up2'   : self.get_image(64, 96),
            }
        self.feet = pygame.Rect(0, 0, self.rect.width*0.5,12)
        self.old_position = self.position.copy()
        self.speed = 3
        self.inventaire = {"gold":10,"wood":0,"steel":0,"hache_wood":0,"pix_wood":0,"shield_wood":0,"sword_wood":0,
                           "hache_steel":0,"pix_steel":0,"shield_steel":0,"sword_steel":0,"steel_horse":0}
        
    def buy(self, materiaux):
        if materiaux == "wood" and self.inventaire["gold"]>=2:
            self.inventaire.update({'gold': self.inventaire["gold"]-2, 'wood': self.inventaire["wood"]+1})
        elif materiaux == "steel" and self.inventaire["gold"]>=5:
            self.inventaire.update({'gold': self.inventaire["gold"]-5, 'steel': self.inventaire["steel"]+1})
            
    def forge(self, materiaux):
        if materiaux == "hache_wood" and self.inventaire["wood"]>=2:
            self.inventaire.update({'wood': self.inventaire["wood"]-2, 'hache_wood': self.inventaire["hache_wood"]+1})
        elif materiaux == "pix_wood" and self.inventaire["wood"]>=2:
            self.inventaire.update({'wood': self.inventaire["wood"]-2, 'pix_wood': self.inventaire["pix_wood"]+1})
        elif materiaux == "shield_wood" and self.inventaire["wood"]>=3:
            self.inventaire.update({'wood': self.inventaire["wood"]-3, 'shield_wood': self.inventaire["shield_wood"]+1})
        elif materiaux == "sword_wood" and self.inventaire["wood"]>=3:
            self.inventaire.update({'wood': self.inventaire["wood"]-3, 'sword_wood': self.inventaire["sword_wood"]+1})
        elif materiaux == "steel_horse" and self.inventaire["steel"]>=1:
            self.inventaire.update({'steel': self.inventaire["steel"]-1, 'steel_horse': self.inventaire["steel_horse"]+1})
        elif materiaux == "hache_steel" and self.inventaire["steel"]>=2 and self.inventaire["wood"]>=1:
            self.inventaire.update({'steel': self.inventaire["steel"]-2,'wood': self.inventaire["wood"]-1, 'hache_steel': self.inventaire["hache_steel"]+1})
        elif materiaux == "pix_steel" and self.inventaire["steel"]>=2 and self.inventaire["wood"]>=1:
            self.inventaire.update({'steel': self.inventaire["steel"]-2,'wood': self.inventaire["wood"]-1, 'pix_steel': self.inventaire["pix_steel"]+1})
        elif materiaux == "shield_steel" and self.inventaire["steel"]>=3:
            self.inventaire.update({'steel': self.inventaire["steel"]-3, 'shield_steel': self.inventaire["shield_steel"]+1})
        elif materiaux == "sword_steel" and self.inventaire["steel"]>=3:
            self.inventaire.update({'steel': self.inventaire["steel"]-3, 'sword_steel': self.inventaire["sword_steel"]+1})
            
    def sold(self, materiaux):
        if materiaux == "hache_wood" and self.inventaire["hache_wood"]>=1:
            self.inventaire.update({'gold': self.inventaire["gold"]+5, 'hache_wood': self.inventaire["hache_wood"]-1})
        elif materiaux == "pix_wood" and self.inventaire["pix_wood"]>=1:
            self.inventaire.update({'gold': self.inventaire["gold"]+5, 'pix_wood': self.inventaire["pix_wood"]-1})
        elif materiaux == "shield_wood" and self.inventaire["shield_wood"]>=1:
            self.inventaire.update({'gold': self.inventaire["gold"]+8, 'shield_wood': self.inventaire["shield_wood"]-1})
        elif materiaux == "sword_wood" and self.inventaire["sword_wood"]>=1:
            self.inventaire.update({'gold': self.inventaire["gold"]+8, 'sword_wood': self.inventaire["sword_wood"]-1})
        elif materiaux == "steel_horse" and self.inventaire["steel_horse"]>=1:
            self.inventaire.update({'gold': self.inventaire["gold"]+6, 'steel_horse': self.inventaire["steel_horse"]-1})
        elif materiaux == "hache_steel" and self.inventaire["hache_steel"]>=1:
            self.inventaire.update({'gold': self.inventaire["gold"]+15, 'hache_steel': self.inventaire["hache_steel"]-1})
        elif materiaux == "pix_steel" and self.inventaire["pix_steel"]>=1:
            self.inventaire.update({'gold': self.inventaire["gold"]+15, 'pix_steel': self.inventaire["pix_steel"]-1})
        elif materiaux == "shield_steel" and self.inventaire["shield_steel"]>=1:
            self.inventaire.update({'gold': self.inventaire["gold"]+20, 'shield_steel': self.inventaire["shield_steel"]-1})
        elif materiaux == "sword_steel" and self.inventaire["sword_steel"]>=1:
            self.inventaire.update({'gold': self.inventaire["gold"]+20, 'sword_steel': self.inventaire["sword_steel"]-1})
        elif materiaux == "wood" and self.inventaire["wood"]>=1:
            self.inventaire.update({'gold': self.inventaire["gold"]+1, 'wood': self.inventaire["wood"]-1})
        elif materiaux == "steel" and self.inventaire["steel"]>=1:
            self.inventaire.update({'gold': self.inventaire["gold"]+2, 'steel': self.inventaire["steel"]-1})
        
        
    def change_animation(self,name):        
        self.image.set_colorkey([0,0,0])
        self.image = self.images[name]        
        self.image.set_colorkey([0,0,0])
    
    def save_location(self): self.old_position = self.position.copy()      
    
    def move_right(self):
        self.image.set_colorkey([0,0,0])
        self.position[0] +=self.speed
    
    def move_left(self):
        self.image.set_colorkey([0,0,0])
        self.position[0] -=self.speed
    
    def move_up(self):
        self.image.set_colorkey([0,0,0])
        self.position[1] -=self.speed
    
    def move_down(self):
        self.image.set_colorkey([0,0,0])
        self.position[1] +=self.speed
        
    def update(self):        
        self.image.set_colorkey([0,0,0])
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom
        
    def move_back(self):
        self.image.set_colorkey([0,0,0])
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom
        
    def get_image(self,x,y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet,(0,0),(x,y,32,32))
        return image