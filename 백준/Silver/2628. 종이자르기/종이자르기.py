from sys import stdin

w,h = map(int,stdin.readline().split())
n = int(stdin.readline())
widths = []
heights = []

for i in range(n):
    command, length = map(int,stdin.readline().split())
    if command == 0:
        heights.append(length) # 가로로 자르면 세로가 2개 생김
        continue
    if command == 1:
        widths.append(length)    
        continue

widths.append(w)    
heights.append(h)    

widths.sort()
heights.sort()

widths_max = widths[0]
heights_max = heights[0]

# print(widths)
# print(heights)

for i in range(1,len(widths)):
    widths_max = max(widths[i] - widths[i-1], widths_max)
for i in range(1,len(heights)):
    heights_max = max(heights[i] - heights[i-1], heights_max)

print(widths_max*heights_max)