value = int(input('Please Enter a Number:'))
if value >= 3:
    rows = value
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end='')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end='')
    print("\r")
