N = int(input())
drinks = list(map(int, input().split()))

drinks.sort()
result = drinks[-1] + sum(x / 2 for x in drinks[:-1])
print(result)
