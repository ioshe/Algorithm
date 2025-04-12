from sys import stdin
print('\n'.join("yes" if 6 <= len(i.strip()) <= 9 else "no" for i in stdin.readlines()[1:]))
