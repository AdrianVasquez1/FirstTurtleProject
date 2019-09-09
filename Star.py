import turtle

turtle.shape("turtle")
turtle.left(80)
turtle.speed(100)


def star(turtle, size):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

def starSpiral():
    size = 1
    for i in range(60):
        star(turtle, size)
        size = size + 5
        turtle.forward(10)
        turtle.right(5)

turtle.color("green")
starSpiral()
turtle.penup()
turtle.forward(200)
turtle.pendown()

turtle.color("red")
starSpiral()
turtle.penup()
turtle.forward(200)
turtle.pendown()

turtle.color("yellow")
starSpiral()
turtle.forward(100)

turtle.exitonclick()
