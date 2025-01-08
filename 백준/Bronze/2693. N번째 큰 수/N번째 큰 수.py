x = int(input())

for i in range(x):
  A = list(map(int, input().split()))
  A.sort()
  print(A[-3])