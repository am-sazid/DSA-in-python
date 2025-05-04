

# n = 1234
# num = n
# result = 0
# while num > 0 :
#     ld = num % 10
#     result = (num * 10)+ld
#     num = num // 10

# print(result)


n = 1221
num= n
result=0
while num>0:
    ld = num%10
    result = (result * 10)+ld
    num=num//10

if result == n:
    print("Palindrome")
else:
    print("Not Palindrome")

# name = "sazid"
# n = name
# n = n[::-1]
# print(n)
# if n == name:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# print(1234 * 10)

# S = input()

# st = S

# st = st[::-1]

# if st == S:
# 	print("Palindrome")
# else:           
#     print("Not Palindrome")