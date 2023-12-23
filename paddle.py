from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        """
        Initializes a Paddle object.

        Args:
            position (tuple): The initial position of the paddle.
        """
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """
        The function `go_up()` is a callback function that moves the paddle up by 20 units when the "Up" key is pressed.
        """
        y = self.ycor()
        y += 20
        self.sety(y)

    def go_down(self):
        """
        The function `go_down()` is a callback function that moves the paddle down by 20 units when the "Down" key is pressed.
        """
        y = self.ycor()
        y -= 20
        self.sety(y)

