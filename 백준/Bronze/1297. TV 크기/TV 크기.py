# https://www.acmicpc.net/problem/1297
import math

D,H,W = map(int,input().split())


# 대각선 길이
diagonal_length = D

# 비율
ratio_height = H
ratio_width = W

# x 값 계산
x_square = diagonal_length**2 / (ratio_height**2 + ratio_width**2)
x = math.sqrt(x_square)

# 높이와 너비 계산
height = ratio_height * x
width = ratio_width * x

print(int(height),int(width))
