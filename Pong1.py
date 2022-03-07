import turtle

win = turtle.Screen()
win.title("Pong by JAACKSONN")
win.bgcolor("black")
win.setup(width = 800, height = 600)
win.tracer(0) #stops the window from updating

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

#Moves paddle up
def paddle_1_up():
    y = paddle_1.ycor() #from turtle, find y coordinate
    y += 20
    paddle_1.sety(y)

win.listen() #listens for keyboard input
win.onkeypress(paddle_1_up, "w") #if they press w, we move up

# Main game loop
while True:
    win.update()
