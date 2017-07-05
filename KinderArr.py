h = int(input('Enter N'))
h2 = 2 * h
for i in range(1, h2):
    print('Day', i)
    for j in range(0, 1):
        if(i != j):
            if i + 1 > 9 or j + 1 > 9 or i > 9 or j > 9:
                i = 0
                j = 0
        print(i, i + 1, j, j + 1)
