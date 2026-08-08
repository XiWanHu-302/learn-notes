## PyCharm
### 快捷键

| 快捷键                       | 对应操作            |
| ------------------------- | --------------- |
| Ctrl + /                  | 行注释（可选中多行）      |
| Ctrl + Alt + L            | 代码格式化           |
| Ctrl + C                  | 复制当前行 / 复制选定的代码 |
| Ctrl + D                  | 重复当前行 / 重复选定的代码 |
| Ctrl + Z                  | 撤销              |
| Ctrl + Y                  | 删除当前行 / 反撤销(重做) |
| Ctrl + X                  | 复制当前行 / 剪切选定的代码 |
| Ctrl + = / -              | 展开 / 折叠当前代码块    |
| Ctrl + Backspace / Delete | 向前 / 向后删除一个单词   |
| Ctrl + Shift + ↑ / ↓      | 将当前行上移 或 下移     |
| Ctrl + F / R              | 查找 / 替换         |
| Tab / Shift + Tab         | 缩进 / 反向缩进       |
| Shift + Enter             | 换行（光标不在结尾处也可换行） |
| Ctrl + P                  | 查看方法传参          |
| Ctrl+Shift+U              | 对选中的字符切换大小写     |
| Ctrl+Alt+Enter            | 在当前行的上一行插入空行    |

### 导入、导出PyCharm的设置
- 导出：`File` → `Manage IDE Settings` → **Export Settings…**，选择保存位置，输出文件为 `settings.zip`，点 OK 完成导出
- 导入：`File` → `Manage IDE Settings` → **Import Settings…**，选中 `settings.zip`，重启 PyCharm 生效
## 字面量
- 字面量，就是直接写在代码中具体值
- python的字符串中可以包含任意字符，且必须使用引号包起来
- 字符串的引号，可以是：单引号、双引号、三个单引号、三个双引号
- 写在python文件头部的字符串，会被自动识别docstring（文档字符串）
- docstring主要作用是：对当前python文件进行说明，必须使用三个双引号字符串
- 调整PyCharm的设置：检查代码、AI智能提示。
```python
"""文档字符串（docstring）写在开头，对当前python文件进行说明"""  
  
'张三'  
18  
65.2  
  
'''李四'''  
22  
74.5  
  
"王五"  
25  
80  
  
"""赵六"""  
34  
70  
  
print(25)  
print(74)
```
## 变量
- 在Python中，当一个新的变量出现时，它必须立即与某个值建立绑定关系。值：字面量、函数、类等等
- 变量名要遵守一定的命名规则
## 标识符
- 标识符，程序中所有我们自己起名的内容。（变量名、函数名、类名、模块名……）
- 命名规则
	- 只能包含：数字、字母、下划线，且不能以数字开头，不能包含空格
	- 标识符区分大小写，例如`Name`和`name`是两个不同的标识符
	- 标识符不能使用关键字
	- 标识符尽量不要与内置函数同名
	- 标识符虽然没有长度限制，但应追求：简洁清晰，具有描述性
