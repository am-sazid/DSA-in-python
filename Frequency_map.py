
num = [2,3,3,1,5,2,3,2,5,6,7,8,9,0]

map = {}

for i in range(len(num)):
    if num[i] in map:
        map [num[i]] += 1
    else:
        map [num[i]] = 1
print(map[2])