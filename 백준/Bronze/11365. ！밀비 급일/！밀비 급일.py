from sys import stdin

texts = stdin.readlines()

for text in texts[:-1] :
    print(text.strip()[::-1])