grid = [[3, 8, 1], [4, 0, 7], [6, 2, 9]]
greatest = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] > greatest:
            greatest = grid[row][col]
print(f"Largest value is {grid[row][col]} at row {row} column {col}")