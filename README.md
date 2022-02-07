# Hello Wordle

My attempt to write a [wordle](https://powerlanguage.co.uk/wordle) solver.

## Installation
Get yourself a virtual environment and do
```
pip install -r requirements.txt # bootstrap poetry
poetry install # install dependencies
```

## Playing
You can play a (not very pretty) interactive version in your terminal with
```
python terminal_wordle.py
```
But be careful! The genius of wordle is that there's only one game per day.
You may get bored quickly.


## Notes
Word lists, pulled from the wordle source code, in `constants.py`.
Core game logic is in `wordle.py`.

