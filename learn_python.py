print("=" * 50)
print("Python 基础学习 - 第1课：变量和数据类型")
print("=" * 50)

name = "小明"
age = 25
height = 1.75
is_student = True

print(f"姓名: {name}")
print(f"年龄: {age}")
print(f"身高: {height}")
print(f"是学生: {is_student}")

print("\n" + "=" * 50)
print("Python 基础学习 - 第2课：数学运算")
print("=" * 50)

a = 10
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

print("\n" + "=" * 50)
print("Python 基础学习 - 第3课：字符串操作")
print("=" * 50)

message = "Hello, Python!"
print(f"原始字符串: {message}")
print(f"字符串长度: {len(message)}")
print(f"大写: {message.upper()}")
print(f"小写: {message.lower()}")
print(f"替换: {message.replace('Python', '世界')}")
print(f"切片前5个字符: {message[:5]}")

print("\n" + "=" * 50)
print("Python 基础学习 - 第4课：列表")
print("=" * 50)

fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print(f"水果列表: {fruits}")
print(f"第一个水果: {fruits[0]}")
print(f"最后一个水果: {fruits[-1]}")
print(f"前两个水果: {fruits[:2]}")

fruits.append("草莓")
print(f"添加草莓后: {fruits}")

fruits[1] = "芒果"
print(f"替换香蕉为芒果后: {fruits}")

print("\n" + "=" * 50)
print("Python 基础学习 - 第5课：条件判断")
print("=" * 50)

score = 85
if score >= 90:
    print(f"分数 {score}：优秀！")
elif score >= 80:
    print(f"分数 {score}：良好！")
elif score >= 60:
    print(f"分数 {score}：及格！")
else:
    print(f"分数 {score}：不及格！")

print("\n" + "=" * 50)
print("Python 基础学习 - 第6课：循环")
print("=" * 50)

print("for 循环遍历列表:")
for fruit in fruits:
    print(f"  - {fruit}")

print("\nfor 循环计数:")
for i in range(1, 6):
    print(f"  数字 {i}")

print("\nwhile 循环:")
count = 1
while count <= 5:
    print(f"  计数 {count}")
    count += 1

print("\n" + "=" * 50)
print("Python 基础学习 - 第7课：函数")
print("=" * 50)

def greet(name):
    return f"你好, {name}!"

result = greet("小明")
print(result)

def add(a, b):
    return a + b

print(f"3 + 5 = {add(3, 5)}")

print("\n🎉 恭喜！你已经完成了 Python 基础学习！")