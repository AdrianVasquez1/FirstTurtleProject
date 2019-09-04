import turtle

turtle.shape("turtle")
turtle.speed(500)
turtle.color("lime")

def square(sidelength):
    for i in range(4):
        turtle.forward(sidelength)
        turtle.right(90)



for i in range(60):
    square(200)
    turtle.right(5)


turtle.exitonclick()
