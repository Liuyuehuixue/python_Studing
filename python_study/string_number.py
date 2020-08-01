str1 = "hello"
str2 = 'PYTHON'
# 首字母大写
print(str1.title())
# 全部大写
print(str1.upper())
# 全部小写
print(str2.lower())
# 拼接
msg = str1+" "+str2+"!"
print(msg)
# 制表符\t 换行\n
print("Language：\n\tc\n\tjava\n\tpython\n\t")

str3 = " python "
# 删除末尾空白（暂时）
print(str3.rstrip())
# 删除前端空白（暂时）
print(str3.lstrip())
# 删除两端空白（暂时）
print(str3.strip())

print(2*2)
print(0.2*0.2)
# 乘方
print(10**6)
# 类型转化
age = 20
print("I'm "+str(age)+"years old!")



