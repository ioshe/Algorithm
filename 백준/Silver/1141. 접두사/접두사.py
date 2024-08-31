# https://www.acmicpc.net/problem/1141

from sys import stdin

def is_in_dict(text,dictionary) :
    for di in dictionary :
        if text == di[:len(text)] :
            return di
    return False

N = int(stdin.readline())
texts = list(map(lambda a: a.strip(),stdin.readlines()))
texts.sort(key=lambda a : -len(a))
dictionary = {}
for text in texts :
    temp = is_in_dict(text,dictionary)
    if not dictionary :
        dictionary[text] = []
    elif temp :
        dictionary[temp].append(text)
    else :
        dictionary[text] = []        

print(len(dictionary))