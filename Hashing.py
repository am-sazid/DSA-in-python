
n = [12,34,1,2,2,4,2,1,25,6,5,7,8]
m = [2,3,5,1,4,11,67]

for num in m:
    count = 0
    for x in n:
        if x == num:
            count += 1

print(count)


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
# Using a dictionary for hashing
hash_dict = {}
for num in n:
    if num in hash_dict:
        hash_dict[num] += 1
    else:
        hash_dict[num] = 1
for num in m:
    if num in hash_dict:
        print(hash_dict[num])
    else:
        print(0)