import pygame
from pygame.sprite import Sprite,Group
import sys
from pathlib import Path
from typing import Dict,Tuple
import math
import random


pygame.init()

scalar = 1

p = Path('./images')

image_dic = dict([ [x.stem, pygame.image.load(x)] for x in p.iterdir() if x.is_file() ])

update_frames = 60
update_interval = 6

fish_property = {
    "fish11": {"image_length": 12, "swimming_length": 8, "base_speed": 3, "speed_range": 1.1, "capture_probability": 0.05, "coin_level": 2, "multiple": 10},
    "fish1": {"image_length": 8, "swimming_length": 4, "base_speed": 1, "speed_range": 2, "capture_probability": 0.7, "coin_level": 1, "multiple": 1},
    "fish2": {"image_length": 8, "swimming_length": 4, "base_speed": 1, "speed_range": 2, "capture_probability": 0.6, "coin_level": 1, "multiple": 2},
    "fish3": {"image_length": 8, "swimming_length": 4, "base_speed": 1.5, "speed_range": 2, "capture_probability": 0.5, "coin_level": 1, "multiple": 3},
    "fish4": {"image_length": 8, "swimming_length": 4, "base_speed": 2, "speed_range": 1, "capture_probability": 0.4, "coin_level": 1, "multiple": 4},
    "fish5": {"image_length": 8, "swimming_length": 4, "base_speed": 1.2, "speed_range": 2.1, "capture_probability": 0.35, "coin_level": 1, "multiple": 5},
    "fish6": {"image_length": 12, "swimming_length": 8, "base_speed": 1.4, "speed_range": 1, "capture_probability": 0.3, "coin_level": 2, "multiple": 1},
    "fish7": {"image_length": 10, "swimming_length": 6, "base_speed": 1, "speed_range": 4, "capture_probability": 0.25, "coin_level": 2, "multiple": 2},
    "fish8": {"image_length": 12, "swimming_length": 8, "base_speed": 2.2, "speed_range": 1, "capture_probability": 0.2, "coin_level": 2, "multiple": 3},
    "fish9": {"image_length": 12, "swimming_length": 8, "base_speed": 1.2, "speed_range": 3, "capture_probability": 0.15, "coin_level": 2, "multiple": 4},
    "fish10": {"image_length": 10, "swimming_length": 6, "base_speed": 1, "speed_range": 2, "capture_probability": 0.1, "coin_level": 2, "multiple": 5}
}



all_sprites = Group()
add_sprites = []
remove_sprites = []
back_image = image_dic["game_bg_2_hd"]

def calculate_angle(x,y,target_position):
        dx = target_position[0] - x
        dy = target_position[1] - y
        return math.atan2(dy, dx) 

class CustomerError(Exception):
    """Exception from this project"""
    pass

class BaseSprite(Sprite):

    @property
    def image(self):
        height_per_frame = self.full_image.get_height() / self.image_length
        _image = self.full_image.subsurface((0, height_per_frame * self.frame_count, self.full_image.get_width(), height_per_frame))
        if hasattr(self, 'angle'):
            _image = pygame.transform.rotate(_image, math.degrees(-self.angle))
        self.rect = _image.get_rect(center=(self.x, self.y))
        if hasattr(self, 'speed'):
            _angle = self.angle if hasattr(self, 'angle') else 0
            self.x += self.speed * math.cos(_angle)
            self.y += self.speed * math.sin(_angle)
            self.rect.center = (self.x, self.y)
        return _image

    def update_interval(self):
        """call update base on update_interval"""
        pass

    def update_frame(self):
        """call by orginal update"""
        pass
    
    def update(self):
        self.update_frame()
        if self.update_count % update_interval == 0:
            self.update_interval()
            if( self.frame_count >= self.image_length-1 ):
                self.frame_count = 0
                return
            self.frame_count += 1

        self.update_count += 1
        if self.update_count >= update_interval:
            self.update_count = 0    

