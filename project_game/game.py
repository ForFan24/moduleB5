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
count = 0


def draw_board():
    print()
    print("   | 0 | 1 | 2 |   ")
    print("----------------")
    for i, row in enumerate(board):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print("----------------")
    print()


def ask():
    while True:
        cords = input("Введите координаты клетки через пробел: ").split()
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

def win():
    win_cords = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                 ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cords:
        symbols = []
        for c in cord:
            symbols.append(board[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл первый игрок!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл второй игрок!")
            return True
    return False


while True:
    count += 1
    draw_board()
    if count % 2 == 1:
        print("Ходит первый игрок")
    else:
        print("Ходит второй игрок")
    x, y = ask()
    if count % 2 == 1:
        board[x][y] = "X"
    else:
        board[x][y] = "0"
    if win():
        break
    if count == 9:
        break
        print("Ничья!")

