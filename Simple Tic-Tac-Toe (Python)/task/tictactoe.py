# a valid solution for hyperskill project
# tictactoe - 10-07-2023

def add_space_every_2nd_pos(str_line)->str:
    line_with_space = ''  # init line with space
    for character in str_line:
        line_with_space = line_with_space + character + ' '
    return line_with_space


def print_grid(str_grid: str):

    str_line1: str = "|" + str_grid[0:3] + "|"
    str_line2: str = "|" + str_grid[3:6] + "|"
    str_line3: str = "|" + str_grid[6:9] + "|"

    print("---------")
    print(add_space_every_2nd_pos(str_line1))
    print(add_space_every_2nd_pos(str_line2))
    print(add_space_every_2nd_pos(str_line3))
    print("---------")


def check_winner(grid,token) -> bool:
    match = False
    str_pattern = token+token+token
    # check rows:
    match = match or (grid[:3] == str_pattern)   # row 1
    match = match or (grid[3:6] == str_pattern)  # row 2
    match = match or (grid[6:9] == str_pattern)  # row 3

    match = match or (grid[0::3] == str_pattern)  # column 1
    match = match or (grid[1::3] == str_pattern)  # column 2
    match = match or (grid[2::3] == str_pattern)  # column 3

    match = match or (grid[::4] == str_pattern)  # diagonal top left to right
    match = match or (grid[2:7:2] == str_pattern)  # diagonal top right to left
    return match


def reset_grid() -> str:
    matrix: str = "_________"
    return matrix


if __name__ == "__main__":
    # grid = reset_grid()  # init grid
    # print_grid(grid)
    TOKEN_X:str = "X"
    TOKEN_O: str = "O"
    TOKEN_SPACE: str = "_"

    grid_coordinates_row: int = -1  # init value
    grid_coordinates_column: int = -1 # init value

    grid = reset_grid()
    print_grid(grid)

    str_coordinates = ''

    valid_coords = False
    while True:
        num_x = grid.count(TOKEN_X)
        num_o = grid.count(TOKEN_O)
        num__ = grid.count(TOKEN_SPACE)
        # print(f'{num_x},{num_o}')

        if (abs(num_x - num_o) > 1) \
                or \
                ((check_winner(grid, TOKEN_X)
                  and check_winner(grid, TOKEN_O))):
            print('Impossible')
        elif check_winner(grid, TOKEN_X):
            print(TOKEN_X + ' wins')
            break
        elif check_winner(grid, TOKEN_O):
            print(TOKEN_O + ' wins')
            break
        elif num__ == 0:
            print('Draw')
            break
        elif num__ > 0:
            while not valid_coords:
                str_coordinates: str = input()
                try:
                    grid_coordinates_row, grid_coordinates_column = str_coordinates.split(" ")
                    if (int(grid_coordinates_row) <= 3) \
                            and (int(grid_coordinates_row) > 0) \
                            and (int(grid_coordinates_column) <= 3) \
                            and (int(grid_coordinates_column) > 0):
                        valid_coords = True
                    else:
                        print("Coordinates should be from 1 to 3!")
                except Exception as e:
                    print("You should only enter numbers!")

                if valid_coords:
                    new_pos: int = (int(grid_coordinates_row) - 1) * 3 + int(grid_coordinates_column) - 1
                    if grid[new_pos] == TOKEN_SPACE:
                        if num_o > num_x:
                            token = TOKEN_X
                        elif num_o == num_x:
                            token = TOKEN_X
                        else:
                            token = TOKEN_O
                        grid = grid[:new_pos] + token + grid[new_pos + 1:]  # replace string at position with token
                    else:
                        print("This cell is occupied! Choose another one!")
                        valid_coords = False
        print_grid(grid)
        valid_coords = False
