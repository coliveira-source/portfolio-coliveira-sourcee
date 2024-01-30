import turtle
sides = input ("Enter number of sides: ")
number = sides
#number = int(number)
internal_angle = (360/int(number))
internal_angle = float(internal_angle)
length = float(input ("Enter length of each side: "))

maria = turtle.Turtle()
screen = turtle.Screen()
colors = (str("blue"))

if colors is not None:
    for color in colors:
        maria.color(color)
for i in range (int(number)):
    maria.left(internal_angle)
    maria.forward(length)

screen.exitonclick()
