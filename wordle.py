import random
from enum import Enum, auto

from constants import GUESSES
from constants import SOLUTIONS

class LetterFeedback(Enum):
    NOT_IN_WORD = auto()
    ELSEWHERE = auto()
    HERE = auto()

class Wordle:
    """
    Rules of the game.
    """

    def __init__(self, answer=None, max_guesses=6):
        """
        You can initialize the game with a specific answer (for testing).
        Or initialize the game with a different number of max guesses (useful for training).

        Don't pass any kwargs for the standard game.
        """

        if answer is None:
            answer = random.choice(SOLUTIONS)

        if answer not in SOLUTIONS:
            raise ValueError(f"Invalid answer: {answer}")

        self._max_guesses = max_guesses
        self._answer = answer
        self._finished = False
        self._win = False
        self._num_guesses = 0

    def guess(self, word) -> bool:
        if self._finished is True:
            raise RuntimeError("Game over already.")

        if word not in GUESSES:
            raise ValueError(f"Invalid guess {word}")

        self._num_guesses = self._num_guesses + 1

        # Feedback...
        feedback = [LetterFeedback.NOT_IN_WORD for _ in word]
        missing_letters = list(self._answer)

        for i, (letter, answer_letter) in enumerate(zip(word, self._answer)):
            if letter == answer_letter:
                feedback[i] = LetterFeedback.HERE
                missing_letters.remove(letter)

        for i, letter in enumerate(word):
            if feedback[i] == LetterFeedback.NOT_IN_WORD and letter in missing_letters:
                feedback[i] = LetterFeedback.ELSEWHERE
                missing_letters.remove(letter)

        if feedback == [LetterFeedback.HERE for _ in self._answer]:
            self._win = True
            self._finished = True

        if self._num_guesses == self._max_guesses:
            self._finished = True

        return feedback

    @property
    def finished(self):
        return self._finished

    @property
    def score(self):
        if self._finished:
            return self._num_guesses
        raise ValueError("Game not over yet.")
