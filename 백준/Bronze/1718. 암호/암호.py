# https://www.acmicpc.net/problem/1718

normal = input()
key = input()

result = []
for index,n in enumerate(normal) : 
    if n == " " :
        result.append(" ") 
        continue
    temp = (ord(n) - ord(key[index % len(key)]) - 1) % 26
    result.append(chr(temp+97))
print("".join(result))