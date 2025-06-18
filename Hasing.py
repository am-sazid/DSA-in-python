
n = [10,2,4,5,6,7,5,9,5,1,5,3]
m = [111,2,5,4,1,3,10]

hashlist = [0] * 11

for num in n:
    hashlist[num] += 1
for num in m:
    if num < 1 or num > 10:
        print(0)
    else:
        print(hashlist[num])

