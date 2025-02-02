# https://www.acmicpc.net/problem/1992

from sys import stdin
from collections import Counter
n = int(stdin.readline())
texts = list(map(lambda a : a.strip(),stdin.readlines()))

def quad(texts):
    
    result = Counter([text for flatting in texts for text in flatting])
    if len(result) >= 2 :
        half = len(texts) // 2
        quadrant_1 = quad([text[half:] for text in texts[:half]])
        quadrant_2 = quad([text[:half] for text in texts[:half]])
        quadrant_3 = quad([text[:half] for text in texts[half:]])
        quadrant_4 = quad([text[half:] for text in texts[half:]])

        return f"({quadrant_2}{quadrant_1}{quadrant_3}{quadrant_4})"
    else :
        return next(iter(result))
    
print(quad(texts))