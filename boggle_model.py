import boggle_board_randomizer
import ex12_utils


TIME = 180
LETTER = 1
SUBMIT = 2
CLEAR = 3
CLEAR_ALL = 4


class BoggleModel:

    def __init__(self):
        """initialize the boggle game"""
        self._start_game()

    def _start_game(self):
        """initialize the word dictionary and clear all the games parameters"""
        self._words_dict = ex12_utils.create_word_dict("boggle_dict.txt")
        self._clear_all()

    def _clear_all(self):
        """set all the game parameters."""
        self._board = boggle_board_randomizer.randomize_board()
        self._time = TIME
        self._score = 0
        self._word_bank = []
        self._last_clicked = None
        self._clear_path_and_word()

    def get_board(self):
        """returns the board"""
        return self._board

    def _clear_path_and_word(self):
        """set the current path and word back to starting position."""
        self._current_path = []
        self._current_word = ""

    def key_pressed(self, button_val):
        """
        The function will operate an action according to the button that was
        pressed.
        :param button_val: what type button was pressed
        """
        self._last_clicked = button_val[0]
        if self._last_clicked == LETTER:
            self.update_path(button_val)
            self.update_word(button_val)
        elif self._last_clicked == SUBMIT:
            word = ex12_utils.is_valid_path(self._board, self._current_path,
                                            self._words_dict)
            if word is not None and word not in self._word_bank:
                self._update_word_bank()
                self.update_score()
            self._clear_path_and_word()
        elif button_val[0] == CLEAR:
            self._clear_path_and_word()
        elif button_val[0] == CLEAR_ALL:
            self._clear_all()

    def _update_word_bank(self):
        """Add the current word to the word bank"""
        self._word_bank.append(self._current_word)

    def update_word(self, button_val):
        """Add the letter of the button to the current word"""
        row = button_val[1]
        col = button_val[2]
        self._current_word += self._board[row][col]

    def update_path(self, button_val):
        """Add the coordinates of the letter on the board to the current
        path"""
        row = button_val[1]
        col = button_val[2]
        self._current_path.append((row, col))

    def update_score(self):
        """add to the score"""
        self._score += len(self._current_path) ** 2


    def get_display(self):
        """return the current word, score, word bank and board"""
        return self._current_word, str(self._score), \
               ", ".join(self._word_bank), self._board
