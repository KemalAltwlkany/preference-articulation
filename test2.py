import decimal as dec
import math as math

x = [1, 2, 3, 4, 5]
for i in range(len(x)):
    x[i] = x[i] + 100
print(x)


# x = [0, 1, 2]
# y = [(3, 3), (30, 30), (500, 500)]
#
# for i,j in zip(x, y):
#     print(i, j)

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(lst[-3:])
#
# print(1.1 + 2.2)
#
# dec.getcontext().prec = 28
# print(dec.Decimal(1)/dec.Decimal(7))
# x = dec.Decimal(-0.00001)
# print(x.is_signed())
# y = dec.Decimal(-0.000001)
# print(x-y)
# print((x-y).is_signed())
# print(x)
# print(dec.Decimal(3.14))
# print(dec.Decimal('0.1'))
# print(dec.Decimal('0.1')+dec.Decimal('0.2')+dec.Decimal(100000000.1))
# print(dec.Decimal(0.1)+dec.Decimal(0.2))
#
# print("----------------")
#
# print(dec.Decimal(math.sqrt(dec.Decimal('0.1'))))
# print(dec.Decimal(math.pow(dec.Decimal(0.1), 2)))