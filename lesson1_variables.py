print("=" * 70)
print("Python 第1课：变量和数据类型（详细讲解）")
print("=" * 70)

print("\n" + "=" * 70)
print("一、什么是变量？")
print("=" * 70)
print("""
变量就像是一个"盒子"，用来存放数据。
你可以给这个盒子起个名字，以后就可以通过这个名字来访问里面的数据。

语法：变量名 = 值

注意事项：
1. 变量名只能包含字母、数字和下划线
2. 变量名不能以数字开头
3. 变量名不能是Python的关键字（如：if, else, for, while等）
4. 变量名区分大小写（name 和 Name 是不同的变量）
""")

name = "小明"
print(f"定义变量 name，值为 '小明': {name}")

age = 25
print(f"定义变量 age，值为 25: {age}")

my_score = 95.5
print(f"定义变量 my_score，值为 95.5: {my_score}")

is_student = True
print(f"定义变量 is_student，值为 True: {is_student}")

print("\n" + "=" * 70)
print("二、变量的赋值和修改")
print("=" * 70)
print("""
变量的值可以随时修改，就像把盒子里的东西换成新的。
""")

x = 10
print(f"x 初始值: {x}")

x = 20
print(f"x 修改后的值: {x}")

x = x + 5
print(f"x = x + 5 后的值: {x}")

x += 3
print(f"x += 3 后的值（等价于 x = x + 3）: {x}")

print("\n" + "=" * 70)
print("三、Python 的五大基本数据类型")
print("=" * 70)

print("\n--- 3.1 字符串 (str) ---")
print("""
字符串就是文本，用引号包裹。
可以使用单引号 ' ' 或双引号 " "
""")

name1 = '张三'
name2 = "李四"
message = "Hello, Python!"
long_text = '''这是一段
多行文本
可以使用三个单引号'''

print(f"单引号字符串: {name1}")
print(f"双引号字符串: {name2}")
print(f"消息字符串: {message}")
print(f"多行文本: {long_text}")

print("\n--- 3.2 整数 (int) ---")
print("""
整数就是没有小数部分的数字。
包括正整数、负整数和零。
""")

age = 25
count = 100
temperature = -5
zero = 0

print(f"年龄（整数）: {age}")
print(f"数量（整数）: {count}")
print(f"温度（负数）: {temperature}")
print(f"零: {zero}")

print("\n--- 3.3 浮点数 (float) ---")
print("""
浮点数就是带有小数部分的数字。
也可以用科学计数法表示。
""")

height = 1.75
weight = 68.5
pi = 3.14159
scientific = 2.5e3

print(f"身高（浮点数）: {height}")
print(f"体重（浮点数）: {weight}")
print(f"圆周率: {pi}")
print(f"科学计数法 2.5e3 = {scientific}")

print("\n--- 3.4 布尔值 (bool) ---")
print("""
布尔值只有两个值：True（真）和 False（假）。
常用于条件判断。
""")

is_student = True
is_adult = False
has_job = True

print(f"是学生吗？: {is_student}")
print(f"是成年人吗？: {is_adult}")
print(f"有工作吗？: {has_job}")

print("\n--- 3.5 空值 (None) ---")
print("""
None 表示空值，即什么都没有。
注意：None 不等于 0 或空字符串。
""")

result = None
print(f"空值: {result}")
print(f"空值的类型: {type(result)}")

print("\n" + "=" * 70)
print("四、type() 函数 - 查看数据类型")
print("=" * 70)
print("""
使用 type() 函数可以查看变量的数据类型。
""")

print(f"type('小明') = {type('小明')}")
print(f"type(25) = {type(25)}")
print(f"type(1.75) = {type(1.75)}")
print(f"type(True) = {type(True)}")
print(f"type(None) = {type(None)}")

print("\n" + "=" * 70)
print("五、数据类型转换")
print("=" * 70)
print("""
可以使用转换函数将一种类型转换为另一种类型：
- str() : 转换为字符串
- int() : 转换为整数
- float() : 转换为浮点数
- bool() : 转换为布尔值
""")

number = 123
str_number = str(number)
print(f"数字 {number} 转换为字符串: '{str_number}'，类型: {type(str_number)}")

text = "456"
int_text = int(text)
print(f"字符串 '{text}' 转换为整数: {int_text}，类型: {type(int_text)}")

text_float = "3.14"
float_text = float(text_float)
print(f"字符串 '{text_float}' 转换为浮点数: {float_text}，类型: {type(float_text)}")

zero = 0
bool_zero = bool(zero)
print(f"整数 0 转换为布尔值: {bool_zero}")

non_zero = 1
bool_non_zero = bool(non_zero)
print(f"整数 1 转换为布尔值: {bool_non_zero}")

empty_str = ""
bool_empty = bool(empty_str)
print(f"空字符串转换为布尔值: {bool_empty}")

non_empty_str = "hello"
bool_non_empty = bool(non_empty_str)
print(f"非空字符串转换为布尔值: {bool_non_empty}")

print("\n" + "=" * 70)
print("六、格式化输出 - f-string")
print("=" * 70)
print("""
f-string 是 Python 3.6+ 引入的格式化字符串方法，非常方便。
在字符串前加 f，然后用 {变量名} 插入变量。
""")

name = "小明"
age = 25
height = 1.75

print(f"我的名字是 {name}，今年 {age} 岁，身高 {height} 米。")
print(f"明年我将 {age + 1} 岁。")
print(f"身高的平方是 {height ** 2:.2f} 平方米。")

print("\n" + "=" * 70)
print("七、常量约定")
print("=" * 70)
print("""
Python 中没有真正的常量，但约定俗成使用全大写字母表示常量。
""")

PI = 3.1415926
GRAVITY = 9.8
MAX_STUDENTS = 50

print(f"圆周率 PI = {PI}")
print(f"重力加速度 GRAVITY = {GRAVITY}")
print(f"最大学生数 MAX_STUDENTS = {MAX_STUDENTS}")

print("\n" + "=" * 70)
print("八、练习题")
print("=" * 70)

student_name = "小红"
student_age = 20
student_height = 1.65
student_is_male = False

print(f"1. 学生姓名: {student_name}")
print(f"2. 学生年龄: {student_age}")
print(f"3. 学生年龄的类型: {type(student_age)}")
print(f"4. 学生身高: {student_height}")
print(f"5. 学生身高的类型: {type(student_height)}")
print(f"6. 学生是男生吗？: {student_is_male}")
print(f"7. 年龄转换为字符串: '{str(student_age)}'")
print(f"8. 身高转换为整数: {int(student_height)}")
print(f"9. 格式化输出: {student_name}今年{student_age}岁，身高{student_height}米")

print("\n🎉 恭喜！你已经完成了第1课的详细学习！")