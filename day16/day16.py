"""
--- Day 16: Reindeer Maze ---
It's time again for the Reindeer Olympics! This year, the big event is the Reindeer Maze, where the Reindeer compete for the lowest score.

You and The Historians arrive to search for the Chief right as the event is about to start. It wouldn't hurt to watch a little, right?

The Reindeer start on the Start Tile (marked S) facing East and need to reach the End Tile (marked E). They can move forward one tile at a time (increasing their score by 1 point), but never into a wall (#). They can also rotate clockwise or counterclockwise 90 degrees at a time (increasing their score by 1000 points).

To figure out the best place to sit, you start by grabbing a map (your puzzle input) from a nearby kiosk. For example:

###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
There are many paths through this maze, but taking any of the best paths would incur a score of only 7036. This can be achieved by taking a total of 36 steps forward and turning 90 degrees a total of 7 times:


###############
#.......#....E#
#.#.###.#.###^#
#.....#.#...#^#
#.###.#####.#^#
#.#.#.......#^#
#.#.#####.###^#
#..>>>>>>>>v#^#
###^#.#####v#^#
#>>^#.....#v#^#
#^#.#.###.#v#^#
#^....#...#v#^#
#^###.#.#.#v#^#
#S..#.....#>>^#
###############
Here's a second example:

#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
In this maze, the best paths cost 11048 points; following one such path would look like this:

#################
#...#...#...#..E#
#.#.#.#.#.#.#.#^#
#.#.#.#...#...#^#
#.#.#.#.###.#.#^#
#>>v#.#.#.....#^#
#^#v#.#.#.#####^#
#^#v..#.#.#>>>>^#
#^#v#####.#^###.#
#^#v#..>>>>^#...#
#^#v###^#####.###
#^#v#>>^#.....#.#
#^#v#^#####.###.#
#^#v#^........#.#
#^#v#^#########.#
#S#>>^..........#
#################
Note that the path shown above includes one 90 degree turn as the very first move, rotating the Reindeer from facing East to facing North.

Analyze your map carefully. What is the lowest score a Reindeer could possibly get?
"""
import heapq
from collections import deque
from os import minor


def part1():
    with open('input.txt') as f:
        lines = f.readlines()
        field = [[char for char in line.strip() ] for line in lines]

        row_count = len(field)
        col_count = len(field[0])

        for row in range(row_count):
            for col in range(col_count):
                if field[row][col] == 'S':
                    start_row, start_col = row, col
                if field[row][col] == 'E':
                    end_row, end_col = row, col

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        queue = [(0, start_row, start_col, directions[1])]
        visited = set()

        while queue:
            cost, row, col, direction = heapq.heappop(queue)
            if (row, col) == (end_row, end_col):
                print(cost)
                break
            if (row, col, direction) in visited:
                continue
            visited.add((row, col, direction))
            dr, dc = direction
            next_row, next_col = row + dr, col + dc
            if 0 <= next_row < row_count and 0 <= next_col < col_count and field[next_row][next_col] != '#':
                heapq.heappush(queue, (cost + 1, next_row, next_col, direction))
            heapq.heappush(queue, (cost + 1000, row, col, (dc, -dr))) # turn clockwise
            heapq.heappush(queue, (cost + 1000, row, col, (-dc, dr))) # turn counter-clockwise








"""
--- Part Two ---
Now that you know what the best paths look like, you can figure out the best spot to sit.

Every non-wall tile (S, ., or E) is equipped with places to sit along the edges of the tile. While determining which of these tiles would be the best spot to sit depends on a whole bunch of factors (how comfortable the seats are, how far away the bathrooms are, whether there's a pillar blocking your view, etc.), the most important factor is whether the tile is on one of the best paths through the maze. If you sit somewhere else, you'd miss all the action!

So, you'll need to determine which tiles are part of any best path through the maze, including the S and E tiles.

In the first example, there are 45 tiles (marked O) that are part of at least one of the various best paths through the maze:

###############
#.......#....O#
#.#.###.#.###O#
#.....#.#...#O#
#.###.#####.#O#
#.#.#.......#O#
#.#.#####.###O#
#..OOOOOOOOO#O#
###O#O#####O#O#
#OOO#O....#O#O#
#O#O#O###.#O#O#
#OOOOO#...#O#O#
#O###.#.#.#O#O#
#O..#.....#OOO#
###############
In the second example, there are 64 tiles that are part of at least one of the best paths:

#################
#...#...#...#..O#
#.#.#.#.#.#.#.#O#
#.#.#.#...#...#O#
#.#.#.#.###.#.#O#
#OOO#.#.#.....#O#
#O#O#.#.#.#####O#
#O#O..#.#.#OOOOO#
#O#O#####.#O###O#
#O#O#..OOOOO#OOO#
#O#O###O#####O###
#O#O#OOO#..OOO#.#
#O#O#O#####O###.#
#O#O#OOOOOOO..#.#
#O#O#O#########.#
#O#OOO..........#
#################
Analyze your map further. How many tiles are part of at least one of the best paths through the maze?
"""

