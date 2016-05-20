class Chessboard:

    def __init__(self, n, m):
        "Defines a n x m chess board."
        self.n = n
        self.m = m

class Path:

    def __init__(self, chessboard, tail, x, y):
        self.chessboard = chessboard # the chessboard
        self.tail = tail # previuos position of the knight
        self.x = x # current x position of the knight
        self.y = y # current y position of the knight
