import turtle  # 1. import modules
import random
import pygame
import math

# Part A (race 1)
window = turtle.Screen()
window.bgcolor("lightblue")

michelangelo = turtle.Turtle()  # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color("orange")
leonardo.color("blue")
michelangelo.shape("turtle")
leonardo.shape("turtle")

michelangelo.up()  # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

x=random.randrange(1,100)
y=random.randrange(1,100)
print(x)
print(y)

leonardo.forward(x)
michelangelo.forward(y)

# Race 2
for i in range (10):
    x=random.randrange(1,10)
    y=random.randrange(1,10)
    leonardo.forward(x)
    michelangelo.forward(y)
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

window.exitonclick()

#Part B

pygame.init()

while True:
    for event in pygame.event.get():
        pass 
    window = pygame.display.set_mode()

    num_sides = [3, 4, 6, 20, 100, 360]
    xpos= 500
    ypos= 500 #where it starts on the screen
    side_length= 100
    points=[]
    
    for _ in (num_sides):
        for i in range(_):
            angle = 360/_
            radians = math.radians(angle * i)
            x = xpos + side_length * math.cos(radians)
            y = ypos + side_length * math.sin(radians)
            points.append([x,y])
        window.fill("purple")
        pygame.draw.polygon (window, "pink", points)
        pygame.display.flip()
        pygame.time.wait(500)
        points=[]
    
    break
