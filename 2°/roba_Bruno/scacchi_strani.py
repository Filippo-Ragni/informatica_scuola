# classi pedine e scacchiera

class piece:
    def __init__(self, x, y, colour, board, pi): 
        self.x = x
        self.y = y
        self.pi = pi
        self.colour  = colour
        self.board = board
        self.board.pieces.append(self) 

class king(piece):
    def __init__(self, x, y, colour, board, pi):
        super().__init__(x, y, colour, board, pi)

    def move(self):
        x = int(input("x: "))
        y = int(input("y: "))
        for p in self.board.pieces:
            if p.x == x and p.y == y and p.colour != self.colour:
                self.board.pieces.remove(p)
                self.x = x
                self.y = y
                break
            elif p.x == x and p.y == y and p.colour == self.colour:
                print("non puoi spostare il re su un altro tuo stesso pezzo")
                break
        if self.x > self.field.w or self.x < 1 or self.y > self.field.h or self.y < 1:
            print("i pezzi non possono essere mossi fuori dalla scacchiera")
        elif self.x == x and self.y == y:
            print("devi muovere il re se selezionato")
        elif (self.x - x) < -1 or (self.x - x) > 1 or (self.y - y) < -1 or (self.y - y):
            print("non puoi muovere il re in questa casella")
        else:
            self.x = x
            self.y = y

class queen(piece):
    def __init__(self, x, y, colour, board, pi):
        super().__init__(x, y, colour, board, pi)

    def move(self):
        x = int(input("x: "))
        y = int(input("y: "))
        if self.x > self.field.w or self.x < 1 or self.y > self.field.h or self.y < 1:
            print("i pezzi non possono essere mossi fuori dalla scacchiera")
        elif self.x == x and self.y == y:
            print("devi muovere la regina se selezionata")
        elif (self.x - x) == (self.y - y) or (self.x - x) == (y - self.y):
            self.x = x
            self.y = y
        elif self.x == x and self.y != y:
            self.x = x
            self.y = y
        elif self.x != x and self.y == y:
            self.x = x
            self.y = y
        else:
            print("non puoi muovere la regina in questa cella")

class rook(piece):
    def __init__(self, x, y, colour, board, pi):
        super().__init__(x, y, colour, board, pi)

class bishop(piece):
    def __init__(self, x, y, colour, board, pi):
        super().__init__(x, y, colour, board, pi)

class knight(piece):
    def __init__(self, x, y, colour, board, pi):
        super().__init__(x, y, colour, board, pi)

class pond(piece):
    def __init__(self, x, y, colour, board, pi):
        super().__init__(x, y, colour, board, pi)

class board:
    def __init__(self):
        self.w = 8
        self.h = 8
        self.pieces = []

    def draw(self):
        for y in range(self.h):
            for x in range(self.w):
                for e in self.pieces:
                    if x + 1 == e.x and y + 1 == e.y:
                        print("[" + e.colour + e.pi + "]", end = "")
                        break
                else: 
                    print("[  ]", end = "")
            print()



# inizio gioco

c_board = board()

wk = king(5, 8, "w", c_board, "k")
wq = queen(4, 8, "w", c_board, "q")
wr1 = rook(1, 8, "w", c_board, "r")
wr2 = rook(8, 8, "w", c_board, "r")
wb1 = bishop(3, 8, "w", c_board, "b")
wb2 = bishop(6, 8, "w", c_board, "b")
wh1 = knight(2, 8, "w", c_board, "h")
wh2 = knight(7, 8, "w", c_board, "h")
wp1 = pond(1, 7, "w", c_board, "p")
wp2 = pond(2, 7, "w", c_board, "p")
wp3 = pond(3, 7, "w", c_board, "p")
wp4 = pond(4, 7, "w", c_board, "p")
wp5 = pond(5, 7, "w", c_board, "p")
wp6 = pond(6, 7, "w", c_board, "p")
wp7 = pond(7, 7, "w", c_board, "p")
wp8 = pond(8, 7, "w", c_board, "p")

bk = king(4, 1, "b", c_board, "k")
bq = queen(5, 1, "b", c_board, "q")
br1 = rook(1, 1, "b", c_board, "r")
br2 = rook(8, 1, "b", c_board, "r")
bb1 = bishop(3, 1, "b", c_board, "b")
bb2 = bishop(6, 1, "b", c_board, "b")
bh1 = knight(2, 1, "b", c_board, "h")
bh2 = knight(7, 1, "b", c_board, "h")
bp1 = pond(1, 2, "b", c_board, "p")
bp2 = pond(2, 2, "b", c_board, "p")
bp3 = pond(3, 2, "b", c_board, "p")
bp4 = pond(4, 2, "b", c_board, "p")
bp5 = pond(5, 2, "b", c_board, "p")
bp6 = pond(6, 2, "b", c_board, "p")
bp7 = pond(7, 2, "b", c_board, "p")
bp8 = pond(8, 2, "b", c_board, "p")

c_board.draw()
