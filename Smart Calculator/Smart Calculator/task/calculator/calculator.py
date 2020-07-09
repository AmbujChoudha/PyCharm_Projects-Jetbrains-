def add(numbers):
    total = sum(numbers)
    return total


while True:
    user_input = input().split()
    length = len(user_input)

    if '/exit' in user_input:
        print('Bye!')
        break
    elif length == 2:
        num = [int(x) for x in user_input]
        print(add(num))
    elif length == 1:
        print(*user_input)
    elif length == 0:
        continue
