"""包含了多章节内容"""
'''character_encoding'''
# message1 = '你好'
# message2 = 'hello'
# message3 = 'สวัสดี'
# message4 = 'こんにちは'
#
# print(message1, message2, message3, message4)
#
'''data type'''
# result = type('张三')
# print(result)
# print(type(18))
# print(type(793.2))
#
# name = '张三'
# print(type(name))

'''integer'''
# import sys
#
# # 所谓整型，就是没有小数点的数字，可以是正数，也可以是负数，也可以是0
# age = 18
# temp = -15
# score = 0
#
# # 当数很大时，我们可以使用下划线将数字进行分组，来让数字变得更易读
# salary = 300_000
# house_price = 3_200_000
# graduates = 12_000_000
# print(salary, house_price, graduates)
#
# # Python中整数的上限值，取决于执行代码的计算机的内存和处理能力
# a = 9 ** 9999
# sys.set_int_max_str_digits(0)
# print(a)

'''float'''
# # 浮点型就是带有小数点的数字
# weight = 65.2
# balance = 242.3
# out_temp = -23.2
# price = 120.0
#
# # 浮点型的科学计数法表示
# speed_of_sound = 3.4e+2  # 3.4乘以10的2次方
# world_population = 7.8e9  # 7.8乘以10的9次方
# distance_sun_earth = 1.496E8  # 1.496乘以10的8次方
# speed_of_light = 2.998E+8  # 2.998乘以10的8次方
#
# print(speed_of_sound)
# print(world_population)
# print(distance_sun_earth)
# print(speed_of_light)
#
# one_ml = 1e-3  # 1乘以10的-3次方
# one_mg = 1E-3
# print(one_ml)
# print(one_mg)

'''four ways to define a string'''
# # 单引号和双引号的写法是等价的，二者都不能直接换行（要用圆括号才能换行），单引号用得多
# message1 = 'As long as you think it\'s right.'
# message2 = "As long as you think it's right."
#
# # 三个单引号，可以直接换行，（换行后回车也会打印出来）并且可以作为多行注释使用
# message3 = '''As long as you think it's right.'''
#
# # 三个双引号，可以直接换行，也可以作为多行注释使用，还能作为文档字符串使用。
# message4 = """As long as you think it's right."""
#
# print(message1)
# print(message2)
# print(message3)
# print(message4)

'''string formatting'''
# name = 'James'
# gender = 'male'
# weight = 56.3
# age = 20
#
# # 写法一：直接用加号进行拼接，写起来麻烦代码乱，并且只能字符串拼接
# info1 = 'My name is ' + name + '. I\'m ' + gender + '.'
# print(info1)
#
# # 写法二：使用占位符(%i占位整数，%d占位10进制的整数，%s是万能的)
# info2 = 'My name is %s. I am %s. My weight is %f kg and I am %i years old.' % (name, gender, weight, age)
# print(info2)
#
# # 写法三：使用f-string，是目前Python最推荐的方式
# info3 = f'我叫{name}，我是{gender}，我体重是{weight}，年龄是{age}'
# print(info3)

'''String placeholder precision control'''
# name = '张三'
# gender = '男'
# weight = 56.55
# age = 20
# info = '我叫%-4.1s,性别是%3.2s,体重是%9.3f,年龄是%6.4d' % (name, gender, weight, age)
# print(info)

'''escape sequence'''
# # 使用 \' 输出 '
# print('在Python中，可以使用\'包裹一个字符串')
#
# # 使用 \" 输出 "
# print("在Python中，可以使用\"包裹一个字符串")
#
# # 使用 \n 进行换行
# print('注册会员需要以下信息：\n姓名\n年龄\n手机号')
#
# # 使用 \\ 输出 \
# print('D:\\nice')
#
# # 使用 \b 删除前一个字符，实现打印机效果
# print('helloo\b')
#
# # 使用 \r 使光标回到本行开头，覆盖输出， 实现进度加载效果
# print('67%\r68%')
#
# # 使用 \t 表示水平制表符（让光标跳转到下一个制表位）
# print('1234123412341234')
# # print('ab\tcd'.expandtabs(4))
# # print('abc\td'.expandtabs(4))
# # print('abcd\ta'.expandtabs(4))
# # print('我是\t中文'.expandtabs(4))
#
# print('ab\tcd')
# print('abc\td')
# print('abcd\ta')
# print('我是\t中文')
#
# print('姓名\t性别\t年龄')
# print('张三\t男\t\t18')
# print('李四\t女\t\t25')
# print('王五\t男\t\t32')

'''type conversion'''
# 使用str()将指定数据类型转换为字符串。
# result1 = str(18)
# result2 = str(75.6)
# result3 = str(1.8E3)
# result4 = str(12_000)
#
# print(type(result1), result1)
# print(type(result2), result2)
# print(type(result3), result3)
# print(type(result4), result4)

