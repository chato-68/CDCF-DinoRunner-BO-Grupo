import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import HEART_TYPE, RUNNING, DEFAULT_TYPE, DUCKING, JUMPING, SHIELD_TYPE, DUCKING_SHIELD, RUNNING_SHIELD, JUMPING_SHIELD
class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 300
    JUMP_VEL = 8.5
    def __init__(self):
        self.run_img = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}
        self.duck_img = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
        self.jump_img = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}

        self.image = self.run_img[DEFAULT_TYPE][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.steps = 0
        self.running = True
        self.ducking = False
        self.jumping = False
        self.jump_vel = self.JUMP_VEL
        self.jump_sound = pygame.mixer.Sound("salto.wav")
        self.duck_sound = pygame.mixer.Sound("agachado.wav")
        
        self.has_lives = True

        self.setup_state_booleans()

    def setup_state_booleans(self):
        self.has_powerup = False
        self.shield = False
        self.plus_heart = False
        self.show_text = False
        self.shield_time_up = 0

    def update(self, input_user):
        if self.running:
            self.run()
        if self.ducking:
            self.duck()
        if self.jumping:
            self.jump()
            #self.jumping_sound()
        if input_user[pygame.K_DOWN] and not self.jumping:
            self.ducking = True
            self.jumping = False
            self.running = False
            self.duck_sound.play()
        elif input_user[pygame.K_UP] and not self.jumping:
            self.jumping = True
            self.ducking = False
            self.running = False
            self.jump_sound.play()
        elif not self.jumping:
            self.running = True
            self.jumping = False
            self.ducking = False
        if self.steps >= 10:
            self.steps = 0
    def run(self):
        self.image = self.run_img[DEFAULT_TYPE][0] if self.steps <=5 else self.run_img[DEFAULT_TYPE][1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.steps += 1
    def duck(self):
        self.image = self.duck_img[DEFAULT_TYPE][0] if self.steps <=5 else self.duck_img[DEFAULT_TYPE][1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS + 30
        self.steps += 1
    def jump(self):
        #self.image = self.jump_img[self.type]
        self.image = JUMPING
        if self.jumping:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.jumping = False
            self.jump_vel = self.JUMP_VEL
    #def jumping_sound(self):
        #if self.jumping == True:
            #self.jump_sound.play()
        #elif self.jumping == False:
            #self.jump_sound.stop()
        
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def check_visibility(self, screen):
        if self.shield:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks()) / 1000,2)
            if (time_to_show >= 0):
                fond = pygame.font.Font("freesansbold.ttf", 18)
                text = fond.render(f"shield enable for {time_to_show}", True, (0, 0, 0))
                textRect = text.get_rect()
                textRect.center = (500, 40)
                screen.blit(text, textRect)
            else:
                self.shield = False
                self.update_to_default(SHIELD_TYPE)

        elif self.plus_heart:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks()) / 1000,2)
            if (time_to_show >= 0):
                fond = pygame.font.Font("freesansbold.ttf", 18)
                text = fond.render(f"shield enable for {time_to_show}", True, (0, 0, 0))
                textRect = text.get_rect()
                textRect.center = (400, 50)
                screen.blit(text, textRect)
            else:
                self.plus_heart = False
                self.update_to_default(HEART_TYPE)
                
    def update_to_default(self, current_type):
        if self.type == current_type:
            self.type = DEFAULT_TYPE