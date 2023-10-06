import numpy as np


x = np.array([[4, 3, 5],
              [9, 5, 5],
              [8, 0, 1]])


y = np.array([[3, 4, 9],
              [8, 6, 8],
              [5, 3, 1]])


#print(x+y)

#changing sibgle value in numpy 
#x[2,1] = 200

#print(x)

i = int(input("input where value you want to change: "))

j = int(input("input where value you want to change: "))

z = int(input("input your new value: "))

x[i,j] = z

print(x)