import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = "X"
winner = None
gameRunning = True

# Game board
def printboard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("---------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("---------")
    print(board[6] + "|" + board[7] + "|" + board[8])

# Take player input
def playerInput(board):
    inp = int(input("Select a spot 1-9: "))
    if board[inp-1] == "-":
        board[inp-1] = current_player
    else:
        print("OOPS!!! A player is already at that spot.")

# Check for win or tie
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] != "-":
        winner = board[6]
        return True
    return False

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] != "-":
        winner = board[2]
        return True
    return False

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] != "-":
        winner = board[2]
        return True
    return False

def checkIfWin(board):
    if checkHorizontle(board) or checkRow(board) or checkDiag(board):
        printboard(board)
        print(f"The winner is {winner}!")
        return True
    return False

def checkIfTie(board):
    if "-" not in board:
        printboard(board)
        print("It's a tie!!!")
        return True
    return False

def switchPlayer():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def computer(board):
    while current_player == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

# Main game loop
while gameRunning:
    printboard(board)
    playerInput(board)
    if checkIfWin(board) or checkIfTie(board):
        gameRunning = False
    switchPlayer()
    computer(board)
    if checkIfWin(board) or checkIfTie(board):
        gameRunning = False
