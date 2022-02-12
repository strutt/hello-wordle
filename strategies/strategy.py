from random import shuffle

from progressbar import progressbar

from constants import SOLUTIONS, GUESSES
from wordle import Wordle

RANDOM_SOLUTIONS = SOLUTIONS[:]
shuffle(RANDOM_SOLUTIONS)

class Strategy:
    """
    Strategy base class.

    This is the stupidest possible strategy that is guarenteed to win
    (with an arbitrarily high number of `max_guesses`), guessing all
    the allowed guesses in order.

    Subclasses should override the `play` method with a smarter.
    """
    def evaluate(self, max_guesses=100):
        score = 0
        solutions = RANDOM_SOLUTIONS[:100]
        for solution in progressbar(solutions):
            game = Wordle(answer=solution, max_guesses=max_guesses)
            self.play(game)
            score = score + game.score
            print(game.score)
        return score/len(solutions)

    def play(self, game) -> int:
        """
        Override this in subclasses with an actual strategy.
        """
        for word in GUESSES:
            game.guess(word)
            if game.finished:
                break
        return game.score
