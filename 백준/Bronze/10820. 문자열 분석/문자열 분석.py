# https://www.acmicpc.net/problem/10820

from sys import stdin
import re

texts = map(lambda a : a.strip("\n"),stdin.readlines())

for text in texts :
    under_letters = len(re.findall("[a-z]",text))
    up_letters = len(re.findall("[A-Z]",text))
    numbers = len(re.findall("\d",text))
    blanks = len(re.findall("\s",text))
    print(under_letters, up_letters, numbers, blanks)