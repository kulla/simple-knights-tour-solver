import re

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
        pass

class Path:

    def __init__(self, chessboard, x, y, tail=None):
        assert 0 <= x and x <= chessboard.n
        assert 0 <= y and y <= chessboard.m

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
    def next_possible_positions(self):
        result = map(lambda p: (self.x + p[0], self.y + p[1]), KNIGHT_STEPS)
        result = filter(lambda p: (p[0] >= 0 and p[1] >= 0
                                             and p[0] <= self.chessboard.n
                                             and p[1] <= self.chessboard.m),
                        result)

        last_positions = self.positions
        result = filter(lambda p: p not in last_positions, result)

        return list(result)

if __name__ == "__main__":
    print("== What is the size of the chess board? ==")
    print("Enter the size in the format nxm like '8x8' or '42x23'")
    print("")

    user_input = input("Size of chess board: ")

    n,m = map(int, re.match(r"(\d+)x(\d+)", user_input).groups())

    chessboard = Chessboard(n,m)

    chessboard.find_knights_tour(0,0)
