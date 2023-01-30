# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 19:45:56 2022

@author: Mathieu
"""

import pygame
import pytmx
import pyscroll
import math
from player import Player

class Game:
    def __init__(self):
        #définir si jeu commencer ou non
        self.is_playing = False
        self.pos = "world"
        self.font = pygame.font.SysFont('Arial', 25)
        
        
        #****** Menu Principal
        # Set the size for the image
        self.DEFAULT_IMAGE_SIZE = (1080, 720)
        #gener la fenetre
        pygame.display.set_caption("GameWorld")
        self.screen = pygame.display.set_mode(self.DEFAULT_IMAGE_SIZE)
        icon = pygame.image.load("asset/icon.png").convert_alpha()
        pygame.display.set_icon(icon)
        pygame.display.get_active()
        
        #importer arrière plan
        background_menu = pygame.image.load('asset/backmenu.png')

        
        # Scale the image to your needed size
        self.image = pygame.transform.scale(background_menu, self.DEFAULT_IMAGE_SIZE)

        #import bouton play
        self.play_button = pygame.image.load('asset/play.png')
        self.play_button = pygame.transform.scale(self.play_button,(150,100))
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = math.ceil(self.screen.get_width()/5.5)
        self.play_button_rect.y = math.ceil(self.screen.get_height()/5.5) 
        
        #**** Carte du Monde
        #carte du jeu
        tmx_data = pytmx.util_pygame.load_pygame('asset/carte.tmx')
        map_data =pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2
        
        #gener le joueur
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x,player_position.y)
        self.position = 0
        
        #definir liste qui contient colision
        self.walls =  []
        
        for obj in tmx_data.objects:
            if obj.name == "colision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        
        #dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)
        
        #definir rectangle de collision de la forge
        forge = tmx_data.get_object_by_name('forge')
        self.forge_rect = pygame.Rect(forge.x, forge.y, forge.width, forge.height)
        
        #definir rectangle de collision du marché de bois et de fer
        buy = tmx_data.get_object_by_name('buy')
        self.buy_rect = pygame.Rect(buy.x, buy.y, buy.width, buy.height)      

        #definir rectangle de collision du marché de vente
        sold = tmx_data.get_object_by_name('sold')
        self.sold_rect = pygame.Rect(sold.x, sold.y, sold.width, sold.height)           
        
        
        
    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.player.move_up()
            if self.position == 0:
                self.player.change_animation('up')
            elif self.position == 1:
                self.player.change_animation('up1')
            elif self.position == 2:
                self.player.change_animation('up2')
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            if self.position == 0:
                self.player.change_animation('down')
            elif self.position == 1:
                self.player.change_animation('down1')
            elif self.position == 2:
                self.player.change_animation('down2')
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            if self.position == 0:
                self.player.change_animation('left')
            elif self.position == 1:
                self.player.change_animation('left1')
            elif self.position == 2:
                self.player.change_animation('left2')
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            if self.position == 0:
                self.player.change_animation('right')
            elif self.position == 1:
                self.player.change_animation('right1')
            elif self.position == 2:
                self.player.change_animation('right2')
        self.position+=1
        if self.position==3:
            self.position=0
        
    def open_forge(self):
        self.pos ="forge"
        
        #carte de la forge
        tmx_data = pytmx.util_pygame.load_pygame('asset/forge.tmx')
        
        map_data =pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        
        #dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        
        #definir rectangle de collision de la sortie
        forge_exit = tmx_data.get_object_by_name('exit')
        self.forge_exit_rect = pygame.Rect(forge_exit.x, forge_exit.y, forge_exit.width, forge_exit.height)
        
        #definir rectangle de collision de hache_wood
        hache_wood = tmx_data.get_object_by_name('hache_wood')
        self.hache_wood_rect = pygame.Rect(hache_wood.x, hache_wood.y, hache_wood.width, hache_wood.height)
        
        #definir rectangle de collision de pix_wood
        pix_wood = tmx_data.get_object_by_name('pix_wood')
        self.pix_wood_rect = pygame.Rect(pix_wood.x, pix_wood.y, pix_wood.width, pix_wood.height)
        
        #definir rectangle de collision de shield_wood
        shield_wood = tmx_data.get_object_by_name('shield_wood')
        self.shield_wood_rect = pygame.Rect(shield_wood.x, shield_wood.y, shield_wood.width, shield_wood.height)
        
        #definir rectangle de collision de sword_wood
        sword_wood = tmx_data.get_object_by_name('sword_wood')
        self.sword_wood_rect = pygame.Rect(sword_wood.x, sword_wood.y, sword_wood.width, sword_wood.height)
        
        #definir rectangle de collision de hache_steel
        hache_steel = tmx_data.get_object_by_name('hache_steel')
        self.hache_steel_rect = pygame.Rect(hache_steel.x, hache_steel.y, hache_steel.width, hache_steel.height)
        
        #definir rectangle de collision de pix_steel
        pix_steel = tmx_data.get_object_by_name('pix_steel')
        self.pix_steel_rect = pygame.Rect(pix_steel.x, pix_steel.y, pix_steel.width, pix_steel.height)
        
        #definir rectangle de collision de shield_steel
        shield_steel = tmx_data.get_object_by_name('shield_steel')
        self.shield_steel_rect = pygame.Rect(shield_steel.x, shield_steel.y, shield_steel.width, shield_steel.height)
        
        #definir rectangle de collision de sword_steel
        sword_steel = tmx_data.get_object_by_name('sword_steel')
        self.sword_steel_rect = pygame.Rect(sword_steel.x, sword_steel.y, sword_steel.width, sword_steel.height)
        
        #definir rectangle de collision de steel_horse
        steel_horse = tmx_data.get_object_by_name('steel_horse')
        self.steel_horse_rect = pygame.Rect(steel_horse.x, steel_horse.y, steel_horse.width, steel_horse.height)
        
        #definir rectangle de collision de wood
        wood = tmx_data.get_object_by_name('wood')
        self.wood_rect = pygame.Rect(wood.x, wood.y, wood.width, wood.height)
        
        #definir rectangle de collision de steel
        steel = tmx_data.get_object_by_name('steel')
        self.steel_rect = pygame.Rect(steel.x, steel.y, steel.width, steel.height)
        
    def exit_forge(self):
        self.pos ="world"
        self.screen = pygame.display.set_mode(self.DEFAULT_IMAGE_SIZE)
        
        #carte du jeu
        tmx_data = pytmx.util_pygame.load_pygame('asset/carte.tmx')
        map_data =pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2
        
        #gener le joueur
        player_position = tmx_data.get_object_by_name("forge_out")
        self.player.position = [player_position.x,player_position.y]
        self.position = 0
        
        #definir liste qui contient colision
        self.walls =  []
        
        for obj in tmx_data.objects:
            if obj.name == "colision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        
        #dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)
        
        
    def open_buy(self):
        self.pos ="buy"
        
        #carte de la forge
        tmx_data = pytmx.util_pygame.load_pygame('asset/buy.tmx')
        
        map_data =pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        
        #dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        
        #definir rectangle de collision de la sortie
        buy_exit = tmx_data.get_object_by_name('exit')
        self.buy_exit_rect = pygame.Rect(buy_exit.x, buy_exit.y, buy_exit.width, buy_exit.height)
        
        #definir rectangle de collision du fer
        steel = tmx_data.get_object_by_name('steel')
        self.steel_rect = pygame.Rect(steel.x, steel.y, steel.width, steel.height)
        
        #definir rectangle de collision du bois
        wood = tmx_data.get_object_by_name('wood')
        self.wood_rect = pygame.Rect(wood.x, wood.y, wood.width, wood.height)
        
        #definir rectangle de collision de l'argent
        money = tmx_data.get_object_by_name('money')
        self.money_rect = pygame.Rect(money.x, money.y, money.width, money.height)
        
        
    def exit_buy(self):
        self.pos ="world"
        self.screen = pygame.display.set_mode(self.DEFAULT_IMAGE_SIZE)
        
        #carte du jeu
        tmx_data = pytmx.util_pygame.load_pygame('asset/carte.tmx')
        map_data =pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2
        
        #gener le joueur
        player_position = tmx_data.get_object_by_name("buy_out")
        self.player.position = [player_position.x,player_position.y]
        self.position = 0
        
        #definir liste qui contient colision
        self.walls =  []
        
        for obj in tmx_data.objects:
            if obj.name == "colision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        
        #dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)
        
        
    def open_sold(self):
        self.pos ="sold"
        
        #carte de la forge
        tmx_data = pytmx.util_pygame.load_pygame('asset/sold.tmx')
        
        map_data =pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        
        #dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        
        #definir rectangle de collision de la sortie
        sold_exit = tmx_data.get_object_by_name('exit')
        self.sold_exit_rect = pygame.Rect(sold_exit.x, sold_exit.y, sold_exit.width, sold_exit.height)
        
        #definir rectangle de collision de hache_wood
        hache_wood = tmx_data.get_object_by_name('hache_wood')
        self.hache_wood_rect = pygame.Rect(hache_wood.x, hache_wood.y, hache_wood.width, hache_wood.height)
        
        #definir rectangle de collision de pix_wood
        pix_wood = tmx_data.get_object_by_name('pix_wood')
        self.pix_wood_rect = pygame.Rect(pix_wood.x, pix_wood.y, pix_wood.width, pix_wood.height)
        
        #definir rectangle de collision de shield_wood
        shield_wood = tmx_data.get_object_by_name('shield_wood')
        self.shield_wood_rect = pygame.Rect(shield_wood.x, shield_wood.y, shield_wood.width, shield_wood.height)
        
        #definir rectangle de collision de sword_wood
        sword_wood = tmx_data.get_object_by_name('sword_wood')
        self.sword_wood_rect = pygame.Rect(sword_wood.x, sword_wood.y, sword_wood.width, sword_wood.height)
        
        #definir rectangle de collision de hache_steel
        hache_steel = tmx_data.get_object_by_name('hache_steel')
        self.hache_steel_rect = pygame.Rect(hache_steel.x, hache_steel.y, hache_steel.width, hache_steel.height)
        
        #definir rectangle de collision de pix_steel
        pix_steel = tmx_data.get_object_by_name('pix_steel')
        self.pix_steel_rect = pygame.Rect(pix_steel.x, pix_steel.y, pix_steel.width, pix_steel.height)
        
        #definir rectangle de collision de shield_steel
        shield_steel = tmx_data.get_object_by_name('shield_steel')
        self.shield_steel_rect = pygame.Rect(shield_steel.x, shield_steel.y, shield_steel.width, shield_steel.height)
        
        #definir rectangle de collision de sword_steel
        sword_steel = tmx_data.get_object_by_name('sword_steel')
        self.sword_steel_rect = pygame.Rect(sword_steel.x, sword_steel.y, sword_steel.width, sword_steel.height)
        
        #definir rectangle de collision de steel_horse
        steel_horse = tmx_data.get_object_by_name('steel_horse')
        self.steel_horse_rect = pygame.Rect(steel_horse.x, steel_horse.y, steel_horse.width, steel_horse.height)
        
        #definir rectangle de collision de wood
        wood = tmx_data.get_object_by_name('wood')
        self.wood_rect = pygame.Rect(wood.x, wood.y, wood.width, wood.height)
        
        #definir rectangle de collision de steel
        steel = tmx_data.get_object_by_name('steel')
        self.steel_rect = pygame.Rect(steel.x, steel.y, steel.width, steel.height)
        
        #definir rectangle de collision de l'argent
        #definir liste qui contient colision
        self.money =  []
        
        for obj in tmx_data.objects:
            if obj.name == "money":
                self.money.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        
        
    def exit_sold(self):
        self.pos ="world"
        self.screen = pygame.display.set_mode(self.DEFAULT_IMAGE_SIZE)
        
        #carte du jeu
        tmx_data = pytmx.util_pygame.load_pygame('asset/carte.tmx')
        map_data =pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2
        
        #gerer le joueur
        player_position = tmx_data.get_object_by_name("sold_out")
        self.player.position = [player_position.x,player_position.y]
        self.position = 0
        
        #definir liste qui contient colision
        self.walls =  []
        
        for obj in tmx_data.objects:
            if obj.name == "colision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        
        #dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)
        
        
        
    def update(self):
        self.group.update()
        
        #vérifier entrer forge
        if self.player.feet.colliderect(self.forge_rect):
            self.open_forge()
            
        #vérifier entrer march bought
        if self.player.feet.colliderect(self.buy_rect):
            self.open_buy()
            
        #vérifier entrer march bought
        if self.player.feet.colliderect(self.sold_rect):
            self.open_sold()
            
        #vérification de colision
        for player in self.group.sprites():
            if player.feet.collidelist(self.walls) > -1:
                player.move_back()
                
        
    def run(self):
        
        clock = pygame.time.Clock()
        
        running = True

        #Boucle tant que cette condition est vraie
        while running:   
            
            self.player.save_location()
            self.handle_input()    
            self.group.center(self.player.rect)
            
            if self.is_playing == False:
                #appliquer l'arrière plan du jeu
                self.screen.blit(self.image, (0,0))
                
                #bouton start
                self.screen.blit(self.play_button, self.play_button_rect)
            
            if self.is_playing == True and self.pos=="forge":
                #wood and steel actualisation
                wood = self.font.render(str(self.player.inventaire["wood"]), False, (255,255,255))
                steel = self.font.render(str(self.player.inventaire["steel"]), False, (255,255,255))
                self.screen.fill([211, 116, 66],self.wood_rect)
                self.screen.blit(wood, (340, 10))
                self.screen.fill([211, 116, 66],self.steel_rect)
                self.screen.blit(steel, (670, 10))
                #si ferme fenetre
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:                        
                        if self.forge_exit_rect.collidepoint(event.pos):
                            self.exit_forge()
                        if self.hache_wood_rect.collidepoint(event.pos):
                            self.player.forge("hache_wood")
                        if self.pix_wood_rect.collidepoint(event.pos):
                            self.player.forge("pix_wood")
                        if self.shield_wood_rect.collidepoint(event.pos):
                            self.player.forge("shield_wood")
                        if self.sword_wood_rect.collidepoint(event.pos):
                            self.player.forge("sword_wood")
                        if self.steel_horse_rect.collidepoint(event.pos):
                            self.player.forge("steel_horse")
                        if self.hache_steel_rect.collidepoint(event.pos):
                            self.player.forge("hache_steel")
                        if self.pix_steel_rect.collidepoint(event.pos):
                            self.player.forge("pix_steel")
                        if self.shield_steel_rect.collidepoint(event.pos):
                            self.player.forge("shield_steel")
                        if self.sword_steel_rect.collidepoint(event.pos):
                            self.player.forge("sword_steel")
                            
            if self.is_playing == True and self.pos=="sold":                
                #money actualisation
                gold = self.font.render(str(self.player.inventaire["gold"]), False, (255,255,255))
                hache_wood = self.font.render(str(self.player.inventaire["hache_wood"]), False, (255,255,255))
                pix_wood = self.font.render(str(self.player.inventaire["pix_wood"]), False, (255,255,255))
                shield_wood = self.font.render(str(self.player.inventaire["shield_wood"]), False, (255,255,255))
                sword_wood = self.font.render(str(self.player.inventaire["sword_wood"]), False, (255,255,255))
                steel_horse = self.font.render(str(self.player.inventaire["steel_horse"]), False, (255,255,255))
                hache_steel = self.font.render(str(self.player.inventaire["hache_steel"]), False, (255,255,255))
                pix_steel = self.font.render(str(self.player.inventaire["pix_steel"]), False, (255,255,255))
                shield_steel = self.font.render(str(self.player.inventaire["shield_steel"]), False, (255,255,255))
                sword_steel = self.font.render(str(self.player.inventaire["sword_steel"]), False, (255,255,255))
                wood_in = self.font.render(str(self.player.inventaire["wood"]), False, (255,255,255))
                steel_in = self.font.render(str(self.player.inventaire["steel"]), False, (255,255,255))
                for x in self.money:                    
                    self.screen.fill([130, 223, 255],x)
                self.screen.blit(gold, (40, 5))
                self.screen.blit(wood_in, (135, 5))
                self.screen.blit(hache_wood, (210, 5))
                self.screen.blit(pix_wood, (290, 5))
                self.screen.blit(shield_wood, (380, 5))
                self.screen.blit(sword_wood, (455, 5))
                self.screen.blit(steel_in, (540, 5))
                self.screen.blit(steel_horse, (595, 5))
                self.screen.blit(hache_steel, (678, 5))
                self.screen.blit(pix_steel, (745, 5))
                self.screen.blit(shield_steel, (825, 5))
                self.screen.blit(sword_steel, (905, 5))
                #si ferme fenetre
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:                        
                        if self.sold_exit_rect.collidepoint(event.pos):
                            self.exit_sold()
                        if self.hache_wood_rect.collidepoint(event.pos):
                            self.player.sold("hache_wood")
                        if self.pix_wood_rect.collidepoint(event.pos):
                            self.player.sold("pix_wood")
                        if self.shield_wood_rect.collidepoint(event.pos):
                            self.player.sold("shield_wood")
                        if self.sword_wood_rect.collidepoint(event.pos):
                            self.player.sold("sword_wood")
                        if self.steel_horse_rect.collidepoint(event.pos):
                            self.player.sold("steel_horse")
                        if self.hache_steel_rect.collidepoint(event.pos):
                            self.player.sold("hache_steel")
                        if self.pix_steel_rect.collidepoint(event.pos):
                            self.player.sold("pix_steel")
                        if self.shield_steel_rect.collidepoint(event.pos):
                            self.player.sold("shield_steel")
                        if self.sword_steel_rect.collidepoint(event.pos):
                            self.player.sold("sword_steel")
                            
            if self.is_playing == True and self.pos=="buy":
                #money actualisation
                texte = self.font.render(str(self.player.inventaire["gold"]), False, (255,255,255))
                self.screen.fill([130, 223, 255],self.money_rect)
                self.screen.blit(texte, (80, 15))
                #si ferme fenetre
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:                        
                        if self.buy_exit_rect.collidepoint(event.pos):
                            self.exit_buy()
                        if self.wood_rect.collidepoint(event.pos):
                            self.player.buy("wood")
                        if self.steel_rect.collidepoint(event.pos):
                            self.player.buy("steel")
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                
            if self.is_playing == True and self.pos=="world":
                self.update()
                self.group.draw(self.screen)
                
            #mettre l'écran à jour
            pygame.display.flip()
            
            #si ferme fenetre
            for event in pygame.event.get():
                #que l'evenement est fermeture dee fenetre
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #vérification si souris collision avec bouton
                    if self.play_button_rect.collidepoint(event.pos):
                        self.is_playing = True
                        
            clock.tick(40)

