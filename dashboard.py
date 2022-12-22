from turtle import Turtle
from winsound import PlaySound, SND_ASYNC

FONT = ('Ariel', 10, 'normal')
HEALTH_BAR = [(-330, 330), (-310, 330), (-290, 330), (-270, 330), (-250, 330)]


class Dashboard:

    def __init__(self):
        self.health_bar = []
        self.level = 1
        self.healthbar()
        self.current = None

    def healthbar(self):
        for health in HEALTH_BAR:
            bar = Turtle()
            bar.color("green")
            bar.shape("square")
            bar.penup()
            bar.goto(health)
            self.health_bar.append(bar)

    def minus_health(self):
        self.health_bar[-1].goto(1000, 1000)
        self.health_bar.pop()

    def display(self):
        display = Turtle()
        display.color("white")
        display.hideturtle()
        display.penup()
        display.goto(-380, 320)
        display.write(
            arg=f"Lives:                                                             press [a,d] to move, [space] to shoot                                                 Level:{self.level}", align="left", font=FONT)
        self.current = display

    def update(self):
        self.current.clear()
        self.display()

    def victory(self):
        g_over = Turtle()
        g_over.color("yellow")
        g_over.hideturtle()
        g_over.penup()
        g_over.write(arg="V I C T O R Y !", align="center",
                     font=('Ariel', 40, 'bold'))
        PlaySound("sounds/win.wav", SND_ASYNC)

    def game_over(self):
        g_over = Turtle()
        g_over.color("red")
        g_over.hideturtle()
        g_over.penup()
        g_over.write(arg="G A M E O V E R !", align="center",
                     font=('Ariel', 40, 'bold'))
        PlaySound("sounds/lose.wav", SND_ASYNC)
