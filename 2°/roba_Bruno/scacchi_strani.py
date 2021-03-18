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

    def move(self, a, o):
        ta = a
        to = o
        print()
        while True:
            if self.x == ta and self.y == to:
                print("devi muovere il re se selezionato")
                ta = int(input("x : "))
                to = int(input("y : "))
            elif ta > self.board.w or self.x < 1 or to > self.board.h or self.y < 1:
                print("i pezzi non possono essere mossi fuori dalla scacchiera")
                ta = int(input("x : "))
                to = int(input("y : "))

            elif (self.x - ta) == -1 and (self.y - to) == -1:
                counter = 0
                for p in self.board.pieces:
                    if p.x == ta and p.y == to and p.colour != self.colour:
                        counter += 1
                        self.board.pieces.remove(p)
                        self.x = a
                        self.y = o
                        break
                    elif p.x == ta and p.y == to and p.colour == self.colour:
                        counter += 1
                        print("non puoi spostare il re su un altro tuo stesso pezzo")
                        ta = int(input("x : "))
                        to = int(input("y : "))
                        break
                if counter == 0:
                    self.x = ta
                    self.y = to
                    break
            elif (self.x - ta) == -1 and (self.y - to) == 0:
                counter = 0
                for p in self.board.pieces:
                    if p.x == ta and p.y == to and p.colour != self.colour:
                        counter += 1
                        self.board.pieces.remove(p)
                        self.x = a
                        self.y = o
                        break
                    elif p.x == ta and p.y == to and p.colour == self.colour:
                        counter += 1
                        print("non puoi spostare il re su un altro tuo stesso pezzo")
                        ta = int(input("x : "))
                        to = int(input("y : "))
                        break
                if counter == 0:
                    self.x = ta
                    self.y = to
                    break
            elif (self.x - ta) == -1 and (self.y - to) == 1:
                counter = 0
                for p in self.board.pieces:
                    if p.x == ta and p.y == to and p.colour != self.colour:
                        counter += 1
                        self.board.pieces.remove(p)
                        self.x = a
                        self.y = o
                        break
                    elif p.x == ta and p.y == to and p.colour == self.colour:
                        counter += 1
                        print("non puoi spostare il re su un altro tuo stesso pezzo")
                        ta = int(input("x : "))
                        to = int(input("y : "))
                        break
                if counter == 0:
                    self.x = ta
                    self.y = to
                    break
            elif (self.x - ta) == 0 and (self.y - to) == -1:
                counter = 0
                for p in self.board.pieces:
                    if p.x == ta and p.y == to and p.colour != self.colour:
                        counter += 1
                        self.board.pieces.remove(p)
                        self.x = a
                        self.y = o
                        break
                    elif p.x == ta and p.y == to and p.colour == self.colour:
                        counter += 1
                        print("non puoi spostare il re su un altro tuo stesso pezzo")
                        ta = int(input("x : "))
                        to = int(input("y : "))
                        break
                if counter == 0:
                    self.x = ta
                    self.y = to
                    break
            elif (self.x - ta) == 0 and (self.y - to) == 1:
                counter = 0
                for p in self.board.pieces:
                    if p.x == ta and p.y == to and p.colour != self.colour:
                        counter += 1
                        self.board.pieces.remove(p)
                        self.x = a
                        self.y = o
                        break
                    elif p.x == ta and p.y == to and p.colour == self.colour:
                        counter += 1
                        print("non puoi spostare il re su un altro tuo stesso pezzo")
                        ta = int(input("x : "))
                        to = int(input("y : "))
                        break
                if counter == 0:
                    self.x = ta
                    self.y = to
                    break
            elif (self.x - ta) == 1 and (self.y - to) == -1:
                counter = 0
                for p in self.board.pieces:
                    if p.x == ta and p.y == to and p.colour != self.colour:
                        counter += 1
                        self.board.pieces.remove(p)
                        self.x = a
                        self.y = o
                        break
                    elif p.x == ta and p.y == to and p.colour == self.colour:
                        counter += 1
                        print("non puoi spostare il re su un altro tuo stesso pezzo")
                        ta = int(input("x : "))
                        to = int(input("y : "))
                        break
                if counter == 0:
                    self.x = ta
                    self.y = to
                    break
            elif (self.x - ta) == 1 and (self.y - to) == 0:
                counter = 0
                for p in self.board.pieces:
                    if p.x == ta and p.y == to and p.colour != self.colour:
                        counter += 1
                        self.board.pieces.remove(p)
                        self.x = a
                        self.y = o
                        break
                    elif p.x == ta and p.y == to and p.colour == self.colour:
                        counter += 1
                        print("non puoi spostare il re su un altro tuo stesso pezzo")
                        ta = int(input("x : "))
                        to = int(input("y : "))
                        break
                if counter == 0:
                    self.x = ta
                    self.y = to
                    break
            elif (self.x - ta) == 1 and (self.y - to) == 1:
                counter = 0
                for p in self.board.pieces:
                    if p.x == ta and p.y == to and p.colour != self.colour:
                        counter += 1
                        self.board.pieces.remove(p)
                        self.x = a
                        self.y = o
                        break
                    elif p.x == ta and p.y == to and p.colour == self.colour:
                        counter += 1
                        print("non puoi spostare il re su un altro tuo stesso pezzo")
                        ta = int(input("x : "))
                        to = int(input("y : "))
                        break
                if counter == 0:
                    self.x = ta
                    self.y = to
                    break

            else:
                print("il re non si può muovere qui")
                ta = int(input("x : "))
                to = int(input("y : "))
        print()

