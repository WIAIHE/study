str = input("请输入五个以上的正整数")
nums = eval(str)
list = []

for i in range(len(nums)):
    list.append(nums[i])

list.sort()
print("结果:", end='')
for i in range(len(nums)):
    print(list[i], end=' ')
