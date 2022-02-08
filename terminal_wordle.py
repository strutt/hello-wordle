from colorama import Back, Style, Fore
from wordle import Wordle, LetterFeedback



class TerminalWordle(Wordle):
    """
    Play Wordle in the terminal.

    It's not pretty, but it is tty.
    
    """

    def __init__(self, answer=None):
        super().__init__(answer=answer)
        self._guesses = []
        while not self._finished:
            try:
                print(self)
                print(f"{self._num_guesses + 1}/6: ", end="")
                self._guesses.append(self.guess())
            except ValueError as e:
                print(e)
        print(self)
        if self._win:
            print(f"Correct! {self.score}/6, the word was {self._answer}")
        else:
            print(f"Bad luck: the word was... {self._answer}")

    def __repr__(self):
        return "\n" + "\n".join(guess for guess in self._guesses) + "\n"
            
    def guess(self):
        word = input()
        feedback = super().guess(word)
        cols = {
            LetterFeedback.NOT_IN_WORD: Back.WHITE,
            LetterFeedback.ELSEWHERE: Back.YELLOW,
            LetterFeedback.HERE: Back.GREEN,
        }

        return "".join(
            f"{cols[col]}{Style.BRIGHT}{char}{Style.RESET_ALL}" for col, char in zip(feedback, word)
        )

if __name__ == "__main__":
    TerminalWordle()
