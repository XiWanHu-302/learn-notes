"""loop"""

'''while loop'''
# n = 1
# while n <= 10:
#     print(f'第{n}次')
#     n += 1
# print(f'while循环以外的代码，此时的n是{n}')
#
# print('您现在身处密室，正确回答问题后才能逃出密室！')
# riddle = '你是什么人？'
# answer = '循环'
# guess = ''
#
# while guess != answer:
#     print(f'问题：{riddle}')
#     guess = input('请输入答案：')
#     if guess == answer:
#         print('答案正确，逃脱成功！')
#     else:
#         print('回答错误，请再想想！')

'''for loop'''
# # 使用for循环遍历range()所指定的数字范围
# for n in range(1, 11):
#     print(n)
# print(f'循环已结束，此时的n是：{n}');
#
# # 使用for循环遍历字符串
# for m in 'abcdef':
#     print(m)
#
# # 演示由于误操作造成的死循环
# # 备注：for循环还能遍历很多我们没有讲到的东西，比如：元组、列表、对象……
# nums = [1,2,3]
# for n in nums:
#     # nums.append(4)
#     print(n)

'''for循环案例'''
# #加密代码
# text = input('请输入加密文字：')
# secret = ''
# for t in text:
#     secret += chr(ord(t) + 1)
# print(f'经过加密后的内容：{secret}')
#
# # 解密代码
# secret = input('请输入解密文字：')
# text = ''
# for s in secret:
#     text += chr(ord(s) - 1)
# print(f'经过解密后的内容：{text}')

'''嵌套循环'''
# for循环实现
# day = 1
# for day in range(1, 31):
#     print(f'*******📅第{day}天******')
#     for group in range(1,4):
#         print(f'💪这是第{group}组仰卧起坐')
#     print(f'✅第{day}天任务完成！明天继续！ \n')
# print(f'🥳为期{day}天的健身计划完成，我的腹肌在闪闪发光！')
#
# # while循环实现
# day = 1
# while day <= 30:
#     print(f'*******📅第{day}天******')
#     group = 1
#     while group <= 3:
#         print(f'💪这是第{group}组仰卧起坐')
#         group += 1
#     print(f'✅第{day}天任务完成！明天继续！ \n')
#     day += 1
# print(f'🥳为期{day - 1}天的健身计划完成，我的腹肌在闪闪发光！')

'''九九乘法表'''
# for n in range(1, 10):
#     for m in range(1, n + 1):
#         print(f'{m}*{n}={m * n}', end='\t')
#     print()

'''continue 与 break'''
# 测试continue
# for day in range(1,5):
#     print(f'******第{day}天******')
#     print('吃饭')
#     continue
#     print('睡觉')

# for day in range(1, 5):
#     print(f'******第{day}天******')
#     print('吃饭')
#     for item in range(1, 3):
#         print(f'面包{item}')
#         if day == 4 and item == 2:
#             continue
#         print(f'牛奶{item}')
#     print('睡觉')

# 测试break
# for day in range(1,5):
#     print(f'******第{day}天******')
#     print('吃饭')
#     break
#     print('睡觉')

# for day in range(1, 5):
#     print(f'******第{day}天******')
#     print('吃饭')
#     for item in range(1, 3):
#         print(f'面包{item}')
#         if day == 3 and item == 2:
#             break
#         print(f'牛奶{item}')
#     print('睡觉')

'''综合案例'''
q1, a1 = '1+1= ?', '2'
q2, a2 = '2+1= ?', '3'
q3, a3 = '3+1= ?', '4'
q, a = '', ''
status = True
for n in range(1, 4):
    if n == 1: q, a = q1, a1
    elif n == 2: q, a = q2, a2
    elif n == 3: q, a = q3, a3
    print(f'第{n}关:',q)
    m = 1
    while m <= 3:
        u1 = str(input('请输入答案：'))
        if u1 == 'q':
            print('游戏退出')
            status = False
            break
        elif u1 == '':
            print('重新作答')
        elif u1 == a:
            print('回答正确')
            break
        else:
            print(f'回答错误，还有{3 - m}次机会')
            m += 1
    if m == 4:
        print('挑战失败！')
        break
    if not False:
        break
if n == 3 and status == True:
    print('挑战成功！！！')
