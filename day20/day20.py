"""
--- Day 20: Race Condition ---
The Historians are quite pixelated again. This time, a massive, black building looms over you - you're right outside the CPU!

While The Historians get to work, a nearby program sees that you're idle and challenges you to a race. Apparently, you've arrived just in time for the frequently-held race condition festival!

The race takes place on a particularly long and twisting code path; programs compete to see who can finish in the fewest picoseconds. The winner even gets their very own mutex!

They hand you a map of the racetrack (your puzzle input). For example:

###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
The map consists of track (.) - including the start (S) and end (E) positions (both of which also count as track) - and walls (#).

When a program runs through the racetrack, it starts at the start position. Then, it is allowed to move up, down, left, or right; each such move takes 1 picosecond. The goal is to reach the end position as quickly as possible. In this example racetrack, the fastest time is 84 picoseconds.

Because there is only a single path from the start to the end and the programs all go the same speed, the races used to be pretty boring. To make things more interesting, they introduced a new rule to the races: programs are allowed to cheat.

The rules for cheating are very strict. Exactly once during a race, a program may disable collision for up to 2 picoseconds. This allows the program to pass through walls as if they were regular track. At the end of the cheat, the program must be back on normal track again; otherwise, it will receive a segmentation fault and get disqualified.

So, a program could complete the course in 72 picoseconds (saving 12 picoseconds) by cheating for the two moves marked 1 and 2:

###############
#...#...12....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
Or, a program could complete the course in 64 picoseconds (saving 20 picoseconds) by cheating for the two moves marked 1 and 2:

###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...12..#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
This cheat saves 38 picoseconds:

###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.####1##.###
#...###.2.#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
This cheat saves 64 picoseconds and takes the program directly to the end:

###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..21...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
Each cheat has a distinct start position (the position where the cheat is activated, just before the first move that is allowed to go through walls) and end position; cheats are uniquely identified by their start position and end position.

In this example, the total number of cheats (grouped by the amount of time they save) are as follows:

There are 14 cheats that save 2 picoseconds.
There are 14 cheats that save 4 picoseconds.
There are 2 cheats that save 6 picoseconds.
There are 4 cheats that save 8 picoseconds.
There are 2 cheats that save 10 picoseconds.
There are 3 cheats that save 12 picoseconds.
There is one cheat that saves 20 picoseconds.
There is one cheat that saves 36 picoseconds.
There is one cheat that saves 38 picoseconds.
There is one cheat that saves 40 picoseconds.
There is one cheat that saves 64 picoseconds.
You aren't sure what the conditions of the racetrack will be like, so to give yourself as many options as possible, you'll need a list of the best cheats. How many cheats would save you at least 100 picoseconds?
"""

def part1():
    with open('input.txt') as f:
        lines = f.read().strip().split('\n')
        lines = [line.strip() for line in lines]
        grid = [list(line) for line in lines]

        row_size = len(grid)
        col_size = len(grid[0])

        for row in range(row_size):
            for col in range(col_size):
                if grid[row][col] == 'S':
                    cur_r, cur_c = row, col


        blueprint = [list(['#'] * col_size) for _ in range(row_size)]
        # print(blueprint)
        blueprint[cur_r][cur_c] = 0

        # for row in blueprint:
        #     print(*row, sep='')


        while grid[cur_r][cur_c] != 'E':
            for next_r, next_c in [(cur_r + 1, cur_c), (cur_r - 1, cur_c), (cur_r, cur_c + 1), (cur_r, cur_c - 1)]:
                if next_r < 0 or next_r >= row_size or next_c < 0 or next_c >= col_size or grid[next_r][next_c] == '#':
                    continue
                if blueprint[next_r][next_c] != '#':
                    continue
                blueprint[next_r][next_c] = blueprint[cur_r][cur_c] + 1
                cur_r, cur_c = next_r, next_c

        # for row in grid:
        #     print(''.join(map(str, row)))

        # for row in blueprint:
        #     print(*row, sep='\t')

        count = 0
        for row in range(row_size):
            for col in range(col_size):
                if grid[row][col] == '#':
                    continue
                for next_r, next_c in [(row + 2, col), (row - 2, col), (row + 1, col + 1), (row - 1, col - 1), (row, col + 2), (row, col - 2), (row - 1, col + 1), (row + 1, col -1)]:
                    if 0 <= next_r < row_size and 0 <= next_c < col_size and grid[next_r][next_c] != '#' and blueprint[row][col] - blueprint[next_r][next_c] >= 102:
                        # print(f'{(next_r,next_c)},{(row,col)},{blueprint[row][col] - blueprint[next_r][next_c]} ')
                        count += 1

        print(count)


