language = ['python', 'c', 'c++', 'java']
for i in language:
    print('hello '+i + '!')

# range函数(打印1-5）
for value in range(1, 6):
    print(value)

# 创建数值列表(list函数加range函数）
numbers = list(range(1, 6))
print(numbers)

# 创建数值列表（1-10，偶数）
even_num = list(range(2, 11, 2))
print(even_num)

# 创建平方列表
squares = []
for i in range(1, 11):
    squares.append(i**2)
print(squares)

# 数字列表统计
print(min(squares))
print(max(squares))
print(sum(squares))

# 列表解析
digits = [i**2 for i in range(1, 11)]
print(digits)

# 切片（打印m-n个元素，切片（m-1，n））
numbers=list(range(1, 11))
print(numbers)
# 打印4-6
print(numbers[3: 6])
# 打印3-最后
print(numbers[2:])
# 从开始到5
print(numbers[: 5])
# 打印最后4个
print(numbers[-4:])
# 打印除了最后4个之外的
print(numbers[:-4])
# 遍历切片
for i in numbers[:5]:
    print(i)

# 列表复制（单独分配地址，两个列表独立）
num1 = [i for i in range(1, 6)]
num2 = num1[:]
num1.append(100)
num2.append(101)
print(num1)
print(num2)

# 元组元素不可修改，但可以重定义元组
num3 = (1, 2)
print(num3)
num3 = (3, 4)
print(num3)

# 判断列表是否为空
num4 = []
if num4:
    print("not null")
else:
    print("null")
