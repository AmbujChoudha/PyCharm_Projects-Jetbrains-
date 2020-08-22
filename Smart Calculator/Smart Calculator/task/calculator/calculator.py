import string
from collections import deque


def expression_conversion(user_exp, **stored_var):
    all_nums = '0123456789'
    numbers, exp_signs, negative = deque(), deque(), False
    cond_2 = False
    converted_expression = ''

    if not stored_var == dict():
        for i in stored_var:
            if i in user_exp:
                user_exp = user_exp.replace(i, str(stored_var[i]))

    if user_exp[-1] in '+-*/^':     # If an expression ends with signs i.e. +, -, *, /, ^
        print('Invalid Expression')
        return 0

    for n in range(len(user_exp)):
        if n != 0:
            if (user_exp[n-1] != '-' and negative) or (negative and exp_signs[-1] == '-' and '-' not in numbers[-1]):
                negative = False
        op = user_exp[n]
        if op == '-' and user_exp[n+1] in all_nums:   # For checking negative numbers at the start as well as in between
            negative = True
        if n == 0:          # For first term seperated just to deal with negative numbers
            if negative:
                numbers.append(op)
            elif op == '-' and user_exp[1] not in all_nums:
                print('Invalid Expression')
                return 0
            elif not negative and op not in all_nums:
                print('Invalid Expression')
                return 0
            else:
                numbers.append(op)

        elif op in all_nums:       # For numbers
            if user_exp[n-1] in all_nums or negative or user_exp[n-1] == '(':
                numbers[-1] += op
            else:
                numbers.append(op)

        elif op in '+-*/^':
            if not exp_signs:  # if there are no signs present
                exp_signs.append(op)
            elif op in '+-':        # For + and -
                if user_exp[n - 1] in '+-':
                    exp_signs[-1] += op
                elif user_exp[n-1] in all_nums or (user_exp[n-1] == ')'):
                    exp_signs.append(op)
                elif user_exp[n-1] == '(':
                    numbers[-1] += op
                else:
                    print('Invalid Expression')
                    return 0
            elif op in '*/^':       # For /, ^ and *
                if user_exp[n-1] not in '+-/*^' and user_exp[n + 1] not in '+-/*^':
                    exp_signs.append(op)
                else:
                    print('Invalid Expression')
                    return 0
        elif op in '()':            # For taking care of the parenthesis
            if op == '(':               # for dealing '566(-+ 98' type of errors
                if user_exp[n-1] in all_nums or ((user_exp[n+1] in '+-*/^') and (user_exp[n+2] not in all_nums)):
                    print('Invalid expression')
                    return 0
                if user_exp[n-1] == '(':
                    numbers[-1] += op
                else:
                    numbers.append('(')
            elif op == ')':
                cond_1 = user_exp[n-1] in '+-*/^'
                if n != len(user_exp) - 1:
                    cond_2 = user_exp[n+1] in all_nums  # for dealing '--+)98' type of errors

                if cond_1 or cond_2:
                    print('Invalid expression')
                    return 0
                if user_exp[n-1] == ')':
                    numbers[-1] += op
                else:
                    numbers[-1] += ')'

    for ind in range(len(exp_signs)):       # For changing '+++---+' to '-'
        sign = exp_signs[ind]
        if '+' in sign or '-' in sign:
            if sign.count('-') % 2 == 0:
                exp_signs[ind] = '+'
            else:
                exp_signs[ind] = '-'

    while len(exp_signs) > 0:
        converted_expression += numbers.popleft()
        converted_expression += exp_signs.popleft()
    converted_expression += numbers.popleft()
    return converted_expression


def brackets_ok(expression):
    a = 0
    for i in expression:
        if i == '(':
            a += 1
        elif i == ')':
            a -= 1
        if a < 0:
            return False
    return not bool(a)


def peek_stack(stack):
    if stack:
        return stack[-1]    # this will get the last element of stack
    else:
        return None


