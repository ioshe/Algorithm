# https://www.acmicpc.net/problem/1544

'''
5
picture
turepic
icturep
word
ordw
'''

from sys import stdin

n = int(stdin.readline())
texts = list(map(lambda a : a.strip(), stdin.readlines()))

queue = {}

for text in texts:
    change = False
    if not queue:
        queue[text] = 1
        continue
    
    for q in queue.keys():
        if text == q :
            change = True
            break
        for t in range(1,len(text)):
            if text[t:] + text[:t] == q:
                change = True
                break
    
    if not change:
        queue[text] = 1
        
        
# print(list(queue.keys()))
print(len(list(queue.keys())))
            
        

