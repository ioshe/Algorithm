import sys
input = sys.stdin.readline
climb, slipped,target = map(int,input().rstrip().split())
divid = climb-slipped

if target%divid>slipped:
    print(target//divid-(slipped//divid)+1)
else:
    print(target//divid-(slipped//divid))