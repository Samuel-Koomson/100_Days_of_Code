class School:
    pass


"""When you do not want your function to anything yet you use the pass
    keyword to make sure that your code continues
    without any errors"""
first_school = School()
first_school.id = '001'
first_school.location = 'Adenta'
print(first_school.id)
print(first_school.location)

class Ball:
    def __init__(self, football, team, player):
        self.football = football
        self.team = team
        self.player = player

    def league(self, country):
        self.country = country
        print(f"Country league name is {self.country}")

""" The constructor defines attributes of the class which can be called by objects as and when needed"""

ball1 = Ball("jabulani", "Barcelona", "Xavi")
print(ball1.football, ball1.team, ball1.player)
ball1.league('Laliga')


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
