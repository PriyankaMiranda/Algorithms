def generate_spiral_matrix(n):
    # Direction vectors for right, down, left, up
    column_offsets = [1, 0, -1, 0]
    row_offsets = [0, 1, 0, -1]

    matrix = [[0] * n for _ in range(n)]

    value = 0
    direction = 0  # Start by moving right
    row_loc, col_loc = 0, 0  # Start at top-left

    while value < n * n:
        value += 1
        matrix[row_loc][col_loc] = value

        # Calculate next position
        next_row = row_loc + row_offsets[direction]
        next_col = col_loc + column_offsets[direction]

        # Check if we need to change direction
        if (
            next_row < 0 or next_col < 0 or  # Out of bounds
            next_row >= n or next_col >= n or  # Out of bounds
            matrix[next_row][next_col] != 0  # Already filled
        ):
            direction = (direction + 1) % 4  # Change direction
            next_row = row_loc + row_offsets[direction]
            next_col = col_loc + column_offsets[direction]

        # Move to next position
        row_loc, col_loc = next_row, next_col

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Example usage
n = 3
matrix = generate_spiral_matrix(n)
print_matrix(matrix)