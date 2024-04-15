import turtle
import time
from datetime import datetime
import keyboard
wn=turtle.Screen()
wn.title("Football")
wn.bgcolor("lawn green")
wn.setup(width=1500, height=780)
wn.tracer(0)
#IMPORTANT VARIABLES
i=1
j=1
p=0
score_a=0
score_b=0
#TOUCHLINES
k=(-750,390)
l=(750,390)
turtle.penup()
turtle.goto(k)
turtle.pendown()
turtle.goto(l)
turtle.hideturtle()
y=(-750,-390)
z=(750,-390)
turtle.penup()
turtle.goto(y)
turtle.pendown()
turtle.goto(z)
turtle.hideturtle()
turtle.penup()
turtle.goto(y)
turtle.pendown()
turtle.goto(k)
turtle.hideturtle()
turtle.penup()
turtle.goto(z)
turtle.pendown()
turtle.goto(l)
turtle.hideturtle()
#PITCH MID LINE
x=(0,-390)
y=(0,390)
turtle.penup()
turtle.goto(x)
turtle.pendown()
turtle.goto(y)
turtle.hideturtle()
#SCORECARD
pen = turtle.Turtle()
pen.speed()
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,350)
pen.write("A:0  B:0", align="center", font=("Courier", 24, "bold"))
#PREVIOUS RESULTS
penp1 = turtle.Turtle()
penp1.speed()
penp1.color("black")
penp1.penup()
penp1.hideturtle()
penp1.goto(0,100)
penp2 = turtle.Turtle()
penp2.speed()
penp2.color("black")
penp2.penup()
penp2.hideturtle()
penp2.goto(0,-20)
penp3 = turtle.Turtle()
penp3.speed()
penp3.color("black")
penp3.penup()
penp3.hideturtle()
penp3.goto(0,-100)
penp4 = turtle.Turtle()
penp4.speed()
penp4.color("black")
penp4.penup()
penp4.hideturtle()
penp4.goto(0,200)

#GOALS
a=(-750,100)
b=(-660,100)
turtle.penup()
turtle.goto(a)
turtle.pendown()
turtle.goto(b)
turtle.hideturtle()

c=(-750,-100)
d=(-660,-100)
turtle.penup()
turtle.goto(c)
turtle.pendown()
turtle.goto(d)
turtle.hideturtle()

turtle.penup()
turtle.goto(d)
turtle.pendown()
turtle.goto(b)
turtle.hideturtle()

e=(750,100)
f=(660,100)
turtle.penup()
turtle.goto(e)
turtle.pendown()
turtle.goto(f)
turtle.hideturtle()

g=(750,-100)
h=(660,-100)
turtle.penup()
turtle.goto(g)
turtle.pendown()
turtle.goto(h)
turtle.hideturtle()

turtle.penup()
turtle.goto(h)
turtle.pendown()
turtle.goto(f)
turtle.hideturtle()
#DECLARATIONS
Pen = turtle.Turtle()
Pen.speed(0)
Pen.color("black")
Pen.penup()
Pen.hideturtle()
Pen.goto(0,0)
#TIME DISPLAY
pen1=turtle.Turtle()
pen1.speed(0)
pen1.color("black")
pen1.penup()
pen1.hideturtle()
pen1.goto(-720,380)
#BALL
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(1)
ball.color("blue")
ball.penup()
ball.goto(0,0)
ball.dx=0
ball.dy=0
#PLAYER A GK
player_a_gk=turtle.Turtle()
player_a_gk.speed(0)
player_a_gk.shape("square")
player_a_gk.shapesize(1.5,1.5)
player_a_gk.color("red")
player_a_gk.penup()
player_a_gk.goto(-660,0)
#PLAYER B GK
player_b_gk=turtle.Turtle()
player_b_gk.speed(0)
player_b_gk.shape("square")
player_b_gk.shapesize(1.5,1.5)
player_b_gk.color("yellow")
player_b_gk.penup()
player_b_gk.goto(660,0)
#PLAYER A ATT
player_a_att1=turtle.Turtle()
player_a_att1.speed(0)
player_a_att1.shape("square")
player_a_att1.shapesize(1.5,1.5)
player_a_att1.color("red")
player_a_att1.penup()
player_a_att1.goto(-100,120)
player_a_att1.dx=0
player_a_att1.dy=0
#PLAYER B ATT
player_b_att1=turtle.Turtle()
player_b_att1.speed(0)
player_b_att1.shape("square")
player_b_att1.shapesize(1.5,1.5)
player_b_att1.color("yellow")
player_b_att1.penup()
player_b_att1.goto(100,120)
player_b_att1.dx=0
player_b_att1.dy=0
#PLAYER A MID
player_a_mid1=turtle.Turtle()
player_a_mid1.speed(0)
player_a_mid1.shape("square")
player_a_mid1.shapesize(1.5,1.5)
player_a_mid1.color("red")
player_a_mid1.penup()
player_a_mid1.goto(-200,-120)
player_a_mid1.dx=0
player_a_mid1.dy=0
#PLAYER B MID
player_b_mid1=turtle.Turtle()
player_b_mid1.speed(0)
player_b_mid1.shape("square")
player_b_mid1.shapesize(1.5,1.5)
player_b_mid1.color("yellow")
player_b_mid1.penup()
player_b_mid1.goto(200,-120)
player_b_mid1.dx=0
player_b_mid1.dy=0
#PLAYER A DEF 1
player_a_def1=turtle.Turtle()
player_a_def1.speed(0)
player_a_def1.shape("square")
player_a_def1.shapesize(1.5,1.5)
player_a_def1.color("red")
player_a_def1.penup()
player_a_def1.goto(-460,90)
player_a_def1.dx=0
player_a_def1.dy=0
#PLAYER A DEF 2
player_a_def2=turtle.Turtle()
player_a_def2.speed(0)
player_a_def2.shape("square")
player_a_def2.shapesize(1.5,1.5)
player_a_def2.color("red")
player_a_def2.penup()
player_a_def2.goto(-460,-90)
player_a_def2.dx=0
player_a_def2.dy=0
#PLAYER B DEF 1
player_b_def1=turtle.Turtle()
player_b_def1.speed(0)
player_b_def1.shape("square")
player_b_def1.shapesize(1.5,1.5)
player_b_def1.color("yellow")
player_b_def1.penup()
player_b_def1.goto(460,90)
player_b_def1.dx=0
player_b_def1.dy=0
#PLAYER B DEF 2
player_b_def2=turtle.Turtle()
player_b_def2.speed(0)
player_b_def2.shape("square")
player_b_def2.shapesize(1.5,1.5)
player_b_def2.color("yellow")
player_b_def2.penup()
player_b_def2.goto(460,-90)
player_b_def2.dx=0
player_b_def2.dy=0

#START GAME


#MOVEMENT
def movement_up():
    player_a_att1.dx=0
    player_a_def1.dx=0
    player_a_def2.dx=0
    player_a_mid1.dx=0
    player_a_att1.dy=0
    player_a_def1.dy=0
    player_a_def2.dy=0
    player_a_mid1.dy=0
    global i
    global j
    if i==1:

        if 750>=player_a_att1.xcor()>=660 and 140>player_a_att1.ycor()>-140:
            pass
        elif -660>=player_a_att1.xcor()>=-750 and 140>player_a_att1.ycor()>-140:
            pass
        else:
            if -30<ball.ycor()-player_a_att1.ycor()<30 and -20<ball.xcor()-player_a_att1.xcor()<20:
                ball.dx=0
                ball.dy=0.4
                ball.sety(player_a_att1.ycor()+ball.dy)
            player_a_att1.dy=0.4
            player_a_att1.sety(player_a_att1.ycor()+player_a_att1.dy)
            player_a_mid1.dy=0.4
            player_a_mid1.sety(player_a_mid1.ycor()+player_a_mid1.dy)
    elif i==2:
         if 750>=player_a_mid1.xcor()>=660 and 140>player_a_mid1.ycor()>-140:
            pass
         elif -660>=player_a_mid1.xcor()>=-750 and 140>player_a_mid1.ycor()>-140:
            pass
         else:
            y=player_a_mid1.ycor()
            if -30<ball.ycor()-player_a_mid1.ycor()<30 and -20<ball.xcor()-player_a_mid1.xcor()<20:
                ball.dx=0
                ball.dy=0.4
                ball.sety(ball.ycor()+ball.dy)
            player_a_mid1.dy=0.4
            player_a_mid1.sety(player_a_mid1.ycor()+player_a_mid1.dy)
            player_a_att1.dy=0.4
            player_a_att1.sety(player_a_att1.ycor()+player_a_att1.dy)
    elif i==3:
        if 750>=player_a_def1.xcor()>=660 and 140>player_a_def1.ycor()>-140:
            pass
        elif -660>=player_a_def1.xcor()>=-750 and 140>player_a_def1.ycor()>-140:
            pass
        
        else:
            if -30<ball.ycor()-player_a_def1.ycor()<30 and -20<ball.xcor()-player_a_def1.xcor()<20:
                ball.dx=0
                ball.dy=0.4
                ball.sety(ball.ycor()+ball.dy)
            player_a_def1.dy=0.4
            player_a_def1.sety(player_a_def1.ycor()+player_a_def1.dy)
            player_a_def2.dy=0.4
            player_a_def2.sety(player_a_def2.ycor()+player_a_def2.dy)
    elif i==4:
        if 750>=player_a_def2.xcor()>=660 and 140>player_a_def2.ycor()>-140:
            pass
        elif -660>=player_a_def2.xcor()>=-750 and 140>player_a_def2.ycor()>-140:
            pass
       
        else:
            if -30<ball.ycor()-player_a_def2.ycor()<30 and -20<ball.xcor()-player_a_def2.xcor()<20:
                ball.dx=0
                ball.dy=0.4
                ball.sety(ball.ycor()+ball.dy)
            player_a_def2.dy=0.4
            player_a_def2.sety(player_a_def2.ycor()+player_a_def2.dy)
            player_a_def1.dy=0.4
            player_a_def1.sety(player_a_def1.ycor()+player_a_def1.dy)
