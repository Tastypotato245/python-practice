x = int(input('width of triangle : '))
for i in range(0, x):
    for j in range(0, i + 1): 
        print('*', end='')
    print()

x = int(input('width of triangle : '))
for i in range(0, x):
    for k in range(0, x - 1 - i):
        print(' ', end='')
    for j in range(0, 2 * i + 1): 
        print('*', end='')
    print()

x = int(input('width of triangle : '))
for i in range(0, x):
    for k in range(0, x - 1 - i):
        print(' ', end='')
    for j in range(0, 2 * i + 1): 
        print('*', end='')
    print()
for i in range(x - 1, 0):
    for k in range(0, x - 1 - i):
        print(' ', end='')
    for j in range(0, 2 * i + 1): 
        print('*', end='')
    print()
