def count_carries(a, b):
    carry = 0
    carry_count = 0
    max_length = max(len(a), len(b))
    
    for i in range(max_length):
        digit_a = int(a[i]) if i < len(a) else 0
        digit_b = int(b[i]) if i < len(b) else 0
        sum_digits = digit_a + digit_b + carry
        
        if sum_digits >= 10:
            carry = 1
            carry_count += 1
        else:
            carry = 0
            
    return carry_count

import sys
input = sys.stdin.read
data = input().strip().split('\n')

for line in data:
    if line == "0 0":
        break
    a, b = line.split()
    result = count_carries(a[::-1], b[::-1])
    print(result)
