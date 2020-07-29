import string


def sign_change(sign_list):  # for changing '+++---' into '-'
    new_signs_list = []
    for sign in sign_list:
        if sign.count('-') % 2 == 0:
            new_signs_list.append('+')
        else:
            new_signs_list.append('-')
    return new_signs_list


class Calculator:
    def __init__(self):
        self.alpha = string.ascii_letters  # All alphabets lowercase and uppercase
        self.not_signs = '0123456789' + self.alpha + '_'  # alphabets needed for checking variables
        self.all_signs = ('-', '+')  # signs in the calculator
        self.userinput = None
        self.left_side, self.right_side = None, None
        self.status = None
        self.variables = dict()
        self.total = None

    def run_calculator(self, userinput):  # Main function in the class
        self.userinput = userinput.replace(' ', '')  # Removes extra spaces in the calculator
        status = self.input_checker()  # gets the status after checking input
        if not status:  # for dealing with 'exit' command given to the calculator
            return 'exit'
        if status != 'assigned':  # if assignment then there is no calculations
            if status == 'calculate':  # otherwise the calculation is done
                self.calculate()
        return 'continue'  # for keeping the calculator running

    def input_checker(self):
        if self.userinput:
            if '/' in self.userinput:  # For checking commands that start with '/'
                if '/exit' in self.userinput:
                    print('Bye!')
                    return 0
                elif '/help' in self.userinput:
                    print('The program calculates the sum and differences of numbers.')
                else:
                    print('Unknown command')

            elif '=' in self.userinput:  # For checking assignments correct as well as incorrect
                if self.userinput.count('=') == 1:  # Only assignments with 1 '=' are analysed
                    if self.check_and_assign():
                        return 'assigned'
                else:
                    print('Invalid Assignment')

            elif all([k not in self.userinput for k in self.all_signs]):  # For checking variables & one positive number
                if all([a in '0123456789' for a in self.userinput]):  # if all of the input has are digits
                    print(self.userinput)  # that means it's a number and then print
                else:
                    if self.userinput in self.variables:  # if the input are not all digits then
                        print(self.variables[self.userinput])  # check variables if in varaibles print
                    else:
                        print('Unknown variable')
                        # For checking negative nos. & variables same logic as above only added condition for
            elif self.userinput.count('-') == 1 and self.userinput[0] == '-':  # negative sign
                if all([b in '0123456789-' for b in self.userinput]):
                    print(self.userinput)
                else:
                    if self.userinput.strip('-') in self.variables:
                        print('-' + self.variables[self.userinput])
                    else:
                        print('Unknown variable')
            else:
                return 'calculate'
        return 1

    def check_and_assign(self):
        left_side, right_side = self.userinput.split('=')   # split input from '=' into LHS and RHS

        if any([i in '0123456789' for i in left_side]):  # Checking the LHS
            print('Invalid Identifer')
            return 0
        else:
            if right_side.count('-') == 1 and right_side[0] == '-':     # for negative RHS
                right_side = right_side.strip('-')
                if right_side in self.variables:  # if the right side in the variables
                    right_side = 0 - self.variables[right_side]
                else:
                    if all([x in self.alpha for x in right_side]):  # if RHS not in variables but contains only letters
                        print('Unknown variable')
                        return 0
                    else:
                        try:
                            int(right_side)
                        except ValueError:              # this where RHS containing letters and digits will get caught
                            print('Invalid Assignment')
                            return 0
                        else:
                            right_side = 0 - int(right_side)          # if okay and negative change sign with same value

            else:
                if right_side in self.variables:  # if the right side in the variables
                    right_side = self.variables[right_side]
                else:  # if right side not in variables
                    if all([x in self.alpha for x in right_side]):  # if there are no digits
                        print('Unknown variable')
                        return 0
                    else:  # if there are digits
                        try:
                            int(right_side)  # if a valid digit is found
                        except ValueError:   # input containing both letters and digits get caught
                            print('Invalid Assignment')
                            return 0
                        else:
                            right_side = int(right_side)
            self.store(left_side, right_side)   # If everything is right store the values in dictionary
            return 1

    def store(self, left, right):           # for storing correct assignments
        self.variables[left] = int(right)
        # print(self.variables.items())

    @property
    def segregate(self):
        self.nums, self.signs = [], []
        negative_start = False
        switch = []
        for i in range(0, len(self.userinput) - 1):  # for checking switching between signs and digits/variables
            condition1 = self.userinput[i] in self.all_signs and self.userinput[i + 1] in self.not_signs
            condition2 = self.userinput[i + 1] in self.all_signs and self.userinput[i] in self.not_signs
            if condition1 or condition2:
                switch.append(i + 1)

        if self.userinput[-1] in self.all_signs:  # For expressions ending with signs rather than digits
            print('Invalid expression')
            return False

        if self.userinput[0] in self.all_signs:  # for expressions not starting with signs instead of digits
            if self.userinput[:switch[0]] != '-':
                print('Invalid expression')
                return False
            else:
                negative_start = True
                self.nums.append(self.userinput[:switch[1]])
                for x in range(1, len(switch) - 1):
                    if x % 2 == 0:
                        self.nums.append(self.userinput[switch[x]:switch[x + 1]])
                    else:
                        self.signs.append(self.userinput[switch[x]:switch[x + 1]])

        else:
            self.nums.append(self.userinput[:switch[0]])  # this is for intial numbers before the first switch
            for x in range(0, len(switch) - 1):
                if x % 2 != 0:
                    self.nums.append(self.userinput[switch[x]:switch[x + 1]])
                else:
                    self.signs.append(self.userinput[switch[x]:switch[x + 1]])

        self.nums.append(self.userinput[switch[-1]:])  # this is for last numbers after the last switch
        if negative_start:
            if self.nums[0].strip('-') in self.variables:
                self.nums[0] = self.variables[self.nums[0].strip('-')]

        self.nums = [self.variables[j] if j in self.variables else int(j) for j in self.nums]

        if negative_start:
            self.nums[0] = 0 - self.nums[0]
        self.signs = sign_change(self.signs)
        return True

    def calculate(self):
        try:
            if not self.segregate:
                return None

        except ValueError:  # this is where invalid numbers like '-685++' will get caught
            print('Invalid expression')
        except IndexError:  # when only signs are typed or when there is only single integer
            print('Invalid expression')  # one of the list will remain empty 'new_signs' or 'nums'
        else:
            self.total = self.nums[0]
            for p in range(len(self.signs)):
                if self.signs[p] == '+':
                    self.total = self.total + self.nums[p + 1]

                elif self.signs[p] == '-':
                    self.total = self.total - self.nums[p + 1]
            print(self.total)


my_calculator = Calculator()
while True:
    internal_status = my_calculator.run_calculator(input())
    if internal_status == 'exit':
        break