class queen(piece):
    def __init__(self, x, y, colour, board, pi):
        super().__init__(x, y, colour, board, pi)

    def move(self, a, o):
        ta = a
        to = o
        print()
        while True:
            if self.x == ta and self.y == to:
                print("devi muovere la regina se selezionata")
                ta = int(input("x : "))
                to = int(input("y : "))
            elif ta > self.board.w or self.x < 1 or to > self.board.h or self.y < 1:
                print("i pezzi non possono essere mossi fuori dalla scacchiera")
                ta = int(input("x : "))
                to = int(input("y : "))

            elif self.x == ta and self.y != to:
                counter = 0
                counter_a = 0
                for p in self.board.pieces:
                    if p.x == self.x and to < self.y:
                        if to < p.y and p.y < self.y:
                            counter_a += 1
                            print("non puoi oltrepassare le pedine con la regina")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                            print("1")
                    elif p.x == self.x and to > self.y:
                        if to > p.y and p.y > self.y:
                            counter_a += 1
                            print("non puoi oltrepassare le pedine con la regina")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                            print("2")
                if counter_a == 0:
                    for p in self.board.pieces:
                        if p.x == ta and p.y == to and p.colour != self.colour:
                            counter += 1
                            self.board.pieces.remove(p)
                            self.x = a
                            self.y = o
                            break
                        elif p.x == ta and p.y == to and p.colour == self.colour:
                            counter += 1
                            print("non puoi spostare la regina su un altro tuo stesso pezzo")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                            break
                    if counter == 0:
                        self.x = ta
                        self.y = to
                        break
            elif self.x != ta and self.y == to:
                counter = 0
                counter_a = 0
                for p in self.board.pieces:
                    if p.y == self.y and ta < self.x:
                        if ta < p.x and p.x < self.x:
                            counter_a += 1
                            print("non puoi oltrepassare le pedine con la regina")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                    elif p.y == self.y and ta > self.x:
                        if ta > p.x and p.x > self.x:
                            counter_a += 1
                            print("non puoi oltrepassare le pedine con la regina")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                if counter_a == 0:
                    for p in self.board.pieces:
                        if p.x == ta and p.y == to and p.colour != self.colour:
                            counter += 1
                            self.board.pieces.remove(p)
                            self.x = a
                            self.y = o
                            break
                        elif p.x == ta and p.y == to and p.colour == self.colour:
                            counter += 1
                            print("non puoi spostare la regina su un altro tuo stesso pezzo")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                            break
                    if counter == 0:
                        self.x = ta
                        self.y = to
                        break
            elif (self.x - ta) == -(self.y - to):
                counter = 0
                counter_a = 0
                for p in self.board.pieces:
                    if ta < self.x:
                        if ta < p.x and p.x < self.x and (p.x - ta) == -(p.y - to):
                            print("non puoi oltrepassare le pedine con la regina")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                    elif ta > self.x:
                        if ta > p.x and p.x > self.x and (p.x - ta) == -(p.y - to):
                            print("non puoi oltrepassare le pedine con la regina")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                if counter_a == 0:
                    for p in self.board.pieces:
                        if p.x == ta and p.y == to and p.colour != self.colour:
                            counter += 1
                            self.board.pieces.remove(p)
                            self.x = a
                            self.y = o
                            break
                        elif p.x == ta and p.y == to and p.colour == self.colour:
                            counter += 1
                            print("non puoi spostare la regina su un altro tuo stesso pezzo")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                            break
                    if counter == 0:
                        self.x = ta
                        self.y = to
                        break
            elif (self.x - ta) == (self.y - to):
                counter = 0
                counter_a = 0
                for p in self.board.pieces:
                    if ta < self.x:
                        if ta < p.x and p.x < self.x and (p.x - ta) == (p.y - to):
                            print("non puoi oltrepassare le pedine con la regina")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                    elif ta > self.x:
                        if ta > p.x and p.x > self.x and (p.x - ta) == (p.y - to):
                            print("non puoi oltrepassare le pedine con la regina")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                if counter_a == 0:
                    for p in self.board.pieces:
                        if p.x == ta and p.y == to and p.colour != self.colour:
                            counter += 1
                            self.board.pieces.remove(p)
                            self.x = a
                            self.y = o
                            break
                        elif p.x == ta and p.y == to and p.colour == self.colour:
                            counter += 1
                            print("non puoi spostare la regina su un altro tuo stesso pezzo")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                            break
                    if counter == 0:
                        self.x = ta
                        self.y = to
                        break

            else:
                print("la regina non si può muovere qui")
                ta = int(input("x : "))
                to = int(input("y : "))
        print()

