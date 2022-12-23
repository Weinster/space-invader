from turtle import Turtle


STARTING_POS = (0, -310)
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        """create player"""
        super().__init__()
        self.shape("pictures/spaceship.gif")
        self.penup()
        self.goto(STARTING_POS)
        self.setheading(90)

    def move_left(self):
        """move player to left"""
        if self.xcor() < 370:
            self.goto(y=self.ycor(), x=self.xcor()+MOVE_DISTANCE)

    def move_right(self):
        """move player to right"""
        if self.xcor() > -370:
            self.goto(y=self.ycor(), x=self.xcor()-MOVE_DISTANCE)
