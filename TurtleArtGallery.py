import turtle

turtle.shape("turtle")
turtle.penup()
turtle.goto(-200, 100)
turtle.speed(50)
turtle.pendown()
turtle.color("saddle brown")


def square(sidelength):
    for i in range(4):
        turtle.forward(sidelength)
        turtle.right(90)


for i in range(60):
    square(50)
    turtle.right(5)

turtle.color("Dim Gray")
for i in range(60):
    square(25)
    turtle.right(5)

turtle.penup()
turtle.goto(200, 100)
turtle.right(115)
turtle.pendown()

turtle.color("saddle brown")
for i in range(60):
    square(50)
    turtle.right(5)

turtle.color("Dim Gray")
for i in range(60):
    square(25)
    turtle.right(5)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.right(115)


def triangle(sidelength):
    for i in range(3):
        turtle.forward(sidelength)
        turtle.left(120)


turtle.color("gold")
triangle(60)
triangle(30)

turtle.exitonclick()
