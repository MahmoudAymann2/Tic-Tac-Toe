import random

# Initialize the Tic-Tac-Toe board
board = [' ' for _ in range(9)]

# Function to display the Tic-Tac-Toe board
def display_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]}|{board[i + 1]}|{board[i + 2]}    {i}|{i + 1}|{i + 2}")
        if i < 6:
            print("-+-+-    -+-+-")

# Function to check if the board is full
def is_board_full(board):
    return ' ' not in board

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to check if the current player wins
def check_current_player_winner(board, player):
    return check_winner(board, player)

# Function for the computer's move (AI)
def computer_move(board):
    empty_cells = [i for i in range(9) if board[i] == ' ']
    return random.choice(empty_cells)

# Function for the player's move
def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if 0 <= move <= 8 and board[move] == ' ':
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function for bidirectional search
def bidirectional_search():
    while True:
        display_board(board)

        # Player's move
        player = player_move(board)
        board[player] = 'X'

        # Check if the player wins
        if check_current_player_winner(board, 'X'):
            display_board(board)
            print("Congratulations! You win!")
            return

        # Check if the board is full (a tie)
        if is_board_full(board):
            display_board(board)
            print("It's a tie!")
            return

        # Computer's move
        computer = computer_move(board)
        board[computer] = 'O'

        # Check if the computer wins
        if check_winner(board, 'O'):
            display_board(board)
            print("The computer wins! You lose.")
            return

        # Check if the board is full (a tie)
        if is_board_full(board):
            display_board(board)
            print("It's a tie!")
            return

# Start the bidirectional search game
bidirectional_search()
