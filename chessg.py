import chess
import chess.svg
import random

# Function to display the chessboard
def display_board(board):
    print(board)

# Function for human move input
def get_human_move(board):
    while True:
        try:
            move = input("Enter your move (e.g. 'e2e4'): ")
            move = chess.Move.from_uci(move)
            if move in board.legal_moves:
                return move
            else:
                print("Invalid move. Please try again.")
        except:
            print("Invalid input. Please try again.")

# Function for random move generator for machine player
def get_random_move(board):
    legal_moves = [move for move in board.legal_moves]
    return random.choice(legal_moves)

# Function for human vs human mode
def human_vs_human():
    board = chess.Board()

    while not board.is_game_over():
        display_board(board)
        move = get_human_move(board)
        board.push(move)

    print("Game Over: " + board.result())

# Function for human vs machine mode
def human_vs_machine():
    board = chess.Board()

    while not board.is_game_over():
        display_board(board)

        if board.turn:
            move = get_human_move(board)
        else:
            move = get_random_move(board)

        board.push(move)

    print("Game Over: " + board.result())

# Function for machine vs machine mode
def machine_vs_machine():
    board = chess.Board()

    while not board.is_game_over():
        display_board(board)
        print("--------------")
        move = get_random_move(board)
        board.push(move)
    print("Game Over: " + board.result())

# Main function
def main():
    print("Welcome to Chess!")
    print("Select a mode:")
    print("1. Human vs Human")
    print("2. Human vs Machine")
    print("3. Machine vs Machine")

    mode = input("Enter mode (1/2/3): ")

    if mode == '1':
        human_vs_human()
    elif mode == '2':
        human_vs_machine()
    elif mode == '3':
        machine_vs_machine()
    else:
        print("Invalid input. Exiting...")

if __name__ == "__main__":
    main()