# def part2():
#     with open('input.txt') as f:
#         lines = f.readlines()
#         field = [[char for char in line.strip() ] for line in lines]
#         # print(field)
#
#         row_count = len(field)
#         col_count = len(field[0])
#
#         for row in range(row_count):
#             for col in range(col_count):
#                 if field[row][col] == 'S':
#                     start_row, start_col = row, col
#
#         directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#
#         # print(start_row, start_col)
#         # print(end_row, end_col)
#
#         visited = set()
#         queue = []
#         heapq.heappush(queue, (0, start_row, start_col, directions[1]))
#         while queue:
#             cost, row, col, direction = heapq.heappop(queue)
#             # print(cost, row, col, direction)
#             if field[row][col] == 'E':
#                 print(cost)
#                 break
#             if (row, col, direction) in visited:
#                 continue
#             visited.add((row, col, direction))
#             dr, dc = direction
#             next_row, next_col = row + dr, col + dc
#             if 0 <= next_row < row_count and 0 <= next_col < col_count and field[next_row][next_col] != '#':
#                 heapq.heappush(queue, (cost + 1, next_row, next_col, direction))
#             heapq.heappush(queue, (cost + 1000, row, col, (dc, -dr))) # turn clockwise
#             heapq.heappush(queue, (cost + 1000, row, col, (-dc, dr))) # turn counter-clockwise

def part2():
    with open('input.txt') as f:
        lines = f.readlines()
        field = [[char for char in line.strip() ] for line in lines]

        row_count = len(field)
        col_count = len(field[0])

        for row in range(row_count):
            for col in range(col_count):
                if field[row][col] == 'S':
                    start_row, start_col = row, col
                if field[row][col] == 'E':
                    end_row, end_col = row, col

        print(start_row, start_col)
        print(end_row, end_col)

    pq = [(0, start_row, start_col, 0, 1)]
    lowest_cost = {(start_row, start_col, 0, 1): 0}
    track = {}
    min_cost = float("inf")
    end_states = set()

    while pq:
        cost, r, c, dr, dc = heapq.heappop(pq)
        if cost > lowest_cost.get((r, c, dr, dc), float("inf")):
            continue
        if field[r][c] == "E":
            if cost > min_cost:
                break
            min_cost = cost
            end_states.add((r, c, dr, dc))
        for new_cost, nr, nc, ndr, ndc in [(cost + 1, r + dr, c + dc, dr, dc), (cost + 1000, r, c, dc, -dr), (cost + 1000, r, c, -dc, dr)]:
            if field[nr][nc] == "#":
                continue
            lowest = lowest_cost.get((nr, nc, ndr, ndc), float("inf"))
            if new_cost > lowest:
                continue
            if new_cost < lowest:
                track[(nr, nc, ndr, ndc)] = set()
                lowest_cost[(nr, nc, ndr, ndc)] = new_cost
            track[(nr, nc, ndr, ndc)].add((r, c, dr, dc))
            heapq.heappush(pq, (new_cost, nr, nc, ndr, ndc))

    states = deque(end_states)
    visited = set(end_states)

    while states:
        key = states.popleft()
        for last in track.get(key, []):
            if last in visited:
                continue
            visited.add(last)
            states.append(last)

    print(len({(r, c) for r, c, _, _ in visited}))


if __name__ == '__main__':
    part1()
    part2()