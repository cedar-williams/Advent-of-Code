# --- Day 6: Trash Compactor ---

def colMath(col_num: int, math_grid) -> int:
    """
    Calculate the result of the cephalopod math on the specified column
    :param col_num: which column to do the math on
    :param math_grid: the math grid
    :return: result of the math function (* or +)
    """
    grid_size = len(math_grid)
    sign = math_grid[grid_size - 1][col_num]

    print(f'calc with sign {sign}')

    if sign == '*':
        calculated_value = 1
        for row_num in range(0, grid_size - 1):
            print(math_grid[row_num][col_num])
            calculated_value *= int(math_grid[row_num][col_num])
    else:
        calculated_value = 0
        for row_num in range(0, grid_size - 1):
            print(math_grid[row_num][col_num])
            calculated_value += int(math_grid[row_num][col_num])

    print(f'Calc value: {calculated_value}\n')
    return calculated_value


# Import the cephalopod math homework
with open("input.txt") as file:
    input_grid = [line.split() for line in file]

print(input_grid)

sum = 0
# For each column, split into its own obj
for column in range(len(input_grid[0])):
    sum += colMath(column, input_grid)

print(f'Total sum: {sum}')