```python
userName = 'dd' # lowerCamelCase 不推荐  
UserName = 'dd' # UpperCamelCase 类名  
user_name = 'dd' # snake_case 变量、函数、文件名  
MAX_VALUE = 100 # UPPER_SNAKE_CASE 常量
```
## 常量
- 常量，一旦被赋值，就不希望被修改的量（区别于变量）
- Python中一般约定使用全大写变量名来表示常量，涉及到多个单词时，用下划线做分隔
- Python中没有强制的常量机制，Python中所谓的常量，其本质还是变量，只不过我们约定好不去修改
## 注释
- 单行注释：# 后的一行内容
- 多行注释：使用==三个单引号==，或==三个双引号==，Python并没有真正的多行注释语法，本质是一个字符串字面量。
- 文件编码注释：写在Python文件开头，用于指定当前文件的字符编码。python3中可以不写，默认使用UTF-8
```Python
#coding=utf-8   
"""在该文件中，主要学习注释相关的内容"""  
  
'''  
下面是一些常量  
ADULT_AGE是法定成人年龄  
MONTH_IN_YEAR是一年中的几个月  
MAX_USERS是最大同时在线人数  
'''  
  
ADULT_AGE = 18  # 成人年龄
MONTH_IN_YEAR = 12  
MAX_USERS = 1200  
  
print(ADULT_AGE, MONTH_IN_YEAR, MAX_USERS)
```
## 字符编码
- ASCII => 大写字母、小写字母、数字、一些符号，共128个
- ISO 8859-1 => 在ASCII基础上，扩充了一些希腊字符等，共计256个
- GB2312 => 继续扩充，收录了6763个常用汉字、682个字符
- GBK => 收录了的汉字和符号达到20000+，支持繁体中文 
- utf-8又称万国码，全球语言通吃，可以对任意语言进行编码
```python
message1 = '你好'  
message2 = 'hello'  
message3 = 'สวัสดี'  
message4 = 'こんにちは'  
  
print(message1, message2, message3, message4)
```
## 数据类型
在Python中：变量无类型，数据有类型
### 整型
- 打印数字时，内部会把数字转换成字符串，再打印。Python中数字在转换字符串的过程中，默认限制是：数字不能超过4300位
```python
import sys  
  
# 所谓整型，就是没有小数点的数字，可以是正数，也可以是负数，也可以是0  
age = 18  
temp = -15  
score = 0  
  
# 当数很大时，我们可以使用下划线将数字进行分组，来让数字变得更易读  
salary = 300_000  
house_price = 3_200_000  
graduates = 12_000_000  
print(salary, house_price, graduates)  
  
# Python中整数的上限值，取决于执行代码的计算机的内存和处理能力  
a = 9 ** 9999  
sys.set_int_max_str_digits(0)  
print(a)
```
### 浮点型
```python
# 浮点型就是带有小数点的数字  
weight = 65.2  
balance = 242.3  
out_temp = -23.2  
price = 120.0  
  
# 浮点型的科学计数法表示  
speed_of_sound = 3.4e+2  # 3.4乘以10的2次方  
world_population = 7.8e9  # 7.8乘以10的9次方  
distance_sun_earth = 1.496E8  # 1.496乘以10的8次方  
speed_of_light = 2.998E+8  # 2.998乘以10的8次方  
  
one_ml = 1e-3  # 1乘以10的-3次方  
one_mg = 1E-3  
```
### 字符串
#### four ways to define a string 
```python
# 单引号和双引号的写法是等价的，二者都不能直接换行（要用圆括号才能换行），单引号用得多  
message1 = 'As long as you think it\'s right.'  
message2 = "As long as you think it's right."  
  
# 三个单引号，可以直接换行，（换行后回车也会打印出来）并且可以作为多行注释使用  
message3 = '''As long as you think it's right.'''  
  
# 三个双引号，可以直接换行，也可以作为多行注释使用，还能作为文档字符串使用。  
message4 = """As long as you think it's right."""
```
#### string formatting
- 按照预先定义的==格式==，将==变量==或==计算结果==，==插入==到字符串中并输出
```python
name = 'James'  
gender = 'male'  
weight = 56.3  
age = 20  
  
# 写法一：直接用加号进行拼接，写起来麻烦代码乱，并且只能字符串拼接  
info1 = 'My name is ' + name + '. I\'m ' + gender + '.'  
print(info1)  
  
# 写法二：使用占位符(%i占位整数，%d占位10进制的整数，%s是万能的)  
info2 = 'My name is %s. I am %s. My weight is %f kg and I am %i years old.' % (name, gender, weight, age) 
print(info2)  
  
# 写法三：使用f-string，是目前Python最推荐的方式  
info3 = f'我叫{name}，我是{gender}，我体重是{weight}，年龄是{age}'  
print(info3)
```
#### String placeholder precision control
- `%m.ns`
	- m
		- 字符串的==最小宽度==，位数==不够==会自动使用空格补全，位数==小于==字符串长度则==不起作用==
		- ==正数==是==右==对齐，==负数==是==左==对齐
	- n
		- ==精度==控制，==最多==输出==n个==字符（若==n大于==实际字符串长度，则不起作用）
