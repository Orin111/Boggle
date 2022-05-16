from boggle_model import BoggleModel
from boggle_gui import BoggleGui


class BoggleController:
    def __init__(self):
        self._model = BoggleModel()
        board = self._model.get_board()
        self._gui = BoggleGui(board)

        # Associate between the buttons and the command that will be executed
        for button_tuple in self._gui.get_buttons_chars():
            action = self.create_button_action(button_tuple)
            self._gui.set_button_command(button_tuple, action)


    def create_button_action(self, button_tuple):
        def inner():
            self._model.key_pressed(button_tuple)
            self._gui.set_display(self._model.get_display())

        return inner


    def run(self):
        self._gui.start_game()


if __name__ == "__main__":
    bg = BoggleController()
    bg.run()





