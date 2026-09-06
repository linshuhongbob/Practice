# 选择题 3.1
print("1.B ;2.B ;3.C ;4.A ;5.B ;6.B ;7.A ;8.C ;9.B ;10.B")

print("-" * 100)

# 必做编程题 3.2 (1)
num1 = int(input("请输入第一个整数: "))
num2 = int(input("请输入第二个整数: "))
print(f"乘积: {num1 * num2}")
print(f"整除结果: {num1 // num2}")
print(f"取余结果: {num1 % num2}")

print("-" * 100)

# 必做编程题 3.2 (2)
num = int(input("请输入一个整数: "))
print(f"{num}的平方: {num ** 2}, 立方: {num ** 3}")

print("-" * 100)

# 必做编程题 3.2 (3)
score = 85
if score >= 60:
    print("及格")
else:
    print("不及格")

print("-" * 100)

# 必做编程题 3.2 (4)
MyFloat = float(input("请输入一个小数: "))
if 0 <= MyFloat <= 100:
    print(f"{MyFloat}在0到100之间")
else:
    print(f"{MyFloat}不在0到100之间")

print("-" * 100)

# 必做编程题 3.2 (5)
MyInt = int(input("请输入一个整数: "))
if MyInt % 3 == 0 and MyInt % 5 == 0:
    print(f"{MyInt}能同时被3和5整除")
else:
    print(f"{MyInt}不能同时被3和5整除")

print("-" * 100)

# 必做编程题 3.2 (6)
a = 10
a += 5
a -= 3
print("a的最终结果为:",a)

print("-" * 100)

# 必做编程题 3.2 (7)
Year = int(input("请输入年份: "))
if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print(f"{Year}是闰年")
else:
    print(f"{Year}不是闰年")

print("-" * 100)

# 必做编程题 3.2 (8)
a = int(input("请输入第一个整数a: "))
b = int(input("请输入第二个整数b: "))
c = b
b = a
a = c
print(f"交换后: a={a}, b={b}")

print("-" * 100)

# 选做编程题 3.3 (1)
StudentScore = int(input("请输入成绩 (0-100) : "))
if 90 <= StudentScore <= 100:
    print("优秀")
elif 80 <= StudentScore <= 89:
    print("良好")
elif 70 <= StudentScore <= 79:
    print("中等")
elif 60 <= StudentScore <= 69:
    print("及格")
elif 0 <= StudentScore <= 59:
    print("不及格")
else:
    print("输入无效")

print("-" * 100)

# 选做编程题 3.3 (2)
Num = int(input("请输入一个整数: "))
if Num > 0:
    print("正数")
elif Num < 0:
    print("负数")
else:
    print("0")

print("-" * 100)

# 选做编程题 3.3 (3)
Day = int(input("请输入1-7的数字: "))
match Day:
    case 1:
        print("周一")
    case 2:
        print("周二")
    case 3:
        print("周三")
    case 4:
        print("周四")
    case 5:
        print("周五")
    case 6:
        print("周六")
    case 7:
        print("周日")
    case _:
        print("输入无效")