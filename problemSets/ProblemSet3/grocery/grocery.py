import string
items = dict()

while True:
    try:
        grocery = input().strip().upper()
        if grocery in items:
            items[grocery] = items[grocery] + 1
        else:
            items[grocery] = 1
    except EOFError:
        break

for alpha in string.ascii_uppercase:
    for grocery in items:
        if grocery.startswith(alpha):
            print(items[grocery], grocery)

