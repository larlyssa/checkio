"""

DIFFICULTY: ELEMENTARY

In cellular automata, the Moore neighborhood comprises the eight cells surrounding a central cell on a two-dimensional square lattice. The neighborhood is named after Edward F. Moore, a pioneer of cellular automata theory. Many board games are played with a rectangular grid with squares as cells. For some games, it is important to know about the conditions of neighbouring cells for chip (figure, draught etc) placement and strategy.
You are given a state for a rectangular board game grid with chips in a binary matrix, where 1 is a cell with a chip and 0 is an empty cell. You are also given the coordinates for a cell in the form of row and column numbers (starting from 0). You should determine how many chips are close to this cell. Every cell interacts with its eight neighbours; those cells that are horizontally, vertically, or diagonally adjacent.
example
For the given examples (see the schema) there is the same grid:
((1, 0, 0, 1, 0),
 (0, 1, 0, 0, 0),
 (0, 0, 1, 0, 1),
 (1, 0, 0, 0, 0),
 (0, 0, 1, 0, 0),)

For the first example coordinates of the cell is (1, 2) and as we can see from the schema this cell has 3 neighbour chips. For the second example coordinates is (0, 0) and this cell contains a chip, but we count only neighbours and the answer is 1.
Input: Three arguments. A grid as a tuple of tuples with integers (1/0), a row number and column number for a cell as integers.
Output: How many neighbouring cells have chips as an integer.

Precondition:
3 ≤ len(grid) ≤ 10
all(len(grid[0]) == len(row) for row in grid)
"""

def count_neighbours(grid, row, col):
    count = 0
    cell = [row, col]
    row_len = len(grid)
    col_len = len(grid[0])
    
    
    #north [row - 1, col]
    if ((row - 1) >= 0 and (row - 1) < row_len) and (col >= 0 and col < col_len):
        if grid[row-1][col] == 1:
            count += 1
        
    #south [row + 1, col]
    if ((row + 1) >= 0 and (row + 1) < row_len) and (col >= 0 and col < col_len):
        if grid[row+1][col] == 1:
            count += 1
        
    #east = [row, col + 1]
    if ((row) >= 0 and (row) < row_len) and ((col+1) >= 0 and (col+1) < col_len):
        if grid[row][col+1] == 1:
            count += 1
        
    #west = [row, col - 1]
    if ((row) >= 0 and (row) < row_len) and ((col-1) >= 0 and (col-1) < col_len):
        if grid[row][col-1] == 1:
            count += 1
    
    #northwest = [row - 1, col - 1]
    if ((row - 1) >= 0 and (row - 1) < row_len) and ((col-1) >= 0 and (col-1) < col_len):
        if grid[row-1][col-1] == 1:
            count += 1
        
    #northeast = [row - 1, col + 1]
    if ((row - 1) >= 0 and (row - 1) < row_len) and ((col+1) >= 0 and (col+1) < col_len):
        if grid[row-1][col+1] == 1:
            count += 1
        
    #southwest = [row + 1, col - 1]
    if ((row + 1) >= 0 and (row + 1) < row_len) and ((col-1) >= 0 and (col-1) < col_len):
        if grid[row+1][col-1] == 1:
            count += 1
    
    #southeast = [row + 1, col + 1]
    if ((row + 1) >= 0 and (row + 1) < row_len) and ((col+1) >= 0 and (col+1) < col_len):
        if grid[row+1][col+1] == 1:
            count += 1
    
    return count
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
