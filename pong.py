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
ball.hideturtle()
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = .2
ball.dy = .2

# Score Board

score_a = 0
score_b = 0

score = turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write('score', align='center', font=('courier', 24, 'normal'))

score_value = turtle.Turtle()
score_value.speed(0)
score_value.color('white')
score_value.penup()
score_value.hideturtle()
score_value.goto(0, 235)
score_value.write('{}  |  {}'.format(score_a, score_b) , align='center', font=('courier', 24, 'normal'))

# starting screen

start = turtle.Turtle()
start.speed(0)
start.color('white')
start.penup()
start.hideturtle()
start.goto(0, 0)
start.write('Press Space Bar to start', align='center', font=('courier', 24, 'normal'))

# Winner Screen
winner = turtle.Turtle()
winner.speed(0)
winner.penup()
winner.hideturtle()
winner.goto(0, 35)

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

# Start Game 

start_game = False

def game_start():
    global score_a
    global score_b
    score_a = 0
    score_b = 0
    score_value.clear()
    score_value.write('{}  |  {}'.format(score_a, score_b) , align='center', font=('courier', 24, 'normal'))
    start.clear()
    winner.clear()
    ball.showturtle()
    paddle_a.sety(0)
    paddle_b.sety(0)
    global start_game 
    start_game = True



# Key Binding
wn.listen()

# Start
wn.onkeypress(game_start, 'space')

# if start_game:



# Main Game Loop
while True:
    wn.update()

    if start_game:


        # Movement
        wn.onkeypress(paddle_a_up, 'w')
        wn.onkeypress(paddle_a_down, 's')
        wn.onkeypress(paddle_b_up, 'Up')
        wn.onkeypress(paddle_b_down, 'Down')

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
            score_value.clear()
            score_value.write('{}  |  {}'.format(score_a, score_b) , align='center', font=('courier', 24, 'normal'))


        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            score_value.clear()
            score_value.write('{}  |  {}'.format(score_a, score_b) , align='center', font=('courier', 24, 'normal'))


        # Paddle Bounce
        
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1   
        
        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1   
        

        # Winner

        if score_a == 5:
            start_game = False
            start.write('Press Space Bar to restart', align='center', font=('courier', 24, 'normal'))
            winner.color('red')
            winner.write('Player A Wins!', align='center', font=('courier', 24, 'normal'))
            ball.hideturtle()

        if score_b == 5:
            start_game = False
            start.write('Press Space Bar to restart', align='center', font=('courier', 24, 'normal'))
            winner.color('blue')
            winner.write('Player B Wins!', align='center', font=('courier', 24, 'normal'))
            ball.hideturtle()

            

