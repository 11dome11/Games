import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import turtle
import winsound
import pygame

clock= pygame.time.Clock() 

# Create window
wn= turtle.Screen()
wn.title("Pong by @11dome11")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

# Score
score_a=0
score_b=0

# Paddle A
paddle_a= turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.shapesize(stretch_wid=6,stretch_len=1)

# Paddle B
paddle_b= turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_wid=6,stretch_len=1)

# Ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.shapesize(stretch_wid=1.5,stretch_len=1.5)
ball.dx= 1.75
ball.dy= 1.75

# Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player green:0      Player red:0", align="center", font=("Arial", 20, "normal" ))



# Function
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)
    
def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)
    
#Keyboard input
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

# Main game loop
while True:
    wn.update()
    
    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #Border Checking 
    if ball.ycor()> 295:
        ball.sety(295)
        ball.dy*= -1
        winsound.PlaySound("bounce-wall_.wav", winsound.SND_ASYNC)
    if ball.ycor()< -295:
        ball.sety(-295)
        ball.dy*= -1
        winsound.PlaySound("bounce-wall_.wav", winsound.SND_ASYNC)
    if ball.xcor()> 395:
        ball.goto(0,0)
        ball.dx*= -1
        score_a+=1
        pen.clear()
        pen.write("Player green:{}      Player red:{}".format(score_a,score_b), align="center", font=("Arial", 20, "normal" ))
       
    if ball.xcor()< -395:
        ball.goto(0,0)
        ball.dx*= -1
        score_b+=1
        pen.clear()
        pen.write("Player green:{}      Player red:{}".format(score_a,score_b), align="center", font=("Arial", 20, "normal" ))
        
    # Paddle and ball collisions
    if (ball.xcor()> 335 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+ 45 and ball.ycor()>paddle_b.ycor()-45):
        ball.setx(335)
        ball.dx*=-1     
        winsound.PlaySound("ping-pong-hit_PPzh3w4Wb.wav", winsound.SND_ASYNC)
    if (ball.xcor()< -335 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+ 45 and ball.ycor()>paddle_a.ycor()-45):
        ball.setx(-335)
        ball.dx*=-1
        winsound.PlaySound("ping-pong-hit_PPzh3w4Wb.wav", winsound.SND_ASYNC)
        
    clock.tick(150) #set the speed so the speed of the ball is constant



    




 
    
    
