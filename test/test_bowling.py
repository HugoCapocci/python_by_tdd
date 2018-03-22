import unittest
from app.bowling import BowlingGame

class BowlingGameTest(unittest.TestCase):

    def test_score_in_a_frame_in_a_roll(self):
        bowlingGame = BowlingGame()
        bowlingGame.roll(4)
        score = bowlingGame.score()
        self.assertEqual(4, score)

if  __name__ == '__main__':
    unittest.main()
