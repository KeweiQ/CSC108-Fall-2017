"""Phrase Puzzler: functions"""

# Phrase Puzzler constants

# Name of file containing puzzles
DATA_FILE = 'puzzles_small.txt'

# Letter values
CONSONANT_POINTS = 1
VOWEL_PRICE = 1
CONSONANT_BONUS = 2

# Players' names
PLAYER_ONE = 'Player One'
PLAYER_TWO = 'Player Two'

# Menu options - includes letter types
CONSONANT = 'C'
VOWEL = 'V'
SOLVE = 'S'
QUIT = 'Q'


# Define your functions here.

def is_win(puzzle: str, view: str) -> bool:
    """Return True if and only if puzzle is the same as view.

    >>> is_win('banana', 'banana')
        True
    >>> is_win('apple', 'a^^le')
        False
    """
    return puzzle == view

def game_over(puzzle: str, view: str, current_selection: str) -> bool:
    """Return True if and only if the puzzle is the same
    as the view or the current selection is QUIT.
    
    >>> game_over('apple', 'apple', 'C')
        True
    >>> game_over('apple', 'a^^le', 'Q')
        False
    """
    return puzzle == view or current_selection == QUIT

def bonus_letter(puzzle: str, view: str, letter_to_evaluate: str) -> bool:
    """Return True if and only if the letter appears
    in the puzzle but not in its view.
    
    >>> bonus_letter('apple', 'a^^le', 'p')
        True
    >>> bonus_letter('banana', '^anana', 'k')
        False
    """
    return letter_to_evaluate in puzzle and not letter_to_evaluate in view

def update_letter_view(puzzle: str, view: str, index: int, guess: str) -> str:
    """Return a single character string representing
    the next view of the character at the given index.
    If the character at that index of the puzzle matches the guess,
    then return that character.
    Otherwise, return the character at that index of the view.
    
    >>> update_letter_view('peach', '^each', 0, 'p')
        'p'
    >>> update_letter_view('peach', '^each', 0 ,'d') 
        '^'
    """
    if puzzle[index] == guess:
        return guess
    else:
        return view[index]
    
def calculate_score(current_score: int, occurrences: int, letter_type: str) -> int:
    """Return the new score by adding CONSONANT_POINTS per occurrence of
    the letter to the current score if the letter is a consonant,
    or by deducting the VOWEL_PRICE from the score if the letter is a vowel.
    
    >>> calculate_score(2, 1, 'C')
        3
    >>> calculate_score(2, 1, 'V')
        1
    """
    if letter_type == CONSONANT:
        return current_score + occurrences * CONSONANT_POINTS
    elif letter_type == VOWEL:
        return current_score - VOWEL_PRICE
    
def next_player(current_player: str, number_of_occurrences: int) -> str:
    """If and only if the number of occurrences is greater than zero,
    the current player plays again.
    Return the next player (one of PLAYER_ONE or PLAYER_TWO).
    
    >>> next_player('Player One', 0)
        'Player Two'    
    >>> next_player('Player One', 5)
        'Player One'    
    """
    if current_player == PLAYER_ONE and number_of_occurrences == 0:
        return PLAYER_TWO
    elif current_player == PLAYER_ONE and number_of_occurrences > 0:
        return PLAYER_ONE
    elif current_player == PLAYER_TWO and number_of_occurrences == 0:
        return PLAYER_ONE
    else:
        return PLAYER_TWO
   