# 选择题 4.1
print("1.B ; 2.C ; 3.A ; 4.C ; 5.B ; 6.B ; 7.B ; 8.C ; 9.A ; 10.A")

print("-" * 100)

# 编程题 4.2 (1)

List = [18,7,25,32,9,41,12]
even_list = []
odd_list = []
Sum = 0
for i in List:
    if i % 2 == 0:
        even_list.append(i)
        Sum += i
EvenAvg = Sum / len(even_list)
for j in List:
    if j % 2 == 1:
        odd_list.append(j)
Maximum = max(odd_list)
print(f"偶数列表: {even_list}, 偶数平均值: {EvenAvg}, 奇数列表: {odd_list}, 奇数最大值: {Maximum}")

print("-" * 100)

# 编程题 4.2 (2)
NewList = ["I", "love", "Python", "is", "easy", "to", "learn", "Pythonic", "is", "not", "Python"]
Count = 0
i = 0
Target_Number = input("请输入你的目标单词: ")
while i < len(NewList):
    if NewList[i] == Target_Number:
        Count += 1
    i += 1
print(f"{Target_Number}出现的个数为: {Count}")