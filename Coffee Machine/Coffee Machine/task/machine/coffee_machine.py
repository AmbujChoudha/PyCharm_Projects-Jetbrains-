from typing import Dict


class CoffeeMachine:
    stop = False
    state = {'water': 400, 'milk': 540, 'coffee beans': 120, 'disposable cups': 9, 'money': 550}

    def __init__(self):
        self.stop = CoffeeMachine.stop
        self.state = CoffeeMachine.state
        self.user_input = None

    def take_input(self, user_input):
        self.user_input = user_input

    def keep_running(self):
        print("\nWrite action (buy, fill, take, remaining, exit): ")
        self.take_input(input())
        self.machine_start()

    def machine_start(self):
        if self.user_input == "buy":
            CoffeeMachine.buy(self)
        elif self.user_input == "fill":
            CoffeeMachine.fill(self)
        elif self.user_input == 'take':
            CoffeeMachine.take(self)
        elif self.user_input == 'remaining':
            CoffeeMachine.status(self)
        elif self.user_input == 'exit':
            CoffeeMachine.exit_func(self)

    def buy(self):
        order = 0  # The code doesn't run unless 'order' is defined (needed in line 23, 26)
        enough = False

        espresso = {"water": 250, "milk": 0, "coffee beans": 16, "money": 4}
        latte = {"water": 350, "milk": 75, "coffee beans": 20, "money": 7}
        cappuccino = {"water": 200, "milk": 100, "coffee beans": 12, "money": 6}

        coffee_type = [espresso, latte, cappuccino]  # All the dictionaries made into list

        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        self.take_input(input())

        if self.user_input == 'back':  # This is for the 'back' option which is to be provided
            self.keep_running()
        else:
            order = int(self.user_input)

        # For changing the number into name of the coffee as defined in the list coffee_type
        coffee_wanted = coffee_type[order - 1]

        for i in coffee_wanted:  # This function is to check whether coffee has material or not
            if i == 'money':  # The money in the coffee machine need not to be checked
                continue
            else:
                if self.state[i] < coffee_wanted[i]:  # if not enough then the function stops
                    print("Sorry, not enough " + i + "!")
                    break
                else:
                    enough = True

        if enough:  # displays the required message
            print("I have enough resources, making you a coffee!")
            for i in coffee_wanted:  # changing the state of the coffee machine depending on the type of coffee ordered
                if i != "money":
                    self.state[i] = self.state[i] - coffee_wanted[i]
                else:
                    self.state[i] = self.state[i] + coffee_wanted[i]

            self.state["disposable cups"] -= 1

    def fill(self):
        print('Write how many ml of water do you want to add:')
        self.take_input(input())
        add_water = int(self.user_input)

        print('Write how many ml of milk do you want to add:')
        self.take_input(input())
        add_milk = int(self.user_input)

        print('Write how many grams of coffee beans do you want to add:')
        self.take_input(input())
        add_coffee = int(self.user_input)

        print('Write how many disposable cups of coffee do you want to add:')
        self.take_input(input())
        add_cups = int(self.user_input)

        refill = {'water': add_water, 'milk': add_milk, 'coffee beans': add_coffee}

        for i in refill:
            self.state[i] = self.state[i] + refill[i]

        self.state['disposable cups'] = self.state['disposable cups'] + add_cups

    def take(self):
        print('I gave you $' + str(self.state['money']))
        self.state['money'] = 0

    def status(self):
        print("The coffee machine has:")

        for parameter in self.state:
            print(self.state[parameter], "of", parameter)

    def exit_func(self):
        self.stop = True  # Stops the loop of function - coffee_machine


my_coffee_machine = CoffeeMachine()

while not my_coffee_machine.stop:
    my_coffee_machine.keep_running()
