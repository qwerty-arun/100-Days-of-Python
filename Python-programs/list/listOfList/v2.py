def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Create an empty matrix with dimensions cols x rows
    transposed = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed

# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose it
result = transpose(matrix)

# Display results
print("Original:")
for row in matrix:
    print(row)

print("\nTransposed:")
for row in result:
    print(row)