def movement_down():
    player_a_att1.dx=0
    player_a_def1.dx=0
    player_a_def2.dx=0
    player_a_mid1.dx=0
    player_a_att1.dy=0
    player_a_def1.dy=0
    player_a_def2.dy=0
    player_a_mid1.dy=0
    global i
    global j
    if i==1:
        if 750>=player_a_att1.xcor()>=660 and 140>player_a_att1.ycor()>-140:
            pass
        elif -660>=player_a_att1.xcor()>=-750 and 140>player_a_att1.ycor()>-140:
            pass
        else:
            y=player_a_att1.ycor()
            if -30<ball.ycor()-player_a_att1.ycor()<30 and -20<ball.xcor()-player_a_att1.xcor()<20:
                ball.dx=0
                ball.dy=-0.4
                ball.sety(ball.ycor()+ball.dy)
            player_a_att1.dy=-0.4
            player_a_att1.sety(player_a_att1.ycor()+player_a_att1.dy)
            player_a_mid1.dy=-0.4
            player_a_mid1.sety(player_a_mid1.ycor()+player_a_mid1.dy)
    elif i==2:
        if 750>=player_a_mid1.xcor()>=660 and 140>player_a_mid1.ycor()>-140:
            pass
        elif -660>=player_a_mid1.xcor()>=-750 and 140>player_a_mid1.ycor()>-140:
            pass
        else:
            y=player_a_mid1.ycor()
            if -30<ball.ycor()-player_a_mid1.ycor()<30 and -20<ball.xcor()-player_a_mid1.xcor()<20:
                ball.dx=0
                ball.dy=-0.4
                ball.sety(ball.ycor()+ball.dy)
            player_a_mid1.dy=-0.4
            player_a_mid1.sety(player_a_mid1.ycor()+player_a_mid1.dy)
            player_a_att1.dy=-0.4
            player_a_att1.sety(player_a_att1.ycor()+player_a_att1.dy)
    elif i==3:
        if 750>=player_a_def1.xcor()>=660 and 140>player_a_def1.ycor()>-140:
            pass
        elif -660>=player_a_def1.xcor()>=-750 and 140>player_a_def1.ycor()>-140:
            pass
       
        else:
            if -30<ball.ycor()-player_a_def1.ycor()<30 and -20<ball.xcor()-player_a_def1.xcor()<20:
                ball.dx=0
                ball.dy=-0.4
                ball.sety(ball.ycor()+ball.dy)
            player_a_def1.dy=-0.4
            player_a_def1.sety(player_a_def1.ycor()+player_a_def1.dy)
            player_a_def2.dy=-0.4
            player_a_def2.sety(player_a_def2.ycor()+player_a_def2.dy)
    elif i==4:
        if 750>=player_a_def2.xcor()>=660 and 140>player_a_def2.ycor()>-140:
            pass
        elif -660>=player_a_def2.xcor()>=-750 and 140>player_a_def2.ycor()>-140:
            pass
       
        else:
            if -30<ball.ycor()-player_a_def2.ycor()<30 and -20<ball.xcor()-player_a_def2.xcor()<20:
                ball.dx=0
                ball.dy=-0.4
                ball.sety(ball.ycor()+ball.dy)
            player_a_def2.dy=-0.4
            player_a_def2.sety(player_a_def2.ycor()+player_a_def2.dy)
            player_a_def1.dy=-0.4
            player_a_def1.sety(player_a_def1.ycor()+player_a_def1.dy)
t1=0
t2=0
t3=0
t4=0
t5=0
t6=0
t7=0
t8=0

def movement_left():
    global i
    global j
    global t1
    global t2
    global t5
    global t6
    player_a_att1.dy=0
    player_a_def1.dy=0
    player_a_def2.dy=0
    player_a_mid1.dy=0
    player_a_att1.dx=0
    player_a_def1.dx=0
    player_a_def2.dx=0
    player_a_mid1.dx=0
    if i==1:
            t1=1
            if -30<ball.ycor()-player_a_att1.ycor()<30 and -20<ball.xcor()-player_a_att1.xcor()<20:
                ball.dy=0
                ball.dx=-0.4
                ball.setx(ball.xcor()+ball.dx)
                
            player_a_att1.dx=-0.4
            player_a_att1.setx(player_a_att1.xcor()+player_a_att1.dx)
            player_a_mid1.dx=-0.4
            player_a_mid1.setx(player_a_mid1.xcor()+player_a_mid1.dx)
    elif i==2:
            t2=1
            if -30<ball.ycor()-player_a_mid1.ycor()<30 and -20<ball.xcor()-player_a_mid1.xcor()<20:
                ball.dy=0
                ball.dx=-0.4
                ball.setx(ball.xcor()+ball.dx)
            player_a_mid1.dx=-0.4
            player_a_mid1.setx(player_a_mid1.xcor()+player_a_mid1.dx)
            player_a_att1.dx=-0.4
            player_a_att1.setx(player_a_att1.xcor()+player_a_att1.dx)
    elif i==3:
            t6=1
            if -30<ball.ycor()-player_a_def1.ycor()<30 and -20<ball.xcor()-player_a_def1.xcor()<20:
                ball.dy=0
                ball.dx=-0.4
                ball.setx(ball.xcor()+ball.dx)
            player_a_def1.dx=-0.4
            player_a_def1.setx(player_a_def1.xcor()+player_a_def1.dx)
            player_a_def2.dx=-0.4
            player_a_def2.setx(player_a_def2.xcor()+player_a_def2.dx)
    elif i==4:
            t5=1
            if -30<ball.ycor()-player_a_def2.ycor()<30 and -20<ball.xcor()-player_a_def2.xcor()<20:
                ball.dy=0
                ball.dx=-0.4
                ball.setx(ball.xcor()+ball.dx)
            player_a_def2.dx=-0.4
            player_a_def2.setx(player_a_def2.xcor()+player_a_def2.dx)
            player_a_def1.dx=-0.4
            player_a_def1.setx(player_a_def1.xcor()+player_a_def1.dx)
    
   
def movement_right():
    global i
    global j
    global t1
    global t2
    global t5
    global t6
    player_a_att1.dy=0
    player_a_def1.dy=0
    player_a_def2.dy=0
    player_a_mid1.dy=0
    player_a_att1.dx=0
    player_a_def1.dx=0
    player_a_def2.dx=0
    player_a_mid1.dx=0
    if i==1:
            t1=0
            if -30<ball.ycor()-player_a_att1.ycor()<30 and -20<ball.xcor()-player_a_att1.xcor()<20:
                ball.dy=0
                ball.dx=0.4
                ball.setx(ball.xcor()+ball.dx)
            player_a_att1.dx=0.4
            player_a_att1.setx(player_a_att1.xcor()+player_a_att1.dx)
            player_a_mid1.dx=0.4
            player_a_mid1.setx(player_a_mid1.xcor()+player_a_mid1.dx)
    elif i==2:
            t2=0
            if -30<ball.ycor()-player_a_mid1.ycor()<30 and -20<ball.xcor()-player_a_mid1.xcor()<20:
                ball.dy=0
                ball.dx=0.4
                ball.setx(ball.xcor()+ball.dx)
            player_a_mid1.dx=0.4
            player_a_mid1.setx(player_a_mid1.xcor()+player_a_mid1.dx)
            player_a_att1.dx=0.4
            player_a_att1.setx(player_a_att1.xcor()+player_a_att1.dx)
    elif i==3:
            t6=0
            if -30<ball.ycor()-player_a_def1.ycor()<30 and -20<ball.xcor()-player_a_def1.xcor()<20:
                ball.dy=0
                ball.dx=0.4
                ball.setx(ball.xcor()+ball.dx)
            player_a_def1.dx=0.4
            player_a_def1.setx(player_a_def1.xcor()+player_a_def1.dx)
            player_a_def2.dx=0.4
            player_a_def2.setx(player_a_def2.xcor()+player_a_def2.dx)
    elif i==4:
            t5=0
            if -30<ball.ycor()-player_a_def2.ycor()<30 and -20<ball.xcor()-player_a_def2.xcor()<20:
                ball.dy=0
                ball.dx=0.4
                ball.setx(ball.xcor()+ball.dx)
            player_a_def2.dx=0.4
            player_a_def2.setx(player_a_def2.xcor()+player_a_def2.dx)
            player_a_def1.dx=0.4
            player_a_def1.setx(player_a_def1.xcor()+player_a_def1.dx)
