""""函数"""

'''Basic usage of functions'''
# 定义函数
def welcome():
    print('jdjdjdj')
    print('jdjdjdjjeeee')

# 调用函数
welcome()
welcome()

'''Usage of Parameters'''
def order(num, dish):
    print(f'您点的是：{num}份{dish}')
order(1, '辣椒炒肉')
order(2, '番茄炒蛋')

'''位置参数'''
# 定义函数（接收位置参数）
def greet(name, gender, age, height):
    print(f'我叫{name}, 性别{gender}, 年龄是{age}, 身高是{height}cm')
# 调用函数
greet('张三', '男', 18, 172)
# 错误示例
# greet('张三', 18, 172)


'''关键字参数'''
# 定义函数
def greet(name, gender, age, height):
    print(f'我叫{name}, 性别{gender}, 年龄是{age}, 身高是{height}cm')

# 调用函数（使用关键字参数）
greet(name='张三', gender='男', age=18, height=172)
greet(height=172, age=18, gender='男', name='张三')
greet('张三', '男', height=172, age=18)

# 错误示例
# greet(height=172, age=18, '张三', '男')
# greet(name='张三', '男', 18, 172)
# greet(name='张三', '男', age=18, 172)
# greet(height=172, age=18, gender='男', name='张三', age=19)
# greet(height=172, age=18, gender='男', name='张三', school='尚硅谷')

'''限制传参方式'''
# 定义函数（使用/和*限制传参方式）
def greet(name, /, gender, *, age, height):
    print(f'我叫{name}, 性别{gender}, 年龄是{age}, 身高是{height}cm')

# 正确示例
greet('张三', '男', age=18, height=172)
greet('张三', gender='男', age=18, height=172)

# 错误示例
# greet(name='张三', gender='男', age=18, height=172)
# greet('张三', '男', 18, height=172)

'''参数默认值'''
# # 定义函数（设置参数默认值）
# def greet(name, gender, age, height, msg='你好'):
#     print(f'我叫{name}, 性别{gender}, 年龄是{age}, 身高是{height}cm')
#     print(f'我想说: {msg}')
#
# # 调用函数
# greet('张三', '男', 18, 172)
# greet('张三', '男', 18, 172, 'hello')
# greet('张三', '男', 18, 172, msg='hello')
#
# # print函数底层给end参数设置了默认值
# print('尚硅谷', end='!!')

'''可变参数'''
# 定义函数（使用*args去接收：可变位置参数）
def test1(*args):
    # 此处args的值，是一种新的数据类型，叫：元组
    print(args)
# 调用函数
test1('张三', '男', 18, 172)  # ('张三', '男', 18, 172)

# 定义函数（使用**kwargs去接收：可变关键字参数）
def test2(**kwargs):
    # 此处kwargs的值，是一种新的数据类型，叫：字典
    print(kwargs)
# 调用函数
test2(name='张三', gender='男', age=18, height=172)  # {'name': '张三', 'gender': '男', 'age': 18, 'height': 172}

# 定义函数（同时使用：可变位置参数、可变关键字参数）
def test3(a, b, *args, c='开心', **kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(kwargs)
test3('张三', '男', '吃饭', '睡觉', c='哈哈哈', age=18, height=172)

'''None'''
# None是一个特殊的字面量，它表示：空值 / 无值 / 无意义。
msg = None

# None 的类型是 NoneType。
print(type(msg))  # <class 'NoneType'>

# None 转为布尔值是 False。
print(bool(msg))
if not msg:
    print('你好')

# 不能参与数学运算，也不能与字符串拼接。
# result1 = msg + 1
# result1 = msg + 'hello'

'''返回值'''
def add(n1, n2):
    print(f'我收到了：{n1}、{n2}, 二者相加是：{n1 + n2}')
    return n1 + n2

result = add(100, 333)
print(result)

res = print('hello')
print(res)  # None

'''全局作用域与局部作用域'''
# 全局作用域 与 局部作用域，以及global的使用
a = 100
b = 200

def test():
    c = '尚硅谷'
    d = '你好啊'
    global a
    a = 300
    print('函数中的打印(a) ', a)
    print('函数中的打印(b) ', b)
    print('函数中的打印(c) ', c)
    print('函数中的打印(d) ', d)

test()
print('****************')
print('全局的打印(a) ', a)
print('全局的打印(b) ', b)
# print(c)
# print(d)

# 局部作用域 和 局部变量，会在函数调用时创建，在函数执行结束后自动销毁
def test2():
    m = 100
    m += 1
    print(f'我是test2函数中打印的m: {m}')

test2()  # 101
test2()  # 101
test2()  # 101

# 全局作用域和全局变量，会在程序开始时创建，在程序结束后销毁
n = 100
def test3():
    global n
    n += 1
    print(f'我是test3函数打印的n: {n}')
test3()  # 101
test3()  # 102
test3()  # 103