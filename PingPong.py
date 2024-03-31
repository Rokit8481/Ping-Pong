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
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 500 - 150:
            self.rect.x += self.speed

    def update_down(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 500 - 150:
            self.rect.x += self.speed

class Ball(GameSprite):
    def __init__(self, ball_image, ball_x, ball_y, size_x, size_y, ball_speed_x, ball_speed_y):
        super().__init__(ball_image, ball_x, ball_y, size_x, size_y, ball_speed_x)
        self.speed_y = ball_speed_y
        self.start_time = time.get_ticks()
    def update(self):
        if time.get_ticks() - self.start_time > 1000:
            self.rect.x += self.speed
            self.rect.y += self.speed_y

        if self.rect.x > 460 or self.rect.x < -10:
            self.speed *= -1

        if self.rect.colliderect(player1.rect) or self.rect.colliderect(player2.rect):
            self.speed_y *= -1

def display_text(text, x, y, color=(255, 255, 255)):  # Додавання параметру color
    text_surface = my_font.render(text, True, color)
    window.blit(text_surface, (x, y))

player1 = Player(img_player, 170, 560, 150, 30, 10)
player2 = Player(img_player, 170, 100, 150, 30, 10)
ball = Ball("ball.png", 235, 335, 50, 50, 2, 2)

font.init()
font_path = font.match_font('arial')
my_font = font.Font(font_path, 30)

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
    ball.update()

    if ball.rect.y < 0:
        display_text("Гравець 2 програв", 150, 350, color=(255, 0, 0)) 
        display_text("Гравець 1 виграв", 150, 300, color=(0, 255, 0)) 
    elif ball.rect.y > 700:
        display_text("Гравець 1 програв", 150, 350, color=(255, 0, 0)) 
        display_text("Гравець 2 виграв", 150, 300, color=(0, 255, 0)) 

    if ball.rect.y < 0 or ball.rect.y > 700: 
        player1.speed = 0
        player2.speed = 0

    player1.reset()
    player2.reset()
    ball.reset()

    display.update()
    clock.tick(FPS)
