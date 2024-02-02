class Board:
    board = []
    candidateMoves = []

    def __init__(self):
        self.resetBoard()

    def printBoard(self):
        boardStr = ""
        for row in self.board:
            boardStr += "|"
            for elem in row:
                boardStr += elem + "|"
            boardStr += "\n"
        print(boardStr)

    def checkWin(self, player):
        win = False
        winConditions = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],

            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],

            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]
        for condition in winConditions:
            win = True
            for row, col in condition:
                if self.board[row][col] != player:
                    win = False
                    break
            if win:
                return win
        return False

    def makeMove(self, move, player):
        if self.board[move[0] - 1][move[0] - 1] == "_":
            self.board[move[0] - 1][move[0] - 1] = player
            self.candidateMoves.remove(move)

    def resetBoard(self):
        self.board = [['_', '_', '_'],
                      ['_', '_', '_'],
                      ['_', '_', '_']]
        self.candidateMoves = [(1, 1), (1, 2), (1, 3),
                               (2, 1), (2, 2), (2, 3),
                               (3, 1), (3, 2), (3, 3)]
