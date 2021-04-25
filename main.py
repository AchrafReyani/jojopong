import turtle
import winsound
import time

wn = turtle.Screen()
wn.title("JoJo Pong")
wn.bgcolor("light blue")
wn.setup(width=800, height=600)
wn.tracer(0)
#wn.bgpic("jodo.gif")

# Score
score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("dark blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1
LeftSpeed = -0.1
RightSpeed = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Jotaro: 0  Dio: 0", align="center", font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 80
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 80
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 80
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 80
    paddle_b.sety(y)


def ZA_WARUDO():
    winsound.PlaySound("assets/ZA WARUDO.wav", winsound.SND_ASYNC)
    wn.bgcolor("pink")
    ball.dx = 0
    ball.dy = 0
    time.sleep(3)
    ball.dx = -1.2
    ball.dy = 1
    wn.bgcolor("light blue")


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "[")
wn.onkeypress(paddle_b_down, "'")
wn.onkeypress(ZA_WARUDO, ";")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = 0.3
        ball.dy = -0.3
        ball.dx *= -1
        LeftSpeed = -0.1
        RightSpeed = 0.1
        score_a += 1
        pen.clear()
        pen.write("Jotaro: {}  Dio: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = 0.3
        ball.dy = -0.3
        ball.dx *= -1
        LeftSpeed = -0.1
        RightSpeed = 0.1
        score_b += 1
        pen.clear()
        pen.write("Jotaro: {}  Dio: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
        ball.setx(340)
        LeftSpeed -= 0.3
        ball.dx = LeftSpeed

        winsound.PlaySound("assets/muda muda.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
        ball.setx(-340)
        RightSpeed += 0.3
        ball.dx = RightSpeed

        winsound.PlaySound("assets/ORA.wav", winsound.SND_ASYNC)
