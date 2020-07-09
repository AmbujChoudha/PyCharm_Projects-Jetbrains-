class TicTocToe:
    def __init__(self, cells=None):
        self.x_list = []
        self.o_list = []
        self.x_win = 0
        self.o_win = 0
        self.cells = [' ', ' ', ' ',
                      ' ', ' ', ' ',
                      ' ', ' ', ' ']
        self.result = None
        self.win = None
        self.move = None
        self.move_cell = None
        self.cell_to_check = None
        self.legal_move = None
        self.legal_cell = None
        self.move_counter = 1
        self.mark = None
        self.game_over = False

    def print_box(self):
        x = 0
        print("---------")
        for i in range(3):
            print('|', end=' ')
            for j in range(3):
                if self.cells is None:
                    print(' ', end=' ')
                else:
                    print(self.cells[x], end=' ')
                x += 1
            print('|')
        print('---------')

    def move_transform(self, move):
        self.move = move
        self.move_cell = 8 + self.move[0] - 3 * self.move[1]

        return self.move_cell

    def empty_cells(self, cell_to_check):
        self.cell_to_check = cell_to_check

        if self.cells[self.cell_to_check] == ' ':
            return True
        else:
            return False

    def play_move(self, legal_move):
        self.legal_move = legal_move
        self.legal_cell = self.move_transform(self.legal_move)

        if self.move_counter % 2 == 0:
            self.mark = 'O'
            self.move_counter += 1
        else:
            self.mark = 'X'
            self.move_counter += 1
        self.cells[self.legal_cell] = self.mark

    def win_check(self):
        self.result = 0
        self.win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                    [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

        for i in range(9):
            if self.cells[i] == 'X':
                self.x_list.append(i)

            elif self.cells[i] == 'O':
                self.o_list.append(i)

        for state in self.win:
            if all(x in self.x_list for x in state):
                self.x_win += 1
                break
        for state in self.win:
            if all(x in self.o_list for x in state):
                self.o_win += 1
                break

        if self.x_win == 1 and self.o_win == 0:
            self.result = 1
        elif self.x_win == 0 and self.o_win == 1:
            self.result = 2
        return self.result

    def print_result(self):
        if self.result == 1:
            print('X wins')
            self.game_over = True
        elif self.result == 2:
            print('O wins')
            self.game_over = True
        elif ' ' not in self.cells:
            print('Draw')
            self.game_over = True


my_game = TicTocToe()
my_game.print_box()

while not my_game.game_over:
    value = None
    while True:
        try:
            input_move = [int(x) for x in input('Enter the coordinates: ').split()]
            if input_move[0] in range(1, 4) and input_move[1] in range(1, 4):
                coordinate = my_game.move_transform(input_move)

                if not my_game.empty_cells(coordinate):
                    print('This cell is occupied! Choose another one!')
                else:
                    value = input_move
                    break
            else:
                print('Coordinates should be from 1 to 3!')
                continue

        except IndexError:
            print('Coordinates should be from 1 to 3!')
            continue
        except TypeError:
            print('You should enter numbers!')
            continue

    my_game.play_move(value)
    my_game.print_box()
    my_game.win_check()
    my_game.print_result()

