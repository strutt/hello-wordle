from strategies.filter_strategy import FilterStrategy

from string import ascii_lowercase

class HighFrequencyLetterStrategy(FilterStrategy):
    """
    Just pick the most common letters.
    """

    def next_guess(self, candidate_words, previous_guesses):

        counts = {k:0 for k in ascii_lowercase}

        for word in candidate_words:
            for char in word:
                counts[char] = counts[char]+1

        _max_score = -1
        _word = None
        for word in candidate_words:
            score = sum(counts[char] for car in word)
            if score > _max_score:
                _max_score = score
                _word = word
        return _word


class HighFrequencyLetterStrategy2(FilterStrategy):
    """
    Just pick the most common letters.
    """

    def next_guess(self, candidate_words, previous_guesses):

        counts = {k:0 for k in ascii_lowercase}

        for word in candidate_words:
            for char in word:
                counts[char] = counts[char]+1

        _max_score = -1
        _word = None
        for word in candidate_words:
            score = sum(counts[char] for car in str(word))
            if score > _max_score:
                _max_score = score
                _word = word
        return _word
