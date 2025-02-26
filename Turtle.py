#Question1

import turtle, random

def square(length):
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)

turtle.color("blue")
turtle.pensize(5)
square(100)

#Question 1 bonus

def square(length):
    colors = ['blue', 'red', 'green', 'yellow', 'purple', 'orange', 'cyan','black', ]
    for i in range(20):
        turtle.color(random.choice(colors))
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.right(22)

turtle.color("blue")
turtle.pensize(5)
square(100)


#Question 2

def spirale():
    for i in range(180):
        turtle.circle(i,10)
turtle.color("red")
turtle.pensize(5)
turtle.speed(100)
spirale()   


#Question 3


#Question 3.1


def losange(lenght):
    for i in range(3):
        turtle.forward(lenght)
        turtle.left(60)
        turtle.forward(lenght)
        turtle.left(120)
        turtle.forward(lenght)
        turtle.left(60)
        turtle.forward(lenght)
        return
losange(100)


#Question 3.2


def cube(lenght):
    turtle.begin_fill()
    turtle.color("pink") 
    losange(lenght)
    turtle.end_fill()

    turtle.right(180)

    turtle.begin_fill() 
    turtle.color("blue")
    losange(lenght)
    turtle.end_fill()

    turtle.left(120)
    turtle.forward(lenght)
    turtle.left(60)
    turtle.forward(lenght)
    turtle.right(180)
    
    turtle.begin_fill() 
    turtle.color("purple")
    losange(lenght)
    turtle.end_fill()
    return
cube(100)