def movement_up_1():
    player_b_att1.dx=0
    player_b_def1.dx=0
    player_b_def2.dx=0
    player_b_mid1.dx=0
    player_b_att1.dy=0
    player_b_def1.dy=0
    player_b_def2.dy=0
    player_b_mid1.dy=0
    global i
    global j

    if j==1:

        if 750>=player_b_att1.xcor()>=660 and 140>player_b_att1.ycor()>-140:
            pass
        elif -660>=player_b_att1.xcor()>=-750 and 140>player_b_att1.ycor()>-140:
            pass
        else:
            
            if -30<ball.ycor()-player_b_att1.ycor()<30 and -20<ball.xcor()-player_b_att1.xcor()<20:
                ball.dx=0
                ball.dy=0.4
                ball.sety(ball.ycor()+ball.dy)
            player_b_att1.dy=0.4
            player_b_att1.sety(player_b_att1.ycor()+player_b_att1.dy)
            player_b_mid1.dy=0.4
            player_b_mid1.sety(player_b_mid1.ycor()+player_b_mid1.dy)
    elif j==2:
         if 750>=player_b_mid1.xcor()>=660 and 140>player_b_mid1.ycor()>-140:
            pass
         elif -660>=player_b_mid1.xcor()>=-750 and 140>player_b_mid1.ycor()>-140:
            pass
         else:
            
            if -30<ball.ycor()-player_b_mid1.ycor()<30 and -20<ball.xcor()-player_b_mid1.xcor()<20:
                ball.dx=0
                ball.dy=0.4
                ball.sety(ball.ycor()+ball.dy)
            player_b_mid1.dy=0.4
            player_b_mid1.sety(player_b_mid1.ycor()+player_b_mid1.dy)
            player_b_att1.dy=0.4
            player_b_att1.sety(player_b_att1.ycor()+player_b_att1.dy)
    elif j==3:
        if 750>=player_b_def1.xcor()>=660 and 140>player_b_def1.ycor()>-140:
            pass
        elif -660>=player_b_def1.xcor()>=-750 and 140>player_b_def1.ycor()>-140:
            pass
        
        else:
            if -30<ball.ycor()-player_b_def1.ycor()<30 and -20<ball.xcor()-player_b_def1.xcor()<20:
                ball.dx=0
                ball.dy=0.4
                ball.sety(ball.ycor()+ball.dy)
            player_b_def1.dy=0.4
            player_b_def1.sety(player_b_def1.ycor()+player_b_def1.dy)
            player_b_def2.dy=0.4
            player_b_def2.sety(player_b_def2.ycor()+player_b_def2.dy)
    elif j==4:
        if 750>=player_b_def2.xcor()>=660 and 140>player_b_def2.ycor()>-140:
            pass
        elif -660>=player_b_def2.xcor()>=-750 and 140>player_b_def2.ycor()>-140:
            pass
       
        else:
            if -30<ball.ycor()-player_b_def2.ycor()<30 and -20<ball.xcor()-player_b_def2.xcor()<20:
                ball.dx=0
                ball.dy=0.4
                ball.sety(ball.ycor()+ball.dy)
            player_b_def2.dy=0.4
            player_b_def2.sety(player_b_def2.ycor()+player_b_def2.dy)
            player_b_def1.dy=0.4
            player_b_def1.sety(player_b_def1.ycor()+player_b_def1.dy)
def movement_down_2():
    player_b_att1.dx=0
    player_b_def1.dx=0
    player_b_def2.dx=0
    player_b_mid1.dx=0
    player_b_att1.dy=0
    player_b_def1.dy=0
    player_b_def2.dy=0
    player_b_mid1.dy=0
    global i
    global j

    
    if j==1:
        if 750>=player_b_att1.xcor()>=660 and 140>player_b_att1.ycor()>-140:
            pass
        elif -660>=player_b_att1.xcor()>=-750 and 140>player_b_att1.ycor()>-140:
            pass
        else:
            if -30<ball.ycor()-player_b_att1.ycor()<30 and -20<ball.xcor()-player_b_att1.xcor()<20:
                ball.dx=0
                ball.dy=-0.4
                ball.sety(ball.ycor()+ball.dy)
            player_b_att1.dy=-0.4
            player_b_att1.sety(player_b_att1.ycor()+player_b_att1.dy)
            player_b_mid1.dy=-0.4
            player_b_mid1.sety(player_b_mid1.ycor()+player_b_mid1.dy)
    elif j==2:
        if 750>=player_b_mid1.xcor()>=660 and 140>player_b_mid1.ycor()>-140:
            pass
        elif -660>=player_b_mid1.xcor()>=-750 and 140>player_b_mid1.ycor()>-140:
            pass
        else:
            if -30<ball.ycor()-player_b_mid1.ycor()<30 and -20<ball.xcor()-player_b_mid1.xcor()<20:
                ball.dx=0
                ball.dy=-0.4
                ball.sety(ball.ycor()+ball.dy)
            player_b_mid1.dy=-0.4
            player_b_mid1.sety(player_b_mid1.ycor()+player_b_mid1.dy)
            player_b_att1.dy=-0.4
            player_b_att1.sety(player_b_att1.ycor()+player_b_att1.dy)
    elif j==3:
        if 750>=player_b_def1.xcor()>=660 and 140>player_b_def1.ycor()>-140:
            pass
        elif -660>=player_b_def1.xcor()>=-750 and 140>player_b_def1.ycor()>-140:
            pass
       
        else:
            if -30<ball.ycor()-player_b_def1.ycor()<30 and -20<ball.xcor()-player_b_def1.xcor()<20:
                ball.dx=0
                ball.dy=-0.4
                ball.sety(ball.ycor()+ball.dy)
            player_b_def1.dy=-0.4
            player_b_def1.sety(player_b_def1.ycor()+player_b_def1.dy)
            player_b_def2.dy=-0.4
            player_b_def2.sety(player_b_def2.ycor()+player_b_def2.dy)
    elif j==4:
        if 750>=player_b_def2.xcor()>=660 and 140>player_b_def2.ycor()>-140:
            pass
        elif -660>=player_b_def2.xcor()>=-750 and 140>player_b_def2.ycor()>-140:
            pass
       
        else:
            if -30<ball.ycor()-player_b_def2.ycor()<30 and -20<ball.xcor()-player_b_def2.xcor()<20:
                ball.dx=0
                ball.dy=-0.4
                ball.sety(ball.ycor()+ball.dy)
            player_b_def2.dy=-0.4
            player_b_def2.sety(player_b_def2.ycor()+player_b_def2.dy)
            player_b_def1.dy=-0.4
            player_b_def1.sety(player_b_def1.ycor()+player_b_def1.dy)


def movement_left_3():
    global t3
    global t4
    global t7
    global t8
    player_b_att1.dx=0
    player_b_def1.dx=0
    player_b_def2.dx=0
    player_b_mid1.dx=0
    player_b_att1.dy=0
    player_b_def1.dy=0
    player_b_def2.dy=0
    player_b_mid1.dy=0
    global i
    global j

    if j==1:
            t3=1
            if -30<ball.ycor()-player_b_att1.ycor()<30 and -20<ball.xcor()-player_b_att1.xcor()<20:
                ball.dy=0
                ball.dx=-0.4
                ball.setx(ball.xcor()+ball.dx)
            player_b_att1.dx=-0.4
            player_b_att1.setx(player_b_att1.xcor()+player_b_att1.dx)
            player_b_mid1.dx=-0.4
            player_b_mid1.setx(player_b_mid1.xcor()+player_b_mid1.dx)
    elif j==2:
            t4=1
            if -30<ball.ycor()-player_b_mid1.ycor()<30 and -20<ball.xcor()-player_b_mid1.xcor()<20:
                ball.dy=0
                ball.dx=-0.4
                ball.setx(ball.xcor()+ball.dx)
            player_b_mid1.dx=-0.4
            player_b_mid1.setx(player_b_mid1.xcor()+player_b_mid1.dx)
            player_b_att1.dx=-0.4
            player_b_att1.setx(player_b_att1.xcor()+player_b_att1.dx)
    elif j==3:
            t7=1
            if -30<ball.ycor()-player_b_def1.ycor()<30 and -20<ball.xcor()-player_b_def1.xcor()<20:
                ball.dy=0
                ball.dx=-0.4
                ball.setx(ball.xcor()+ball.dx)
            player_b_def1.dx=-0.4
            player_b_def1.setx(player_b_def1.xcor()+player_b_def1.dx)
            player_b_def2.dx=-0.4
            player_b_def2.setx(player_b_def2.xcor()+player_b_def2.dx)
    elif j==4:
            t8=1
            if -30<ball.ycor()-player_b_def2.ycor()<30 and -20<ball.xcor()-player_b_def2.xcor()<20:
                ball.dy=0
                ball.dx=-0.4
                ball.setx(ball.xcor()+ball.dx)
            player_b_def2.dx=-0.4
            player_b_def2.setx(player_b_def2.xcor()+player_b_def2.dx)
            player_b_def1.dx=-0.4
            player_b_def1.setx(player_b_def1.xcor()+player_b_def1.dx)
   

def movement_right_4():
    global t3
    global t4
    global t7
    global t8
    player_b_att1.dx=0
    player_b_def1.dx=0
    player_b_def2.dx=0
    player_b_mid1.dx=0
    player_b_att1.dy=0
    player_b_def1.dy=0
    player_b_def2.dy=0
    player_b_mid1.dy=0
    global i
    global j

    if j==1:
            t3=0
            if -30<ball.ycor()-player_b_att1.ycor()<30 and -20<ball.xcor()-player_b_att1.xcor()<20:
                ball.dy=0
                ball.dx=0.4
                ball.setx(ball.xcor()+ball.dx)
            player_b_att1.dx=0.4
            player_b_att1.setx(player_b_att1.xcor()+player_b_att1.dx)
            player_b_mid1.dx=0.4
            player_b_mid1.setx(player_b_mid1.xcor()+player_b_mid1.dx)
    elif j==2:
            t4=0
            if -30<ball.ycor()-player_b_mid1.ycor()<30 and -20<ball.xcor()-player_b_mid1.xcor()<20:
                ball.dy=0
                ball.dx=0.4
                ball.setx(ball.xcor()+ball.dx)
            player_b_mid1.dx=0.4
            player_b_mid1.setx(player_b_mid1.xcor()+player_b_mid1.dx)
            player_b_att1.dx=0.4
            player_b_att1.setx(player_b_att1.xcor()+player_b_att1.dx)
    elif j==3:
            t7=0
            if -30<ball.ycor()-player_b_def1.ycor()<30 and -20<ball.xcor()-player_b_def1.xcor()<20:
                ball.dy=0
                ball.dx=0.4
                ball.setx(ball.xcor()+ball.dx)
            player_b_def1.dx=0.4
            player_b_def1.setx(player_b_def1.xcor()+player_b_def1.dx)
            player_b_def2.dx=0.4
            player_b_def2.setx(player_b_def2.xcor()+player_b_def2.dx)
    elif j==4:
            t8=0
            if -30<ball.ycor()-player_b_def2.ycor()<30 and -20<ball.xcor()-player_b_def2.xcor()<20:
                ball.dy=0
                ball.dx=0.4
                ball.setx(ball.xcor()+ball.dx)
            player_b_def2.dx=0.4
            player_b_def2.setx(player_b_def2.xcor()+player_b_def2.dx)
            player_b_def1.dx=0.4
            player_b_def1.setx(player_b_def1.xcor()+player_b_def1.dx)
def gka_up():
    y=player_a_gk.ycor()
    player_a_gk.sety(player_a_gk.ycor()+10)
    
    
