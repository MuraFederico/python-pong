import turtle

wn = turtle.Screen()

wn.title('pong by Murataci')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=4,stretch_len=1)
paddle_a.color('red')
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=4,stretch_len=1)
paddle_b.color('blue')
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = .2
ball.dy = .2

# Score Board

score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('score', align='center', font=('courier', 24, 'normal'))

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color('white')
pen2.penup()
pen2.hideturtle()
pen2.goto(0, 235)
pen2.write('{}  |  {}'.format(score_a, score_b) , align='center', font=('courier', 24, 'normal'))

# Functions

# Paddle A movement
def paddle_a_up():
    y = paddle_a.ycor()
    y += 10
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 10
    paddle_a.sety(y)

# Paddle B movement

def paddle_b_up():
    y = paddle_b.ycor()
    y += 10
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 10
    paddle_b.sety(y)



# Key Binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')


# Main Game Loop
while True:
    wn.update()

    # Ball movement

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # Borders check

    # Top & Bottom

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Left & right

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen2.clear()
        pen2.write('{}  |  {}'.format(score_a, score_b) , align='center', font=('courier', 24, 'normal'))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen2.clear()
        pen2.write('{}  |  {}'.format(score_a, score_b) , align='center', font=('courier', 24, 'normal'))


    # Paddle Bounce
    
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1   
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1   
    
