# main.py
import random

# Initial and goal states
initial_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Find the empty tile
def find_empty_tile(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return (i, j)
    return None

# Check if a move is valid
def is_valid_move(x, y):
    return 0 <= x < 3 and 0 <= y < 3

# Swap tiles
def swap_tiles(puzzle, x1, y1, x2, y2):
    puzzle[x1][y1], puzzle[x2][y2] = puzzle[x2][y2], puzzle[x1][y1]

# Move functions
def move_up(puzzle):
    x, y = find_empty_tile(puzzle)
    if is_valid_move(x - 1, y):
        swap_tiles(puzzle, x, y, x - 1, y)
        return True
    return False

def move_down(puzzle):
    x, y = find_empty_tile(puzzle)
    if is_valid_move(x + 1, y):
        swap_tiles(puzzle, x, y, x + 1, y)
        return True
    return False

def move_left(puzzle):
    x, y = find_empty_tile(puzzle)
    if is_valid_move(x, y - 1):
        swap_tiles(puzzle, x, y, x, y - 1)
        return True
    return False

def move_right(puzzle):
    x, y = find_empty_tile(puzzle)
    if is_valid_move(x, y + 1):
        swap_tiles(puzzle, x, y, x, y + 1)
        return True
    return False

# Shuffle the puzzle
def shuffle_puzzle(puzzle, moves=20):
    for _ in range(moves):
        move = random.choice([move_up, move_down, move_left, move_right])
        move(puzzle)

# Display the puzzle
def display_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(str(tile) if tile != 0 else " " for tile in row))
    print()

# Check for win
def is_goal_state(puzzle):
    return puzzle == goal_state

# Game loop
def play_game():
    puzzle = [row[:] for row in initial_state]  # Create a copy of the initial state
    shuffle_puzzle(puzzle)
    
    while not is_goal_state(puzzle):
        display_puzzle(puzzle)
        move = input("Enter move (u/d/l/r): ").strip().lower()
        
        if move == 'u':
            if not move_up(puzzle):
                print("Invalid move!")
        elif move == 'd':
            if not move_down(puzzle):
                print("Invalid move!")
        elif move == 'l':
            if not move_left(puzzle):
                print("Invalid move!")
        elif move == 'r':
            if not move_right(puzzle):
                print("Invalid move!")
        else:
            print("Invalid input! Use u (up), d (down), l (left), r (right).")
    
    print("Congratulations! You solved the puzzle!")
    display_puzzle(puzzle)

# Run the game
if __name__ == "__main__":
    play_game()