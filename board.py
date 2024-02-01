
def createBoard():
    return [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]


def printBoard(board):
    boardStr = ""
    for row in board:
        boardStr += "|"
        for elem in row:
            boardStr += elem + "|"
        boardStr += "\n"
    return boardStr


def checkWin(board, player):
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
        for row, col in condition:
            if board[row][col] != player:
                return False
    return True