"""
--- Part Two ---
The programs seem perplexed by your list of cheats. Apparently, the two-picosecond cheating rule was deprecated several milliseconds ago! The latest version of the cheating rule permits a single cheat that instead lasts at most 20 picoseconds.

Now, in addition to all the cheats that were possible in just two picoseconds, many more cheats are possible. This six-picosecond cheat saves 76 picoseconds:

###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#1#####.#.#.###
#2#####.#.#...#
#3#####.#.###.#
#456.E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
Because this cheat has the same start and end positions as the one above, it's the same cheat, even though the path taken during the cheat is different:

###############
#...#...#.....#
#.#.#.#.#.###.#
#S12..#.#.#...#
###3###.#.#.###
###4###.#.#...#
###5###.#.###.#
###6.E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
Cheats don't need to use all 20 picoseconds; cheats can last any amount of time up to and including 20 picoseconds (but can still only end when the program is on normal track). Any cheat time not used is lost; it can't be saved for another cheat later.

You'll still need a list of the best cheats, but now there are even more to choose between. Here are the quantities of cheats in this example that save 50 picoseconds or more:

There are 32 cheats that save 50 picoseconds.
There are 31 cheats that save 52 picoseconds.
There are 29 cheats that save 54 picoseconds.
There are 39 cheats that save 56 picoseconds.
There are 25 cheats that save 58 picoseconds.
There are 23 cheats that save 60 picoseconds.
There are 20 cheats that save 62 picoseconds.
There are 19 cheats that save 64 picoseconds.
There are 12 cheats that save 66 picoseconds.
There are 14 cheats that save 68 picoseconds.
There are 12 cheats that save 70 picoseconds.
There are 22 cheats that save 72 picoseconds.
There are 4 cheats that save 74 picoseconds.
There are 3 cheats that save 76 picoseconds.
Find the best cheats using the updated cheating rules. How many cheats would save you at least 100 picoseconds?
"""

def part2():
    with open('input.txt') as f:
        lines = f.read().strip().split('\n')
        lines = [line.strip() for line in lines]
        grid = [list(line) for line in lines]

        row_size = len(grid)
        col_size = len(grid[0])

        for row in range(row_size):
            for col in range(col_size):
                if grid[row][col] == 'S':
                    cur_r, cur_c = row, col


        blueprint = [list(['#'] * col_size) for _ in range(row_size)]
        # print(blueprint)
        blueprint[cur_r][cur_c] = 0

        # for row in blueprint:
        #     print(*row, sep='')


        while grid[cur_r][cur_c] != 'E':
            for next_r, next_c in [(cur_r + 1, cur_c), (cur_r - 1, cur_c), (cur_r, cur_c + 1), (cur_r, cur_c - 1)]:
                if next_r < 0 or next_r >= row_size or next_c < 0 or next_c >= col_size or grid[next_r][next_c] == '#':
                    continue
                if blueprint[next_r][next_c] != '#':
                    continue
                blueprint[next_r][next_c] = blueprint[cur_r][cur_c] + 1
                cur_r, cur_c = next_r, next_c

        # for row in grid:
        #     print(''.join(map(str, row)))

        # for row in blueprint:
        #     print(*row, sep='\t')

        count = 0
        for row in range(row_size):
            for col in range(col_size):
                if grid[row][col] == '#':
                    continue
                for cheat_time in range(2, 21):
                    for dr in range(cheat_time + 1):
                        dc = cheat_time - dr
                        for next_r, next_c in {(row + dr, col + dc), (row - dr, col - dc), (row + dr, col - dc), (row - dr, col + dc)}: # set because of vertical and horizontal symmetry
                            if 0 <= next_r < row_size and 0 <= next_c < col_size and grid[next_r][next_c] != '#' and blueprint[row][col] - blueprint[next_r][next_c] >= 100 + cheat_time:
                                # print(f'{(next_r,next_c)},{(row,col)},{blueprint[row][col] - blueprint[next_r][next_c]} ')
                                count += 1

        print(count)

if __name__ == "__main__":
    part1() # 1411
    part2() # 1411