class rook(piece):
    def __init__(self, x, y, colour, board, pi):
        super().__init__(x, y, colour, board, pi)

    def move(self, a, o):
        ta = a
        to = o
        print()
        while True:
            if self.x == ta and self.y == to:
                print("devi muovere la torre se selezionata")
                ta = int(input("x : "))
                to = int(input("y : "))
            elif ta > self.board.w or self.x < 1 or to > self.board.h or self.y < 1:
                print("i pezzi non possono essere mossi fuori dalla scacchiera")
                ta = int(input("x : "))
                to = int(input("y : "))

            elif self.x == ta and self.y != to:
                counter = 0
                counter_a = 0
                for p in self.board.pieces:
                    if p.x == self.x and to < self.y:
                        if to < p.y and p.y < self.y:
                            counter_a += 1
                            print("non puoi oltrepassare le pedine con la torre")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                            print("1")
                    elif p.x == self.x and to > self.y:
                        if to > p.y and p.y > self.y:
                            counter_a += 1
                            print("non puoi oltrepassare le pedine con la torre")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                            print("2")
                if counter_a == 0:
                    for p in self.board.pieces:
                        if p.x == ta and p.y == to and p.colour != self.colour:
                            counter += 1
                            self.board.pieces.remove(p)
                            self.x = a
                            self.y = o
                            break
                        elif p.x == ta and p.y == to and p.colour == self.colour:
                            counter += 1
                            print("non puoi spostare la torre su un altro tuo stesso pezzo")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                            break
                    if counter == 0:
                        self.x = ta
                        self.y = to
                        break
            elif self.x != ta and self.y == to:
                counter = 0
                counter_a = 0
                for p in self.board.pieces:
                    if p.y == self.y and ta < self.x:
                        if ta < p.x and p.x < self.x:
                            counter_a += 1
                            print("non puoi oltrepassare le pedine con la torre")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                    elif p.y == self.y and ta > self.x:
                        if ta > p.x and p.x > self.x:
                            counter_a += 1
                            print("non puoi oltrepassare le pedine con la torre")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                if counter_a == 0:
                    for p in self.board.pieces:
                        if p.x == ta and p.y == to and p.colour != self.colour:
                            counter += 1
                            self.board.pieces.remove(p)
                            self.x = a
                            self.y = o
                            break
                        elif p.x == ta and p.y == to and p.colour == self.colour:
                            counter += 1
                            print("non puoi spostare la torre su un altro tuo stesso pezzo")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                            break
                    if counter == 0:
                        self.x = ta
                        self.y = to
                        break

            else:
                print("la torre non si può muovere qui")
                ta = int(input("x : "))
                to = int(input("y : "))
        print()

