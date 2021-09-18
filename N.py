import turtle
t = turtle.Turtle()
t.speed(2)
t.pensize(7)
t.pencolor("blue")
turtle.bgcolor("grey")

#for N
t.right(90)
t.forward(10)
t.backward(100)
t.left(90)
t.right(60)
t.forward(120)
t.right(-150)
t.forward(100)
t.right(90)

# for I
t.penup()
t.forward(50)
t.right(90)
t.pendown()
t.forward(90)
t.right(90)
t.forward(40)
t.backward(70)
t.forward(30)
t.right(90)
t.forward(90)
t.right(90)
t.forward(30)
t.backward(55)

# for Y
t.penup()
t.forward(95)
t.pendown()
t.right(105)
t.forward(95)
t.backward(55)
t.right(125)
t.forward(43)

#for O
t.right(130)
t.penup()
t.forward(75)
t.pendown()
t.circle(-40)

#for R
t.penup()
t.forward(65)
t.pendown()
t.circle(-40, 180)
t.left(90)
t.backward(75)
t.forward(115)
t.backward(45)
t.left(48)
t.forward(90)


