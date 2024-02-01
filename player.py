import questionary


def validMove(board, move):
    if board[move[0] - 1][move[1] - 1] != "_":
        return False
    return True


def validateMove(move):
    if not move.isnumeric():
        return "Must be a number"
    elif int(move) > 3 or int(move) < 1:
        return "Must be from 1-3"
    return True


def getMove():
    row = questionary.text(
        "Enter the row from 1-3",
        validate=validateMove
    ).ask()

    col = questionary.text(
        "Enter the col from 1-3",
        validate=validateMove
    ).ask()
    return (int(row), int(col))
