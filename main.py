import pygame
from pygame.locals import *
import chess

display_size_x, display_size_y = 480, 480
pygame.init()
display = pygame.display.set_mode((display_size_x, display_size_y))
tile_colour_black = (105, 75, 60)
tile_colour_white = (235, 210, 180)

random_fen = "8/8/p7/4n3/3K4/2BbN1k1/4Q3/4R3 w - - 0 1"
board = chess.Board(random_fen)

#board = chess.Board(random_fen)

#Pieces:
whitePawn = pygame.image.load("Python\Chess\PNG's\White_pawn.png")
whiteRook = pygame.image.load("Python\Chess\PNG's\White_rook.png")
whiteKnight = pygame.image.load("Python\Chess\PNG's\White_knight.png")
whiteBishop = pygame.image.load("Python\Chess\PNG's\White_bishop.png")
whiteQueen = pygame.image.load("Python\Chess\PNG's\White_queen.png")
whiteKing = pygame.image.load("Python\Chess\PNG's\White_king.png")

blackPawn = pygame.image.load("Python\Chess\PNG's\Black_pawn.png")
blackRook = pygame.image.load("Python\Chess\PNG's\Black_rook.png")
blackKnight = pygame.image.load("Python\Chess\PNG's\Black_knight.png")
blackBishop = pygame.image.load("Python\Chess\PNG's\Black_bishop.png")
blackQueen = pygame.image.load("Python\Chess\PNG's\Black_queen.png")
blackKing = pygame.image.load("Python\Chess\PNG's\Black_king.png")

def splitString(string):
    return [char for char in string]

def printFen():
    fen_split_on_slash = board.fen().split("/")
    fen_split = fen_split_on_slash[0:7] + fen_split_on_slash[7].split()

    #column_fen:
    columns = {
        "column1" : splitString(fen_split[0]),
        "column2" : splitString(fen_split[1]),
        "column3" : splitString(fen_split[2]),
        "column4" : splitString(fen_split[3]),
        "column5" : splitString(fen_split[4]),
        "column6" : splitString(fen_split[5]),
        "column7" : splitString(fen_split[6]),
        "column8" : splitString(fen_split[7])
    }

    for column in columns:
        for index, i in enumerate(columns[column]):
            if i.isdigit():
                j = int(i)
                columns[column].pop(index)
                for ii in range(j):
                    columns[column].insert(index+ii, " ")
        print(columns[column])
        
def drawBoard():
    for x in range(0, 8):
        for y in range(0, 8):
            if (x + y) % 2 == 1:
                pygame.draw.rect(display, tile_colour_black , pygame.Rect(x*(display_size_x/8), y*(display_size_y/8), display_size_x/8, display_size_y/8))

def main():
    pygame.display.set_caption("Chess")
    display.fill(tile_colour_white)
    drawBoard()
    printFen()
    running = True

    while running:
        pygame.display.flip()
        drawBoard()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.type == K_ESCAPE:
                    running = False
            
if __name__ == "__main__":
    main()