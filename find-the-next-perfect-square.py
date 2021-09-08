import math


def find_next_square(sq):
    square = str(math.sqrt(sq)).split('.')
    if square[1] != "0":
        return -1
    square = int(square[0]) + 1
    return square * square
