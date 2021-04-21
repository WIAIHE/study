a = int(input("请输入所要相加的数字："))
b = int(input("请输入相加的次数："))
s = a
ans = a
for i in range(1, b):
    s = s * 10 + a
    ans = ans + s

print(ans)
