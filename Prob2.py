##################################################
# Name:Jack
# Collaborators:Chatgpt
# Estimate of time spent (hr):1
##################################################
def is_magic_square(square: list[list[int]]) -> bool:
    n = len(square)
    
    # Check if square
    for row in square:
        if len(row) != n:
            return False

    # Target sum from first row
    target_sum = sum(square[0])

    # Check rows
    for row in square:
        if sum(row) != target_sum:
            return False

    # Check columns
    for col in range(n):
        if sum(square[row][col] for row in range(n)) != target_sum:
            return False

    # Check diagonals
    if sum(square[i][i] for i in range(n)) != target_sum:
        return False
    if sum(square[i][n - 1 - i] for i in range(n)) != target_sum:
        return False

    # Ensure values are unique and within expected range
    unique_values = {num for row in square for num in row}
    if unique_values != set(range(1, n * n + 1)):
        return False

    return True

# Test cases
test_square_1 = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]

test_square_2 = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

non_magic_square = [
    [5, 5, 5],
    [5, 5, 5],
    [5, 5, 5]
]

print("Testing test_square_1 (should return True):")
result_1 = is_magic_square(test_square_1)
print("Result:", result_1)

print("\nTesting test_square_2 (should return True):")
result_2 = is_magic_square(test_square_2)
print("Result:", result_2)

print("\nTesting non_magic_square (should return False):")
result_3 = is_magic_square(non_magic_square)
print("Result:", result_3)

