def prime_num(num):
    prime = [2]

    for i in range(3, num):
        flag = True
        for j in prime:
            if i % j == 0:
                flag = False
                break
        if flag:
            prime.append(i)

    for i in prime:
        if num % i == 0:
            print('This number is not prime')
            break
    else:
        print('This number is prime')


number = int(input())

if number == 1 or number == 2:
    print('This number is not prime')
else:
    prime_num(number)