class bishop(piece):
    def __init__(self, x, y, colour, board, pi):
        super().__init__(x, y, colour, board, pi)

    def move(self, a, o):
        ta = a
        to = o
        print()
        while True:
            if self.x == ta and self.y == to:
                print("devi muovere l'alfiere se selezionata")
                ta = int(input("x : "))
                to = int(input("y : "))
            elif ta > self.board.w or self.x < 1 or to > self.board.h or self.y < 1:
                print("i pezzi non possono essere mossi fuori dalla scacchiera")
                ta = int(input("x : "))
                to = int(input("y : "))

            elif (self.x - ta) == -(self.y - to):
                counter = 0
                counter_a = 0
                for p in self.board.pieces:
                    if ta < self.x:
                        if ta < p.x and p.x < self.x and (p.x - ta) == -(p.y - to):
                            print("non puoi oltrepassare le pedine con l'alfiere'")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                    elif ta > self.x:
                        if ta > p.x and p.x > self.x and (p.x - ta) == -(p.y - to):
                            print("non puoi oltrepassare le pedine con l'alfiere'")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                if counter_a == 0:
                    for p in self.board.pieces:
                        if p.x == ta and p.y == to and p.colour != self.colour:
                            counter += 1
                            self.board.pieces.remove(p)
                            self.x = a
                            self.y = o
                            break
                        elif p.x == ta and p.y == to and p.colour == self.colour:
                            counter += 1
                            print("non puoi spostare l'alfiere su un altro tuo stesso pezzo")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                            break
                    if counter == 0:
                        self.x = ta
                        self.y = to
                        break
            elif (self.x - ta) == (self.y - to):
                counter = 0
                counter_a = 0
                for p in self.board.pieces:
                    if ta < self.x:
                        if ta < p.x and p.x < self.x and (p.x - ta) == (p.y - to):
                            print("non puoi oltrepassare le pedine con l'alfiere")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                    elif ta > self.x:
                        if ta > p.x and p.x > self.x and (p.x - ta) == (p.y - to):
                            print("non puoi oltrepassare le pedine con l'alfiere")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                if counter_a == 0:
                    for p in self.board.pieces:
                        if p.x == ta and p.y == to and p.colour != self.colour:
                            counter += 1
                            self.board.pieces.remove(p)
                            self.x = a
                            self.y = o
                            break
                        elif p.x == ta and p.y == to and p.colour == self.colour:
                            counter += 1
                            print("non puoi spostare l'alfiere su un altro tuo stesso pezzo")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                            break
                    if counter == 0:
                        self.x = ta
                        self.y = to
                        break

            else:
                print("l'alfiere non si può muovere qui")
                ta = int(input("x : "))
                to = int(input("y : "))
        print()

