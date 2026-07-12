print("=" * 50)
print("Python 练习：简单计算器")
print("=" * 50)

num1 = 50
num2 = 10

print(f"第一个数字: {num1}")
print(f"第二个数字: {num2}")
print(f"\n{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("除数不能为零！")

print("\n" + "=" * 50)
print("Python 练习：学生成绩统计")
print("=" * 50)

students = [
    {"name": "小明", "score": 95},
    {"name": "小红", "score": 88},
    {"name": "小刚", "score": 76},
    {"name": "小丽", "score": 92},
    {"name": "小强", "score": 85},
]

total_score = 0
for student in students:
    total_score += student["score"]
    print(f"{student['name']}: {student['score']}分")

average_score = total_score / len(students)
print(f"\n平均分: {average_score:.2f}分")

print("\n" + "=" * 50)
print("Python 练习：猜数字游戏")
print("=" * 50)

target_number = 42
guess = 10

print(f"目标数字是: {target_number}")
print(f"你的猜测是: {guess}")

if guess == target_number:
    print("🎉 恭喜！猜对了！")
elif guess < target_number:
    print("📈 猜小了！")
else:
    print("📉 猜大了！")