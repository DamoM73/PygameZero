import pgzrun
from random import randint

def place_apple():
    apple.x = randint(10,800)
    apple.y = randint(10,600)

def draw():
    screen.clear()
    apple.draw()



def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot!")
        place_apple()
    else:
        print("You missed!")
        quit()

# ----- MAIN PROGRAM ----

apple = Actor("apple")

place_apple()
pgzrun.go()