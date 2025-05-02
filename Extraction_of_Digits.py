
n = 5873

num = n
resuilt = 0
while num > 0:
    digit = num % 10
    resuilt = (resuilt * 10) + digit
    num = num // 10
print(resuilt)

# n = 5873
# # convert to string
# n = str(n) # then Reverse the string
# n = n[::-1]
# print(n)
