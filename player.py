import questionary


def validMove(board, move):
    if board[move[0]][move[1]] != "_":
        return False
    return True
