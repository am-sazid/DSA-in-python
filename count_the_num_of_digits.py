from math import*

def count_digts(num):
    return int(log10(num)+1)

n = count_digts(3235345464654645535345535464335)

print(n)













# def count_digits(n):

#     count = 0
#     while n > 0:
#         n = n // 10
#         count += 1
#     return count

# n = count_digits(2343225)
# print(n)


