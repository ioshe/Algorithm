from sys import stdin
texts =stdin.read().splitlines()
texts_3 = []
for te in texts[1:] :
    if len(te) == 3 :
        texts_3.append(te)
for i in range(2,-1,-1) :
    texts_3.sort(key= lambda j : j[i])

print(texts_3[0])