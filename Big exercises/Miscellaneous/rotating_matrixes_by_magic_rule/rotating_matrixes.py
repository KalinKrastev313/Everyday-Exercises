if __name__ == '__main__':
    n = int(input().strip())

    puzzle = []

    for _ in range(n):
        puzzle.append(list(map(int, input().rstrip().split())))

    # Write your code here


def count_good_pairs():
    count = 0
    # Checks rows
    for row in puzzle:
        for index in range(len(row) - 1):
            for second_index in range(index + 1, len(row)):
                if row[index] < row[second_index]:
                    count += 1
    # Checks columns
    for col_index in range(len(puzzle)):
        for row_index in range(len(puzzle) - 1):
            for row_second_index in range(row_index + 1, len(puzzle)):
                if puzzle[row_index][col_index] < puzzle[row_second_index][col_index]:
                    count += 1

    return count


def rotate_a_square(square_r, square_c, square_side):
    # create the rotated square
    new_rows = []
    for col in range(square_c, square_c + square_side):
        new_row = []
        for row in range(square_r + square_side - 1, square_r - 1, -1):
            new_row.append(puzzle[row][col])
        new_rows.append(new_row)

    for row in range(square_r, square_r + square_side):
        for n in range(square_side):
            for i in range(square_side):
                puzzle[row][square_c + n - 1] = new_rows[i][n]


print(puzzle)
square_r, square_c, square_side = list(map(int, input().split()))
rotate_a_square(square_r, square_c, square_side)
print(puzzle)

