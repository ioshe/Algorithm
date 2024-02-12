import sys
input = sys.stdin.readline
height = []
max = 9
for _ in range(max) :
    height.append(int(input().rstrip()))

height = sorted(height)
total_height = sum(height) 
end = False

for i in range(0,max) :
    if end :
        break
    for j in range(i+1,max) :
        if total_height - height[i] -height[j] == 100 :
            for k in range(0,max):
                if k != i and k != j :
                    print(height[k])
                    end = True          
            break
