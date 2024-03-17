from pygame import *

window = display.set_mode((500, 700))
display.set_caption('Пінг-Понг')
background = transform.scale(image.load("sky.jpg"), (500, 700))

img_player = "platform1.png"


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
 
        self.image = transform.scale(
            image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_up(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 500 - 150:
            self.rect.x += self.speed

    def update_down(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 500 - 150:
            self.rect.x += self.speed

player1 = Player(img_player, 170, 560, 150, 30, 10)
player2 = Player(img_player, 170, 100, 150, 30, 10)

clock = time.Clock()
FPS = 60

game = True

while game:
    window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    player1.update_up()  
    player2.update_down()  
    #player1.update()
    #player2.update()

    player1.reset()
    player2.reset()
    display.update()
    clock.tick(FPS)