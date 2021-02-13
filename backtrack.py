import random
from datetime import datetime


def is_safe(x, y, board, size):
    return 0 <= x < size and 0 <= y < size and board[x][y] == -1


def print_solution(n, board):
    for i in range(n):
        line_str = ""

        for j in range(n):
            c = str(board[i][j])
            line_str += c

            for k in range(4 - len(c)):
                line_str += " "

        print(line_str)


def solve_kt(size):
    """
        This function solves the Knight Tour problem using
        Backtracking. This function mainly uses solveKTUtil()
        to solve the problem. It returns false if no complete
        tour is possible, otherwise return true and prints the
        tour.
        Please note that there may be more than one solutions,
        this function prints one of the feasible solutions.
    """

    # Initialization of Board matrix
    board = [[-1 for _ in range(size)] for _ in range(size)]

    # move_x and move_y define next move of Knight.
    # move_x is for next value of x coordinate
    # move_y is for next value of y coordinate
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # start the Knight from a random position
    kx = random.randint(0, size - 1)
    ky = random.randint(0, size - 1)

    # Since the Knight is initially at the first block
    board[kx][ky] = 0

    # Step counter for knight's position
    pos = board[kx][ky] + 1

    # Checking if solution exists or not
    if not solve_kt_util(size, board, kx, ky, move_x, move_y, pos):
        print("Solution does not exist")
    else:
        print_solution(size, board)


def solve_kt_util(size, board, curr_x, curr_y, move_x, move_y, pos):
    """
        A recursive utility function to solve Knight Tour
        problem
    """

    """print("Iteration #" + str(len(m)))
    m.append(1)"""

    if pos == size**2:
        return True

    # Try all next moves from the current coordinate x, y
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]

        if is_safe(new_x, new_y, board, size):
            board[new_x][new_y] = pos
            if solve_kt_util(size, board, new_x, new_y, move_x, move_y, pos + 1):
                return True

            # undo move and try another route
            board[new_x][new_y] = -1
    return False


def print_time(msg):
    t = datetime.now().time()
    print(msg + str(t))


if __name__ == "__main__":
    while True:
        try:
            size = int(input(">> Pick the size of the board: "))
            print_time("Before:")
            solve_kt(size)
            print_time("After:")
            break
        except ValueError as e:
            print(e)
