
#https://www.acmicpc.net/problem/20920

'''
7 4
apple
ant
sand
apple
append
sand
sand

'''


from sys import stdin

N,M = map(int,stdin.readline().split())
texts = {}
for text in map(lambda a: a.strip(), stdin.readlines()) :
    if len(text) < M :
        continue
    if text in texts : 
        texts[text] += 1
    else :
        texts[text] = 1

sorted_words = sorted(texts.keys(), key=lambda word: (-texts[word], -len(word), word))

print("\n".join(map(str,sorted_words)))