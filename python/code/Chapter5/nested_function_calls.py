"""函数"""

'''Nested function calls'''
# 函数嵌套调用测试2
def test1():
    print('进入 test1 函数')
    test2()
    print('退出 test1 函数')

def test2():
    print('进入 test2 函数')
    test3()
    print('退出 test2 函数')

def test3():
    print('进入 test3 函数')
    print('***正在执行 test3 函数')
    print('退出 test3 函数')

test1()

'''递归调用'''
# 使用递归打印n次“你好啊”（从大到小）
def welcome(n):
    print(f'你好啊{n}')
    if n > 1:
        welcome(n - 1)
welcome(5)

print('***************')
# 使用递归打印n次“你好啊”（从小到大）
def welcome1(n):
    if n > 1:
        welcome1(n - 1)
    print(f'你好啊{n}')
welcome1(5)

'''递归的应用'''
# 使用递归求阶乘
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
result = factorial(5)
print(result)

'''函数的说明文档'''
def add(a, b):
    """
    计算两个数相加的结果
    :param a: 第一个数
    :param b: 第二个数
    :return: 二者相加的结果
    """
    return a + b
result = add(1, 2)