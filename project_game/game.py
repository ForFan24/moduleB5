def greet():
    print("-------------------------")
    print("Сыграем в крестики-нолики")
    print("-------------------------")
    print("    Формат ввода: x,y    ")
    print("    x - номер строки     ")
    print("    y - номер столбца    ")
    print("-------------------------")


greet()

board = [[" ", " ", " "] for i in range(3)]


def draw_board():
    print()
    print("   | 0 | 1 | 2 |   ")
    print("----------------")
    for i, row in enumerate(board):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print("----------------")
    print()


draw_board()

def ask():
    while True:
        cords = input("Введите координаты клетки: ").split()
        if len(cords) != 2:
            print("Введите две координаты")
            continue
        x, y = cords
        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа!")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапазона!")
            continue
        if board[x][y] != " ":
            print("Клетка занята")
            continue
        return x, y


ask()