
#Credit to pelle
import chess
import time


start = time.time()


board = chess.Board()
for i in range(0, 1):
    legal_moves = str(board.legal_moves)
    legal_moves = legal_moves.split(" ")[3::]
    removetable = str.maketrans(" ", " ", "<(),>")
    legal_moves = [s.translate(removetable) for s in legal_moves]


print(time.time() - start)