def gka_down():
    y=player_a_gk.ycor()
    player_a_gk.sety(player_a_gk.ycor()-10)

def gkb_up():
    y=player_b_gk.ycor()
    player_b_gk.sety(player_b_gk.ycor()+10)
    
    
def gkb_down():
    y=player_b_gk.ycor()
    player_b_gk.sety(player_b_gk.ycor()-10)

def shoota():
    global i
    if i==1:
        if 100>=ball.ycor()>=-100 and ball.xcor()>=420:
            if -30<ball.ycor()-player_a_att1.ycor()<30 and -20<ball.xcor()-player_a_att1.xcor()<20:
                ball.dx=0.9
                ball.setx(ball.xcor()+ball.dx)

    elif i==2:
        if 100>=ball.ycor()>=-100 and ball.xcor()>=420:
            if -30<ball.ycor()-player_a_mid1.ycor()<30 and -20<ball.xcor()-player_a_mid1.xcor()<20:
                ball.dx=0.9
                ball.setx(ball.xcor()+ball.dx)


    elif i==3:
        if 100>=ball.ycor()>=-100 and ball.xcor()>=420:
            if -30<ball.ycor()-player_a_def1.ycor()<30 and -20<ball.xcor()-player_a_def1.xcor()<20:
                ball.dx=0.9
                ball.setx(ball.xcor()+ball.dx)

                

    elif i==4:
        if 100>=ball.ycor()>=-100 and ball.xcor()>=420:
            if -30<ball.ycor()-player_a_def2.ycor()<30 and -20<ball.xcor()-player_a_def2.xcor()<20:
                ball.dx=0.9
                ball.setx(ball.xcor()+ball.dx)
def shootb():

    global j
    if j==1:
        if 100>=ball.ycor()>=-100 and -420>=ball.xcor():
            if -30<ball.ycor()-player_b_att1.ycor()<30 and -20<ball.xcor()-player_b_att1.xcor()<20:
                ball.dx=-0.9
                ball.setx(ball.xcor()+ball.dx)
    elif j==2:
        if 100>=ball.ycor()>-100 and -420>=ball.xcor():
            if -30<ball.ycor()-player_b_mid1.ycor()<30 and -20<ball.xcor()-player_b_mid1.xcor()<20:
                ball.dx=-0.9
                ball.setx(ball.xcor()+ball.dx)
                
    elif j==3:
        if 100>=ball.ycor()>-100 and -420>=ball.xcor():
            if -30<ball.ycor()-player_b_def1.ycor()<30 and -20<ball.xcor()-player_b_def1.xcor()<20:
                ball.dx=-0.9
                ball.setx(ball.xcor()+ball.dx)
               
    elif j==4:
        if 100>=ball.ycor()>-100 and -420>=ball.xcor():
            if -30<ball.ycor()-player_b_def2.ycor()<30 and -20<ball.xcor()-player_b_def2.xcor()<20:
                ball.dx=-0.9
                ball.setx(ball.xcor()+ball.dx)
def switcha():
    global i
    if i==1:
        i=2
    elif i==2:
        i=3
    elif i==3:
        i=4
    elif i==4:
        i=1

def switchb():
    global j
    if j==1:
        j=2
    elif j==2:
        j=3
    elif j==3:
        j=4
    elif j==4:
        j=1

def passinga():
    global i
    global j
    if -30<ball.ycor()-player_a_att1.ycor()<30 and -20<ball.xcor()-player_a_att1.xcor()<20:
        ball.dx=0
        ball.dy=0
        if player_a_mid1.ycor()==player_b_def1.ycor() and (player_b_def1.xcor()-player_a_mid1.xcor()==20 or player_b_def1.xcor()-player_a_mid1.xcor()==-10):
            ball.sety(player_b_def1.ycor())
            ball.setx(player_b_def1.xcor())
            j=3
        elif player_a_mid1.ycor()==player_b_def2.ycor() and (player_b_def2.xcor()-player_a_mid1.xcor()==20 or player_b_def2.xcor()-player_a_mid1.xcor()==-10):
            
            ball.sety(player_b_def2.ycor())
            ball.setx(player_b_def2.xcor())
            j=4
        elif player_a_mid1.ycor()==player_b_att1.ycor() and (player_b_att1.xcor()-player_a_mid1.xcor()==20 or player_b_att1.xcor()-player_a_mid1.xcor()==-10):
            
            ball.sety(player_b_att1.ycor())
            ball.setx(player_b_att1.xcor())
            j=1
        elif player_a_mid1.ycor()==player_b_mid1.ycor() and (player_b_mid1.xcor()-player_a_mid1.xcor()==20 or player_b_mid1.xcor()-player_a_mid1.xcor()==-10):
            
            ball.sety(player_b_mid1.ycor())
            ball.setx(player_b_mid1.xcor())
            j=2
        elif player_a_mid1.xcor()==player_b_def1.xcor() and (player_b_def1.ycor()-player_a_mid1.ycor()==30 or player_b_def1.ycor()-player_a_mid1.ycor()==-20):
            print('yes')
            ball.sety(player_b_def1.ycor())
            ball.setx(player_b_def1.xcor())
            j=3
        elif player_a_mid1.xcor()==player_b_def2.xcor() and (player_b_def2.ycor()-player_a_mid1.ycor()==30 or player_b_def2.ycor()-player_a_mid1.ycor()==-20):
            
            ball.sety(player_b_def2.ycor())
            ball.setx(player_b_def2.xcor())
            j=4
        elif player_a_mid1.xcor()==player_b_att1.xcor() and (player_b_att1.ycor()-player_a_mid1.ycor()==30 or player_b_att1.ycor()-player_a_mid1.ycor()==-20):
            
            ball.sety(player_b_att1.ycor())
            ball.setx(player_b_att1.xcor())
            j=1
        elif player_a_mid1.xcor()==player_b_mid1.xcor() and (player_b_mid1.ycor()-player_a_mid1.ycor()==30 or player_b_mid1.ycor()-player_a_mid1.ycor()==-20):
            
            ball.sety(player_b_mid1.ycor())
            ball.setx(player_b_mid1.xcor())
            j=2
        else:
            player_a_att1.dx=0
            player_a_mid1.dx=0
            player_a_att1.dy=0
            player_a_mid1.dy=0
            ball.sety(player_a_mid1.ycor()+ball.dy)
            ball.setx(player_a_mid1.xcor()+ball.dx+10)
            i=2
    elif -30<ball.ycor()-player_a_mid1.ycor()<30 and -20<ball.xcor()-player_a_mid1.xcor()<20:
        ball.dx=0
        ball.dy=0
        if player_a_def1.ycor()==player_b_def1.ycor() and (player_b_def1.xcor()-player_a_def1.xcor()==20 or player_b_def1.xcor()-player_a_def1.xcor()==-10):
            
            ball.sety(player_b_def1.ycor())
            ball.setx(player_b_def1.xcor())
            j=3
        elif player_a_def1.ycor()==player_b_def2.ycor() and (player_b_def2.xcor()-player_a_def1.xcor()==20 or player_b_def2.xcor()-player_a_def1.xcor()==-10):
            
            ball.sety(player_b_def2.ycor())
            ball.setx(player_b_def2.xcor())
            j=4
        elif player_a_def1.ycor()==player_b_att1.ycor() and (player_b_att1.xcor()-player_a_def1.xcor()==20 or player_b_att1.xcor()-player_a_def1.xcor()==-10):
            
            ball.sety(player_b_att1.ycor())
            ball.setx(player_b_att1.xcor())
            j=1
        elif player_a_def1.ycor()==player_b_mid1.ycor() and (player_b_mid1.xcor()-player_a_def1.xcor()==20 or player_b_mid1.xcor()-player_a_def1.xcor()==-10):
            
            ball.sety(player_b_mid1.ycor())
            ball.setx(player_b_mid1.xcor())
            j=2
        elif player_a_def1.xcor()==player_b_def1.xcor() and (player_b_def1.ycor()-player_a_def1.ycor()==30 or player_b_def1.ycor()-player_a_def1.ycor()==-20):
            
            ball.sety(player_b_def1.ycor())
            ball.setx(player_b_def1.xcor())
            j=3
        elif player_a_def1.xcor()==player_b_def2.xcor() and (player_b_def2.ycor()-player_a_def1.ycor()==30 or player_b_def2.ycor()-player_a_def1.ycor()==-20):
            
            ball.sety(player_b_def2.ycor())
            ball.setx(player_b_def2.xcor())
            j=4
        elif player_a_def1.xcor()==player_b_att1.xcor() and (player_b_att1.ycor()-player_a_def1.ycor()==30 or player_b_att1.ycor()-player_a_def1.ycor()==-20):
            
            ball.sety(player_b_att1.ycor())
            ball.setx(player_b_att1.xcor())
            j=1
        elif player_a_def1.xcor()==player_b_mid1.xcor() and (player_b_mid1.ycor()-player_a_def1.ycor()==30 or player_b_mid1.ycor()-player_a_def1.ycor()==-20):
            
            ball.sety(player_b_mid1.ycor())
            ball.setx(player_b_mid1.xcor())
            j=2
        elif 360<=player_a_mid1.xcor()<680:
            player_a_att1.dx=0
            player_a_mid1.dx=0
            player_a_att1.dy=0
            player_a_mid1.dy=0
            ball.sety(player_a_att1.ycor()+ball.dy)
            ball.setx(player_a_att1.xcor()+ball.dx+10)
            i=1
        else:
            player_a_def1.dx=0
            player_a_mid1.dx=0
            player_a_def1.dy=0
            player_a_mid1.dy=0
            player_a_att1.dx=0
            player_a_att1.dy=0
            ball.sety(player_a_def1.ycor()+ball.dy)
            ball.setx(player_a_def1.xcor()+ball.dx+10)
            i=3
    elif -30<ball.ycor()-player_a_def1.ycor()<30 and -20<ball.xcor()-player_a_def1.xcor()<20:
        ball.dx=0
        ball.dy=0
        if player_a_def2.ycor()==player_b_def1.ycor() and (player_b_def1.xcor()-player_a_def2.xcor()==20 or player_b_def1.xcor()-player_a_def2.xcor()==-10):
            
            ball.sety(player_b_def1.ycor())
            ball.setx(player_b_def1.xcor())
            j=3
        elif player_a_def2.ycor()==player_b_def2.ycor() and (player_b_def2.xcor()-player_a_def2.xcor()==20 or player_b_def2.xcor()-player_a_def2.xcor()==-10):
            
            ball.sety(player_b_def2.ycor())
            ball.setx(player_b_def2.xcor())
            j=4
        elif player_a_def2.ycor()==player_b_att1.ycor() and (player_b_att1.xcor()-player_a_def2.xcor()==20 or player_b_att1.xcor()-player_a_def2.xcor()==-10):
            
            ball.sety(player_b_att1.ycor())
            ball.setx(player_b_att1.xcor())
            j=1
        elif player_a_def2.ycor()==player_b_mid1.ycor() and (player_b_mid1.xcor()-player_a_def2.xcor()==20 or player_b_mid1.xcor()-player_a_def2.xcor()==-10):
            
            ball.sety(player_b_mid1.ycor())
            ball.setx(player_b_mid1.xcor())
            j=2
        elif player_a_def2.xcor()==player_b_def1.xcor() and (player_b_def1.ycor()-player_a_def2.ycor()==30 or player_b_def1.ycor()-player_a_def2.ycor()==-20):
            
            ball.sety(player_b_def1.ycor())
            ball.setx(player_b_def1.xcor())
            j=3
        elif player_a_def2.xcor()==player_b_def2.xcor() and (player_b_def2.ycor()-player_a_def2.ycor()==30 or player_b_def2.ycor()-player_a_def2.ycor()==-20):
            
            ball.sety(player_b_def2.ycor())
            ball.setx(player_b_def2.xcor())
            j=4
        elif player_a_def2.xcor()==player_b_att1.xcor() and (player_b_att1.ycor()-player_a_def2.ycor()==30 or player_b_att1.ycor()-player_a_def2.ycor()==-20):
            
            ball.sety(player_b_att1.ycor())
            ball.setx(player_b_att1.xcor())
            j=1
        elif player_a_def2.xcor()==player_b_mid1.xcor() and (player_b_mid1.ycor()-player_a_def2.ycor()==30 or player_b_mid1.ycor()-player_a_def2.ycor()==-20):
            
            ball.sety(player_b_mid1.ycor())
            ball.setx(player_b_mid1.xcor())
            j=2
        else:
            player_a_def2.dx=0
            player_a_def1.dx=0
            player_a_def1.dy=0
            player_a_def2.dy=0
            ball.sety(player_a_def2.ycor()+ball.dy)
            ball.setx(player_a_def2.xcor()+ball.dx+10)
            print(1)
            i=4
    elif -30<ball.ycor()-player_a_def2.ycor()<30 and -20<ball.xcor()-player_a_def2.xcor()<20:
        ball.dx=0
        ball.dy=0
        if player_a_att1.ycor()==player_b_def1.ycor() and (player_b_def1.xcor()-player_a_att1.xcor()==20 or player_b_def1.xcor()-player_a_att1.xcor()==-10):
            
            ball.sety(player_b_def1.ycor())
            ball.setx(player_b_def1.xcor())
            j=3
        elif player_a_att1.ycor()==player_b_def2.ycor() and (player_b_def2.xcor()-player_a_att1.xcor()==20 or player_b_def2.xcor()-player_a_att1.xcor()==-10):
            
            ball.sety(player_b_def2.ycor())
            ball.setx(player_b_def2.xcor())
            j=4
        elif player_a_att1.ycor()==player_b_att1.ycor() and (player_b_att1.xcor()-player_a_att1.xcor()==20 or player_b_att1.xcor()-player_a_att1.xcor()==-10):
            
            ball.sety(player_b_att1.ycor())
            ball.setx(player_b_att1.xcor())
            j=1
        elif player_a_att1.ycor()==player_b_mid1.ycor() and (player_b_mid1.xcor()-player_a_att1.xcor()==20 or player_b_mid1.xcor()-player_a_att1.xcor()==-10):
            
            ball.sety(player_b_mid1.ycor())
            ball.setx(player_b_mid1.xcor())
            j=2
        elif player_a_att1.xcor()==player_b_def1.xcor() and (player_b_def1.ycor()-player_a_att1.ycor()==30 or player_b_def1.ycor()-player_a_att1.ycor()==-20):
            
            ball.sety(player_b_def1.ycor())
            ball.setx(player_b_def1.xcor())
            j=3
        elif player_a_att1.xcor()==player_b_def2.xcor() and (player_b_def2.ycor()-player_a_att1.ycor()==30 or player_b_def2.ycor()-player_a_att1.ycor()==-20):
            
            ball.sety(player_b_def2.ycor())
            ball.setx(player_b_def2.xcor())
            j=4
        elif player_a_att1.xcor()==player_b_att1.xcor() and (player_b_att1.ycor()-player_a_att1.ycor()==30 or player_b_att1.ycor()-player_a_att1.ycor()==-20):
            
            ball.sety(player_b_att1.ycor())
            ball.setx(player_b_att1.xcor())
            j=1
        elif player_a_att1.xcor()==player_b_mid1.xcor() and (player_b_mid1.ycor()-player_a_att1.ycor()==30 or player_b_mid1.ycor()-player_a_att1.ycor()==-20):
            
            ball.sety(player_b_mid1.ycor())
            ball.setx(player_b_mid1.xcor())
            j=2
        else:
            player_a_def2.dx=0
            player_a_att1.dx=0
            player_a_att1.dy=0
            player_a_def2.dy=0
            player_a_def1.dx=0
            player_a_def1.dy=0
            ball.sety(player_a_att1.ycor()+ball.dy)
            ball.setx(player_a_att1.xcor()+ball.dx+10)
            i=1
            print(2)

    elif ball.ycor()==player_a_gk.ycor() and ball.xcor()==player_a_gk.xcor():
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_def1.ycor())
            ball.setx(player_a_def1.xcor()+10)
            i=3
            print(3)
