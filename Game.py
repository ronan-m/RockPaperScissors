import random
from History import History
from Results import Results


class Game:
    history = History()
    results = Results()
    player_handsign = ""
    elements = ("rock", "paper", "scissors")
    message = "You played {}, I played {}, you {}"

    def check(self, handsign):
        if handsign in Game.elements:
            print(Game.play(handsign))
        else:
            return 400

    def play(self, player_handsign):
        computer_handsign = random.choice(self.elements)
        self.history.computer_last_handsign = computer_handsign
        self.history.player_last_handsign = player_handsign
        self.compare(computer_handsign, player_handsign)

    def compare(self, computer_handsign, player_handsign):
        if player_handsign == computer_handsign:
            return Game.drow(self)
        # player wins
        elif (player_handsign == "rock" and computer_handsign == "scissors") \
                or (player_handsign == "paper" and computer_handsign == "rock") \
                or (player_handsign == "scissors" and computer_handsign == "paper"):
            return Game.player_win(self)
        # computer wins
        elif (player_handsign == "rock" and computer_handsign == "paper") \
                or (player_handsign == "paper" and computer_handsign == "scissors") \
                or (player_handsign == "scissors" and computer_handsign == "rock"):
            return Game.player_lose(self)

    def player_win(self):
        Game.results.player_number_of_win += 1
        Game.print_message(self, "win")
        return 201

    def player_lose(self):
        Game.results.computer_number_of_win += 1
        Game.print_message(self, "lose")
        return 204

    def drow(self):
        return 418

    def print_message(self, result):
        return Game.message.format(Game.history.player_last_handsign, Game.history.computer_last_handsign, result)

    def show_results(self):
        Game.results.show()

    def init(self):
        Game.results = Results()
        Game.history = History()

    def reset(self):
        Game.init()
