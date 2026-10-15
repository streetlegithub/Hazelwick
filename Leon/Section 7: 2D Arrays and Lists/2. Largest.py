# hardcoded grid, initialise variable
grid = [[3, 8, 1], [4, 0, 7], [6, 2, 9]]
greatest = 0
# find the greatest
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] > greatest:
            greatest = grid[row][col]
# print it all at once
print(f"Largest value {grid[row][col]} at row {row}, column {col}")