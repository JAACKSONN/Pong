import turtle
import os

win = turtle.Screen()
win.title("Pong by JAACKSONN")
win.bgcolor("black")
win.setup(width = 800, height = 600)
win.tracer(0) #stops the window from updating


#Pen for scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() #so that there is not a line moving
pen.hideturtle() #just want to see the text that it writes
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font = ("Courier", 24, "normal"))

#Score
score_a = 0
score_b = 0

# Create paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0) #speed of animation, sets it to maximum possible speed
paddle_1.shape("square")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.color("blue")
paddle_1.penup()
paddle_1.goto(-350, 0) #chooses the start coordinate

#Create paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0) #speed of animation, sets it to maximum possible speed
paddle_2.shape("square")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.color("red")
paddle_2.penup()
paddle_2.goto(350, 0) #chooses the start coordinate

#Create ball
ball = turtle.Turtle()
ball.speed(0) #speed of animation, sets it to maximum possible speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0) #chooses the start coordinate
#separate movement into two parts, x and y
ball.dx = 2
ball.dy = 2

#Moves paddle up
def paddle_1_up():
    y = paddle_1.ycor() #from turtle, find y coordinate
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor() #from turtle, find y coordinate
    y -= 20
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor() #from turtle, find y coordinate
    y += 20
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor() #from turtle, find y coordinate
    y -= 20
    paddle_2.sety(y)

win.listen() #listens for keyboard input
win.onkeypress(paddle_1_up, "w") #if they press w, we move up
win.onkeypress(paddle_1_down, "s")
win.onkeypress(paddle_2_up, "Up")
win.onkeypress(paddle_2_down, "Down")


# Main game loop
while True:
    #updates window
    win.update()

    #moves ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #check for border collision

    #top check
    if ball.ycor() > 285:
        ball.sety(285)
        ball.dy *= -1
        os.system("afplay pong_bounce.mp3&")
    #bottom check
    if ball.ycor() < -285:
        ball.sety(-285)
        ball.dy *= -1
        os.system("afplay pong_bounce.mp3&")
    #right check
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        os.system("afplay pong_bounce.mp3&")
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font = ("Courier", 24, "normal"))
    #left check
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        os.system("afplay pong_bounce.mp3&")
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font = ("Courier", 24, "normal"))

    #paddle1 collision
    if(ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50)):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay pong_bounce.mp3&")
    
    
    if(ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50)):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay pong_bounce.mp3&")