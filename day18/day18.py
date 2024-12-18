"""
--- Day 18: RAM Run ---
You and The Historians look a lot more pixelated than you remember. You're inside a computer at the North Pole!

Just as you're about to check out your surroundings, a program runs up to you. "This region of memory isn't safe! The User misunderstood what a pushdown automaton is and their algorithm is pushing whole bytes down on top of us! Run!"

The algorithm is fast - it's going to cause a byte to fall into your memory space once every nanosecond! Fortunately, you're faster, and by quickly scanning the algorithm, you create a list of which bytes will fall (your puzzle input) in the order they'll land in your memory space.

Your memory space is a two-dimensional grid with coordinates that range from 0 to 70 both horizontally and vertically. However, for the sake of example, suppose you're on a smaller grid with coordinates that range from 0 to 6 and the following list of incoming byte positions:

5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
Each byte position is given as an X,Y coordinate, where X is the distance from the left edge of your memory space and Y is the distance from the top edge of your memory space.

You and The Historians are currently in the top left corner of the memory space (at 0,0) and need to reach the exit in the bottom right corner (at 70,70 in your memory space, but at 6,6 in this example). You'll need to simulate the falling bytes to plan out where it will be safe to run; for now, simulate just the first few bytes falling into your memory space.

As bytes fall into your memory space, they make that coordinate corrupted. Corrupted memory coordinates cannot be entered by you or The Historians, so you'll need to plan your route carefully. You also cannot leave the boundaries of the memory space; your only hope is to reach the exit.

In the above example, if you were to draw the memory space after the first 12 bytes have fallen (using . for safe and # for corrupted), it would look like this:

...#...
..#..#.
....#..
...#..#
..#..#.
.#..#..
#.#....
You can take steps up, down, left, or right. After just 12 bytes have corrupted locations in your memory space, the shortest path from the top left corner to the exit would take 22 steps. Here (marked with O) is one such path:

OO.#OOO
.O#OO#O
.OOO#OO
...#OO#
..#OO#.
.#.O#..
#.#OOOO
Simulate the first kilobyte (1024 bytes) falling onto your memory space. Afterward, what is the minimum number of steps needed to reach the exit?
"""


def part1():
    with open("input.txt") as f:
        grid_size = 71
        kbs = 1024
        grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]
        lines = f.read().strip()
        coordinates = [list(map(int, line.split(","))) for line in lines.split("\n")]
        for col, row in coordinates[:kbs]:
            grid[row][col] = "#"

        visited = set()
        route = [(0, 0, 0)]
        while len(route) > 0:
            r, c, step = route.pop()
            if r == grid_size - 1 and c == grid_size - 1:
                print(step)
                return
            if (r, c) in visited:
                continue
            visited.add((r, c))
            # print(r, c)
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_row, next_col = r + dr, c + dc
                if (
                    0 <= next_row < grid_size
                    and 0 <= next_col < grid_size
                    and grid[next_row][next_col] == "."
                ):
                    route = [(next_row, next_col, step + 1)] + route


"""
--- Part Two ---
The Historians aren't as used to moving around in this pixelated universe as you are. You're afraid they're not going to be fast enough to make it to the exit before the path is completely blocked.

To determine how fast everyone needs to go, you need to determine the first byte that will cut off the path to the exit.

In the above example, after the byte at 1,1 falls, there is still a path to the exit:

O..#OOO
O##OO#O
O#OO#OO
OOO#OO#
###OO##
.##O###
#.#OOOO
However, after adding the very next byte (at 6,1), there is no longer a path to the exit:

...#...
.##..##
.#..#..
...#..#
###..##
.##.###
#.#....
So, in this example, the coordinates of the first byte that prevents the exit from being reachable are 6,1.

Simulate more of the bytes that are about to corrupt your memory space. What are the coordinates of the first byte that will prevent the exit from being reachable from your starting position? (Provide the answer as two integers separated by a comma with no other characters.)
"""


def part2(): # brute force
    with open("input.txt") as f:
        grid_size = 71
        grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]
        lines = f.read().strip()

        for i, line in enumerate(lines.split("\n")):
            x, y = [int(p) for p in line.strip().split(",")]
            grid[y][x] = "#"

            can_exit = False
            visited = set()
            route = [(0, 0)]
            while len(route) > 0:
                r, c = route.pop()
                if r == grid_size - 1 and c == grid_size - 1:
                    can_exit = True
                    break
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    next_row, next_col = r + dr, c + dc
                    if (
                        0 <= next_row < grid_size
                        and 0 <= next_col < grid_size
                        and grid[next_row][next_col] == "."
                    ):
                        route = [(next_row, next_col)] + route
            if not can_exit:
                print(f'{x},{y}')
                break


def part2_bs():
    with open("input.txt") as f:
        grid_size = 71
        lines = f.read().strip()
        coordinates = [list(map(int, line.split(","))) for line in lines.split("\n")]

        def can_exit_at(index):
            # print(coordinates[:index])
            grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]
            for x, y in coordinates[:index]:
                grid[y][x] = "#"

            can_exit = False
            visited = set()
            route = [(0, 0)]
            while len(route) > 0:
                r, c = route.pop()
                if r == grid_size - 1 and c == grid_size - 1:
                    can_exit = True
                    break
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    next_row, next_col = r + dr, c + dc
                    if (
                        0 <= next_row < grid_size
                        and 0 <= next_col < grid_size
                        and grid[next_row][next_col] == "."
                    ):
                        route = [(next_row, next_col)] + route
            return can_exit

    # binary search for the first index that can't exit
    lowest_index = 0
    highest_index = len(coordinates) - 1

    while lowest_index < highest_index:
        mid = (lowest_index + highest_index) // 2
        if can_exit_at(mid + 1):
            lowest_index = mid + 1
        else:
            highest_index = mid

    print(",".join(map(str,coordinates[lowest_index])))


if __name__ == "__main__":
    part1() # 330
    part2()  # 10,38
    part2_bs()  # 10,38
