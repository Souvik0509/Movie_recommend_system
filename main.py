lst = [1,2,3,4,5,6]
inpt = range(3,6+1)
tot_sum = 0

for i in inpt:
    if i in lst:
        tot_sum+=i

print(tot_sum)
