import questionary

def createBoard():
    return [['_','_','_'],['_','_','_'],['_','_','_']]

def printBoard(board):
    boardStr = ""
    for row in board:
        boardStr += "|"
        for elem in row:
            boardStr += elem + "|"
        boardStr += "\n"
    return boardStr

print(printBoard(createBoard()))
def validMove(board, move):
    pass

def checkWin(board):
    pass

def startGameEasy():
    pass

def startGameMedium():
    pass

def startGameHard():
    pass

def main():
    print("Welcome to tic-tac-toe!")
    level = questionary.rawselect(
        "What level would you like to play at?", 
        choices = ["easy", "medium", "hard"])
    if level == "easy":
        startGameEasy()
    elif level == "medium":
        startGameMedium()
    else:
        startGameHard()
    
