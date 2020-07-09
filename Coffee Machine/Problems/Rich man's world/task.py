money = int(input())
i = 7.1
year = 0

while money < 700000:
    money = money * (i / 100 + 1)
    year = year + 1

print(year)
