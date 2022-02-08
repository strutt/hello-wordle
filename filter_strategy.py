from typing import List
from collections import defaultdict

from constants import GUESSES
from wordle import LetterFeedback
from strategy import Strategy

def _zero():
    return 0


class Filter:
    """
    Filter the list of allowed guesses based on a previous guess.
    """
    def __init__(self, last_guess, feedbacks: List[LetterFeedback]):
        self.last_guess = last_guess
        self.feedbacks = feedbacks
        must_match = [None for _ in last_guess]
        must_not_match = [None for _ in last_guess]
        required_count = defaultdict(_zero)
        for i, letter, feedback in zip(range(len(self.last_guess)), self.last_guess, self.feedbacks):
            if feedback == LetterFeedback.HERE:
                must_match[i] = letter
                required_count[letter] = required_count[letter] + 1
            elif feedback == LetterFeedback.ELSEWHERE:
                must_not_match[i] = letter
                required_count[letter] = required_count[letter] + 1

        max_count = defaultdict(_zero)
        for i, letter, feedback in zip(range(len(self.last_guess)), self.last_guess, self.feedbacks):
            if feedback == LetterFeedback.NOT_IN_WORD:
                max_count[letter] = required_count.get(letter, 0)

        self.must_match = must_match
        self.must_not_match = must_not_match
        self.required_count = dict(**required_count)
        self.max_count = dict(**max_count)

    def __call__(self, word):
        for char, must_match, must_not_match in zip(word, self.must_match, self.must_not_match):
            if must_match and char != must_match:
                return False
            if must_not_match and char == must_not_match:
                return False

            char_count = word.count(char)
            if char in self.required_count:
                if char_count < self.required_count[char]:
                    return False

            if char in self.max_count:
                if char_count > self.max_count[char]:
                    return False

        return True


class FilterStrategy(Strategy):
    """
    Shorten a candidate list of words based on feedback from the
    wordle game.
    """

    def next_guess(self, candidate_words):
        counts = [defaultdict(_zero) for _ in range(5)]
        for word in candidate_words:
            for i, char in enumerate(word):
                counts[i][char] = counts[i][char] + 1
        word_scores = {}
        for word in candidate_words:
            score = 0
            for i, char in enumerate(word):
                score = score + counts[i][char]
            word_scores[word] = score
        best_score = max(word_scores.values())
        for word, score in word_scores.items():
            if score == best_score:
                return word

    def __init__(self, candidate_words = None):
        if candidate_words is None:
            candidate_words = GUESSES[:]
        self.candidate_words = candidate_words


    def play(self, wordle):
        candidate_words = self.candidate_words[:]
        while not wordle.finished:
            guess = self.next_guess(candidate_words)
            feedback = wordle.guess(guess)
            candidate_words = list(filter(Filter(guess, feedback), candidate_words))
        return wordle.score
