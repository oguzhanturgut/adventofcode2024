"""
--- Day 8: Resonant Collinearity ---
You find yourselves on the roof of a top-secret Easter Bunny installation.

While The Historians do their thing, you take a look at the familiar huge antenna. Much to your surprise, it seems to have been reconfigured to emit a signal that makes people 0.1% more likely to buy Easter Bunny brand Imitation Mediocre Chocolate as a Christmas gift! Unthinkable!

Scanning across the city, you find that there are actually many such antennas. Each antenna is tuned to a specific frequency indicated by a single lowercase letter, uppercase letter, or digit. You create a map (your puzzle input) of these antennas. For example:

............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
The signal only applies its nefarious effect at specific antinodes based on the resonant frequencies of the antennas. In particular, an antinode occurs at any point that is perfectly in line with two antennas of the same frequency - but only when one of the antennas is twice as far away as the other. This means that for any pair of antennas with the same frequency, there are two antinodes, one on either side of them.

So, for these two antennas with frequency a, they create the two antinodes marked with #:

..........
...#......
..........
....a.....
..........
.....a....
..........
......#...
..........
..........
Adding a third antenna with the same frequency creates several more antinodes. It would ideally add four antinodes, but two are off the right side of the map, so instead it adds only two:

..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......#...
..........
..........
Antennas with different frequencies don't create antinodes; A and a count as different frequencies. However, antinodes can occur at locations that contain antennas. In this diagram, the lone antenna with frequency capital A creates no antinodes but has a lowercase-a-frequency antinode at its location:

..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......A...
..........
..........
The first example has antennas with two different frequencies, so the antinodes they create look like this, plus an antinode overlapping the topmost A-frequency antenna:

......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#.
Because the topmost A-frequency antenna overlaps with a 0-frequency antinode, there are 14 total unique locations that contain an antinode within the bounds of the map.

Calculate the impact of the signal. How many unique locations within the bounds of the map contain an antinode?
"""

from collections import defaultdict


def part1():
    with open('input.txt') as f:
        field = f.read().splitlines()
        field = [list(x.strip()) for x in field]

        row_len = len(field)
        col_len = len(field[0])
        antenna_locs = defaultdict(list)

        for i in range(row_len):
            for j in range(col_len):
                if field[i][j] != '.':
                    antenna_locs[field[i][j]].append((i,j))

        antinodes = set()
        for antenna,locations in antenna_locs.items():
            for (point1_r,point1_c) in locations:
                for (point2_r,point2_c) in locations:
                    if (point1_r,point1_c) == (point2_r,point2_c):
                        continue

                    dr = point2_r - point1_r
                    dc = point2_c - point1_c

                    point3 = (point2_r + dr, point2_c + dc)
                    point4 = (point1_r - dr, point1_c - dc)

                    if 0 <= point3[0] < row_len and 0 <= point3[1] < col_len:
                        antinodes.add(point3)
                    if 0 <= point4[0] < row_len and 0 <= point4[1] < col_len:
                        antinodes.add(point4)
        print(len(antinodes))
        return len(antinodes)

"""
--- Part Two ---
Watching over your shoulder as you work, one of The Historians asks if you took the effects of resonant harmonics into your calculations.

Whoops!

After updating your model, it turns out that an antinode occurs at any grid position exactly in line with at least two antennas of the same frequency, regardless of distance. This means that some of the new antinodes will occur at the position of each antenna (unless that antenna is the only one of its frequency).

So, these three T-frequency antennas now create many antinodes:

T....#....
...T......
.T....#...
.........#
..#.......
..........
...#......
..........
....#.....
..........
In fact, the three T-frequency antennas are all exactly in line with two antennas, so they are all also antinodes! This brings the total number of antinodes in the above example to 9.

The original example now has 34 antinodes, including the antinodes that appear on every antenna:

##....#....#
.#.#....0...
..#.#0....#.
..##...0....
....0....#..
.#...#A....#
...#..#.....
#....#.#....
..#.....A...
....#....A..
.#........#.
...#......##
Calculate the impact of the signal using this updated model. How many unique locations within the bounds of the map contain an antinode?
"""

def part2():
    with open('input.txt') as f:
        field = f.read().splitlines()
        field = [list(x.strip()) for x in field]

        row_len = len(field)
        col_len = len(field[0])
        antenna_locs = defaultdict(list)

        for i in range(row_len):
            for j in range(col_len):
                if field[i][j] != '.':
                    antenna_locs[field[i][j]].append((i,j))

        antinodes = set()

        for antenna,locations in antenna_locs.items():
            for (point1_r,point1_c) in locations:
                for (point2_r,point2_c) in locations:
                    if (point1_r,point1_c) == (point2_r,point2_c):
                        continue
                    dr = point2_r - point1_r
                    dc = point2_c - point1_c

                    # Antennas are also antinodes!!!
                    temp_r1 = point1_r
                    temp_c1 = point1_c

                    while 0 <= temp_r1 < row_len and 0 <= temp_c1 < col_len:
                        antinodes.add((temp_r1,temp_c1))
                        temp_r1 += dr
                        temp_c1 += dc

                    temp_r2 = point2_r
                    temp_c2 = point2_c
                    while 0 <= temp_r2 < row_len and 0 <= temp_c2 < col_len:
                        antinodes.add((temp_r2,temp_c2))
                        temp_r2 -= dr
                        temp_c2 -= dc

        print(len(antinodes))
        return len(antinodes)


if __name__ == '__main__':
    assert part1() == 396
    assert part2() == 1200