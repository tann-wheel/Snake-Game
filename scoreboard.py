from turtle import Turtle
import random

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.ht()
        self.write(f"Score:{self.score} ",align="center",font=('Arial', 10, 'normal'))



    def update_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score:{self.score} ",align="center",font=('Arial', 10, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=('Arial', 10, 'normal'))
