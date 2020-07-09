word = list(input().strip())
flag = False

for i in range(len(word)// 2):
    if word[i] == word[-i-1]:
        flag = True
    else:
        flag = False
        print("Not palindrome")
        break
if flag:
    print("Palindrome")