- `%m.nf`
	- n：精度控制，保留n位小数（n的默认值为6），不够0来补，截断时会四舍五入
	- m
		- 控制整体宽度（整体宽度 = 整数宽度 + 小数点 + 小数宽度）
		- 位数不够空格来补，位数小于整体宽度，则自动失效
		- 正数是右对齐，负数是左对齐
- `m.nd`
	- m
		- 最小宽度，位数不够会使用空格补全，位数小于整数位数，则自动失效
		- 正数是右对齐，负数是左对齐
	- n
		- 精度控制，最少用n位显示数字
		- 位数不够用0来补，位数小于整数位，则自动失效 
```python
name = '张三'  
gender = '男'  
weight = 56.55  
age = 20  
info = '我叫%-4.1s,性别是%3.2s,体重是%9.3f,年龄是%6.4d' % (name, gender, weight, age)  
print(info)  # 我叫张   ,性别是  男,体重是   56.550,年龄是  0020
```
#### escape sequence
- 是一种在字符串中用于表示特殊含义的字符组合，通常以反斜杠开头，通常用于表示那些在字符串中不能直接写出的字符
- \t：水平制表符（让光标跳转到下一个制表位）
	- ![230](assets/python_basic/file-20260807231250139.png)
```python
# 使用 \' 输出 'print('在Python中，可以使用\'包裹一个字符串')  
  
# 使用 \" 输出 "print("在Python中，可以使用\"包裹一个字符串")  
  
# 使用 \n 进行换行  
print('注册会员需要以下信息：\n姓名\n年龄\n手机号')  
  
# 使用 \\ 输出 \print('D:\\nice')  
  
# 使用 \b 删除前一个字符，实现打印机效果  
print('helloo\b')  
  
# 使用 \r 使光标回到本行开头，覆盖输出， 实现进度加载效果  
print('67%\r68%')  
  
# 使用 \t 表示水平制表符（让光标跳转到下一个制表位）  
print('1234123412341234')  
# print('ab\tcd'.expandtabs(4))  
# print('abc\td'.expandtabs(4))  
# print('abcd\ta'.expandtabs(4))  
# print('我是\t中文'.expandtabs(4))  
  
print('ab\tcd')  
print('abc\td')  
print('abcd\ta')  
print('我是\t中文')
```
### 布尔类型 boolean
`True` `False`
```python

```
## 数据类型转换
- 为什么要进行数据类型转换
	- 用户输入的内容是都是字符串，若需要进行数学运算，就必须进行数据类型转换。
	- 对文件进行写入操作时，要将其他类型的数据转为字符串。
	- 从数据库中读取出的内容都是字符串，若需要进行数学运算，也需要数据类型转换。
- 把指定数据转为字符串：`str()`
	- 任何类型都可以转成字符串类型
```python
# 使用str()将指定数据类型转换为字符串。  
result1 = str(18)  
result2 = str(75.6)  
result3 = str(1.8E3)  
result4 = str(12_000)
```
- 把指定数据转为整型：`int()`
```python
# 使用int()将指定数据类型转换为整型。  
result1 = int(15.6)  
result2 = int('79')  
result3 = int('   79   ')  
result4 = int(48)  
# 以下是错误示例  
# int('  7 9  ')  
# int('你好')  
# int('15.6')  #特别注意
```
- 把指定数据转为浮点型：`float()`
```python
# 使用float()将指定数据类型转换为浮点型。  
result1 = float(18)  
result2 = float('15.6')  
result3 = float('  5.7  ')  
result4 = float(14.8)  
result5 = float('89')  
  
# 以下是错误示例  
# float(' 5.  7 ')  
# float('你好')  
# float('5.23.534')
```
- 把指定内容转为布尔类型：`bool()`
```python
# 布尔类型是int类型的子类型，底层的本质是用1表示True，用0表示False  
print(int(True))  # 1  
print(int(False))  # 0  
  
# print(4 + True)  
# print(8 - False)  

# print(True + True)  
# print(True - False) 
 
# print(7 > True)  
# print(False <= 0)  
  
# 使用bool()将指定内容转为布尔类型  
print(bool(1))  # True  
print(bool(0))  # False  
  
# Python中除0以外的任何数，转为布尔值后都为True  
print(bool(300))  
print(bool(25.6))  
print(bool(1.8e3))  
print(bool(12_000))  
print(bool(-10))  # True  
  
# Python中除空字符串以外的任何字符串，转为布尔值都是True  
print(bool('hello'))  
print(bool('0'))  
print(bool('18.5'))  
print(bool('-9'))  
print(bool(''))  # False
```
## 运算符
### 算数运算符

