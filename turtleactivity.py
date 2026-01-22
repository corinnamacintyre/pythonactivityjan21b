import turtle

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("white") 

box2 =turtle.Turtle()
box2.shape("square")
box2.color("lime")
box2.shapesize(21,21)

box = turtle.Turtle()
box.shape("square")
box.color("black")
box.shapesize(20,20)

screen.addshape("loading.png")
loading = turtle.Turtle()
loading.shape("loading.png")
loading.shapesize(1,6)

screen.addshape("deltasoul.png")
soul = turtle.Turtle()
soul.hideturtle()
soul.shape("deltasoul.png")
soul.penup()
soul.speed(1)

screen.addshape("tobyfoxdog.gif")
annoyingdog = turtle.Turtle()
annoyingdog.hideturtle()
annoyingdog.shape("tobyfoxdog.gif")
annoyingdog.penup()

annoyingdog.speed(1)
annoyingdog.right(90)
annoyingdog.forward(160)
annoyingdog.left(90)

loading.hideturtle()
soul.showturtle()
annoyingdog.showturtle()
annoyingdog.speed(1)

soul.right(90)
annoyingdog.forward(150)
soul.speed(3)
soul.forward(100)
soul.speed(2)
soul.right(180)
soul.forward(10)
soul.right(90)
soul.forward(5)
soul.left(90)
soul.forward(5)
soul.speed(1)
soul.forward(5)
soul.forward(20)
soul.right(90)
annoyingdog.left(180)
soul.forward(125)

walkcycle = True
while walkcycle == True:
    annoyingdog.forward(300)
    annoyingdog.right(180)
    soul.right(180)
    soul.forward(250)
    annoyingdog.forward(300)
    annoyingdog.right(180)
    soul.left(180)
    soul.forward(250)

turtle.done()
