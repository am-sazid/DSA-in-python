n = 123
num = n
res = len(str(num))
total = 0


while num > 0:
    ld = num % 10
    total += ld ** res
    num = num // 10

print(total)
if total == n:
    print("Armstrong")
else:
    print("Not Armstrong")


