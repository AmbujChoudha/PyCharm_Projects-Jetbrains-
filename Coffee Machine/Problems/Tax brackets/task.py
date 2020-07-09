income = abs(int(input()))

if income <= 15527:
    tax = 0
elif income <= 42707:
    tax = 15
elif income <= 132406:
    tax = 25
else:
    tax = 28

total_tax = (tax / 100) * income

print(f'The tax for {income} is {tax}%. That is {round(total_tax)} dollars!')