def passingb():
    global j
    global i
    if -30<ball.ycor()-player_b_att1.ycor()<30 and -20<ball.xcor()-player_b_att1.xcor()<20:
        if player_b_mid1.ycor()==player_a_def1.ycor() and (player_a_def1.xcor()-player_b_mid1.xcor()==20 or player_a_def1.xcor()-player_b_mid1.xcor()==-10):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_def1.ycor())
            ball.setx(player_a_def1.xcor())
            i=3
        elif player_b_mid1.ycor()==player_a_def2.ycor() and (player_a_def2.xcor()-player_b_mid1.xcor()==20 or player_a_def2.xcor()-player_b_mid1.xcor()==-10):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_def2.ycor())
            ball.setx(player_a_def2.xcor())
            i=4
        elif player_b_mid1.ycor()==player_a_att1.ycor() and (player_a_att1.xcor()-player_b_mid1.xcor()==20 or player_a_att1.xcor()-player_b_mid1.xcor()==-10):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_att1.ycor())
            ball.setx(player_a_att1.xcor())
            i=1
        elif player_b_mid1.ycor()==player_a_mid1.ycor() and (player_a_mid1.xcor()-player_b_mid1.xcor()==20 or player_a_mid1.xcor()-player_b_mid1.xcor()==-10):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_mid1.ycor())
            ball.setx(player_a_mid1.xcor())
            i=2
        elif player_b_mid1.xcor()==player_a_def1.xcor() and (player_a_def1.ycor()-player_b_mid1.ycor()==30 or player_a_def1.ycor()-player_b_mid1.ycor()==-20):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_def1.ycor())
            ball.setx(player_a_def1.xcor())
            i=3
        elif player_b_mid1.xcor()==player_a_def2.xcor() and (player_a_def2.ycor()-player_b_mid1.ycor()==30 or player_a_def2.ycor()-player_b_mid1.ycor()==-20):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_def2.ycor())
            ball.setx(player_a_def2.xcor())
            i=4
        elif player_b_mid1.xcor()==player_a_att1.xcor() and (player_a_att1.ycor()-player_b_mid1.ycor()==30 or player_a_att1.ycor()-player_b_mid1.ycor()==-20):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_att1.ycor())
            ball.setx(player_a_att1.xcor())
            i=1
        elif player_b_mid1.xcor()==player_a_mid1.xcor() and (player_a_mid1.ycor()-player_b_mid1.ycor()==30 or player_a_mid1.ycor()-player_b_mid1.ycor()==-20):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_mid1.ycor())
            ball.setx(player_a_mid1.xcor())
            i=2
        
        else:
            ball.dx=0
            ball.dy=0
            player_b_mid1.dx=0
            player_b_att1.dx=0
            player_b_att1.dy=0
            player_b_mid1.dy=0
            ball.sety(player_b_mid1.ycor()+ball.dy)
            ball.setx(player_b_mid1.xcor()+ball.dx-10)
            j=2
    elif -30<ball.ycor()-player_b_mid1.ycor()<30 and -20<ball.xcor()-player_b_mid1.xcor()<20:
        if player_b_def1.ycor()==player_a_def1.ycor() and (player_a_def1.xcor()-player_b_def1.xcor()==20 or player_a_def1.xcor()-player_b_def1.xcor()==-10):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_def1.ycor())
            ball.setx(player_a_def1.xcor())
            i=3
        elif player_b_def1.ycor()==player_a_def2.ycor() and (player_a_def2.xcor()-player_b_def1.xcor()==20 or player_a_def2.xcor()-player_b_def1.xcor()==-10):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_def2.ycor())
            ball.setx(player_a_def2.xcor())
            i=4
        elif player_b_def1.ycor()==player_a_att1.ycor() and (player_a_att1.xcor()-player_b_def1.xcor()==20 or player_a_att1.xcor()-player_b_def1.xcor()==-10):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_att1.ycor())
            ball.setx(player_a_att1.xcor())
            i=1
        elif player_b_def1.ycor()==player_a_mid1.ycor() and (player_a_mid1.xcor()-player_b_def1.xcor()==20 or player_a_mid1.xcor()-player_b_def1.xcor()==-10):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_mid1.ycor())
            ball.setx(player_a_mid1.xcor())
            i=2
        elif player_b_def1.xcor()==player_a_def1.xcor() and (player_a_def1.ycor()-player_b_def1.ycor()==30 or player_a_def1.ycor()-player_b_def1.ycor()==-20):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_def1.ycor())
            ball.setx(player_a_def1.xcor())
            i=3
        elif player_b_def1.xcor()==player_a_def2.xcor() and (player_a_def2.ycor()-player_b_def1.ycor()==30 or player_a_def2.ycor()-player_b_def1.ycor()==-20):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_def2.ycor())
            ball.setx(player_a_def2.xcor())
            i=4
        elif player_b_def1.xcor()==player_a_att1.xcor() and (player_a_att1.ycor()-player_b_def1.ycor()==30 or player_a_att1.ycor()-player_b_def1.ycor()==-20):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_att1.ycor())
            ball.setx(player_a_att1.xcor())
            i=1
        elif player_b_def1.xcor()==player_a_mid1.xcor() and (player_a_mid1.ycor()-player_b_def1.ycor()==30 or player_a_mid1.ycor()-player_b_def1.ycor()==-20):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_mid1.ycor())
            ball.setx(player_a_mid1.xcor())
            i=2
        elif -680<player_b_mid1.xcor()<=-360:
            ball.dx=0
            ball.dy=0
            player_b_att1.dx=0
            player_b_mid1.dx=0
            player_b_att1.dy=0
            player_b_mid1.dy=0
            ball.sety(player_b_att1.ycor()+ball.dy)
            ball.setx(player_b_att1.xcor()+ball.dx-10)
            j=1
        else:
            ball.dx=0
            ball.dy=0
            player_b_att1.dx=0
            player_b_mid1.dx=0
            player_b_att1.dy=0
            player_b_mid1.dy=0
            player_b_def1.dx=0
            player_b_def1.dy=0
            ball.sety(player_b_def1.ycor()+ball.dy)
            ball.setx(player_b_def1.xcor()+ball.dx-10)
            j=3
    elif -30<ball.ycor()-player_b_def1.ycor()<30 and -20<ball.xcor()-player_b_def1.xcor()<20:
        if player_b_def2.ycor()==player_a_def1.ycor() and (player_a_def1.xcor()-player_b_def2.xcor()==20 or player_a_def1.xcor()-player_b_def2.xcor()==-10):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_def1.ycor())
            ball.setx(player_a_def1.xcor())
            i=3
        elif player_b_def2.ycor()==player_a_def2.ycor() and (player_a_def2.xcor()-player_b_def2.xcor()==20 or player_a_def2.xcor()-player_b_def2.xcor()==-10):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_def2.ycor())
            ball.setx(player_a_def2.xcor())
            i=4
        elif player_b_def2.ycor()==player_a_att1.ycor() and (player_a_att1.xcor()-player_b_def2.xcor()==20 or player_a_att1.xcor()-player_b_def2.xcor()==-10):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_att1.ycor())
            ball.setx(player_a_att1.xcor())
            i=1
        elif player_b_def2.ycor()==player_a_mid1.ycor() and (player_a_mid1.xcor()-player_b_def2.xcor()==20 or player_a_mid1.xcor()-player_b_def2.xcor()==-10):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_mid1.ycor())
            ball.setx(player_a_mid1.xcor())
            i=2
        elif player_b_def2.xcor()==player_a_def1.xcor() and (player_a_def1.ycor()-player_b_def2.ycor()==30 or player_a_def1.ycor()-player_b_def2.ycor()==-20):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_def1.ycor())
            ball.setx(player_a_def1.xcor())
            i=3
        elif player_b_def2.xcor()==player_a_def2.xcor() and (player_a_def2.ycor()-player_b_def2.ycor()==30 or player_a_def2.ycor()-player_b_def2.ycor()==-20):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_def2.ycor())
            ball.setx(player_a_def2.xcor())
            i=4
        elif player_b_def2.xcor()==player_a_att1.xcor() and (player_a_att1.ycor()-player_b_def2.ycor()==30 or player_a_att1.ycor()-player_b_def2.ycor()==-20):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_att1.ycor())
            ball.setx(player_a_att1.xcor())
            i=1
        elif player_b_def2.xcor()==player_a_mid1.xcor() and (player_a_mid1.ycor()-player_b_def2.ycor()==30 or player_a_mid1.ycor()-player_b_def2.ycor()==-20):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_mid1.ycor())
            ball.setx(player_a_mid1.xcor())
            i=2
        else:
            ball.dx=0
            ball.dy=0
            player_b_def1.dx=0
            player_b_def2.dx=0
            player_b_def1.dy=0
            player_b_def2.dy=0
            ball.sety(player_b_def2.ycor()+ball.dy)
            ball.setx(player_b_def2.xcor()+ball.dx-10)
            j=4
    elif -30<ball.ycor()-player_b_def2.ycor()<30 and -20<ball.xcor()-player_b_def2.xcor()<20:
        if player_b_att1.ycor()==player_a_def1.ycor() and (player_a_def1.xcor()-player_b_att1.xcor()==20 or player_a_def1.xcor()-player_b_att1.xcor()==-10):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_def1.ycor())
            ball.setx(player_a_def1.xcor())
            i=3
        elif player_b_att1.ycor()==player_a_def2.ycor() and (player_a_def2.xcor()-player_b_att1.xcor()==20 or player_a_def2.xcor()-player_b_att1.xcor()==-10):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_def2.ycor())
            ball.setx(player_a_def2.xcor())
            i=4
        elif player_b_att1.ycor()==player_a_att1.ycor() and (player_a_att1.xcor()-player_b_att1.xcor()==20 or player_a_att1.xcor()-player_b_att1.xcor()==-10):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_att1.ycor())
            ball.setx(player_a_att1.xcor())
            i=1
        elif player_b_att1.ycor()==player_a_mid1.ycor() and (player_a_mid1.xcor()-player_b_att1.xcor()==20 or player_a_mid1.xcor()-player_b_att1.xcor()==-10):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_mid1.ycor())
            ball.setx(player_a_mid1.xcor())
            i=2
        elif player_b_att1.xcor()==player_a_def1.xcor() and (player_a_def1.ycor()-player_b_att1.ycor()==30 or player_a_def1.ycor()-player_b_att1.ycor()==-20):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_def1.ycor())
            ball.setx(player_a_def1.xcor())
            i=3
        elif player_b_att1.xcor()==player_a_def2.xcor() and (player_a_def2.ycor()-player_b_att1.ycor()==30 or player_a_def2.ycor()-player_b_att1.ycor()==-20):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_def2.ycor())
            ball.setx(player_a_def2.xcor())
            i=4
        elif player_b_att1.xcor()==player_a_att1.xcor() and (player_a_att1.ycor()-player_b_att1.ycor()==30 or player_a_att1.ycor()-player_b_att1.ycor()==-20):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_att1.ycor())
            ball.setx(player_a_att1.xcor())
            i=1
        elif player_b_att1.xcor()==player_a_mid1.xcor() and (player_a_mid1.ycor()-player_b_att1.ycor()==30 or player_a_mid1.ycor()-player_b_att1.ycor()==-20):
            ball.dx=0
            ball.dy=0
            ball.sety(player_a_mid1.ycor())
            ball.setx(player_a_mid1.xcor())
            i=2
        else:
            ball.dx=0
            ball.dy=0
            player_b_def1.dx=0
            player_b_def2.dx=0
            player_b_def1.dy=0
            player_b_def2.dy=0
            player_b_att1.dx=0
            player_b_att1.dy=0
            ball.sety(player_b_att1.ycor()+ball.dy)
            ball.setx(player_b_att1.xcor()+ball.dx-10)
            
            j=1
    elif ball.ycor()==player_b_gk.ycor() and ball.xcor()==player_b_gk.xcor():
            ball.dx=0
            ball.dy=0
            ball.sety(player_b_def1.ycor())
            ball.setx(player_b_def1.xcor()-10)
            j=3
    
