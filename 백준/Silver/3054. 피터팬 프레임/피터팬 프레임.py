
text = input().strip()

result = [" " for i in range(5)]

for i in range(len(text)):
    symbol = "#"
    if (i+1) % 3 == 0 :
        symbol = "*"
    fisrt_line = ".."+symbol+".."
    second_line = "."+symbol+"."+symbol+"."
    result[0] = result[0][:-1] + fisrt_line
    result[1] = result[1][:-1] + second_line
    result[2] = result[2][:-1] + ".".join([symbol,text[i],symbol]) if result[2][-1] != "*" else result[2] + "."+text[i]+"."+symbol
    result[3] = result[3][:-1] + second_line
    result[4] = result[4][:-1] + fisrt_line
# print(result)
print("\n".join("".join(a) for a in result))