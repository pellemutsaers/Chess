
import pygame, chess, random, time

display_size_x, display_size_y = 480, 480 + 32
pygame.init()
display = pygame.display.set_mode((display_size_x, display_size_y))
tile_colour_black = (115, 85, 70)
tile_colour_white = (235, 210, 180)
base_font = pygame.font.Font(None, 32)


random_fen = "7r/1P2p3/3bB2N/3K2pp/4P3/5PR1/kP2pP2/8 w KQkq - 0 1"
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
whitePawn = pygame.image.load("PNGs/White_pawn.png")
whiteRook = pygame.image.load("PNGs/White_rook.png")
whiteKnight = pygame.image.load("PNGs/White_knight.png")
whiteBishop = pygame.image.load("PNGs/White_bishop.png")
whiteQueen = pygame.image.load("PNGs/White_queen.png")
whiteKing = pygame.image.load("PNGs/White_king.png")

blackPawn = pygame.image.load("PNGs/Black_pawn.png")
blackRook = pygame.image.load("PNGs/Black_rook.png")
blackKnight = pygame.image.load("PNGs/Black_knight.png")
blackBishop = pygame.image.load("PNGs/Black_bishop.png")
blackQueen = pygame.image.load("PNGs/Black_queen.png")
blackKing = pygame.image.load("PNGs/Black_king.png")

def splitString(string):
    return [char for char in string]

def printFen():
    fen_split_on_slash = board.fen().split("/")
    fen_split = fen_split_on_slash[0:7] + fen_split_on_slash[7].split()

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
        #print(columns[column])
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
    time.sleep(1)
    running = True
    White_Is_Computer = True
    Black_Is_Computer = False
    user_text = ""
    movenumber = 0
    Finished = False
    WhiteToMove = True

    while running:
        if movenumber % 2 == 0:
            WhiteToMove = True
        else:
            WhiteToMove = False
        Human_move = False
        Computer_move = False
        if WhiteToMove:
            if White_Is_Computer:
                Computer_move = True
            elif Black_Is_Computer:
                Human_move = True
        else:
            if Black_Is_Computer:
                Computer_move = True
            elif White_Is_Computer:
                Human_move = True
            
        if Human_move and not Finished:
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
                            movenumber += 1
                        except:
                            print("Illegal move")
                        drawBoard()
                        printFen()
                        user_text = ""
                        checkmate_status = board.is_checkmate()
                        repetition_status = board.is_stalemate()
                        insufficient_material_status = board.is_insufficient_material()

                        if checkmate_status == True:
                            if WhiteToMove:
                                user_text = "Black won"
                                Finished = True
                            else:
                                user_text = "White won"
                                Finished = True
                        if repetition_status or insufficient_material_status:
                            user_text = "Draw"
                            Finished = True

                    else:
                        user_text += event.unicode

        if Computer_move and not Finished:
            legal_moves = str(board.legal_moves)
            legal_moves = legal_moves.split(" ")[3::]
            removetable = str.maketrans(" ", " ", "<(),>")
            legal_moves = [s.translate(removetable) for s in legal_moves]
            length = len(legal_moves)
            index = random.randint(0, length)
            move = legal_moves[index-1]

            try:
                board.push_san(move)
                movenumber += 1
                drawBoard()
                printFen()
            except:
                Finished = True

            checkmate_status = board.is_checkmate()
            repetition_status = board.is_stalemate()
            insufficient_material_status = board.is_insufficient_material()

            if checkmate_status == True:

                if WhiteToMove:
                    user_text = "Black won"
                    Finished = True
                else:
                    user_text = "White won"
                    Finished = True

            if repetition_status or insufficient_material_status:
                user_text = "Draw"
                Finished = True
                 
            drawBoard()
            printFen()

        pygame.draw.rect(display, (50, 50, 50) , pygame.Rect(0, display_size_y-32, display_size_x, display_size_y))
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        display.blit(text_surface, (0, display_size_y-32 + 5))
        pygame.display.flip()

        if Finished:
            closing = str(input("Press any button to close: "))
            if type(closing) == str:
                running = False
            
if __name__ == "__main__":
    main()