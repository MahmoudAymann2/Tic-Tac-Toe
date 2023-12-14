import random

# Initialize the Tic-Tac-Toe board
board = [' ' for _ in range(9)]


# Function to display the Tic-Tac-Toe board
def display_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])


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


# Function for the computer's move (AI)
def computer_move(board):
    empty_cells = [i for i in range(9) if board[i] == ' ']
    return random.choice(empty_cells)


# Main game loop
def play_game():
    while True:
        display_board(board)

        # Player's move
        while True:
            player_move = int(input("Enter your move (0-8): "))
            if board[player_move] == ' ':
                board[player_move] = 'X'
                break
            else:
                print("Invalid move. Try again.")

        # Check if the player wins
        if check_winner(board, 'X'):
            display_board(board)
            print("Congratulations! You win!")
            break

        # Check if the board is full (a tie)
        if is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break

        # Computer's move
        computer = computer_move(board)
        board[computer] = 'O'

        # Check if the computer wins
        if check_winner(board, 'O'):
            display_board(board)
            print("The computer wins! You lose.")
            break

        # Check if the board is full (a tie)
        if is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break


# Function for the computer's move using DLS
def computer_move_dls(board, player, max_depth):
    best_move = None
    best_score = -float('inf')

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O' if player == 'X' else 'X'
            score = dls(board, 0, False, player, max_depth)
            board[i] = ' '  # Reset the board

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


# Depth-limited search algorithm (DLS)
def dls(board, depth, is_maximizing, player, max_depth):
    if depth == max_depth or check_winner(board,
                                          'O' if player == 'X' else 'X'):
        return 0
    elif check_winner(board, player):
        return 1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O' if player == 'X' else 'X'
                score = dls(board, depth + 1, False, player, max_depth)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = player
                score = dls(board, depth + 1, True, player, max_depth)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score


# Main game loop with DLS-based computer move
def play_game_dls():
    while True:
        display_board(board)

        # Player's move
        while True:
            player_move = int(input("Enter your move (0-8): "))
            if board[player_move] == ' ':
                board[player_move] = 'X'
                break
            else:
                print("Invalid move. Try again.")

        # Check if the player wins
        if check_winner(board, 'X'):
            display_board(board)
            print("Congratulations! You win!")
            break

        # Check if the board is full (a tie)
        if is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break

        # Computer's move using DLS
        computer = computer_move_dls(
            board, 'O', max_depth=3)  # You can adjust the depth as needed
        board[computer] = 'O'

        # Check if the computer wins
        if check_winner(board, 'O'):
            display_board(board)
            print("The computer wins! You lose.")
            break

        # Check if the board is full (a tie)
        if is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break


# Start the game with DLS-based computer move
play_game_dls()