# Chessboard pattern printing using nested loops

white = '\u25A1'  # white square
black = '\u25A0'  # black square

rows = 8
columns = 8

for row in range(rows):
    for col in range(columns):
        if (row + col) % 2 == 0:
            print(white, end=' ')
        else:
            print(black, end=' ')
    print()
