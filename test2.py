from Solution import *

x = Solution([1, 2, 3, 3.15555])
y = Solution([1, 2, 3, 3.155554])
z = Solution([1, 2, 3, 3.1551])
print(x == y)
print(x == z)
print(z == y)
