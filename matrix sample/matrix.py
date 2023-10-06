x = [[4, 3, 5],
     [9, 5, 5],
     [8, 0, 1]]

for i in range(3):
    print(x[i])


y = [[3, 4, 9],
     [8, 6, 8],
     [5, 3, 1]]

print()

for i in range(3):
    print(y[i])

z = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

for i in range(3):
    for j in range(3):
        z[i][j] = x[i][j] + y[i][j]

print()

for i in range(3):
    print(z[i])


p = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

for i in range(3):
    for j in range(3):
        p[i][j] = x[i][j] - y[i][j]

print()

for i in range(3):
    print(p[i])
    