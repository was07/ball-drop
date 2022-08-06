import pygame
import colorama


def error_message(message):
    print(colorama.Fore.RED + '[+] ' + colorama.Style.RESET_ALL + message)


class Ball:
    def __init__(self, surface, height=200, exeleration=12, bounce_percentage=100):
        self.surface = surface
        self.rect = pygame.Rect(10, surface.get_height()-height, 20, 20)
        self.exeleration = exeleration  # possitive = right,   negative = left
        self.fall_speed = 0    # possitive = falling, negative = rising

        if bounce_percentage > 100:
            bounce_percentage = 100
            error_message("bounce_percentage > 100, set to 100")
        
        self.bounce = bounce_percentage / 100

        b = bounce_percentage * 2.25
        self._color = (225-b, 225-b/2, 200)
    
    def update(self):
        self.rect.move_ip(self.exeleration, self.fall_speed)
        if self.rect.x > (self.surface.get_width() - self.rect.width):
            self.exeleration = -self.exeleration * self.bounce
        elif self.rect.x < 0:
            self.exeleration = -self.exeleration * self.bounce

        if self.rect.y > (self.surface.get_height() - self.rect.height):
            self.fall_speed = -(self.fall_speed - 1) * self.bounce
            self.rect.y = self.surface.get_height() - self.rect.height
        elif self.rect.y < 0:
            self.fall_speed = -self.fall_speed * self.bounce
            self.rect.y = self.rect.height
        
        if .5 > self.fall_speed > -.5: self.fall_speed += 1
        else: self.fall_speed += 0.1
        
        if self.exeleration > 0:
            self.exeleration *= .99
        
    def draw(self):
        pygame.draw.rect(self.surface, self._color, self.rect, border_radius=10)
    
    def is_stopped(self):
        return (not int(self.exeleration)) and (not int(self.fall_speed))
