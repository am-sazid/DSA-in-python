
n = [12,34,1,2,2,4,2,1,25,6,5,7,8]
m = [2,3,5,1,4,11,67]

for num in m:
    count = 0
    for x in n:
        if x == num:
            count += 1

print(count)