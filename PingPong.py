from pygame import *

window = display.set_mode((500, 700))
display.set_caption('Пінг-Понг')
background = transform.scale(image.load("sky.jpg"), (500, 700))

clock = time.Clock()
FPS = 60

game = True

while game:
    window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)