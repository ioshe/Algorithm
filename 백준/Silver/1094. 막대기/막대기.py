x = int(input())
count = 0
for i in format(x, '07b') :
    count += int(i)
print(count)