day_digit = int(input())

car_digits = list(map(int, input().split()))

violations = sum(1 for digit in car_digits if digit == day_digit)

print(violations)

