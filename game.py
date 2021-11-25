import sys
import random
import turtle
import time

lives=1
score=0

wn = turtle.Screen()
wn.title("Game by @baglanovaaidana")
wn.bgcolor("olive")
wn.setup(width=840, height=840)
wn.tracer(0)
wn.addshape("warrior.gif")
wn.addshape("coin.gif")
#grid-y
grid=turtle.Turtle()
grid.color("darkolivegreen")
y = -390
for ctr in range(14):  ## draw 13 columns
    grid.penup()
    grid.goto(y, 390)
    grid.pendown()
    grid.goto((y, -390))
    y += 60
grid.hideturtle()
#grid-x
gridx=turtle.Turtle()
gridx.color("darkolivegreen")
x = -390
for ctr in range(12):  ## draw 13 columns
    grid.up()
    grid.goto(390, x)
    grid.down()
    grid.goto((-390, x))
    x += 60
gridx.hideturtle()
#create warrior
warrior=turtle.Turtle()
warrior.speed(3)
warrior.shape("warrior.gif") 
warrior.shapesize(stretch_wid=0.3, stretch_len=0.3)
warrior.penup()
warrior.goto(0, 0)
warrior.dx=2
warrior.dy=-2

#score
pen=turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.goto(0, 390)
pen.pendown()
pen.write('Score:{} Lives:{}'.format(score, lives), align='center',font=('Courier', 60))
#coins
coins=[]
for _ in range(10):
    coin=turtle.Turtle()
    coin.shape("coin.gif")
    coin.shapesize(stretch_wid=0.4, stretch_len=0.4)
    coin.penup()
    y=random.randint(-405, 405)
    x=random.randint(-405, 405)
    coin.setposition(x,y)
    coins.append(coin)
#functions to move warrior
def warrior_up():
    y = warrior.ycor()
    y += 60
    warrior.sety(y)
def warrior_down():
    y = warrior.ycor()
    y -= 60
    warrior.sety(y)
def warrior_right():
    x = warrior.xcor()
    x += 60
    warrior.setx(x)
def warrior_left():
    x = warrior.xcor()
    x -= 60
    warrior.setx(x)
# keybord binding
wn.listen()
wn.onkeypress(warrior_up, "Up")
wn.onkeypress(warrior_down, "Down")
wn.onkeypress(warrior_left, "Left")
wn.onkeypress(warrior_right, "Right")
while True:
    wn.update()
    #border check
    if warrior.ycor()>400:
        warrior.sety(400)
        warrior.dy *= -1
    if warrior.ycor()<-400:
        warrior.sety(-400)
        warrior.dy *= -1   
    if warrior.xcor()>400:
        warrior.goto(0, 0)
        warrior.dx *= -1
    if warrior.xcor()<-400:
        warrior.goto(0, 0)
        warrior.dx *= -1
    
    for coin in coins:
        if warrior.distance(coin)<60:
            y=random.randint(-405, 405)
            x=random.randint(-405,  405)
            coin.goto(x,y)

