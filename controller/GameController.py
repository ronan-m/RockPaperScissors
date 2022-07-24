from masonite.controllers import Controller
from masonite.request import Request
from Game import Game


class GameController(Controller):
    def show_results(self):
        return Game.show_results()

    def reset_game(self):
        return Game.reset()

    def play(self, request: Request):
        Game.check(request.input("myHand"))
