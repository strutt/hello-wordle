"""
This generates a 2D numpy array 
"""

import numpy as np
from progressbar import progressbar
from constants import GUESSES, SOLUTIONS

from feedback.feedback import LetterFeedback, feedback_to_int


x = np.zeros((len(GUESSES),
              len(SOLUTIONS)),
             dtype=np.uint8)


for i, guess in progressbar(enumerate(GUESSES)):
    for j, answer in enumerate(SOLUTIONS):

        feedback = [LetterFeedback.NOT_IN_WORD for _ in guess]
        missing_letters = list(answer)

        for k, (letter, answer_letter) in enumerate(zip(guess, answer)):
            if letter == answer_letter:
                feedback[k] = LetterFeedback.HERE
                missing_letters.remove(letter)

        for k, letter in enumerate(guess):
            if feedback[k] == LetterFeedback.NOT_IN_WORD and letter in missing_letters:
                feedback[k] = LetterFeedback.ELSEWHERE
                missing_letters.remove(letter)
        # print(f"{i}, {j}")
        x[i][j] = feedback_to_int(tuple(feedback))

np.save("feedback.npy", x)
