# # 列表操作
# # 定义
# s = [56, 90, 88, 65, 90, "A", "Hello", True]
# print(type(s))
# # 访问列表元素
# # 获取
# print(s[0])# 正向索引，从0开始
# print(s[-8])# 反向索引，从-1开始
# print(s[2])
# print(s[-6])
#
# # 修改
# s[5] = "ABC"
# print(s)
# # 注意：如果指定的索引超出范围，会报错 list assignment index out of range
# # s[10] = "DEF"
# # print(s)
#
# # 删除
# del s[6]
# print(s)
#
# # 遍历
# for item in s:
#     print(item)

# # ------------------列表切片------------------
# # 定义列表
# s = ["A", "C", "H", "K", "L", "B", "D", "X", "C", "U"]
# # 切片操作 s[开始索引:结束索引:步长]
# print(s[0:5:1])
# print(type(s[0:5:1]))
#
# print(s[:5:1])
# print(s[:5:])
# print(s[:5])
#
# print(s[:5:2])
# print(s[0:-2:1])

# # -----------------列表list的常用方法----------------
# # 列表定义
# s = [56, 90, 88, 65, 90, 100, 209, 72, 145]
# print(s)
# # append():在列表尾部追加元素
# s.append(188)
# print(s)
# # insert():在指定索引之前插入元素
# s.insert(2, 80)
# print(s)
# # remove():移除列表中第一个匹配到的元素
# s.remove(90)
# print(s)
# # pop():删除列表中指定索引位置的元素并返回（如果未指定，默认删除最后一个）
# e = s.pop(1)
# print(e)
# e = s.pop()
# print(e)
# print(s)
# # sort():排序
# s.sort()
# print(s)
# # reverse():反转列表元素
# s.reverse()
# print(s)

# # ---------------列表list案例--------------
# # 案例1:
# # 1. 定义列表
# num_list = []
# # 2.存入列表
# for i in range(10):
#     num = int(input("请输入1个有效数字："))
#     num_list.append(num)
# print("数字列表：",num_list)
# # 3. 排序
# num_list.sort()
# print("排序后的数字列表：",num_list)
# # 4.输出最小值、最大值和平均值--->sum()求和；len()获取元素的个数
# print("最小值：",num_list[0])
# print("最大值：",num_list[-1])
# print("平均值：",sum(num_list)/len(num_list))

# 案例2:合并去重
"""原代码
num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
# 1. 合并列表
for num in num_list2:
    num_list1.append(num)
print("合并后的原始列表：",num_list1)
# 2. 去除重复记录
new_list = [] # 去除重复记录后的列表
for num in num_list1:
    if num not in new_list:
        new_list.append(num)
print("去除重复记录后的列表：",new_list)
"""
# 简化
"""
num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
# 1. 合并列表
# 解包：将列表这一类容器解开成一个一个独立元素
# 组包：将多个值合并到一个容器
num_list = [*num_list1, *num_list2]
print("合并后的原始列表：",num_list)
# 2. 去除重复记录
new_list = [] # 去除重复记录后的列表
for num in num_list:
    if num not in new_list:
        new_list.append(num)
print("去除重复记录后的列表：",new_list)
"""
# 方式三
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
# # 1. 合并列表
# num_list = num_list1 + num_list2
# print("合并后的原始列表：",num_list)
# # 2. 去除重复记录
# new_list = [] # 去除重复记录后的列表
# for num in num_list:
#     if num not in new_list:
#         new_list.append(num)
# print("去除重复记录后的列表：",new_list)

# # 案例3:生成1-20的平方列表---> range(1,21)
# # 方式一：
# num_list = []
# for i in range(1,21):
#     num_list.append(i**2)
# print(num_list)
# # 方式二：列表推导式--->按照一定的规则快速生成一个列表的方法--->语法格式1:[要插入的值 for i in 序列/列表]
# num_list2 = [i**2 for i in range(1,21)]
# print(num_list2)

# # 案例4:从一个数字列表中提取所有偶数，并计算其平方，组成一个新的列表--->判断偶数：num % 2 == 0
# # 列表推导式--->按照一定的规则快速生成一个列表的方法--->语法格式2:[要插入的值 for i in 序列/列表 if 条件]
# num_list = [12, 32, 45, 77, 80, 92, 33, 57, 97, 98, 110, 111, 122]
# new_list = [i**2 for i in num_list if i % 2 == 0]
# print(new_list)

# # 练习1:合并去重排序
# list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
# list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
# list3 = ['W', 'A', 'S', 'D']
# new_list1 = list1 +list2 +list3
# print(new_list1)
# new_list2 = []
# for num in new_list1:
#     if num not in new_list2:
#         new_list2.append(num)
# print(new_list2)
# new_list2.sort()
# print(new_list2)

# # 练习2:将下面序列中能被3或5整除的元素提出来，获取平方组成新列表
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# list2 = [i**2 for i in list1 if i % 3 == 0 or i % 5 == 0]
# print(list2)

# 练习3:将如下列表中的正数提取出来，封装成一个新的列表
list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
list2 = [i for i in list1 if i > 0]
print(list2)
