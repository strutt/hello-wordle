"""
Explore ideas...
"""
from collections import defaultdict

from constants import SOLUTIONS, GUESSES



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

# print(weird_words())
print(len(SOLUTIONS))
print(len(GUESSES))
import sys
sys.exit(1)

"""
There are 5 letters, each letter has 3 possible colours B, Y, G...

Therefore there are 3*3*3*3*3 possible sets of feedback from any given guess


"""
num_sets_of_possible_feedback = pow(3, 5) # 243

# A "perfect guess" would have equal probability of all sets of
# feedback.  That guess would then split the solution space down by
# 1/243.  Clearly this is not actually possible since there's only one
# GGGGG possibility, which is the solution.

# But pretending it is, if there's 2300-ish solutions, you'd go down
# to 10 possibilites.  So, the good guesses have a wide distribution
# of possible feedback. How do I quantify this width?