def generate_postfix(user_input, **cal_variables):
    priority_list = {'^': -1, '*': -2, '/': -3, '+': -4, '-': -4, '(': 0}
    negative_num = False
    higher_precedence = True
    stack_top = 0
    postfix = []
    sign_stack = deque()

    for index in range(len(user_input)):
        exp = user_input[index]
        if exp not in '()':
            stack_top = peek_stack(sign_stack)
        if exp in ('+', '-', '*', '/', '^') and len(sign_stack) != 0:
            higher_precedence = priority_list[exp] > priority_list[stack_top]

        if exp in cal_variables:  # for detecting any variables in the expression
            exp = cal_variables[exp]

        if index == 0:        # For checking the first incoming expression
            if exp == '-' and user_input[index + 1] in '0123456789':
                negative_num = True
                postfix.append(exp)
            else:
                postfix.append(exp)

        elif exp in '0123456789':  # for joining the digits of a number
            if user_input[index - 1] in '0123456789' or negative_num:  # if the last no. stored is a digit
                postfix[-1] += exp  # or if it is a -ve no. then add it to the number
            else:
                postfix.append(exp)  # 1 -- eles add operands as they arrive

        elif (not sign_stack) or (stack_top == '('):  # 2
            sign_stack.append(exp)

        elif exp == '(':        # 5
            sign_stack.append(exp)

        elif exp == ')':  # 6
            while peek_stack(sign_stack) != '(':
                postfix.append(sign_stack.pop())
            sign_stack.pop()  # For discarding left parenthesis
            continue  # For discarding right parenthsis

        else:
            if higher_precedence:  # 3
                sign_stack.append(exp)
            else:  # 4
                postfix.append(sign_stack.pop())
                sign_stack.append(exp)

    while len(sign_stack) > 0:  # 7 after the expression ends, emptying the stack
        postfix.append(sign_stack.pop())
    return postfix


class Calculator:
    def __init__(self):
        self.alpha = string.ascii_letters  # All alphabets lowercase and uppercase
        self.not_signs = '0123456789' + self.alpha + '_'  # alphabets needed for checking variables
        self.all_signs = ('-', '+', '*', '/', '^')  # signs in the calculator
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
            if '/' in self.userinput and self.userinput[0] == '/':  # For checking commands that start with '/'
                if '/exit' in self.userinput:
                    print('Bye!')
                    return 0
                elif '/help' in self.userinput:
                    print('''This program is like the day-to-day calculator with the ability to
                             to save variables. Additionally it can also handle brackets as
                             well as exponential calculations.
                             NOTE: The only thing remaining is to deal with the -ve numbers 
                                   in between the expression.''')
                else:
                    print('Unknown command')

            elif '=' in self.userinput:  # For checking assignments correct as well as incorrect
                if self.userinput.count('=') == 1:  # Only assignments with 1 '=' are analysed
                    if self.check_and_assign():
                        return 'assigned'
                else:
                    print('Invalid Assignment')

            elif all([k not in self.userinput for k in self.all_signs]):  # For checking variables or one positive no.
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
                if not brackets_ok(self.userinput):
                    print('Invalid expression')  # if brackets are not correct
                else:
                    self.userinput = expression_conversion(self.userinput, **self.variables)
                    if self.userinput:
                        return 'calculate'
        return 1

    def check_and_assign(self):
        left_side, right_side = self.userinput.split('=')  # split input from '=' into LHS and RHS

        if any([i in '0123456789' for i in left_side]):  # Checking the LHS
            print('Invalid Identifer')
            return 0
        else:
            if right_side.count('-') == 1 and right_side[0] == '-':  # for negative RHS
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
                        except ValueError:  # this where RHS containing letters and digits will get caught
                            print('Invalid Assignment')
                            return 0
                        else:
                            right_side = 0 - int(right_side)  # if okay and negative change sign with same value

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
                        except ValueError:  # input containing both letters and digits get caught
                            print('Invalid Assignment')
                            return 0
                        else:
                            right_side = int(right_side)
            self.store(left_side, right_side)  # If everything is right store the values in dictionary
            return 1

    def store(self, left, right):  # for storing correct assignments
        self.variables[left] = int(right)

    def calculate(self):        # only calculatable expression reach here!
        result = 0
        calculation_stack = deque()
        postfix_exp = generate_postfix(self.userinput, **self.variables)
        # print(postfix_exp, '*****************************line255')
        for i in postfix_exp:
            try:
                calculation_stack.append(int(i))

            except ValueError:
                b = calculation_stack.pop()
                a = calculation_stack.pop()
                if i == '+':
                    result = a + b
                elif i == '-':
                    result = a - b
                elif i == '*':
                    result = a * b
                elif i == '/':
                    result = int(a / b)
                elif i == '^':
                    result = a ** b
                calculation_stack.append(result)
        print(calculation_stack.pop())


my_calculator = Calculator()
while True:
    internal_status = my_calculator.run_calculator(input())
    if internal_status == 'exit':
        break
