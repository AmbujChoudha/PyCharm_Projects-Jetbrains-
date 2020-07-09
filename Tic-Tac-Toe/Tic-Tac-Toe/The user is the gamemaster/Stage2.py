# prints the X-O box 

l = list(input())
print("---------")
for i in range(0, 9, 3):
    print('|', *l[i:i + 3], '|')
print('---------')



# Another way to do it!
# Method 2:

'''
cells = input()
field = """
---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------
""".format(*cells)

print(field)

'''
