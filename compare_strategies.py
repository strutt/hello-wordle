from constants import GUESSES, SOLUTIONS

from strategy import Strategy
from filter_strategy import FilterStrategy

scores = {
    "sequential": Strategy().evaluate(),
    "short_list_guesses": FilterStrategy(candidate_words=GUESSES[:]).evaluate(),
    "short_list_solutions": FilterStrategy(candidate_words=SOLUTIONS[:]).evaluate(),
}


if __name__ == "__main__":
    for name, score in scores.items():
        print(f"{name} = {score}")
