language = ["python", "c", "java", "c++"]
print("Language：\n\t"+language[0].title())
# 列表最后一个元素-1
print("\t"+language[-1])

# 添加列表元素
language.append("c#")
print(language)

# 插入列表元素
language.insert(0, "javascript")
print(language)
# 删除列表元素
del language[0]
print(language)

# pop()删除列表末尾元素 pop(n)删除列表第n+1个元素
last_language = language.pop()
print(language)
print(last_language)
last_language = language.pop(2)
print(language)
print(last_language)

# 根据值删除
language.remove('c')
print(language)

language.append('c')
language.append('java')
print(language)
# 列表排序
language.sort()
print(language)
# 列表排序(反向）
language.sort(reverse=True)
print(language)
# 临时排序
print(sorted(language))
print(language)
# 反向排序
language.reverse()
print(language)

# 列表长度
print(len(language))


