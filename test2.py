import numpy as np

def bk1():
    return 3,4,5

objectives = bk1()

for i in objectives:
    print(i)

print(objectives[1])

objectives = list(objectives)
objectives[1] = 17

x = 40
y = 50
lst = [x, y]
print(type(lst))
print(lst)
print(objectives)

lst = [[5, 7], [5, 8], [5, 9]]

print(lst)
lst.remove([5,7])
print(lst)
