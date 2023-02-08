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