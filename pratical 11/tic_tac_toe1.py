import random

def display_grid(d, grid_size):
    """Display the grid dynamically based on the grid size."""
    print(('.'+'-'*3)*grid_size + '.')
    for row in d:
        print('|', end='')
        for cell in row:
            print(f'{cell}'.center(3), end='|')
        print()
        print(('.' + '-'*3)*grid_size + '.')

def check(d, p, grid_size):
    """Check if the player has won in rows, columns, or diagonals."""
    # Check rows and columns
    for i in range(grid_size):
        if all(d[i][j] == p for j in range(grid_size)):  # Row check
            return True
        if all(d[j][i] == p for j in range(grid_size)):  # Column check
            return True
    
    # Check diagonals
    if all(d[i][i] == p for i in range(grid_size)):  # Left-to-right diagonal
        return True
    if all(d[i][grid_size-i-1] == p for i in range(grid_size)):  # Right-to-left diagonal
        return True
    
    return False

def enter_values(d, player, grid_size):
    """Handle player input and gameplay for the dynamic grid size."""
    z1 = random.randint(0, 1)
    current_player = player[z1]  # Randomly choose who starts first
    
    while True:
        print(f"Player {current_player}'s turn:")
        
        # Get valid coordinates from the player
        x = int(input(f"Enter x coordinate (0-{grid_size-1}): "))
        y = int(input(f"Enter y coordinate (0-{grid_size-1}): "))
        
        # Ensure the coordinates are valid
        if 0 <= x < grid_size and 0 <= y < grid_size:
            if d[x][y] == '':  # Check if the position is empty
                initialize(x, y, d, current_player, grid_size)
            else:
                print("Position is already filled, try again.")
                continue  # Ask for new coordinates if position is filled
        else:
            print(f"Coordinates out of bounds, try again. Valid range: 0 to {grid_size-1}.")
            continue  # Ask for new coordinates if out of bounds
        
        # Check if the current player wins
        if check(d, current_player, grid_size):
            print(f"Player {current_player} wins!")
            break
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'
        
        # Check if the board is full
        if all(d[i][j] != '' for i in range(grid_size) for j in range(grid_size)):
            print("It's a tie!")
            break

def initialize(x, y, d, z1, grid_size):
    """Place the player's symbol on the grid and display the updated grid."""
    d[x][y] = z1
    display_grid(d, grid_size)

# Main program to make the game dynamic
grid_size = int(input("Enter the grid size (e.g., 3 for 3x3 grid): "))
d = [['' for _ in range(grid_size)] for _ in range(grid_size)]  # Initialize grid dynamically
display_grid(d, grid_size)
player = ['X', 'O']
enter_values(d, player, grid_size)
