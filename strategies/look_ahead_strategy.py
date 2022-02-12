from collections import defaultdict

from strategies.filter_strategy import FilterStrategy, get_filter
from feedback.feedback import LetterFeedback, feedback_to_int, get_feedback
from constants import GUESSES
from progressbar import progressbar

def _zero():
    return 0


class LookAheadStrategy(FilterStrategy):

    """
    There are 5 letters, each letter has 3 possible colours B, Y, G...

    Therefore there are 3*3*3*3*3 = 243 possible sets of feedback from any
    given guess.

    A "perfect guess" would have equal probability of all sets of
    feedback.  That guess would then split the solution space down by
    1/243.  Clearly this is not actually possible since there's only
    one GGGGG possibility, which is the solution.

    But pretending it is, if there's 2300-ish solutions, you'd go down
    to 10 possibilites.  So, the good guesses have a wide distribution
    of possible feedback.  How do I quantify this width?
    """
    # num_sets_of_possible_feedback = pow(3, 5) # 243

    def next_guess(self, candidate_words, previous_guesses):
        # It always chose the first thing each time
        if len(previous_guesses) == 0:
            return "reast" #"slate"
        
        best = None
        best_score = None
        for g_i, next_guess in enumerate(GUESSES):
            if next_guess in previous_guesses:
                continue

            values = [0 for _ in range(243)]
            for candidate_word in candidate_words:
                i = get_feedback(next_guess, candidate_word, as_int=True)
                values[i] = values[i] + 1
            values = sorted(values, reverse=True)

            score=0
            for _i, v in enumerate(values):
                if v == 0:
                    break
                score = score + (_i+1)*v

            # Add bonus points for guess being in candidate words list
            if next_guess in candidate_words:
                score = score + 10
                
            if best_score is None or score > best_score:
                best_score = score
                best = next_guess
                # print(f"{next_guess}: {score}... {best}: {best_score}")
                
        # print(f"{best}: {best_score}")
        return best
            

            
