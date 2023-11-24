from sys import stdin
import math
texts = stdin.read().splitlines()
nums = [*map(int,texts[1].split())]
execute, deputy= map(int,texts[2].split())

require = 0

for i in nums :
    if i - execute < 0 :
        require +=1
    else :
        require += math.ceil((i - execute)/deputy) +1

print(require)
