# https://www.acmicpc.net/problem/1543
text = input()
target = input()

limit = len(text)
find_len = len(target)
i = count = 0

while i< limit :
    if text[i:i+find_len] == target :
        count += 1
        i +=find_len
        continue
    i+=1
print(count)