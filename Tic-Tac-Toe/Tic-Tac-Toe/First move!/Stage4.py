class TicTocToe:
    def __init__(self, cells):
        self.x_list = []
        self.o_list = []
        self.x_win = 0
        self.o_win = 0
        self.cells = cells
        self.impossible = None
        self.result = None
        self.win = None
        self.move = None
        self.move_cell = None
        self.cell_to_check = None
        self.legal_move = None
        self.new_move = None

    def print_box(self):
        print("---------")  # this part is for printing the box
        for i in range(0, 9, 3):
            print('|', *self.cells[i:i + 3], '|')
        print('---------')

    def move_transform(self, move):
        self.move = move
        self.move_cell = 8 + self.move[0] - 3 * self.move[1]

        return self.move_cell

    def empty_cells(self, cell_to_check):
        self.cell_to_check = cell_to_check
        if self.cells[self.cell_to_check] == '_':
            return True
        else:
            return False

    def play_move(self, legal_move):
        self.legal_move = legal_move

        self.new_move = self.move_transform(self.legal_move)

        self.cells[self.new_move] = 'X'

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
        elif self.x_win == 1 and self.o_win == 1:
            self.result = 3
        return self.result

    def impossible_state(self):
        self.impossible = False
        if abs(self.cells.count('X') - self.cells.count('O')) > 1:
            self.impossible = True

        elif self.result == 3:
            self.impossible = True
        return self.impossible

    def print_result(self):

        if self.impossible:
            print('Impossible')
        elif self.result == 1:
            print('X wins')
        elif self.result == 2:
            print('O wins')
        else:
            if self.cells.count('_') == 0:
                print('Draw')
            else:
                print('Game not finished')


user_input = list((input('Enter cells: ')))
my_game = TicTocToe(user_input)

my_game.print_box()
value = None

while True:
    try:
        input_move = [int(x) for x in input('Enter the coordinates: ').split()]
        if input_move[0] in range(1, 4) and input_move[0] in range(1, 4):
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
