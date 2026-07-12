print("=" * 70)
print("Python 第2课：数学运算（详细讲解）")
print("=" * 70)

print("\n" + "=" * 70)
print("一、基本算术运算")
print("=" * 70)
print("""
Python 支持所有基本的数学运算：
+  加法
-  减法
*  乘法
/  除法（结果是浮点数）
// 整除（结果是整数）
%  取余（求余数）
** 幂运算（次方）
""")

a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

print("\n--- 除法 vs 整除 ---")
print("""
注意：
- /  除法：结果总是浮点数，哪怕能整除
- // 整除：结果是整数，小数部分会被丢弃
""")

print(f"10 / 2 = {10 / 2}   → 浮点数")
print(f"10 // 2 = {10 // 2} → 整数")
print(f"10 / 3 = {10 / 3}   → 浮点数")
print(f"10 // 3 = {10 // 3} → 整数（丢弃小数）")

print("\n--- 取余运算 ---")
print("""
% 是求余数，比如：
10 除以 3，商是 3，余数是 1
所以 10 % 3 = 1
""")

print(f"7 % 3 = {7 % 3}   → 7除以3余1")
print(f"10 % 2 = {10 % 2} → 10除以2余0（能整除）")
print(f"5 % 7 = {5 % 7}   → 5除以7商0余5")

print("\n--- 幂运算 ---")
print("""
** 是次方运算：
a ** b 表示 a 的 b 次方
""")

print(f"2 ** 10 = {2 ** 10}   → 2的10次方")
print(f"10 ** 3 = {10 ** 3}   → 10的3次方")
print(f"3 ** 4 = {3 ** 4}     → 3的4次方")
print(f"25 ** 0.5 = {25 ** 0.5} → 25的平方根")

print("\n" + "=" * 70)
print("二、运算符优先级")
print("=" * 70)
print("""
和数学一样，Python也有运算优先级：
1. 括号 ()
2. 幂运算 **
3. 乘法 *、除法 /、整除 //、取余 %
4. 加法 +、减法 -

口诀：先乘除后加减，有括号先算括号里的
""")

print(f"2 + 3 * 4 = {2 + 3 * 4}")
print(f"(2 + 3) * 4 = {(2 + 3) * 4}")
print(f"10 / 2 + 3 = {10 / 2 + 3}")
print(f"10 / (2 + 3) = {10 / (2 + 3)}")
print(f"2 ** 3 * 4 = {2 ** 3 * 4}")
print(f"2 ** (3 * 4) = {2 ** (3 * 4)}")

print("\n" + "=" * 70)
print("三、赋值运算符")
print("=" * 70)
print("""
赋值运算符可以简化代码：
x = x + 5  等价于  x += 5
x = x - 5  等价于  x -= 5
x = x * 5  等价于  x *= 5
x = x / 5  等价于  x /= 5
x = x // 5 等价于  x //= 5
x = x % 5  等价于  x %= 5
x = x ** 5 等价于  x **= 5
""")

x = 10
print(f"x 初始值: {x}")

x += 5
print(f"x += 5 后: {x}")

x *= 2
print(f"x *= 2 后: {x}")

x -= 3
print(f"x -= 3 后: {x}")

x /= 2
print(f"x /= 2 后: {x}")

print("\n" + "=" * 70)
print("四、比较运算符")
print("=" * 70)
print("""
比较运算符用于比较两个值，返回布尔值（True/False）：
>   大于
<   小于
>=  大于等于
<=  小于等于
==  等于
!=  不等于
""")

score = 85
print(f"分数 = {score}")
print(f"score > 90 ? {score > 90}")
print(f"score >= 80 ? {score >= 80}")
print(f"score < 60 ? {score < 60}")
print(f"score == 85 ? {score == 85}")
print(f"score != 100 ? {score != 100}")

print("\n--- 注意：== 和 = 的区别 ---")
print("""
=  是赋值运算符，把右边的值赋给左边的变量
== 是比较运算符，判断两边是否相等

x = 5    → 把5赋给x
x == 5   → 判断x是否等于5，返回True或False
""")

print("\n" + "=" * 70)
print("五、逻辑运算符")
print("=" * 70)
print("""
逻辑运算符用于组合多个条件：
and  → 逻辑与（两边都为True才返回True）
or   → 逻辑或（只要有一边为True就返回True）
not  → 逻辑非（取反）
""")

age = 25
has_job = True

print(f"age = {age}, has_job = {has_job}")
print(f"age > 18 and has_job: {age > 18 and has_job}")
print(f"age > 18 or has_job: {age > 18 or has_job}")
print(f"not has_job: {not has_job}")
print(f"age > 30 and has_job: {age > 30 and has_job}")
print(f"age > 30 or has_job: {age > 30 or has_job}")

print("\n" + "=" * 70)
print("六、数学函数")
print("=" * 70)
print("""
Python 内置了一些常用的数学函数：
abs()    → 绝对值
round()  → 四舍五入
max()    → 最大值
min()    → 最小值
pow()    → 幂运算（和 ** 一样）
""")

print(f"abs(-10) = {abs(-10)}")
print(f"abs(5 - 15) = {abs(5 - 15)}")
print(f"round(3.14159) = {round(3.14159)}")
print(f"round(3.14159, 2) = {round(3.14159, 2)}")
print(f"max(1, 3, 5, 2) = {max(1, 3, 5, 2)}")
print(f"min(1, 3, 5, 2) = {min(1, 3, 5, 2)}")
print(f"pow(2, 10) = {pow(2, 10)}")

print("\n" + "=" * 70)
print("七、数学模块 math")
print("=" * 70)
print("""
Python 的 math 模块提供了更多数学函数：
math.sqrt()    → 平方根
math.pi        → 圆周率
math.sin()     → 正弦
math.cos()     → 余弦
math.log()     → 对数
math.exp()     → 指数
""")

import math

print(f"math.pi = {math.pi}")
print(f"math.sqrt(25) = {math.sqrt(25)}")
print(f"math.sqrt(2) = {math.sqrt(2)}")
print(f"math.sin(math.pi / 2) = {math.sin(math.pi / 2)}")
print(f"math.cos(0) = {math.cos(0)}")
print(f"math.log(10) = {math.log(10)}")
print(f"math.exp(1) = {math.exp(1)}")

print("\n" + "=" * 70)
print("八、练习题")
print("=" * 70)

width = 8
height =
print(f"1. 长方形面积（宽={width}, 高={height}）: {width * height}")

radius = 10
print(f"2. 圆的面积（半径={radius}）: {math.pi * radius ** 2:.2f}")

num1 = 17
num2 = 5
print(f"3. {num1} 除以 {num2}: 商={num1 // num2}, 余数={num1 % num2}")

x = 2
print(f"4. {x} 的平方根: {math.sqrt(x):.4f}")

temperature = -15
print(f"5. 温度 {temperature}°C 的绝对值: {abs(temperature)}")

print("\n🎉 恭喜！你已经完成了第2课的学习！")