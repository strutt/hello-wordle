from constants import SOLUTIONS, GUESSES


def test_consistent():
    for solution in SOLUTIONS:
        assert solution in GUESSES
    
