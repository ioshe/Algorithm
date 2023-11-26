from sys import stdin
colors = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white':9}
texts = stdin.read().splitlines()
print((colors[texts[0]]*10+colors[texts[1]])*(10**colors[texts[2]]))


