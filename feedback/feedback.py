from enum import IntEnum, auto
from collections import defaultdict
import pathlib

import numpy as np

from constants import GUESSES, SOLUTIONS

NUM_FEEDBACK = 243

if len(GUESSES) != 12972:
    raise ValueError("Invalid GUESSES")
if len(SOLUTIONS) != 2315:
    raise ValueError("Invalid SOLUTIONS")


_guess_indices = {w: i for i, w in enumerate(GUESSES)}
_solution_indices = {w: i for i, w in enumerate(SOLUTIONS)}

_feedback = None

def _get_feedback():
    global _feedback
    if _feedback is None:
        _feedback = np.load(pathlib.Path(__file__).parent.joinpath("feedback.npy"))
    return _feedback

def get_feedback(guess, solution, as_int=False):
    i = guess if isinstance(guess, int) else _guess_indices[guess]
    j = _solution_indices[solution]
    f = _get_feedback()[i][j]
    if as_int:
        return f
    return int_to_feedback(f)

def get_feedback_array(guess):
    i = _guess_indices[guess]
    return _get_feedback()[i]


class LetterFeedback(IntEnum):
    NOT_IN_WORD = 0
    ELSEWHERE = 1
    HERE = 2


_feedback_to_int = {}

def feedback_to_int(feedback):
    feedback = tuple(feedback)
    global _feedback_to_int
    if feedback in _feedback_to_int:
        return _feedback_to_int[feedback]

    multiplier = 1
    s = 0
    for l in feedback:
        s = s + l*multiplier
        multiplier = multiplier*3
    _feedback_to_int[feedback] = s
    return s

_int_to_feedback = None

def int_to_feedback(i):
    global _int_to_feedback
    if _int_to_feedback is None:
        _int_to_feedback = list(range(243))
        for lfb0 in LetterFeedback:
            for lfb1 in LetterFeedback:
                for lfb2 in LetterFeedback:
                    for lfb3 in LetterFeedback:
                        for lfb4 in LetterFeedback:
                            fb = (lfb0, lfb1, lfb2, lfb3, lfb4)
                            j = feedback_to_int(fb)
                            _int_to_feedback[j] = fb

    return _int_to_feedback[i]
                            

                    



    


