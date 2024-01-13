

import math
from sys import stdin
result = {}
lines = stdin.read().splitlines()[1:]  
int_values = [int(line) for line in lines]  
for i in sorted(int_values) :
    result[i] = result.get(i,0)+1
max = float('-inf')
index = ''
#print(result)
for i in result :
    #print(i,result[i])
    if result[i] > max :
        max = result[i]
        index = i

print(int(index))

