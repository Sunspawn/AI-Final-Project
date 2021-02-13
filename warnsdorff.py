# Knight's Tour using Warnsdorff's Rule
# http://en.wikipedia.org/wiki/Knight's_tour
from heapq import heappush, heappop     # for priority queue
import random
from backtrack import print_solution
from datetime import datetime


def warnsdorff(size):
    board = [[0 for _ in range(size)] for _ in range(size)]  # chessboard
    # directions the Knight can move on the chessboard
    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    # start the Knight from a random position
    kx = random.randint(0, size - 1)
    ky = random.randint(0, size - 1)

    # force the starting position to be even in case of an odd-sized board.
    if size % 2:
        kx = (kx + kx % 2) % size
        ky = (ky + ky % 2) % size

    for k in range(size * size):
        board[ky][kx] = k + 1
        pq = []  # priority queue of available neighbors

        for i in range(8):
            nx = kx + dx[i]
            ny = ky + dy[i]

            if 0 <= nx < size and 0 <= ny < size:
                if board[ny][nx] == 0:  # count the available neighbors of the neighbor
                    ctr = 0
                    for j in range(8):
                        ex = nx + dx[j]
                        ey = ny + dy[j]

                        if 0 <= ex < size and 0 <= ey < size:
                            if board[ey][ex] == 0:
                                ctr += 1
                    heappush(pq, (ctr, i))
        # move to the neighbor that has min number of available neighbors
        if len(pq) > 0:
            (p, m) = heappop(pq)
            kx += dx[m]
            ky += dy[m]
        else:
            break
    return board


def print_time(msg):
    t = datetime.now().time()
    print(msg + str(t))


if __name__ == "__main__":
    while True:
        try:
            n = int(input(">> Pick the size of the board: "))
            print_time("Before:")
            solution = warnsdorff(n)
            print_solution(n, solution)
            print_time("After:")
            break
        except ValueError as e:
            print(e)
