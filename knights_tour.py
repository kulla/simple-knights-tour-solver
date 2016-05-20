import re

class Chessboard:

    def __init__(self, n, m):
        "Defines a n x m chess board."

        assert n > 0
        assert m > 0

        self.n = n
        self.m = m

    def find_knights_tour(self, start_x, start_y):
        pass

class Path:

    def __init__(self, chessboard, tail, x, y):
        assert 0 <= x and x <= chessboard.n
        assert 0 <= y and y <= chessboard.m

        self.chessboard = chessboard # the chessboard
        self.tail = tail # previuos position of the knight
        self.x = x # current x position of the knight
        self.y = y # current y position of the knight

    @property
    def positions(self):
        "Returns a list of positions where the knight has been."
        if self.tail:
            result = self.tail.positions
            result.append( (self.x, self.y) )
            return result
        else:
            return []

if __name__ == "__main__":
    print("== What is the size of the chess board? ==")
    print("Enter the size in the format nxm like '8x8' or '42x23'")
    print("")

    user_input = input("Size of chess board: ")

    n,m = map(int, re.match(r"(\d+)x(\d+)", user_input).groups())

    chessboard = Chessboard(n,m)

    chessboard.find_knights_tour(0,0)
