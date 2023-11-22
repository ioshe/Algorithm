#https://www.acmicpc.net/problem/4358

from sys import stdin
text = sorted(stdin.read().splitlines())
length = len(text) 
dictionary = {}
for te in text :
    dictionary[te] = dictionary.get(te,0) +1 
result=[]
for key,value in dictionary.items() :
    result.append("{} {:.4f}".format(key,value/length*100,4))
    
print("\n".join(result))