| 运算符 | 说明      | 示例     | 结果  |
| --- | ------- | ------ | --- |
| +   | 加       | 9 + 7  | 16  |
| -   | 减       | 7 - 2  | 5   |
| *   | 乘       | 3 * 4  | 12  |
| /   | 除       | 9 / 6  | 1.5 |
| //  | 取整除（取整） | 9 // 6 | 1   |
| %   | 取余（取模）  | 9 % 6  | 3   |
| **  | 指数      | 2 ** 3 | 8   |
|     |         |        |     |
### 赋值运算符 & 复合赋值运算符

| 运算符 | 含义     | 示例            | 等价代码                   |
| --- | ------ | ------------- | ---------------------- |
| =   | 赋值运算   | age = 18      |                        |
| +=  | 加法赋值运算 | age += 1      | age = age + 1          |
| -=  | 减法赋值运算 | age -= 1      | age = age - 1          |
| *=  | 乘法赋值运算 | price *= 0.8  | price = price * 0.8    |
| /=  | 除法赋值运算 | pay /= 5      | pay = pay / 5          |
| //= | 取整赋值运算 | apple //= 14  | apple = apple // 14    |
| %=  | 取模赋值运算 | seconds %= 60 | seconds = seconds % 60 |
| **= | 指数赋值运算 | a **= b       | a = a ** b             |
### 比较运算符

| 运算符 | 作用           |
| --- | ------------ |
| ==  | 判断左右两侧是否相等   |
| !=  | 判断左右两侧是否不等   |
| >   | 判断左侧是否大于右侧   |
| <   | 判断左侧是否小于右侧   |
| >=  | 判断左侧是否大于等于右侧 |
| <=  | 判断左侧是否小于等于右侧 |
- Python中字符串进行比较时，是依次比较每个字符的Unicode编码。
- Unicode 编码不是Python特有的，而是全世界通用的标准。例如 `a` 的Unicode编码是97，`我`是25105
- Python中可以使用如下方式进行字符与Unicode编码之间的转化
	- 使用`ord()`查看Unicode 码
	- 使用`chr()`将Unicode 码转为字符
```python
# 使用ord()查看指定字符的Unicode编码  
print(ord('a'))  # 97  
print(ord('我'))  # 25105  
print(ord('中'))  # 20013  
  
# 使用chr()将Unicode编码转为字符  
print(chr(97))  
print(chr(25105))  
  
msg1 = 'abc'  
msg2 = 'xyz'  
msg3 = '我爱你'  
msg4 = '中国'  
msg5 = 'abc'  
msg6 = 'abcdef'  
print(msg1 == msg5)  # True  
print(msg1 < msg2)  # True  
print(msg3 > msg4)  
print(msg5 < msg6)
```
### 逻辑运算符

| 运算符 | 名称   | 功能描述                                   |
|--------|--------|--------------------------------------------|
| and    | 逻辑与 | 判断其两侧的值，是否都为True               |
| or     | 逻辑或 | 判断其两侧的值，是否至少有一个为True       |
| not    | 逻辑非 | 用于对一个值取反                           |
```python
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
```
