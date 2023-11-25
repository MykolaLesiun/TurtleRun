import random, turtle

scr=turtle.Screen()

scr.bgcolor("light blue")
scr.setup(0.8,0.7)

pen=turtle.Turtle()

pen.speed(0)
pen.penup()
pen.goto(-450,200)
pen.pendown()
finishLineX=450

def draw_lines():
    
    for i in range(1,11):
        pen.pendown()
        pen.write(i, font=('Arial',13))
        pen.setheading(-90)
        pen.forward(400)
        pen.penup()
        pen.goto(pen.xcor()+100,200)
        
    pen.goto(finishLineX,-200)
    pen.write("Finish", align="left", font=('Arial',15))
    pen.penup()
    pen.goto(550,200)

def create_player(color, startx, starty):
    player=turtle.Turtle()
    player.color(color)
    player.shape("turtle")
    player.penup()
    player.goto(startx, starty)
    player.pendown()
    return player

p1=create_player('indian red',-460,150)
p2=create_player('deep sky blue',-460,100)
p3=create_player('yellow',-460,50)
p4=create_player('green',-460,0)
p5=create_player('indigo',-460,-50)
p6=create_player('orange',-460,-100)

draw_lines()

while True:
    p1.forward(random.randint(5,10))
    if p1.pos()[0]>=finishLineX:
        p1.write(' I won!',font=('Arial',13))
        break
    p2.forward(random.randint(5,10))
    if p2.pos()[0]>=finishLineX:
        p2.write(' I won!',font=('Arial',13))
        break
    p3.forward(random.randint(5,10))
    if p3.pos()[0]>=finishLineX:
        p3.write(' I won!',font=('Arial',13))
        break
    p4.forward(random.randint(5,10))
    if p4.pos()[0]>=finishLineX:
        p4.write(' I won!',font=('Arial',13))
        break
    p5.forward(random.randint(5,10))
    if p5.pos()[0]>=finishLineX:
        p5.write(' I won!',font=('Arial',13))
        break
    p6.forward(random.randint(5,10))
    if p6.pos()[0]>=finishLineX:
        p6.write(' I won!',font=('Arial',13))
        break
