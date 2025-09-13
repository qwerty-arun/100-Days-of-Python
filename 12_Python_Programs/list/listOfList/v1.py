def transpose(matrix):
    # Use zip to unpack and regroup the rows into columns
    return [list(row) for row in zip(*matrix)]

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = transpose(matrix)

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in result:
    print(row)

