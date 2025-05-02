
# n = int(input("Enter a number: "))
# result = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         result.append(i)
# print(result)

# n = int(input("Enter a number: "))
# result = []
# for i in range(1, n //2 + 1):
#     if n % i == 0:
#         result.append(i)
# result.append(n)
# print(result)

from math import sqrt
from math import log

n = 36
result = []

for i in range(1, int(sqrt(n)) +1 ):
    if n % i == 0:
        result.append(i)
        if n // i != i:
            result.append(n // i)
result.sort()
print(result)