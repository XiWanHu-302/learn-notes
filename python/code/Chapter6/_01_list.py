"""列表"""

'''定义列表'''

# # 定义有内容的列表
# list1 = [34, 54, 65, 243]
# list2 = ['北京', 'shide']
# list3 = [23, 'beijing', True, None]
# list4 = [23, 'beijing', True, None, [100, 343, 'good']]
#
# # 定义空列表（列表中的数据，后期会通过特定写法填充）
# list5 = []
# list6 = list()
#
# print(list1, type(list1))
# print(list2, type(list2))
# print(list3, type(list3))
# print(list4, type(list4))
# print(list5, type(list5))
# print(list6, type(list6))

'''下标（索引值）'''
# nums = [10, 20, 30, 40, 50]
#
# # 测试正索引
# print(nums[0])
# print(nums[1])
# print(nums[2])
# print(nums[3])
# print(nums[4])
#
# # 测试负索引
# print(nums[-1])
# print(nums[-2])
# print(nums[-3])
# print(nums[-4])
# print(nums[-5])
#
# # 测试错误索引
# # print(nums[5])
#
# # 定义一个嵌套列表
# nums2 = [10, 20, ['你好啊', '我不好'], 40, 50]
# # 取出“我不好”
# print(nums2[2][1])

'''新增操作'''
# # 方式一：通过列表的append方法，在列表尾部追加一个元素
# nums = [10, 20, 30, 40]
# nums.append(50)
# print(nums)
#
# # 方式二：通过列表的insert方法，在列表的指定下标处添加一个元素
# nums = [10, 20, 30, 40]
# nums.insert(2, 666)
# print(nums)
#
# # 方式三：通过列表的extend方法，将可迭代对象中的内容依次取出，追加到列表尾部
# nums = [10, 20, 30, 40]
# nums.extend('天气好')
# nums.extend(range(1,4))
# nums.extend([70, 80, 90])
# print(nums)  # [10, 20, 30, 40, '天', '气', '好', 1, 2, 3, 70, 80, 90]

'''删除操作'''
# 方式一：通过列表的pop方法，删除指定位置的元素，并返回该元素
nums = [10, 20, 30, 40, 50]
result = nums.pop(1)
print(nums)  # [10, 30, 40, 50]
print(result)  # 20

# 方式二：通过列表的remove方法，删除列表中第一次出现的特定值
nums = [10, 20, 10, 40, 50]
nums.remove(10)
print(nums)  # [20, 10, 40, 50]

# 方式三：通过列表的clear方法，删除列表中所有的元素（清空列表）
nums = [10, 20, 30, 40, 50]
nums.clear()
print(nums)  # []

# 方式四：通过del关键字，删除指定元素
nums = [10, 20, 30, 40, 50]
del nums[3]
print(nums)

'''常用方法'''
# 1.使用 index 方法，查找指定元素在列表中第一次出现的下标，返回值是：元素下标。
fruits = ['香蕉', '苹果', '橙子', '香蕉']
result = fruits.index('香蕉')
print(result)  # 0

# 2.使用 count 方法，统计某个元素在列表中出现的次数，返回值是：元素出现的次数。
nums = [10, 20, 10, 30, 10, 40, [10, 10, 10]]
result = nums.count(10)
print(result)  # 3

# 3.使用 reverse 方法，对列表进行反转（会改变原列表）。
nums = [23, 11, 32, 30, 17]
nums.reverse()
print(nums)  # [17, 30, 32, 11, 23]

# 4.使用 sort 方法，对列表排序（默认从小到大），若想从大到小，可以将 reverse 参数设为True。
# 4.1 若列表中的元素：都是数字，则按照数字的大小顺序进行排序。
nums = [23, 11, 32, 30, 17]
nums.sort(reverse=True)
print(nums)  # [32, 30, 23, 17, 11]