# 使用int()将指定数据类型转换为整型。
# result1 = int(15.6)
# result2 = int('79')
# result3 = int('   79   ')
# result4 = int(48)
# 以下是错误示例
# int('  7 9  ')
# int('你好')
# int('15.6')

# print(type(result1), result1)
# print(type(result2), result2)
# print(type(result3), result3)
# print(type(result4), result4)

# 使用float()将指定数据类型转换为浮点型。
# result1 = float(18)
# result2 = float('15.6')
# result3 = float('  5.7  ')
# result4 = float(14.8)
# result5 = float('89')

# 以下是错误示例
# float(' 5.  7 ')
# float('你好')
# float('5.23.534')
#
# print(type(result1), result1)
# print(type(result2), result2)
# print(type(result3), result3)
# print(type(result4), result4)
# print(type(result5), result5)

'''比较运算符'''
# msg1 = 'abc'
# msg2 = 'abc'
# print(msg1 == msg2)  # True
#
# # 使用ord()查看指定字符的Unicode编码
# print(ord('a'))  # 97
# print(ord('我'))  # 25105
# print(ord('中'))  # 20013
#
# # 使用chr()将Unicode编码转为字符
# print(chr(97))
# print(chr(25105))
#
# msg1 = 'abc'
# msg2 = 'xyz'
# msg3 = '我爱你'
# msg4 = '中国'
# msg5 = 'abc'
# msg6 = 'abcdef'
# print(msg1 == msg5)  # True
# print(msg1 < msg2)  # True
# print(msg3 > msg4)
# print(msg5 < msg6)


'''boolean'''
# # 自己定义的布尔值
# a = True
# b = False
# # 靠程序执行得到的布尔值
# c = 5 > 3
# d = 7 < 2
# print(type(a), a)  # <class 'bool'> True
# print(type(b), b)  # <class 'bool'> False
# print(type(c), c)  # <class 'bool'> True
# print(type(d), d)  # <class 'bool'> False
#
# # 布尔类型是int类型的子类型，底层的本质是用1表示True，用0表示False
# print(int(True))  # 1
# print(int(False))  # 0
#
# # print(4 + True)
# # print(8 - False)
# #
# # print(True + True)
# # print(True - False)
# #
# # print(7 > True)
# # print(False <= 0)
#
# # 使用bool()将指定内容转为布尔类型
# print(bool(1))  # True
# print(bool(0))  # False
#
# # Python中除0以外的任何数，转为布尔值后都为True
# print(bool(300))
# print(bool(25.6))
# print(bool(1.8e3))
# print(bool(12_000))
# print(bool(-10))  # True
#
# # Python中除空字符串以外的任何字符串，转为布尔值都是True
# print(bool('hello'))
# print(bool('0'))
# print(bool('18.5'))
# print(bool('-9'))
# print(bool(''))  # False

'''逻辑运算符'''
# print(True and False)
# print(False and True)
# print(False and False)
# print(8 > 7 and 8 > 7)
# print(8 > 7 and 2 > 3)
# print(2 > 3 and 8 > 7)
# print(2 > 3 and 2 > 3)

# and具备"逻辑短路"能力
print(False and 3 / 0)  # False
print(3 > 9 and 3 / 0)  # False
# print(True and 3 / 0)  # ZeroDivisionError

# and返回的不一定是布尔值，它返回的是某个参与计算的值本身
# 规则：and会先看左边，如果左边是“假”，就直接返回左边，否则返回右边
# 备注：若参与and运算的值不是布尔值，那Python会自动转为布尔值，然后再进行逻辑操作
print(2 - 2 and True)  # 0
print('' and True)  # 空字符串
print(True and 8 / 2)  # 4.0
print(3 + 3 and 3 * 4)  # 12

# or用于判断其两侧，是否至少有一个为True（只要有一个是True，那就返回True）
# or同样具有“逻辑短路”的能力
print(True or 3 / 0)

# or返回的也不一定是布尔值，它返回的是参与计算的值本身
# 规则：or会先看左边，如果左边为“真”，就直接返回左边，否则返回右边
# 备注：若参与or运算的值不是布尔值，那Python会自动转为布尔值，然后再进行逻辑操作
print(7 - 2 or False)  # 5
print('你好' or '尚硅谷')  # 你好
print(False or 8 / 2)  # 4.0
print(2 - 2 or 3 * 4)  # 12

# not用于取反
# 备注：若参与not运算的值不是布尔值，那Python会自动转为布尔值，然后再进行逻辑操作
# not返回的值，一定是布尔值!
print(not 0)  # True
print(not 3 > 2)  # False
print(not 9 // 4)  # False
print(not 'abc')  # False