from sys import stdin
import re 

n = int(stdin.readline())
texts = list(map(lambda a : a.strip(), stdin.readlines()))

boj_patten = re.compile(r"boj\.kr/\d*")


texts.sort(key=lambda a : (100+len(a) if boj_patten.search(a) else len(a), a))

print("\n".join(texts))



