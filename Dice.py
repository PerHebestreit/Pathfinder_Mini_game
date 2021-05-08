import random


class Dice:
    def d20(self):
        result = random.randint(1, 20)
        return result