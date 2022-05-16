import tkinter
import tkinter as tki
from tkinter import messagebox, scrolledtext


TIME = 180
LETTER = 1
SUBMIT = 2
CLEAR = 3
CLEAR_ALL = 4

FONT_STYLE = 'Comic Sans MS'
MIDDLE_BUTTONS_STYLE = {"bg": "White", "fg": "Black", "width": 5,
                        "height": 2, "font": (FONT_STYLE, '10', "bold")}
LOWER_BUTTON_STYLE = {"bg": "white", "fg": "Black", "width": 5,
                     "height": 2, "font": (FONT_STYLE, '20', "bold")}


def combine_funcs(BoggleGui,img):
    BoggleGui._chosen_avatar_img = img
    BoggleGui.main_window()
    return


class BoggleGui:

    def __init__(self, board):
        # create a dictionary that will contain all the buttons that we create
        self._buttons = dict()

        # The board containing letters:
        self._board = board


        # creating the main window
        self.root = tki.Tk()
        self.root.title("Boggle")
        # create avatars
        self._avatar_frame = tki.Frame(self.root, bg='#394d59')
        self._avatar_frame.pack(side=tki.TOP, fill=tki.BOTH)
        img1 = tki.PhotoImage(file="photos\_avatar1.png")
        img2 = tki.PhotoImage(file="photos\_avatar2.png")
        img3 = tki.PhotoImage(file="photos\_avatar3.png")
        img4 = tki.PhotoImage(file="photos\_avatar4.png")
        self._chosen_avatar_img = img1
        self.avatar_lbl = tki.Label(self._avatar_frame, text="choose your avatar:",
                                       bg="#394d59", fg="black",
                                       font=(FONT_STYLE, '17', "bold"))
        self.avatar_lbl.pack(side=tki.TOP)
        self._avatar1_btn = tki.Button(self._avatar_frame, image=img1,borderwidth=0,
                                     command=combine_funcs(self, img1))
        self._avatar1_btn.photo = img1
        self._avatar1_btn.pack(side=tki.RIGHT)
        self._avatar2_btn = tki.Button(self._avatar_frame, image=img2,borderwidth=0,
                                     command=combine_funcs(self, img2))
        self._avatar2_btn.photo = img2
        self._avatar2_btn.pack(side=tki.RIGHT)
        self._avatar3_btn = tki.Button(self._avatar_frame, image=img3,borderwidth=0,
                                     command=self.main_window)
        self._avatar3_btn.photo = img3
        self._avatar3_btn.pack(side=tki.RIGHT)
        self._avatar4_btn = tki.Button(self._avatar_frame, image=img4,borderwidth=0,
                                     command=self.main_window)
        self._avatar4_btn.photo = img4
        self._avatar4_btn.pack(side=tki.RIGHT)

        # create a fictive button that will start a new game if the user wants
        # to play again
        self._clear_all_btn = tki.Button(self.root)
        self._buttons[(CLEAR_ALL, 0, 0)] = self._clear_all_btn

        # setting the avatar label:
        self._avatar_lbl = tki.Label(self._avatar_frame, image=img1)
        self._avatar_lbl.photo = img1

        # Setting the frame that will consist the logo, score,
        # timer and text box
        self._outer_frame = tki.Frame(self.root, bg='#394d59')
        self._outer_frame.pack(side=tki.TOP, fill=tki.BOTH)

        # setting the timer:
        self._timer_lbl = tki.Label(self._outer_frame, font=78)

        # setting the logo:
        logo_img = tki.PhotoImage(file="photos\logo.png")
        self._logo_lbl = tki.Label(self._outer_frame, image=logo_img,
                                   borderwidth=0, highlightthickness=0)
        self._logo_lbl.photo = logo_img

        # setting the score label:
        self.display_score = tki.Label(self._outer_frame, text="score\n0",
                                       bg="#394d59", fg="Yellow",
                                       font=(FONT_STYLE, '17', "bold"))

        # setting the users choices label
        self._middle_frame = tki.Frame(self.root, bg='#394d59')
        self._middle_frame.pack(side=tki.TOP, fill=tki.BOTH)
        self._current_word_lbl = tki.Label(self._middle_frame, text="",
                                           bg="gray", width=56, height=3,
                                           font=(FONT_STYLE, 8, "bold"))

        # setting the submit button
        self._submit_btn = tki.Button(self._middle_frame, text="Submit",
                                      **MIDDLE_BUTTONS_STYLE)
        self._buttons[(SUBMIT, 0, 0)] = self._submit_btn

        # setting the clear button
        self._clear_btn = tki.Button(self._middle_frame, text="Clear",
                                     **MIDDLE_BUTTONS_STYLE)
        self._buttons[(CLEAR, 0, 0)] = self._clear_btn

        # Setting the frame that will include the board buttons(letters)
        self._lower_frame = tki.Frame(self.root, bg='#394d59')
        self._lower_frame.pack(side=tki.TOP, fill=tki.BOTH, padx=(0, 300))

        # Create the board buttons:
        self.make_lower_frame_buttons()

        # Create a title for Word Bank
        self._word_bank_lbl = tki.Label(self._lower_frame, text="WORD BANK",
                                        bg='#394d59',
                                        font=(FONT_STYLE, 20, "bold"),
                                        width=19)

        # Create a text box to put in it all the words of the word bank.
        self._word_bank_text = tki.scrolledtext.ScrolledText(self._lower_frame,
                                                             width=19,
                                                             height=10,
                                                             bg='#394d59',
                                                             font=(FONT_STYLE,
                                                                   14, "bold"),
                                                             state="disabled",
                                                             wrap=tki.WORD)



    def main_window(self):

        # destroying the start window in order to show the main game window:
        self._avatar1_btn.destroy()
        self._avatar2_btn.destroy()
        self._avatar3_btn.destroy()
        self._avatar4_btn.destroy()
        self.avatar_lbl.destroy()

        # setting the window
        self.root.configure(bg='#394d59')
        self.root.geometry("1200x600")

        # Placing the timer in the window:
        self._timer_lbl.grid(row=0, column=0, sticky=tki.N)
        self.game_timer(TIME)

        # Placing the logo of boggle in the window:
        self._logo_lbl.grid(row=0, column=1, padx=400)

        # Placing the avatar
        self._avatar_lbl.grid(row=1, column=3)

        # Placing the score and current word display box in the window:
        self.display_score.grid(row=1, column=1, padx=278, sticky=tki.NE)
        self._current_word_lbl.grid(row=0, column=0, padx=(400, 0),
                                    pady=(0, 2))
        self._current_word_lbl.columnconfigure(0, weight=10)

        # Placing the submit and clear buttons in the window:
        self._submit_btn.grid(row=0, column=1, padx=(2, 0))
        self._clear_btn.grid(row=0, column=2)

        # Placing the word bank title and word bank text box in the window

        self._word_bank_lbl.grid(row=0, column=0, padx=(0, 70), rowspan=1)
        self._word_bank_text.grid(row=1, column=0, rowspan=4, sticky=tki.NSEW)
        # Placing the board buttons in the window
        self.place_board_buttons_in_window()

    def place_board_buttons_in_window(self):
        """This function will place all the buttons of letters on the window"""
        for i in range(len(self._board)):
            tki.Grid.rowconfigure(self._lower_frame, i, weight=1)
        for i in range(1, len(self._board) + 1):
            tki.Grid.columnconfigure(self._lower_frame, i, weight=1)
        for key, val in self._buttons.items():
            if key[0] == LETTER:
                val.grid(row=key[1], column=key[2] + 1, sticky=tki.NSEW,
                         padx=(1,0))

    def make_lower_frame_buttons(self):
        """This function will create a button for each letter on the
        board given and add it to the dictionary of buttons"""
        for row in range(len(self._board)):
            for col in range(len(self._board[0])):
                button_char = self._board[row][col]
                self.make_board_button(button_char, row, col)

    def make_board_button(self, button_char, row, col):
        """This function will create a single button for a letter"""
        button = tki.Button(self._lower_frame, text=button_char,
                            **LOWER_BUTTON_STYLE)
        self._buttons[(LETTER, row, col)] = button

    def update_board_buttons(self):
        """updates the text of the board buttons to the letters of the new
        board"""
        for button, button_val in self._buttons.items():
            if button[0] == LETTER:
                row = button[1]
                col = button[2]
                button_val.configure(text=self._board[row][col])

    def game_timer(self, countdown):
        """Creates a timer for the game and asks the user if he would
        like to play again. If he does: creates a new game."""
        min, sec = divmod(countdown, 60)
        # show the timer with up to 2 decimal places in minutes and second:
        self._timer_lbl['text'] = "{:02d}:{:02d}".format(int(min), int(sec))

        if countdown != 0:
            self.root.after(1000, self.game_timer, countdown - 1)
        else:
            # Ask the user if he wants to play again:
            another_round = messagebox.askquestion("play again",
                                                   "Time's up! Play again?")
            if another_round == "no":
                self.root.destroy()
            # create a New game:
            else:
                self.game_timer(TIME)
                # execute the command of clear all button:
                self._clear_all_btn.invoke()
                self.update_board_buttons()

    def set_display(self, display_values):
        """update the display of the gui to new display."""
        current_word = display_values[0]
        current_score = display_values[1]
        word_bank = display_values[2]
        board = display_values[3]
        self._current_word_lbl["text"] = current_word
        self.display_score["text"] = "score\n" + current_score
        self._word_bank_text.config(state="normal")
        self._word_bank_text.delete("1.0", "end")
        self._word_bank_text.insert(tki.INSERT, word_bank)
        self._word_bank_text.config(state="disabled")
        self._board = board

    def set_button_command(self, button_tuple, cmd):
        """associates between a button and the command that will be executed
        when the button is clicked."""
        self._buttons[button_tuple].configure(command=cmd)

    def get_buttons_chars(self):
        """returns the button dictionary"""
        return self._buttons

    def start_game(self):
        """will start the game"""
        self.root.mainloop()