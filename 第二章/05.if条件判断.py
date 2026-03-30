# # if条件判断
# score = 700
# if score > 680:
#     print("欢迎你来清华读书")
#     print("也恭喜你即将踏入精彩的大学生活")
# print("-----------------------------")

# # 案例：输入密码后登录B站
# ok_account = "18888888888"
# ok_password = "666888"
# # 1.接受用户输入的账号密码
# account = input("请输入您的B站账号：")
# password = input("请输入您的B站密码：")
# # 2.判断账号密码是否正确
# if account == ok_account and password == ok_password:
#     print("登录成功～")
#     print("进入B站首页～")
# # 3.判断是否有错
# if account != ok_account or password != ok_password:
#     print("登录失败～")
#     print("帐号或密码错误！")

# # if..else..案例：输入密码后登录B站
# ok_account = "18888888888"
# ok_password = "666888"
# # 1.接受用户输入的账号密码
# account = input("请输入您的B站账号：")
# password = input("请输入您的B站密码：")
# # 2.判断账号密码是否正确
# if account == ok_account and password == ok_password:
#     print("登录成功～")
#     print("进入B站首页～")
# else:
#     print("登录失败～")
#     print("帐号或密码错误！")

# # 案例1:闰年平年
# year = int(input("请输入需要判定的年份："))
# if (year % 100 != 0 and year % 4 == 0) or (year % 400) == 0:
#     print("f{year}是闰年")
# else:
#     print("f{year}是平年")

# # 需求1:
# num = int(input("请输入整数："))
# if num % 2 == 0:
#     print("您输入的是偶数")
# else:
#     print("您输入的是奇数")

# # 需求2:
# age = int(input("请输入您的年龄："))
# if age >= 18:
#     print("已成年")
# else:
#     print("未成年")

# # 需求3:
# num = int(input("请输入数字："))
# if num > 0:
#     print(f"{num}正数")
# elif num < 0:
#     print(f"{num}负数")
# else:
#     print(f"{num}=0")

# # 需求4:
# score = int(input("请输入考试分数："))
# if score >= 60:
#     print("及格")
# else:
#     print("不及格")

# # 案例：
# username = input("请输入用户名：")
# password = input("请输入密码：")
# if username == "admin" and password == "666888":
#     print("登录成功")
# elif username == "root" and password == "547527":
#     print("登录成功")
# elif username == "zhangsan" and password == "123456":
#     print("登录成功")
# else:
#     print("登录失败，用户名或密码错误")

# # 需求1:
# score = int(input("请输入考试成绩："))
# if score >= 85:
#     print("优秀")
# elif 60 <= score < 85:
#     print("及格")
# else:
#     print("不及格")

# # 需求2:
# amount = int(input("请输入商品总额："))
# if amount >= 500:
#     print("8折")
# elif 300 <= amount < 500:
#     print("9折")
# elif 100 <= amount < 300:
#     print("95折")
# else:
#     print("无折扣")

# """
# 案例：
# 三角形类型判断-pass是空语句
# """
# a = int(input("请输入第一个边的边长："))
# b = int(input("请输入第二个边的边长："))
# c = int(input("请输入第三个边的边长："))
# if a + b > c and b + c > a and c + a > b:
#     if a == b == c:
#         print(f"{a} {b} {c}这三个边长构成等边三角形")
#     elif a == b or b == c or a == c:
#         print(f"{a} {b} {c}这三个边长构成等腰三角形")
#     else:
#         print(f"{a} {b} {c}这三个边长构成普通三角形")
# else:
#     print(f"{a} {b} {c}这三个边长不能构成三角形")

# 练习：
ele = float(input("请输入用电度数："))
if ele < 2880:
    amount = ele * 0.4883
    print(f"电费为{amount}")
elif 2880 <= ele < 4800:
    amount = 2880 * 0.4883 + (ele-2880) * 0.5383
    print(f"电费为{amount}")
else:
    amount = 2880 * 0.4883 + (4800 - 2880) * 0.5383 + (ele-4800) * 0.7883
    print(f"电费为{amount}")