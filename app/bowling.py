class BowlingGame(object):
    def __init__(self):
        self._score = 0

    def roll(self, pin):
        self._score = pin

    def score(self):
        return self._score