class knight(piece):
    def __init__(self, x, y, colour, board, pi):
        super().__init__(x, y, colour, board, pi)

    def move(self, a, o):
        ta = a
        to = o
        print()
        while True:
            if self.x == ta and self.y == to:
                print("devi muovere il cavallo se selezionato")
                ta = int(input("x : "))
                to = int(input("y : "))
            elif ta > self.board.w or self.x < 1 or to > self.board.h or self.y < 1:
                print("i pezzi non possono essere mossi fuori dalla scacchiera")
                ta = int(input("x : "))
                to = int(input("y : "))

            elif ta == self.x + 2 and to == self.y + 1:
                counter = 0
                for p in self.board.pieces:
                    if p.x == ta and p.y == to and p.colour != self.colour:
                        counter += 1
                        self.board.pieces.remove(p)
                        self.x = a
                        self.y = o
                        break
                    elif p.x == ta and p.y == to and p.colour == self.colour:
                        counter += 1
                        print("non puoi spostare il cavallo su un altro tuo stesso pezzo")
                        ta = int(input("x : "))
                        to = int(input("y : "))
                        break
                if counter == 0:
                    self.x = ta
                    self.y = to
                    break
            elif ta == self.x + 2 and to == self.y - 1:
                counter = 0
                for p in self.board.pieces:
                    if p.x == ta and p.y == to and p.colour != self.colour:
                        counter += 1
                        self.board.pieces.remove(p)
                        self.x = a
                        self.y = o
                        break
                    elif p.x == ta and p.y == to and p.colour == self.colour:
                        counter += 1
                        print("non puoi spostare il cavallo su un altro tuo stesso pezzo")
                        ta = int(input("x : "))
                        to = int(input("y : "))
                        break
                if counter == 0:
                    self.x = ta
                    self.y = to
                    break
            elif ta == self.x - 2 and to == self.y + 1:
                counter = 0
                for p in self.board.pieces:
                    if p.x == ta and p.y == to and p.colour != self.colour:
                        counter += 1
                        self.board.pieces.remove(p)
                        self.x = a
                        self.y = o
                        break
                    elif p.x == ta and p.y == to and p.colour == self.colour:
                        counter += 1
                        print("non puoi spostare il cavallo su un altro tuo stesso pezzo")
                        ta = int(input("x : "))
                        to = int(input("y : "))
                        break
                if counter == 0:
                    self.x = ta
                    self.y = to
                    break
            elif ta == self.x - 2 and to == self.y -1:
                counter = 0
                for p in self.board.pieces:
                    if p.x == ta and p.y == to and p.colour != self.colour:
                        counter += 1
                        self.board.pieces.remove(p)
                        self.x = a
                        self.y = o
                        break
                    elif p.x == ta and p.y == to and p.colour == self.colour:
                        counter += 1
                        print("non puoi spostare il cavallo su un altro tuo stesso pezzo")
                        ta = int(input("x : "))
                        to = int(input("y : "))
                        break
                if counter == 0:
                    self.x = ta
                    self.y = to
                    break
            elif ta == self.x + 1 and to == self.y + 2:
                counter = 0
                for p in self.board.pieces:
                    if p.x == ta and p.y == to and p.colour != self.colour:
                        counter += 1
                        self.board.pieces.remove(p)
                        self.x = a
                        self.y = o
                        break
                    elif p.x == ta and p.y == to and p.colour == self.colour:
                        counter += 1
                        print("non puoi spostare il cavallo su un altro tuo stesso pezzo")
                        ta = int(input("x : "))
                        to = int(input("y : "))
                        break
                if counter == 0:
                    self.x = ta
                    self.y = to
                    break
            elif ta == self.x + 1 and to == self.y - 2:
                counter = 0
                for p in self.board.pieces:
                    if p.x == ta and p.y == to and p.colour != self.colour:
                        counter += 1
                        self.board.pieces.remove(p)
                        self.x = a
                        self.y = o
                        break
                    elif p.x == ta and p.y == to and p.colour == self.colour:
                        counter += 1
                        print("non puoi spostare il cavallo su un altro tuo stesso pezzo")
                        ta = int(input("x : "))
                        to = int(input("y : "))
                        break
                if counter == 0:
                    self.x = ta
                    self.y = to
                    break
            elif ta == self.x - 1 and to == self.y + 2:
                counter = 0
                for p in self.board.pieces:
                    if p.x == ta and p.y == to and p.colour != self.colour:
                        counter += 1
                        self.board.pieces.remove(p)
                        self.x = a
                        self.y = o
                        break
                    elif p.x == ta and p.y == to and p.colour == self.colour:
                        counter += 1
                        print("non puoi spostare il cavallo su un altro tuo stesso pezzo")
                        ta = int(input("x : "))
                        to = int(input("y : "))
                        break
                if counter == 0:
                    self.x = ta
                    self.y = to
                    break
            elif ta == self.x - 1 and to == self.y - 2:
                counter = 0
                for p in self.board.pieces:
                    if p.x == ta and p.y == to and p.colour != self.colour:
                        counter += 1
                        self.board.pieces.remove(p)
                        self.x = a
                        self.y = o
                        break
                    elif p.x == ta and p.y == to and p.colour == self.colour:
                        counter += 1
                        print("non puoi spostare il cavallo su un altro tuo stesso pezzo")
                        ta = int(input("x : "))
                        to = int(input("y : "))
                        break
                if counter == 0:
                    self.x = ta
                    self.y = to
                    break

            else:
                print("il cavallo non si può muovere qui")
                ta = int(input("x : "))
                to = int(input("y : "))
        print()

