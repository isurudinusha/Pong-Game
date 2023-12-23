from turtle import Turtle, Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)

def go_up():
    """
    The function `go_up()` moves the paddle up by 20 units.
    """
    y = paddle.ycor()
    y += 20
    paddle.sety(y)


screen.listen()
screen.onkey(paddle.go_up(), "Up")


screen.exitonclick()