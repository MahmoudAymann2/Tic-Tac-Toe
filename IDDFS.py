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

# Function for the computer's move using IDDFS
def computer_move_iddfs(board, player, max_depth):
    best_move = None

    for depth in range(1, max_depth + 1):
        move, _ = iddfs(board, depth, player, player, max_depth)
        if move is not None:
            best_move = move

    return best_move

# Iterative Deepening Depth-First Search (IDDFS)
def iddfs(board, depth, current_player, player, max_depth):
    if depth == 0 or check_winner(board, 'O' if player == 'X' else 'X'):
        return None, 0

    best_move = None
    best_score = -float('inf') if current_player == player else float('inf')

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O' if current_player == 'X' else 'X'
            _, score = iddfs(board, depth - 1, player, player, max_depth)
            board[i] = ' '

            if current_player == player:
                if score > best_score:
                    best_score = score
                    best_move = i
            else:
                if score < best_score:
                    best_score = score
                    best_move = i

    return best_move, best_score

# Main game loop with IDDFS-based computer move
def play_game_iddfs():
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

        # Computer's move using IDDFS
        computer = computer_move_iddfs(board, 'O', max_depth=9)  # You can adjust the depth as needed
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

# Start the game with IDDFS-based computer move
play_game_iddfs()
