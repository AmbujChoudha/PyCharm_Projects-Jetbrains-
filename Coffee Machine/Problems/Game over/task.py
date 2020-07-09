scores = input().split()
lives, count = 3, 0
for i in scores:
    if i == "I":
        lives -= 1
        if lives == 0:
            print('Game over')
            break
    else:
        count += 1
if lives != 0:
    print('You won')
print(count)
