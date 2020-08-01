# # 用户输入
# number = input("please input a number ,tell you even or odd?:")
# number = int(number)
# if number % 2==0:
#     print(str(number)+"is even!")
# else:
#     print(str(number) + " is odd!")


# prompt = "tell me sth"
# prompt += "\nEnter ''quit to end!"
#
# message = ''
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# # continue break
# num = 0
# while True:
#     num += 1
#     if num % 2 == 0:
#         continue
#     if num>10:
#         break
#     print(num)

# 列表
unconfirmed_users = ['a', 'b', 'c']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: "+ current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['dog', 'cat', 'fish', 'rabbit', 'cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# 字典
responses = {}
flag = True
while flag:
    name = input("what's your name? :")
    response = input("which pets do you like? :")
    responses[name] = response
    repeat = input("continue? Y/N ：")
    if repeat == 'N':
        flag = False

for name, response in responses.items():
    print(name+' likes '+response+'.')




