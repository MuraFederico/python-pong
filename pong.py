import turtle

wn = turtle.Screen()

wn.title('pong by Murataci')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)


# Main Game Loop
while True:
    wn.update()
