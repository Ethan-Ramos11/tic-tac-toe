import random


class EasyBot:
    """
    The simplest bot in the game. It picks a random spot on the board
    regardless of the state of the game.
    """
    token = ""

    def __init__(self, token) -> None:
        self.token = token

    def pickSpot(self):
        return (random.randint(0, 2), random.randint(0, 2))