class Coin(BaseSprite):
    def __init__(self, x,y,coin_level,coin_multiple) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.full_image = image_dic[f"coin{coin_level}"]
        self.image_length = 10
        self.frame_count = 0
        self.update_count = 0
        self.coin_multiple = coin_multiple
        self.target_position = (200, 768)
        self.speed = 6
        self.angle = calculate_angle(self.x,self.y,self.target_position)


    @property
    def image(self):
        height_per_frame = self.full_image.get_height() / self.image_length
        _image = self.full_image.subsurface((0, height_per_frame * self.frame_count, self.full_image.get_width(), height_per_frame))
        self.rect = _image.get_rect()
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        self.rect.center = (self.x, self.y)
        return _image       


class Bullet(BaseSprite):
    def __init__(self,target_position:Tuple,level ) -> None:
        super().__init__()
        self.x = 512
        self.y = 730
        self.level = level
        self.target_position = target_position
        self.full_image = image_dic[f"bullet{level}"]
        self.image_length = 1
        self.frame_count = 0
        self.update_count = 0
        self.speed = 5 + level
        self.angle = calculate_angle(self.x,self.y,self.target_position)

    @property
    def image(self):
        height_per_frame = self.full_image.get_height() / self.image_length
        _image = self.full_image.subsurface((0, height_per_frame * self.frame_count, self.full_image.get_width(), height_per_frame))
        if hasattr(self, 'angle'):
            _image = pygame.transform.rotate(_image, math.degrees(-self.angle))
        self.rect = _image.get_rect(center=(self.x, self.y))
        if hasattr(self, 'speed'):
            _angle = self.angle if hasattr(self, 'angle') else 0
            self.x += self.speed * math.cos(_angle)
            self.y += self.speed * math.sin(_angle)
            self.rect.center = (self.x, self.y)
        print(self.rect.width)
        return _image
    
class Web(BaseSprite):
    def __init__(self,x,y,level) -> None:
        super().__init__()
        self.x = x 
        self.y = y
        self.full_image = image_dic[f"web{level}"]
        self.image_length = 1
        self.frame_count = 0
        self.update_count = 0
        self.check_collide_frame_count = 0
        self.display_frame_count = 0
    
    def update(self):
        self.display_frame_count += 1
        #display 20 frames
        if self.display_frame_count > 20 :
            remove_sprites.append(self)

class Fish(BaseSprite):
    def __init__(self,name) -> None:
        super().__init__()
        self.full_image = image_dic[name]
        self.property = fish_property[name]
        self.is_left = True if random.randint(0,2) == 0 else False
        self.x = -100 if self.is_left else 1200
        self.y = random.randint(0,768)
        self.target_position = (1200 if self.is_left else -100,random.randint(0,768))
        self.image_length = self.property["image_length"]
        self.speed = self.property["base_speed"] + random.uniform(0.0 , self.property["speed_range"])
        self.frame_count = 0
        self.update_count = 0
        self.angle = calculate_angle(self.x,self.y,self.target_position)
        self.is_alive = True
    
    def update(self):
        if self.update_count % update_interval == 0:
            _swimming_length = self.property["swimming_length"]
            _image_length = self.property["image_length"]
            _max = _swimming_length if self.is_alive else _image_length
            _min = 0 if self.is_alive else _swimming_length
            if self.frame_count >= _max-1:
                self.frame_count = _min
                return
            self.frame_count += 1

        self.update_count += 1
        if self.update_count >= update_interval:
            self.update_count = 0

