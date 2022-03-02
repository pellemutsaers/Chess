import pygame, chess, random

display_size_x, display_size_y = 480, 480 + 32
pygame.init()
display = pygame.display.set_mode((display_size_x, display_size_y))
tile_colour_black = (115, 85, 70)
tile_colour_white = (235, 210, 180)
base_font = pygame.font.Font(None, 32)

random_fen = "7r/1P2p3/3bB2N/3K2pp/4P3/5PR1/kP2pP2/8 w - - 0 1"
drawn_fen = "8/8/8/8/8/6Q1/8/7k w - - 0 1"
board = chess.Board()

def drawBoard():
    for x in range(0, 8):
        for y in range(0, 8):
            if (x + y) % 2 == 1:
                pygame.draw.rect(display, tile_colour_black , pygame.Rect(x*(display_size_x/8), y*((display_size_y-32)/8), display_size_x/8, (display_size_y-32)/8))
            if (x + y) % 2 == 0:
                pygame.draw.rect(display, tile_colour_white , pygame.Rect(x*(display_size_x/8), y*((display_size_y-32)/8), display_size_x/8, (display_size_y-32)/8))
    pygame.display.flip()

#Pieces:
whitePawn = pygame.image.load("PNG's\White_pawn.png")
whiteRook = pygame.image.load("PNG's\White_rook.png")
whiteKnight = pygame.image.load("PNG's\White_knight.png")
whiteBishop = pygame.image.load("PNG's\White_bishop.png")
whiteQueen = pygame.image.load("PNG's\White_queen.png")
whiteKing = pygame.image.load("PNG's\White_king.png")

blackPawn = pygame.image.load("PNG's\Black_pawn.png")
blackRook = pygame.image.load("PNG's\Black_rook.png")
blackKnight = pygame.image.load("PNG's\Black_knight.png")
blackBishop = pygame.image.load("PNG's\Black_bishop.png")
blackQueen = pygame.image.load("PNG's\Black_queen.png")
blackKing = pygame.image.load("PNG's\Black_king.png")

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

#Credit to GijsPeletier
    for column in columns:
        for index, i in enumerate(columns[column]):
            if i.isdigit():
                j = int(i)
                columns[column].pop(index)
                for ii in range(j):
                    columns[column].insert(index+ii, " ")
#End of credit to GijsPeletier

    for column_val, column in enumerate(columns):
        for index, j in enumerate(columns[column]):
            drawPieces(j, index, column_val)
        pygame.display.flip()

def drawPieces(string, index, column):
    if string == " ":
        pass
    if string == "P":
        display.blit(whitePawn, ((index)*60, (column)*60))
    if string == "R":
        display.blit(whiteRook, ((index)*60, (column)*60))
    if string == "N":
        display.blit(whiteKnight, ((index)*60, (column)*60))
    if string == "B":
        display.blit(whiteBishop, ((index)*60, (column)*60))
    if string == "Q":
        display.blit(whiteQueen, ((index)*60, (column)*60))
    if string == "K":
        display.blit(whiteKing, ((index)*60, (column)*60))
    if string == "p":
        display.blit(blackPawn, ((index)*60, (column)*60))
    if string == "r":
        display.blit(blackRook, ((index)*60, (column)*60))
    if string == "n":
        display.blit(blackKnight, ((index)*60, (column)*60))
    if string == "b":
        display.blit(blackBishop, ((index)*60, (column)*60))
    if string == "q":
        display.blit(blackQueen, ((index)*60, (column)*60))
    if string == "k":
        display.blit(blackKing, ((index)*60, (column)*60))

def main():
    pygame.display.set_caption("Chess")
    drawBoard()
    printFen()
    running = True
    random_moves = False
    user_text = ""
    movenumber = 0
    done = False
    Clock = pygame.time.Clock()

    while running:
        if not random_moves:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]

                    elif event.key == pygame.K_SPACE:
                        try:
                            board.push_san(user_text)
                        except:
                            print("Illegal move")

                        drawBoard()
                        printFen()
                        movenumber += 1
                        user_text = ""
                        checkmate_status = board.is_checkmate()
                        repetition_status = board.is_stalemate()
                        insufficient_material_status = board.is_insufficient_material()

                        if checkmate_status == True:
                            if movenumber % 2 == 1:
                                user_text = "White won"
                            else:
                                user_text = "Black won"
                        if repetition_status or insufficient_material_status:
                            user_text = "Draw"

                    else:
                        user_text += event.unicode
        
        if random_moves and not done:
            movenumber += 1
            legal_moves = str(board.legal_moves)
            legal_moves = legal_moves.split(" ")[3::]
            removetable = str.maketrans(" ", " ", "<(),>")
            legal_moves = [s.translate(removetable) for s in legal_moves]
            length = len(legal_moves)
            index = random.randint(0, length-1)
            move = legal_moves[index]

            try:
                board.push_san(move)
            except:
                done = True
            
            checkmate_status = board.is_checkmate()
            repetition_status = board.is_stalemate()
            insufficient_material_status = board.is_insufficient_material()

            if checkmate_status == True:

                if movenumber % 2 == 1:
                    user_text = "White won"
                    done = True
                else:
                    user_text = "Black won"
                    done = True
            if repetition_status or insufficient_material_status:
                user_text = "Draw"
                done = True 
            Clock.tick(120)         

            drawBoard()
            printFen()

        pygame.draw.rect(display, (50, 50, 50) , pygame.Rect(0, 480, 480, 480 + 32))
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        display.blit(text_surface, (0, 480 + 5))

        pygame.display.flip()
            
if __name__ == "__main__":
    main()