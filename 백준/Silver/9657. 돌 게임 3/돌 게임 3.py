#https://www.acmicpc.net/problem/9657
game =[1,0,1,1] 
for i in range(4,10001) :
	if game[i-1] and game[i-3] and game[i-4]:
		game.append(0)
	else :
		game.append(1)

print("SK" if game[int(input())-1] == 1 else "CY")