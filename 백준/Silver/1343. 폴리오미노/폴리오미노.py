# https://www.acmicpc.net/problem/1343

texts = input().split(".")
for text in texts :
    if len(text) % 2 == 1 :
        print(-1)
        exit(0)

result = []
for text in texts :
    temp = ""
    temp += "AAAA" * (len(text) // 4) + "BB" * (len(text) % 4 // 2)
    result.append(temp)

print(".".join(result))


