# 1812. Determine Color of a Chessboard Square

# You are given coordinates, a string that represents the coordinates of 
# a square of the chessboard. Below is a chessboard for your reference.

class Solution:
    def squareIsWhite(self, coord: str) -> bool:
        x_axis = "abcdefgh"
        y_axis = "12345678"

        if coord[0] in "aceg" and coord[1] in "1357":
            return False
        elif coord[0] in "bdfh" and coord[1] in "2468":
            return False
        else:
            return True
