"""
Explore ideas...
"""
from collections import defaultdict

from constants import SOLUTIONS



def find_solution_with_highest_frequencies():
    counts = [defaultdict(lambda: 0) for _ in range(5)]

    for solution in SOLUTIONS:
        for i, char in enumerate(solution):
            counts[i][char] = counts[i][char] + 1

    solution_scores = {}
    for solution in SOLUTIONS:
        score = 0
        for i, char in enumerate(solution):
            score = score + counts[i][char]
        solution_scores[solution] = score


    best_score = max(solution_scores.values())
    for solution, score in solution_scores.items():
        if score == best_score:
            print(solution)


# find_solution_with_highest_frequencies()

def weird_words():

    def get_max(word):
        chars = set(word)
        return max(word.count(char) for char in chars)

    _max = 0
    _max_word = None
    for word in SOLUTIONS:
        this_max = get_max(word)
        if this_max > _max:
            _max= this_max
    words = [word for word in SOLUTIONS if get_max(word) >= _max]
    return words

print(weird_words())
