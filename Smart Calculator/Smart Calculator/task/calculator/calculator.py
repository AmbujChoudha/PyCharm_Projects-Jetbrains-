def sign_change(sign_list):
    new_signs_list = []
    for sign in sign_list:
        if sign.count('-') % 2 == 0:
            new_signs_list.append('+')
        else:
            new_signs_list.append('-')
    return new_signs_list


def segregate(sequence):
    signs, numbers = [], []
    for i in sequence:
        if '+' in i or '-' in i:
            if i.count('-') == 1 and i.count('+') == 0 and len(i) > 1:
                numbers.append(i)
            else:
                signs.append(i)
        else:
            numbers.append(i)

    changed_signs = sign_change(signs)
    numbers = [int(x) for x in numbers]
    return changed_signs, numbers


while True:
    user_input = input().split()

    if '/exit' in user_input:
        print('Bye!')
        break
    elif '/help' in user_input:
        print('The program calculates the sum of numbers')
        continue
    elif not user_input:
        continue

    new_signs, nums = segregate(user_input)
    total = nums[0]

    for p in range(len(new_signs)):

        if new_signs[p] == '+':
            total = total + nums[p + 1]

        elif new_signs[p] == '-':
            total = total - nums[p + 1]
    print(total)


