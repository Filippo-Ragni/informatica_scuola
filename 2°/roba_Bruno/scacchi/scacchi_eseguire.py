from scacchi_classi import *

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
print("le cordinate sia delle ascisse che delle ordinate vanno da 1 a 8 partendo:")
print("per le ascisse da sinistra a destra")
print("per le ordinate dall'alto al basso")
print()
print("parte il bianco si selezionano le cordinate della pedina che si vuole muovere")
print("si continua finchè non saranno inserite delle cordinate valide poi tocca all'altro")
print()

while wk in c_board.pieces and bk in c_board.pieces:
    if wk not in c_board.pieces:
        print("ha vinto il nero!")
        break
    elif bk not in c_board.pieces:
        print("ha vinto il bianco!")
        break
    else:
        c_x = int(input("x : "))
        c_y = int(input("y : "))
        for piec in c_board.pieces:
            if piec.x == c_x and piec.y == c_y:
                piec.move()
        c_board.draw()
        print()
