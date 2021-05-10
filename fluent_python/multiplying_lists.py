#!/usr/bin/env python

# wrong way

wrong_board = [["_"] * 3] * 3
print("wrong_board", wrong_board)
wrong_board[0][0] = "x"
print("wrong_board", wrong_board)

right_board = [["_"] * 3 for i in range(3)]
print("right_board", right_board)
right_board[0][0] = "x"
print("right_board", right_board)