paused = False

def pause():
    global paused

    if not paused:
        #create new screen
        keypress = 1
        while keypress != 'p':
            keypress = keyboard.read_key()
            wn.update()
            print('')
    #create a new pen that covers the whole screen in green and shows 'paused, press ___ to resume'
    paused = not paused



#LINK KEYBOARD KEYS
wn.listen()
wn.onkeyrelease(pause,'p')
wn.onkeyrelease(movement_up,'w')
wn.onkeyrelease(movement_down,'s')
wn.onkeyrelease(movement_left,'a')
wn.onkeyrelease(movement_right,'d')
wn.onkeyrelease(gka_up,'q')
wn.onkeyrelease(gka_down,'z')
wn.onkeyrelease(shoota,'c')
wn.onkeyrelease(passinga,'x')
wn.onkeyrelease(switcha,'Tab')
wn.onkeyrelease(movement_up_1,'Up')
wn.onkeyrelease(movement_down_2,'Down')
wn.onkeyrelease(movement_left_3,'Left')
wn.onkeyrelease(movement_right_4,'Right')
wn.onkeyrelease(gkb_up,'8')
wn.onkeyrelease(gkb_down,'2')
wn.onkeyrelease(shootb,'0')
wn.onkeyrelease(switchb,'1')
wn.onkeyrelease(passingb,'3')


