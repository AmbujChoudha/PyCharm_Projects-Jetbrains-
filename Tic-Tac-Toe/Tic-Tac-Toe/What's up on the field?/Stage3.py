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

    def print_box(self):    # this part is for printing the box
        print("---------")
        for i in range(0, 9, 3):
            print('|', *self.cells[i:i + 3], '|')
        print('---------')

    def win_check(self):    # this part checks whether X wins or O or both
        self.result = 0
        self.win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                    [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

        for i in range(9):      # makes a list of positions of X
            if self.cells[i] == 'X':
                self.x_list.append(i)

            elif self.cells[i] == 'O':      # makes a list of positions of O
                self.o_list.append(i)

        for state in self.win:      # Checks if X wins
            if all(x in self.x_list for x in state):
                self.x_win += 1
                break
        for state in self.win:      # Checks if Y wins
            if all(x in self.o_list for x in state):
                self.o_win += 1
                break

        if self.x_win == 1 and self.o_win == 0:
            self.result = 1
        elif self.x_win == 0 and self.o_win == 1:
            self.result = 2
        elif self.x_win == 1 and self.o_win == 1:
            self.result = 3
        return self.result      # returns the result of the evaluation

    def impossible_state(self):     # checks whether impossible condition or not
        self.impossible = False
        if abs(self.cells.count('X') - self.cells.count('O')) > 1:
            self.impossible = True

        elif self.result == 3:
            self.impossible = True
        return self.impossible

    def print_result(self):        # prints the result as passed by 'win_check' method

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

    def tic_tac(self):         # uses all the previous methods to provide the soultion
        self.print_box()       # can be skipped by calling the methods individually
        self.win_check()
        self.impossible_state()
        self.print_result()


user_input = list(input('Enter cells: '))

my_game = TicTocToe(user_input)
my_game.tic_tac()
