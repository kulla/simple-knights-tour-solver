# parse_sitemap.py
#
# Written in 2016 by Stephan Kulla ( http://kulla.me/ )
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain
# worldwide. This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along
# with this software. If not, see
# < http://creativecommons.org/publicdomain/zero/1.0/ >.

from itertools import *

import re
import sys

KNIGHT_STEPS = [ (2,1), (2,-1), (-2,1), (-2,-1),
                 (1,2), (1,-2), (-1,2), (-1, -2)]

class Chessboard:

    def __init__(self, n, m):
        "Defines a n x m chess board."

        assert n > 0
        assert m > 0

        self.n = n
        self.m = m

    @property
    def number_fields(self):
        return self.n * self.m

    def find_knights_tour(self, start_x, start_y):
        sys.setrecursionlimit(self.number_fields*10)

        return Path(self, start_x, start_y).find_knights_tour()

class Path:

    def __init__(self, chessboard, x, y, tail=None):
        assert 0 <= x and x < chessboard.n
        assert 0 <= y and y < chessboard.m

        self.chessboard = chessboard # the chessboard
        self.tail = tail # previuos position of the knight
        self.x = x # current x position of the knight
        self.y = y # current y position of the knight

    @property
    def positions(self):
        "Returns a list of positions where the knight has been."
        result = self.tail.positions if self.tail else []
        result.append( (self.x, self.y) )

        return result

    @property
    def next_steps(self):
        result = map(lambda p: (self.x + p[0], self.y + p[1]), KNIGHT_STEPS)
        result = filter(lambda p: (p[0] >= 0 and p[1] >= 0
                                             and p[0] < self.chessboard.n
                                             and p[1] < self.chessboard.m),
                        result)

        return list(result)


    @property
    def next_possible_positions(self):
        last_positions = self.positions

        return list(filter(lambda p: p not in last_positions, self.next_steps))

    def is_knights_tour(self):
        pos = self.positions

        return (len(pos) == self.chessboard.number_fields
                and pos[0] in self.next_steps)

    def find_knights_tour(self):
        if self.is_knights_tour():
            return self
        else:
            print(len(self.positions))
            next_steps = self.next_possible_positions
            next_steps = list(map(lambda x: Path(self.chessboard,
                                                 x[0], x[1], self),
                                  next_steps))
            next_steps.sort(key = lambda x: len(x.next_possible_positions))

            for step in next_steps:
                path = step.find_knights_tour()

                if path:
                    return path

            return None

    def print_path(self):
        pos = {}
        num = len("%d" % self.chessboard.number_fields)
        form = "%" + str(num) + "d"

        for p, n in zip(self.positions, count(1)):
            pos[p] = n

        print("-" * ((num+1) * self.chessboard.n + 1))

        for y in range(self.chessboard.m):
            for x in range(self.chessboard.n):
                print("|", end="")
                print(form % pos[(x,y)], end="")

            print("|")
            print("-" * (3 * self.chessboard.n + 1))

if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        x = int(sys.argv[3])
        y = int(sys.argv[4])

        chessboard = Chessboard(n,m)
        solution = chessboard.find_knights_tour(x,y)

        if solution:
            solution.print_path()
        else:
            print("Keine Lösung!")
    except:
        print("USAGE: python3 knights_tour.py [n] [m] [x] [y]")
        print()
        print("Chess board has size nxm and the start point is (x,y)")
        print("with 0 <= x < n and 0 <= y < m.")
