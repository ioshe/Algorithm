# 햄버거 가격 입력
hamburger_prices = [int(input()) for _ in range(3)]

# 음료 가격 입력
drink_prices = [int(input()) for _ in range(2)]

# 모든 가능한 세트 메뉴 가격 계산
set_menu_prices = [hamburger + drink - 50 for hamburger in hamburger_prices for drink in drink_prices]

# 가장 저렴한 세트 메뉴 가격 출력
print(min(set_menu_prices))
