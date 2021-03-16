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
