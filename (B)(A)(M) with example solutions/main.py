def possible(x_cord, y_cord, number, grid_):
    # checks for same number in row and column
    for i in range(9):
        if grid_[x_cord][i] == number:
            return False
        if grid_[i][y_cord] == number:
            return False

    x0, y0 = x_cord // 3 * 3, y_cord // 3 * 3
    # checks for same number in square
    for i in range(x0, x0 + 3):
        for j in range(y0, y0 + 3):
            if grid_[i][j] == number:
                return False
    return True


def solve(sudoku_grid):
    for x in range(9):
        for y in range(9):
            if sudoku_grid[x][y] == 0:
                for z in range(1, 10):
                    if possible(x, y, z, sudoku_grid):
                        sudoku_grid[x][y] = z
                        if solve(sudoku_grid):
                            return True
                        sudoku_grid[x][y] = 0
                return False
    print("solved " + str(N + 1))
    return True


def write_solved_to_file(grid_to_write, output_filename):
    line_to_write = ''
    for line in range(9):
        line_to_write += ' '.join(str(number) for number in grid_to_write[line]) + '\n'
    answer_file = open(output_filename, 'a')
    answer_file.write(line_to_write + '\n')
    answer_file.close()
    return


def print_in_terminal(grid_to_print):
    for line in range(9):
        print(" ".join(str(number) for number in grid_to_print[line]))
    print()
    return


def get_input_output_file_names():
    input_name = input('Input file name (default = "tests.txt"):\n')
    if not input_name:
        input_name = "tests.txt"

    output_name = input('Output file name (default = "solutions.txt"):\n')
    if not output_name:
        output_name = "solutions.txt"

    # clear file
    reset = open(output_name, "w")
    reset.close()

    return input_name, output_name


def count_puzzles_from_input_file(lines_to_count):
    count_lines = 0
    for line in open(lines_to_count).readlines():
        count_lines += 1
    return (count_lines+1)//10


input_file_name, output_file_name = get_input_output_file_names()
puzzle_number = count_puzzles_from_input_file(input_file_name)
input_file = open(input_file_name, "r")

for N in range(puzzle_number):

    grid = []

    for y in range(9):
        one_line = [int(m) for m in input_file.readline().split()]
        grid.append(one_line)
    input_file.readline()

    solve(grid)
    write_solved_to_file(grid, output_file_name)
    print_in_terminal(grid)

input_file.close()
