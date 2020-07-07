#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 03:56:05 2020

@author: ankuraggarwal
"""
import turtle
import time

wn = turtle.Screen()
wn.title("Ice Hockey")
#wn.bgcolor("black")
wn.bgpic("stadium.gif")
wn.setup(width =800,height=600)
wn.tracer(0)


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("aquamarine4")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-300, 10)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(3)
paddle_b.shape("square")
paddle_b.color("brown")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(290,0)
 
# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("DarkSlateBlue")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
   
def paddle_a_left():
    x = paddle_a.xcor()
    x += 20
    paddle_a.setx(x)
    
def paddle_a_right():
    x = paddle_a.xcor()
    x -= 20
    paddle_a.setx(x)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def paddle_b_left():
    x = paddle_b.xcor()
    x -= 20
    paddle_b.setx(x)

def paddle_b_right():
    x = paddle_b.xcor()
    x += 20
    paddle_b.setx(x)
# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(paddle_a_right, "a")
wn.onkeypress(paddle_a_left, "d")
wn.onkeypress(paddle_b_left, "Left")
wn.onkeypress(paddle_b_right, "Right")

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Score
score_a = 0
score_b = 0
    
    
    
    

while True:
    wn.update()
    
  # movement of ball  
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
   # Border checking 
      



   # Top and bottom
   
   # for paddle
    if paddle_a.ycor() > 200 :
        paddle_a.goto(paddle_a.xcor(),200)
        
    if paddle_b.ycor() > 200 :
        paddle_b.goto(paddle_b.xcor(),200)
        
    if paddle_a.ycor() < -190 :
        paddle_a.goto(paddle_a.xcor(),-190)
    
    if paddle_b.ycor() < -190 :
        paddle_b.goto(paddle_b.xcor(),-190)
        
    if paddle_b.xcor() > 370 :
        paddle_b.goto(370,paddle_b.ycor())
    
    if paddle_a.xcor() < -390 :
        paddle_a.goto(-390,paddle_a.ycor())
    
    # for ball
    
    if ball.ycor() > 240:
        ball.sety(240)
        ball.dy *= -1
        
    elif ball.ycor() < -240:
        ball.sety(-240)
        ball.dy *= -1
        
     # Left and right
     
    if ball.xcor() > 370:
        ball.setx(370)
        ball.dx *= -1
        
    elif ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
     
     # goal score condition
     
    if ball.xcor() > 310 and ball.ycor() > -20 and ball.ycor() < 20 and ball.xcor() < 320 :
        pen.goto(0,0)
        pen.write("score",align="center", font=("Courier", 36, "normal"))
        time.sleep(3)
        pen.clear()
        pen.goto(0,260)
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        
    if ball.xcor() < -310 and ball.ycor() > -20 and ball.ycor() < 20 and ball.xcor() > -320 :
        pen.goto(0,0)
        pen.write("score",align="center", font=("Courier", 36, "normal"))
        time.sleep(3)
        pen.clear()
        pen.goto(0,260)
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        
  # Paddle and ball collisions
  
    if ball.xcor() == paddle_a.xcor() and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1   
        
    if ball.xcor() == paddle_b.xcor() and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1  
        
  # Paddle boundary condition 
  
    if paddle_a.xcor() > 0:
        pen.goto(0,0)
        pen.write("score",align="center", font=("Courier", 36, "normal"))
        time.sleep(3)
        pen.clear()
        pen.goto(0,260)
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        paddle_a.goto(-300, 10)
    
    if paddle_b.xcor() < 0:
        pen.goto(0,0)
        pen.write("score",align="center", font=("Courier", 36, "normal"))
        time.sleep(3)
        pen.clear()
        pen.goto(0,260)
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        paddle_b.goto(290,0)
         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        