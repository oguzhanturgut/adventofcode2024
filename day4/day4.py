# --- Day 4: Ceres Search ---
# "Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!
#
# As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.
#
# This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:
#
#
# ..X...
# .SAMX.
# .A..A.
# XMAS.S
# .X....
# The actual word search will be full of letters instead. For example:
#
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:
#
# ....XXMAS.
# .SAMXMS...
# ...S..A...
# ..A.A.MS.X
# XMASAMX.MM
# X.....XA.A
# S.S.S.S.SS
# .A.A.A.A.A
# ..M.M.M.MM
# .X.X.XMASX
# Take a look at the little Elf's word search. How many times does XMAS appear?


def get_matrix(file):
    file = file.read()
    lines = file.split('\n')
    matrix = []
    for line in lines:
        matrix.append(list(line))
    return matrix

def part1():
    with open('input.txt') as file:
        matrix = get_matrix(file)
        count = 0
        row_len = len(matrix)
        col_len = len(matrix[0])
        for row in range(row_len):
            for col in range(col_len):
                if row + 3 < col_len and matrix[col][row] == 'X' and matrix[col][row+1] == 'M' and matrix[col][row+2] == 'A' and matrix[col][row+3] == 'S': # horizontal
                    count += 1
                if row + 3 < col_len and matrix[col][row] == 'S' and matrix[col][row+1] == 'A' and matrix[col][row+2] == 'M' and matrix[col][row+3] == 'X': # horizontal reverse
                    count += 1
                if col + 3 < len(matrix[0]) and matrix[col][row] == 'X' and matrix[col+1][row] == 'M' and matrix[col+2][row] == 'A' and matrix[col+3][row] == 'S': # vertical
                    count += 1
                if col + 3 < col_len and matrix[col][row] == 'S' and matrix[col+1][row] == 'A' and matrix[col+2][row] == 'M' and matrix[col+3][row] == 'X': # vertical reverse
                    count += 1
                if col + 3 < row_len and row + 3 < col_len and matrix[col][row] == 'X' and matrix[col+1][row+1] == 'M' and matrix[col+2][row+2] == 'A' and matrix[col+3][row+3] == 'S': # diagonal ↘
                    count += 1
                if col + 3 < row_len and row + 3 < col_len and matrix[col][row] == 'S' and matrix[col+1][row+1] == 'A' and matrix[col+2][row+2] == 'M' and matrix[col+3][row+3] == 'X': # diagonal reverse ↖
                    count += 1
                if row + 3 < col_len and col - 3 >= 0 and matrix[col][row] == 'X' and matrix[col-1][row+1] == 'M' and matrix[col-2][row+2] == 'A' and matrix[col-3][row+3] == 'S': # diagonal ↗
                    count += 1
                if row + 3 < col_len and col - 3 >= 0 and matrix[col][row] == 'S' and matrix[col-1][row+1] == 'A' and matrix[col-2][row+2] == 'M' and matrix[col-3][row+3] == 'X': # diagonal reverse ↙
                    count += 1

        print(count)
        return count


# --- Part Two ---
# The Elf looks quizzically at you. Did you misunderstand the assignment?
#
# Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:
#
# M.S
# .A.
# M.S
# Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.
#
# Here's the same example from before, but this time all of the X-MASes have been kept instead:
#
# .M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# ..........
# In this example, an X-MAS appears 9 times.
#
# Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?


def part2():
    with open('input.txt') as file:
        matrix = get_matrix(file)
        count = 0
        row_len = len(matrix)
        col_len = len(matrix[0])
        # M.S
        # .A.
        # M.S

        # S.M
        # .A.
        # S.M

        # S.S
        # .A.
        # M.M

        # M.M
        # .A.
        # S.S
        for x in range(row_len - 2): # don't need to check the last two rows
            for y in range(col_len - 2): # don't need to check the last two columns
                if x < row_len and y < col_len and matrix[x][y] == 'M' and matrix[x+1][y+1] == 'A' and matrix[x+2][y+2] == 'S' and matrix[x][y+2] == 'M' and matrix[x+2][y] == 'S':
                    count += 1
                if x < row_len and y < col_len and matrix[x][y] == 'M' and matrix[x+1][y+1] == 'A' and matrix[x+2][y+2] == 'S' and matrix[x][y+2] == 'S' and matrix[x+2][y] == 'M':
                    count += 1
                if x < row_len and y < col_len and matrix[x][y] == 'S' and matrix[x+1][y+1] == 'A' and matrix[x+2][y+2] == 'M' and matrix[x][y+2] == 'M' and matrix[x+2][y] == 'S':
                    count += 1
                if x < row_len and y < col_len and matrix[x][y] == 'S' and matrix[x+1][y+1] == 'A' and matrix[x+2][y+2] == 'M' and matrix[x][y+2] == 'S' and matrix[x+2][y] == 'M':
                    count += 1
        print(count)
        return count


if __name__ == '__main__':
    assert part1() == 2545
    assert part2() == 1886