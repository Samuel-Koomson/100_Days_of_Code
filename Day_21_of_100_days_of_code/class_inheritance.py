class Human:
    def __init__(self):
        self.move = 'move'

    def walk(self):
        print('move forward one step at a time')

class Woman(Human):
    def __init__(self):
        super().__init__()
    def dance(self):
        print('women dance by shaking their waists')

kofi = Human()
kofi.walk()

adwoa = Woman()
adwoa.walk()
adwoa.dance()
print(adwoa.move)