import board
import player


def gameLoop():
    currBoard = board.Board()
    gameStillGoing = True
    bot = player.getLevel()
    while gameStillGoing:
        currBoard.printBoard()
        move = player.getMove()
        break


gameLoop()
