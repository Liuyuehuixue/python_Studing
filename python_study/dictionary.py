# 创建字典，键值对
alien_0 = {}
alien_0['color'] = 'green','red'
alien_0['points'] = 5
print(alien_0)
# 删除键值对
del alien_0["points"]

favorite_language = {}
favorite_language['A'] = 'java'
favorite_language['B'] = 'python'
favorite_language['C'] = 'c'

# 遍历键值对
for name,language in favorite_language.items():
    print('\nname: ' + name)
    print('language: ' + language.title())

# 遍历键keys(),遍历值values()
print('\nAll keys:')
for name in favorite_language.keys():
    print(name.title())

# 嵌套

# 列表存字典
alien_0 = {'color': 'red', 'point': 5}
alien_1 = {'color': 'green', 'point': 10}
alien_2 = {'color': 'yellow', 'point': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# 字典存列表
favorite_language = {
    'A': ['C', 'Python'],
    'B': ['Java']
}

for name , languages in favorite_language.items():
    print(name+': ')
    for language in languages:
        print('\t'+language)

# 字典存字典
aliens = {
    'alien_0': {
        'color': 'red',
        'point': 5
    },
    'alien_1': {
        'color': 'green',
        'point': 10
    },
}

for alien_num, alien_info in aliens.items():
    print('alien_num: '+ alien_num)
    print('\t' + alien_info['color'])
    print('\t' + str(alien_info['point']))

