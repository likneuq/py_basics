# # for循环：遍历输入的字符串
# msg = input("请输入需要遍历的字符串：")
# for s in msg:
#     print(f"元素：{s}")
# else:
#     print("遍历结束")

# 案例1：1-100
# total = 0
# #原始：
# # for i in range(1,101):
# #     if i % 2 == 1:
# #         total += i
# #简化
# for i in range(1,101,2):
#     total += i
# print("1-100之间的奇数累加之和：",total)

# #案例2:100-500
# total = 0
# for i in range(100,501):
#     if i % 3 == 0:
#         total += i
# print("100-500之间所有3的倍数累加之和：",total)

"""
    嵌套循环：m*n的长方形
"""
# #1.接受键盘录入
# m = int(input("请输入长方形的长度："))
# n = int(input("请输入长方形的宽度："))
# #2.打印长方形
# for j in range(n):
#     for i in range(m):
#         print("*",end=" ")
#     print()

# # 嵌套循环案例：打印99乘法表
# for i in range(1,10):# 外层循环控制行
#     for j in range(1,i + 1):# 内层循环控制列
#         print(f"{j} x {i} = {j * i}",end="\t")
#     print()

# # 练习：
# # 需求1:打印等腰直角三角形
# n = int(input("请输入直角边边长："))
# for i in range(n):
#     for j in range(i+1):
#         print("*", end="\t")
#     print()

# # 需求2:打印数字金字塔
# n = int(input("请输入数字："))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end="\t")
#     print()

# 需求3:打印国际象棋棋盘□ ■
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("■",end="\t")
        else:
            print("□",end="\t")
    print()