# """
# 案例2:猜数字游戏
# """
# import random
# random_number = random.randint(1,100)# 生成随机数
# while True:
#     num = int(input("请输入一个数字："))
#     if num > random_number:
#         print("您输入的数字太大了！")
#     elif num < random_number:
#         print("您输入的数字太小了！")
#     else:
#         print("恭喜您，猜对了！")
#         break # 跳出循环
# print("随机生成的数字是：",random_number)

# # 练习
# # 需求1:将1-1000之间（含1000）所有的5的倍数的数字累加起来
# total = 0
# for i in range(1,1001):
#     if i % 5 == 0:
#         total += i
# print("1-1000之间（含1000）所有5的倍数之和为：",total)

# 需求2:统计字符串"akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"字符串中有多少个a和k
total = 0
stri = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
for i in stri:
    if i == "a" or i == "k":
        total += 1
print(f"字符串中有{total}个a和k")