# 4.2 若列表中的元素：既有数字，又有字符串，那就会报错。
# nums = [23, 11, 32, 30, 17, '尚硅谷']
# nums.sort()
# print(nums)

# 4.3 若列表中的元素：都是字符串，则按照字符串的 Unicode 编码大小进行排序
msg_list = ['北京', '北硅谷', '北好']
msg_list.sort()
print(msg_list)
print(ord('京'), ord('好'), ord('硅'))  # 20140 22909 30789

# 备注：所有的列表方法，都只作用于“当前层”的元素（浅层操作），不会自动进入嵌套的“里层”结构中。

'''内置函数'''
# 1.使用内置的 sorted 函数，返回一个排序后的新容器（不改变原容器，默认顺序：从小到大）
# 1.1 若列容器中的元素：都是数字，则按照数字的大小顺序进行排序。
nums = [23, 11, 32, 30, 17]
result = sorted(nums, reverse=True)
print(nums)  # [23, 11, 32, 30, 17]
print(result)  # [32, 30, 23, 17, 11]

# 1.2 若列容器中的元素：既有数字，又有字符串，那就会报错。
# nums = [23, 11, 32, 30, 17, '尚硅谷']
# sorted(nums)

# 1.3 若列容器中的元素：都是字符串，则按照字符串的 Unicode 编码大小进行排序。
msg_list = ['北京', '尚硅谷', '你好']
result = sorted(msg_list)
print(msg_list)  # ['北京', '尚硅谷', '你好']
print(result)  # ['你好', '北京', '尚硅谷']

# 2.使用内置的 len 函数，获取容器中元素的总数量，返回值是：元素总数量。
nums = [10, 20, 10, 30, 10, 40, [50, 60, 70]]
result = len(nums)
print(result)  # 7

# 3.使用内置的 max 函数，获取容器中的最大值，返回值是：最大值。
# 3.1 如果容器中的元素：都是数字，那 max 返回的是最大的数。
nums = [23, 11, 32, 30, 17]
result = max(nums)
print(nums)  # [23, 11, 32, 30, 17]
print(result)  # 32

# 3.2 如果容器中的元素：既有数字又有字符串，那 max 会报错。
# nums = [23, 11, 32, 30, 17, '尚硅谷']
# max(nums)

# 3.3 如果容器中的元素：都是字符串，那 max 会返回：Unicode 编码最大的字符。
msg_list = ['北京', '尚硅谷', '你好']
result = max(msg_list)
print(msg_list)  # ['北京', '尚硅谷', '你好']
print(result)  # 尚硅谷

# 3.4 max 函数也可以接收多个值，并筛选出最大值
result = max(33, 45, 12, 78, 99)
print(result)  # 99

# 4.使用内置的 min 函数，获取容器中的最小值，返回值是：最小值。
# 备注: min 函数的使用方式与注意点与 max 函数一样，只不过 min 函数返回的是最小值
nums = [23, 11, 32, 30, 17]
result = min(nums)
print(result)  # 11

# 5.使用内置的 sum 函数，对容器中的数据进行求和 (元素只能是数值)。
nums = [10, 20, 30, 40, 50]
result = sum(nums)
print(result)  # 150

'''循环遍历'''
# 定义一个成绩列表
score_list = [62, 50, 60, 48, 80, 20, 95]

# 使用while循环遍历列表
index = 0
while index < len(score_list):
    print(score_list[index])
    index += 1

# 使用for循环遍历列表（通过range函数 和 len函数按照索引遍历）
for index in range(len(score_list)):
    print(score_list[index])

# 使用for循环遍历列表（通过enumerate函数，同时获取下标（索引值）和元素）
# enumerate 的 start 参数, 可以让计数从指定值开始（改变的是循环时的“编号”，不是真正的索引值）
for index, item in enumerate(score_list, start=5):
    print(index, item, score_list[0])
print('最后的打印', score_list[0])
'''
5 62 62
6 50 62
7 60 62
8 48 62
9 80 62
10 20 62
11 95 62
'''