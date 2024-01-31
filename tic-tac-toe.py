import questionary


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
    