class Cannon(BaseSprite):
    def __init__(self, level) -> None:
        super().__init__()
        self.full_image = image_dic[f"cannon{level}"]
        self.level = level
        self.x = 512
        self.y = 730
        self.frame_count = 0
        self.update_count = 0
        self.speed = 0
        self.on_fire = False
        self.angle = 0
        self.image_length = 5
    
    def fire(self,x,y):
        if self.on_fire:
            return
        self.aim(x,y)
        self.on_fire = True
        add_sprites.append(Bullet((x,y),self.level))
        

    def aim(self,x,y):
        self.angle =  calculate_angle(self.x,self.y,(x,y)) + math.pi/2

    def update(self):
        _fire_interval = 1 + int(self.level/2)
        if self.update_count % _fire_interval == 0 and self.on_fire:
            if( self.frame_count >= self.image_length-1 ):
                self.on_fire = False
                self.frame_count = 0
                return
            self.frame_count += 1

        self.update_count += 1
        if self.update_count >= _fire_interval:
            self.update_count = 0    


stage_cannon_level = 1
cannons = [ Cannon(i) for i in range(1,8) ]

fish_sequence=[1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,6,6,6,7,7,7,8,8,8,9,9,10,10,11]

fish_sequence = [ f'fish{i}' for i in fish_sequence]


def create_fish():
    _index = random.randint(0,len(fish_sequence)-1)
    all_sprites.add(Fish(fish_sequence[_index]))

print(back_image.get_width(), back_image.get_height())

screen = pygame.display.set_mode((back_image.get_width(), back_image.get_height()))
pygame.display.set_caption("py_fish")

#add_sprites.append(Fish('fish11'))
stage_update_count = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            cannons[stage_cannon_level-1].fire(mouse_pos[0],mouse_pos[1])
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            cannons[stage_cannon_level-1].aim(mouse_pos[0],mouse_pos[1])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                stage_cannon_level += 1
                if stage_cannon_level == 8:
                    stage_cannon_level = 0
            if event.key == pygame.K_LEFT:
                stage_cannon_level -= 1
                if stage_cannon_level == -1:
                    stage_cannon_level = 7

    screen.blit(back_image,(0,0))
    # Update all sprites
    all_sprites.update()
    all_sprites.draw(screen)

    cannons[stage_cannon_level-1].update()
    screen.blit(cannons[stage_cannon_level-1].image,cannons[stage_cannon_level-1].rect)

    fishs = [x for x in all_sprites if isinstance(x,Fish) and hasattr(x, 'rect') ]
    bullets = [x for x in all_sprites if isinstance(x,Bullet) and hasattr(x, 'rect') ]
    webs = [x for x in all_sprites if isinstance(x,Web) and hasattr(x, 'rect') ]

    for fish in fishs:
        # remove sprite which is out of screen
        if not screen.get_rect().colliderect(fish.rect):
            if fish.is_left and fish.rect.x < 0:
                continue
            if not fish.is_left and fish.rect.x > 1024:
                continue
            #print("--------fish out")
            remove_sprites.append(fish)
        #Bullet collide fish
        for bullet in bullets:
            if bullet.rect.colliderect(fish.rect):
                add_sprites.append(Web(bullet.x,bullet.y,bullet.level))
                remove_sprites.append(bullet)
        
        #web collide fish
        for web in webs:
            #web has 3 fream to checking collide with fish
            if web.check_collide_frame_count <=3 and web.rect.colliderect(fish.rect):
                web.check_collide_frame_count += 1
                if random.random() < fish.property["capture_probability"]:
                    #fish has been captured
                    add_sprites.append(Coin(fish.x,fish.y,fish.property["coin_level"],fish.property["multiple"]))
                    remove_sprites.append(fish)       

    for bullet in bullets:
        # remove bullet which is out of screen
        #print(bullet.x)
        if not screen.get_rect().colliderect(bullet.rect):
            print("--------bullet out")
            remove_sprites.append(bullet)
        
    all_sprites.remove(*remove_sprites)
    remove_sprites = []
    all_sprites.add(*add_sprites)
    add_sprites = []

    if stage_update_count % 10 == 0:
        create_fish()
        print(f"sprites count:{len(all_sprites)}")
    stage_update_count += 1
    if stage_update_count >= 1000:
        stage_update_count = 0

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()