start_time = datetime.now()
u=0
while True:
                wn.update()
                if u==0:
                    u=1
                    time.sleep(1)
                    f1=open('scoresheet.txt','a+')
                    r=f1.readlines()
                    penp4.write(('PREVIOUS RESULTS'), align="center", font=("Courier", 24, "bold"))
                    if len(r)>=3:
                        penp1.write(r[-1], align="center", font=("Courier", 24, "bold"))
                        penp2.write(r[-2], align="center", font=("Courier", 24, "bold"))
                        penp3.write(r[-3], align="center", font=("Courier", 24, "bold"))
                    elif len(r)==2:
                        penp1.write(r[-1], align="center", font=("Courier", 24, "bold"))
                        penp2.write(r[-2], align="center", font=("Courier", 24, "bold"))
                    elif len(r)==1:
                        penp2.write(r[-1], align="center", font=("Courier", 24, "bold"))
                    else:
                        penp2.write('NO PREVIOUS RESULTS', align="center", font=("Courier", 24, "bold"))
                    time.sleep(5)
                    penp1.clear()
                    penp2.clear()
                    penp3.clear()
                    penp4.clear()
                    f1.close()
                
                ball.setx(ball.xcor()+ball.dx)
                ball.sety(ball.ycor()+ball.dy)
                player_a_att1.setx(player_a_att1.xcor()+player_a_att1.dx)
                player_a_att1.sety(player_a_att1.ycor()+player_a_att1.dy)
                player_a_mid1.setx(player_a_mid1.xcor()+player_a_mid1.dx)
                player_a_mid1.sety(player_a_mid1.ycor()+player_a_mid1.dy)
                player_a_def1.setx(player_a_def1.xcor()+player_a_def1.dx)
                player_a_def1.sety(player_a_def1.ycor()+player_a_def1.dy)
                player_a_def2.setx(player_a_def2.xcor()+player_a_def2.dx)
                player_a_def2.sety(player_a_def2.ycor()+player_a_def2.dy)
                player_b_att1.setx(player_b_att1.xcor()+player_b_att1.dx)
                player_b_att1.sety(player_b_att1.ycor()+player_b_att1.dy)
                player_b_mid1.setx(player_b_mid1.xcor()+player_b_mid1.dx)
                player_b_mid1.sety(player_b_mid1.ycor()+player_b_mid1.dy)
                player_b_def1.setx(player_b_def1.xcor()+player_b_def1.dx)
                player_b_def1.sety(player_b_def1.ycor()+player_b_def1.dy)
                player_b_def2.setx(player_b_def2.xcor()+player_b_def2.dx)
                player_b_def2.sety(player_b_def2.ycor()+player_b_def2.dy)
            
                seconds1,minutes1 = ((datetime.now() - start_time).seconds%60), (datetime.now()- start_time).seconds//60
                pen1.clear()
                pen1.setposition(-700,340)
                pen1.write("{}:{}".format(minutes1, seconds1), align="center", font=("Courier", 24, "bold"))
                          
                               
                ball.setx(ball.xcor())
                ball.sety(ball.ycor())
                #GOALIE RULES
                if player_a_gk.ycor()==100:
                    player_a_gk.sety(player_a_gk.ycor()-10)
                if player_a_gk.ycor()==-100:
                    player_a_gk.sety(player_a_gk.ycor()+10)
                if player_b_gk.ycor()==100:
                    player_b_gk.sety(player_b_gk.ycor()-10)
                if player_b_gk.ycor()==-100:
                    player_b_gk.sety(player_b_gk.ycor()+10)
                if -30<ball.ycor()-player_a_gk.ycor()<30 and ball.xcor()<(-640):
                    ball.sety(player_a_gk.ycor())
                    ball.setx(player_a_gk.xcor())
                if -30<ball.ycor()-player_b_gk.ycor()<30 and ball.xcor()>640:
                    ball.sety(player_b_gk.ycor())
                    ball.setx(player_b_gk.xcor())
                #PREVENT BALL FROM LEAVING
                if (ball.xcor()>=750):
                    ball.dx=0
                    ball.dy=0
                    ball.setx(ball.xcor()-20)
                if ball.xcor()<=-750:
                    ball.dx=0
                    ball.dy=0
                    ball.setx(ball.xcor()+20)
                if  ball.ycor()<=-390:
                    ball.dy=0
                    ball.dx=0
                if  ball.ycor()>=390:
                    ball.dy=0
                    ball.dx=0
                
                
                #PREVENT FROM LEAVING
                if player_a_att1.ycor()>=390:
                    player_a_att1.sety(player_a_att1.ycor()-20)
                if player_a_att1.ycor()<=-390:
                    player_a_att1.sety(player_a_att1.ycor()+30)
                if player_a_def1.ycor()>=390:
                    player_a_def1.sety(player_a_def1.ycor()-20)
                if player_a_def1.ycor()<=-390:
                    player_a_def1.sety(player_a_def1.ycor()+30)
                if player_a_def2.ycor()>=390:
                    player_a_def2.sety(player_a_def2.ycor()-20)
                if player_a_def2.ycor()<=-390:
                    player_a_def2.sety(player_a_def2.ycor()+30)
                if player_a_mid1.ycor()>=390:
                    player_a_mid1.sety(player_a_mid1.ycor()-20)
                if player_a_mid1.ycor()<=-390:
                    player_a_mid1.sety(player_a_mid1.ycor()+30)
                if player_b_att1.ycor()>=390:
                    player_b_att1.sety(player_b_att1.ycor()-20)
                if player_b_att1.ycor()<=-390:
                    player_b_att1.sety(player_b_att1.ycor()+30)
                if player_b_mid1.ycor()>=390:
                    player_b_mid1.sety(player_b_mid1.ycor()-20)
                if player_b_mid1.ycor()<=-390:
                    player_b_mid1.sety(player_b_mid1.ycor()+30)
                if player_b_def1.ycor()>=390:
                    player_b_def1.sety(player_b_def1.ycor()-20)
                if player_b_def1.ycor()<=-390:
                    player_b_def1.sety(player_b_def1.ycor()+30)
                if player_b_def2.ycor()>=390:
                    player_b_def2.sety(player_b_def2.ycor()-20)
                if player_b_def2.ycor()<=-390:
                    player_b_def2.sety(player_b_def2.ycor()+30)
                if player_a_att1.xcor()>=760:
                    player_a_att1.setx(player_a_att1.xcor()-10)
                if player_a_att1.xcor()<=-760:
                    player_a_att1.setx(player_a_att1.xcor()+20)
                if player_a_def1.xcor()>=760:
                    player_a_def1.setx(player_a_def1.xcor()-10)
                if player_a_def1.xcor()<=-760:
                    player_a_def1.setx(player_a_def1.xcor()+20)
                if player_a_def2.xcor()>=760:
                    player_a_def2.setx(player_a_def2.xcor()-10)
                if player_a_def2.xcor()<=-760:
                    player_a_def2.setx(player_a_def2.xcor()+20)
                if player_a_mid1.xcor()>=760:
                    player_a_mid1.setx(player_a_mid1.xcor()-10)
                if player_a_mid1.xcor()<=-760:
                    player_a_mid1.setx(player_a_mid1.xcor()+20)
                if player_b_att1.xcor()>=760:
                    player_b_att1.setx(player_b_att1.xcor()-10)
                if player_b_att1.xcor()<=-760:
                    player_b_att1.setx(player_b_att1.xcor()+20)
                if player_b_mid1.xcor()>=760:
                    player_b_mid1.setx(player_b_mid1.xcor()-10)
                if player_b_mid1.xcor()<=-760:
                    player_b_mid1.setx(player_b_mid1.xcor()+20)
                if player_b_def1.xcor()>=760:
                    player_b_def1.setx(player_b_def1.xcor()-10)
                if player_b_def1.xcor()<=-760:
                    player_b_def1.setx(player_b_def1.xcor()+20)
                if player_b_def2.xcor()>=760:
                    player_b_def2.setx(player_b_def2.xcor()-10)
                if player_b_def2.xcor()<=-760:
                    player_b_def2.setx(player_b_def2.xcor()+20)   
                #PREVENT ENTRY IN GOAL
                if 660<player_a_att1.xcor()<750 and -100<player_a_att1.ycor()<100:
                    player_a_att1.setx(player_a_att1.xcor()-10)
                if -660>player_a_att1.xcor()>-750 and -100<player_a_att1.ycor()<100:
                    player_a_att1.setx(player_a_att1.xcor()+20)
                if 660<player_a_def1.xcor()<750 and -100<player_a_def1.ycor()<100:
                    player_a_def1.setx(player_a_def1.xcor()-10)
                if -660>player_a_def1.xcor()>-750 and -100<player_a_def1.ycor()<100:
                    player_a_def1.setx(player_a_def1.xcor()+20)
                if 660<player_a_def2.xcor()<750 and -100<player_a_def2.ycor()<100:
                    player_a_def2.setx(player_a_def2.xcor()-10)
                if -660>player_a_def2.xcor()>-750 and -100<player_a_def2.ycor()<100:
                    player_a_def2.setx(player_a_def2.xcor()+20)
                if 660<player_a_mid1.xcor()<750 and -100<player_a_mid1.ycor()<100:
                    player_a_mid1.setx(player_a_mid1.xcor()-10)
                if -660>player_a_mid1.xcor()>-750 and -100<player_a_mid1.ycor()<100:
                    player_a_mid1.setx(player_a_mid1.xcor()+20)
                if 660<player_b_att1.xcor()<750 and -100<player_b_att1.ycor()<100:
                    player_b_att1.setx(player_b_att1.xcor()-10)
                if -660>player_b_att1.xcor()>-750 and -100<player_b_att1.ycor()<100:
                    player_b_att1.setx(player_b_att1.xcor()+20)
                if 660<player_b_mid1.xcor()<750 and -100<player_b_mid1.ycor()<100:
                    player_b_mid1.setx(player_b_mid1.xcor()-10)
                if -660>player_b_mid1.xcor()>-750 and -100<player_b_mid1.ycor()<100:
                    player_b_mid1.setx(player_b_mid1.xcor()+20)
                if 660<player_b_def1.xcor()<750 and -100<player_b_def1.ycor()<100:
                    player_b_def1.setx(player_b_def1.xcor()-10)
                if -660>player_b_def1.xcor()>-750 and -100<player_b_def1.ycor()<100:
                    player_b_def1.setx(player_b_def1.xcor()+20)
                if 660<player_b_def2.xcor()<750 and -100<player_b_def2.ycor()<100:
                    player_b_def2.setx(player_b_def2.xcor()-10)
                if -660>player_b_def2.xcor()>-750 and -100<player_b_def2.ycor()<100:
                    player_b_def2.setx(player_b_def2.xcor()+20)
                #STEAL
                if -20<ball.ycor()-player_a_att1.ycor()<20 and -10<ball.xcor()-player_a_att1.xcor()<10:
                    ball.sety(player_a_att1.ycor())
                    if t1==1:
                        ball.setx(player_a_att1.xcor()-10)
                    else:
                        ball.setx(player_a_att1.xcor()+10)
                    i=1
                if -20<ball.ycor()-player_a_mid1.ycor()<20 and -10<ball.xcor()-player_a_mid1.xcor()<10:
                    ball.sety(player_a_mid1.ycor())
                    if t2==1:
                        ball.setx(player_a_mid1.xcor()-10)
                    else:
                        ball.setx(player_a_mid1.xcor()+10)
                    i=2
                if -20<ball.ycor()-player_b_att1.ycor()<20 and -10<ball.xcor()-player_b_att1.xcor()<10:
                    ball.sety(player_b_att1.ycor())
                    if t3==1:
                        ball.setx(player_b_att1.xcor()-10)
                    else:
                        ball.setx(player_b_att1.xcor()+10)
                    
                    j=1
                if -20<ball.ycor()-player_b_mid1.ycor()<20 and -10<ball.xcor()-player_b_mid1.xcor()<10:
                    ball.sety(player_b_mid1.ycor())
                    if t4==1:
                        ball.setx(player_b_mid1.xcor()-10)
                    else:
                        ball.setx(player_b_mid1.xcor()+10)
                    j=2
                if  -20<ball.ycor()-player_a_def2.ycor()<20 and -10<ball.xcor()-player_a_def2.xcor()<10:
                    ball.sety(player_a_def2.ycor())
                    if t5==1:
                        ball.setx(player_a_def2.xcor()-10)
                    else:
                        ball.setx(player_a_def2.xcor()+10)
                    i=4
                if  -20<ball.ycor()-player_a_def1.ycor()<20 and -10<ball.xcor()-player_a_def1.xcor()<10:
                    ball.sety(player_a_def1.ycor())
                    if t6==1:
                        ball.setx(player_a_def1.xcor()-10)
                    else:
                        ball.setx(player_a_def1.xcor()+10)
                    i=3
                if  -20<ball.ycor()-player_b_def1.ycor()<20 and -10<ball.xcor()-player_b_def1.xcor()<10:
                    ball.sety(player_b_def1.ycor())
                    if t7==1:
                        ball.setx(player_b_def1.xcor()-10)
                    else:
                        ball.setx(player_b_def1.xcor()+10)
                    j=3
                if -20<ball.ycor()-player_b_def2.ycor()<20 and -10<ball.xcor()-player_b_def2.xcor()<10:
                    ball.sety(player_b_def2.ycor())
                    if t8==1:
                        ball.setx(player_b_def2.xcor()-10)
                    else:
                        ball.setx(player_b_def2.xcor()+10)
                    j=4
                #SCORE
                if (-100<ball.ycor()<100) and (-670>ball.xcor()>-750) and (minutes1==0 or (seconds1<30 and minutes1==1)):
                    Pen.clear()
                    pen.clear()
                    score_b+=1
                    i=1
                    j=1
                    pen.write("A:{}  B:{}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
                    Pen.write("GOALLLL", align="center", font=("Courier", 60, "bold"))
                    player_a_att1.goto(-100,120)
                    player_a_def2.goto(-460,-90)
                    player_a_def1.goto(-460,90)
                    player_a_mid1.goto(-200,-120)
                    player_a_gk.goto(-660,0)
                    player_b_att1.goto(100,120)
                    player_b_mid1.goto(200,-120)
                    player_b_def1.goto(460,90)
                    player_b_def2.goto(460,-90)
                    player_b_gk.goto(660,0)
                    ball.goto(0,0)
                    ball.dx=0
                    ball.dy=0
                    ball.dx=0
                    ball.dy=0
                    player_a_att1.dx=0
                    player_a_def1.dx=0
                    player_a_def2.dx=0
                    player_a_mid1.dx=0
                    player_a_att1.dy=0
                    player_a_def1.dy=0
                    player_a_def2.dy=0
                    player_a_mid1.dy=0
                    player_b_att1.dx=0
                    player_b_def1.dx=0
                    player_b_def2.dx=0
                    player_b_mid1.dx=0
                    player_b_att1.dy=0
                    player_b_def1.dy=0
                    player_b_def2.dy=0
                    player_b_mid1.dy=0
                    time.sleep(2)
                    Pen.clear()

                elif (-100<ball.ycor()<100) and (750>ball.xcor()>670) and (minutes1==0 or (seconds1<30 and minutes1==1)):
                    pen.clear()
                    Pen.clear()
                    score_a+=1
                    pen.write("A:{}  B:{}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
                    Pen.write("GOALLLL", align="center", font=("Courier", 60, "bold"))        
                    player_a_att1.goto(-100,120)
                    player_a_def2.goto(-460,-90)
                    player_a_def1.goto(-460,90)
                    player_a_mid1.goto(-200,-120)
                    player_a_gk.goto(-660,0)
                    player_b_att1.goto(100,120)
                    player_b_mid1.goto(200,-120)
                    player_b_def1.goto(460,90)
                    player_b_def2.goto(460,-90)
                    player_b_gk.goto(660,0)
                    ball.goto(0,0)
                    ball.dx=0
                    ball.dy=0
                    player_a_att1.dx=0
                    player_a_def1.dx=0
                    player_a_def2.dx=0
                    player_a_mid1.dx=0
                    player_a_att1.dy=0
                    player_a_def1.dy=0
                    player_a_def2.dy=0
                    player_a_mid1.dy=0
                    player_b_att1.dx=0
                    player_b_def1.dx=0
                    player_b_def2.dx=0
                    player_b_mid1.dx=0
                    player_b_att1.dy=0
                    player_b_def1.dy=0
                    player_b_def2.dy=0
                    player_b_mid1.dy=0
                    i=1
                    j=1
                    time.sleep(2)
                    Pen.clear()
                if (-100<ball.ycor()<100) and (-670>ball.xcor()>-750) and (seconds1>30 and minutes1>=1):
                    Pen.clear()
                    pen.clear()
                    score_b+=1
                    i=1
                    j=1
                    pen.write("A:{}  B:{}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
                    Pen.write("GOALLLL", align="center", font=("Courier", 60, "bold"))
                    p=0.5
                    player_a_att1.goto(-100,120)
                    player_a_def2.goto(-460,-90)
                    player_a_def1.goto(-460,90)
                    player_a_mid1.goto(-200,-120)
                    player_a_gk.goto(-660,0)
                    player_b_att1.goto(100,120)
                    player_b_mid1.goto(200,-120)
                    player_b_def1.goto(460,90)
                    player_b_def2.goto(460,-90)
                    player_b_gk.goto(660,0)
                    ball.goto(0,0)
                    ball.dx=0
                    ball.dy=0
                    ball.dx=0
                    ball.dy=0
                    player_a_att1.dx=0
                    player_a_def1.dx=0
                    player_a_def2.dx=0
                    player_a_mid1.dx=0
                    player_a_att1.dy=0
                    player_a_def1.dy=0
                    player_a_def2.dy=0
                    player_a_mid1.dy=0
                    player_b_att1.dx=0
                    player_b_def1.dx=0
                    player_b_def2.dx=0
                    player_b_mid1.dx=0
                    player_b_att1.dy=0
                    player_b_def1.dy=0
                    player_b_def2.dy=0
                    player_b_mid1.dy=0
                    time.sleep(2)
                    Pen.clear()

                elif (-100<ball.ycor()<100) and (750>ball.xcor()>670) and (seconds1>30 and minutes1>=1):
                    pen.clear()
                    Pen.clear()
                    score_a+=1
                    pen.write("A:{}  B:{}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
                    Pen.write("GOALLLL", align="center", font=("Courier", 60, "bold"))        
                    p=0.5
                    player_a_att1.goto(-100,120)
                    player_a_def2.goto(-460,-90)
                    player_a_def1.goto(-460,90)
                    player_a_mid1.goto(-200,-120)
                    player_a_gk.goto(-660,0)
                    player_b_att1.goto(100,120)
                    player_b_mid1.goto(200,-120)
                    player_b_def1.goto(460,90)
                    player_b_def2.goto(460,-90)
                    player_b_gk.goto(660,0)
                    ball.goto(0,0)
                    ball.dx=0
                    ball.dy=0
                    player_a_att1.dx=0
                    player_a_def1.dx=0
                    player_a_def2.dx=0
                    player_a_mid1.dx=0
                    player_a_att1.dy=0
                    player_a_def1.dy=0
                    player_a_def2.dy=0
                    player_a_mid1.dy=0
                    player_b_att1.dx=0
                    player_b_def1.dx=0
                    player_b_def2.dx=0
                    player_b_mid1.dx=0
                    player_b_att1.dy=0
                    player_b_def1.dy=0
                    player_b_def2.dy=0
                    player_b_mid1.dy=0
                    i=1
                    j=1
                    time.sleep(2)
                    Pen.clear()
                if seconds1 == (36+(score_a+score_b+p)*2) and minutes1 == 1:
                    pen.clear()
                    Pen.clear()
                    pen1.clear()
                    pen.goto(0,0)
                    pen1.goto(0,-100)
                    pen.write("A:{}  B:{}".format(score_a, score_b), align="center", font=("Courier", 100, "bold"))
                    if score_a>score_b:
                        pen1.write("A WINS", align="center", font=("Courier", 80, "bold"))
                    if score_a<score_b:
                        pen1.write("B WINS", align="center", font=("Courier", 80, "bold"))
                    if score_a==score_b:
                        pen1.write("DRAW", align="center", font=("Courier", 80, "bold"))
                    s=['A:',str(score_a),' B:',str(score_b)]
                    f1=open('scoresheet.txt','a+')
                    f1.write('\n')
                    f1.write(' '.join(s))
                    f1.close()
                    time.sleep(5)
                    break            
