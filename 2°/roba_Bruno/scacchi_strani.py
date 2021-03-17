# classi pedine e scacchiera

class piece:
    def __init__(self, x, y, colour, board): 
        self.x = x
        self.y = y
        self.colour  = colour
        self.board = board
        self.board.pieces.append(self) 

class king(piece):
    def __init__(self, x, y, board, pi):
        super().__init__(x, y, colour, board)

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
    def __init__(self, x, y, board, pi):
        super().__init__(x, y, colour, board)

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
    def __init__(self, x, y, board, pi):
        super().__init__(x, y, colour, board)

class bishop(piece):
    def __init__(self, x, y, board, pi):
        super().__init__(x, y, colour, board)

class knight(piece):
    def __init__(self, x, y, board, pi):
        super().__init__(x, y, colour, board)

class pond(piece):
    def __init__(self, x, y, board, pi):
        super().__init__(x, y, colour, board)

class board:
    def __init__(self):
        self.w = 8
        self.h = 8
        self.entities = []

    def draw(self):
        for y in range(self.h):
            for x in range(self.w):
                for e in self.entities:
                    if x + 1 == e.x and y + 1 == e.y and e.pi == "wq":
                        print("[wq]", end = "")
                        break
                    if x + 1 == e.x and y + 1 == e.y and e.pi == "wk":
                        print("[wk]", end = "")
                        break
                    if x + 1 == e.x and y + 1 == e.y and e.pi == "wb":
                        print("[wb]", end = "")
                        break
                    if x + 1 == e.x and y + 1 == e.y and e.pi == "wr":
                        print("[wr]", end = "")
                        break
                    if x + 1 == e.x and y + 1 == e.y and e.pi == "wh":
                        print("[wh]", end = "")
                        break
                    if x + 1 == e.x and y + 1 == e.y and e.pi == "wp":
                        print("[wp]", end = "")
                        break
                    if x + 1 == e.x and y + 1 == e.y and e.pi == "bq":
                        print("[bq]", end = "")
                        break
                    if x + 1 == e.x and y + 1 == e.y and e.pi == "bk":
                        print("[bk]", end = "")
                        break
                    if x + 1 == e.x and y + 1 == e.y and e.pi == "bb":
                        print("[bb]", end = "")
                        break
                    if x + 1 == e.x and y + 1 == e.y and e.pi == "br":
                        print("[br]", end = "")
                        break
                    if x + 1 == e.x and y + 1 == e.y and e.pi == "bh":
                        print("[bh]", end = "")
                        break
                    if x + 1 == e.x and y + 1 == e.y and e.pi == "bp":
                        print("[bp]", end = "")
                        break
                else: 
                    print("[  ]", end = "")
            print()



# inizio gioco

c_board = board()

wk = king(5, 8, "w", c_board)
wq = queen(4, 8, "w", c_board)
wr1 = rook(1, 8, "w", c_board)
wr2 = rook(8, 8, "w", c_board)
wb1 = bishop(3, 8, "w", c_board)
wb2 = bishop(6, 8, "w", c_board)
wh1 = knight(2, 8, "w", c_board)
wh2 = knight(7, 8, "w", c_board)
wp1 = pond(1, 7, "w", c_board)
wp2 = pond(2, 7, "w", c_board)
wp3 = pond(3, 7, "w", c_board)
wp4 = pond(4, 7, "w", c_board)
wp5 = pond(5, 7, "w", c_board)
wp6 = pond(6, 7, "w", c_board)
wp7 = pond(7, 7, "w", c_board)
wp8 = pond(8, 7, "w", c_board)

bk = king(4, 1, "b", c_board)
bq = queen(5, 1, "b", c_board)
br1 = rook(1, 1, "b", c_board)
br2 = rook(8, 1, "b", c_board)
bb1 = bishop(3, 1, "b", c_board)
bb2 = bishop(6, 1, "b", c_board)
bh1 = knight(2, 1, "b", c_board)
bh2 = knight(7, 1, "b", c_board)
bp1 = pond(1, 2, "b", c_board)
bp2 = pond(2, 2, "b", c_board)
bp3 = pond(3, 2, "b", c_board)
bp4 = pond(4, 2, "b", c_board)
bp5 = pond(5, 2, "b", c_board)
bp6 = pond(6, 2, "b", c_board)
bp7 = pond(7, 2, "b", c_board)
bp8 = pond(8, 2, "b", c_board)

c_board.draw()
