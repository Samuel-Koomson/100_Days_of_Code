from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.write('Score', False, "Center", ('Arial', 8, 'normal'))
        self.hideturtle()

    def update_score(self):
        self.write(f"Score {self.score}", False, "Center", ('Arial', 8, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "Center", ('Arial', 12, 'normal'))

    def new_score(self):
        self.score += 1
        self.clear()
        self.update_score()