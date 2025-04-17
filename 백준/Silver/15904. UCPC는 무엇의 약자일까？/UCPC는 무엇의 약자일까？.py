# https://www.acmicpc.net/problem/15904

text = input()

asssemble = ['U', 'C', 'P', 'C']
count = 0

for i in range(len(text)):
    if text[i] == asssemble[count]:
        count += 1
    if count == 4:
        break

if count == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")