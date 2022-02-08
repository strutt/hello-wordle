from constants import GUESSES, SOLUTIONS

from strategies.strategy import Strategy
from strategies.filter_strategy import FilterStrategy
from strategies.high_frequency_letter_strategy import HighFrequencyLetterStrategy, HighFrequencyLetterStrategy2
from strategies.memory_strategy import MemoryStrategy

scores = {
    # "sequential": Strategy().evaluate(),
    # "default_filter_guesses": FilterStrategy(candidate_words=GUESSES[:]).evaluate(),
    "high_frequency_letter_strategy": HighFrequencyLetterStrategy(candidate_words=GUESSES[:]).evaluate(),
    "high_frequency_letter_strategy2": HighFrequencyLetterStrategy2(candidate_words=GUESSES[:]).evaluate(),
    # "memory_strategy": MemoryStrategy(candidate_words=GUESSES[:]).evaluate(),
}


if __name__ == "__main__":
    for name, score in scores.items():
        print(f"{name} = {score}")
