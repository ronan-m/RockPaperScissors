class Results:
    player_number_of_win = 0
    computer_number_of_win = 0

    def show(self):
        return {"player": self.player_number_of_win,
                "computer": self.computer_number_of_win}