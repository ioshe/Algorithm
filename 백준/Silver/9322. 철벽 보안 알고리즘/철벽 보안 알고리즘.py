# https://www.acmicpc.net/problem/9322

from sys import stdin

n = int(stdin.readline().strip())
result = []
for _ in range(n):
    word_len = int(stdin.readline().strip())
    words = [stdin.readline().split() for w in range(3)]
    original_index = {v:i for i,v in enumerate(words[0])}
    passwd_index = {original_index[v]:i for i,v in enumerate(words[1])}
    temp_result = []
    for j in range(word_len):
        temp_result.append(words[2][passwd_index[j]])
    result.append(' '.join(temp_result))

print('\n'.join(result))