class pond(piece):
    def __init__(self, x, y, colour, board, pi):
        super().__init__(x, y, colour, board, pi)

    def move(self):
        ta = int(input("x : "))
        to = int(input("y : "))
        print()
        while True:
            if self.x == ta and self.y == to:
                print("devi muovere il pedone se selezionato")
                ta = int(input("x : "))
                to = int(input("y : "))
            elif ta > self.board.w or self.x < 1 or to > self.board.h or self.y < 1:
                print("i pezzi non possono essere mossi fuori dalla scacchiera")
                ta = int(input("x : "))
                to = int(input("y : "))
            elif self.colour == "w" and to >= self.y:
                print("non puoi mandare indietro i pedoni")
                ta = int(input("x : "))
                to = int(input("y : "))
                break
            elif self.colour == "b" and to <= self.y:
                print("non puoi mandare indietro i pedoni")
                ta = int(input("x : "))
                to = int(input("y : "))
                break
            elif self.colour == "w" and to < self.y:
                elif ta == self.x and self.y - 1 == to:
                    counter = 0
                    for p in self.board.pieces:
                        if p.x == ta and p.y == to:
                            counter += 1
                            print("non puoi mangiare in avanti col pedone")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                            break
                    if counter == 0:
                        self.x = ta
                        self.y = to
                        break
                elif self.x - 1 == ta and self.y - 1 == to:
                    counter = 0
                    for p in self.board.pieces:
                        if p.x == ta and p.y == to and p.colour != self.colour:
                            counter += 1
                            self.board.pieces.remove(p)
                            self.x = a
                            self.y = o
                            break
                        elif p.x == ta and p.y == to and p.colour == self.colour:
                            counter += 1
                            print("non puoi spostare il pedone su un altro tuo stesso pezzo")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                            break
                    if counter == 0:
                        self.x = ta
                        self.y = to
                        break
                elif self.x + 1 == ta and self.y - 1 == to:
                    counter = 0
                    for p in self.board.pieces:
                        if p.x == ta and p.y == to and p.colour != self.colour:
                            counter += 1
                            self.board.pieces.remove(p)
                            self.x = a
                            self.y = o
                            break
                        elif p.x == ta and p.y == to and p.colour == self.colour:
                            counter += 1
                            print("non puoi spostare il pedone su un altro tuo stesso pezzo")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                            break
                    if counter == 0:
                        self.x = ta
                        self.y = to
                        break

                else:
                    print("il pedone non si può muovere qui")
                    ta = int(input("x : "))
                    to = int(input("y : "))
                print()
            elif self.colour == "b" and to > self.y:
                elif ta == self.x and self.y + 1 == to:
                    counter = 0
                    for p in self.board.pieces:
                        if p.x == ta and p.y == to:
                            counter += 1
                            print("non puoi mangiare in avanti col pedone")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                            break
                    if counter == 0:
                        self.x = ta
                        self.y = to
                        break
                elif self.x - 1 == ta and self.y + 1 == to:
                    counter = 0
                    for p in self.board.pieces:
                        if p.x == ta and p.y == to and p.colour != self.colour:
                            counter += 1
                            self.board.pieces.remove(p)
                            self.x = a
                            self.y = o
                            break
                        elif p.x == ta and p.y == to and p.colour == self.colour:
                            counter += 1
                            print("non puoi spostare il pedone su un altro tuo stesso pezzo")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                            break
                    if counter == 0:
                        self.x = ta
                        self.y = to
                        break
                elif self.x + 1 == ta and self.y + 1 == to:
                    counter = 0
                    for p in self.board.pieces:
                        if p.x == ta and p.y == to and p.colour != self.colour:
                            counter += 1
                            self.board.pieces.remove(p)
                            self.x = a
                            self.y = o
                            break
                        elif p.x == ta and p.y == to and p.colour == self.colour:
                            counter += 1
                            print("non puoi spostare il pedone su un altro tuo stesso pezzo")
                            ta = int(input("x : "))
                            to = int(input("y : "))
                            break
                    if counter == 0:
                        self.x = ta
                        self.y = to
                        break

                else:
                    print("il pedone non si può muovere qui")
                    ta = int(input("x : "))
                    to = int(input("y : "))
                print()

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
print()


