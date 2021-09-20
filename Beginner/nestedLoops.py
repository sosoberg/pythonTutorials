# 2D lists

numerGrid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# print out the one - reference the row and then the column
print("Select One: " + numerGrid[0][0])

# nested loop to get all of the elements in the 2D list
for row in numerGrid:
    # print the grid

    print(row)
    for col in row:
        # print each element in the grid
        print(col)