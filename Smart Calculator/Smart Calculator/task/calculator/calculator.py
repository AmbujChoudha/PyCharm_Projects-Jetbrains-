def sign_change(sign_list):     # for changing '+++---' into '-'
    new_signs_list = []
    for sign in sign_list:
        if sign.count('-') % 2 == 0:
            new_signs_list.append('+')
        else:
            new_signs_list.append('-')
    return new_signs_list


def segregate(sequence):    # sequence is numbers as well as the signs which are present in between
    signs, numbers = [], []     # empty lists for storing segregated output
    for i in sequence:      # for every element in the sequence
        if all(s in ('+', '-') for s in i):     # for checking every element against '+' or '-'
            signs.append(i)
        else:
            numbers.append(i)   # '-7' or '+7' will get stored in numbers even '-+-56++' will get stored

    changed_signs = sign_change(signs)
    numbers = [int(x) for x in numbers]  # this step will cause error for all the invalid enteries
                                        # filtering them out in the process
    return changed_signs, numbers


while True:
    user_input = input()            # note that here input is not converted into a list

    if '/' in user_input:           # here the input is checked as a string
        if '/exit' in user_input:
            print('Bye!')
            break
        elif '/help' in user_input:
            print('The program calculates the sum of numbers.')
            continue
        else:
            print('Unknown command')

    elif not user_input:
        continue

    try:
        new_signs, nums = segregate(user_input.split())    # only during segregation input is passed as a list
        total = nums[0]
    except ValueError:      # this is where invalid numbers like '-685++' will get caught
        print('Invalid expression')
    except IndexError:      # when only signs are typed or when there is only single integer
        print('Invalid expression')  # one of the list will remain empty 'new_signs' or 'nums'
    else:
        for p in range(len(new_signs)):
            if new_signs[p] == '+':
                total = total + nums[p + 1]

            elif new_signs[p] == '-':
                total = total - nums[p + 1]
        print(total)
