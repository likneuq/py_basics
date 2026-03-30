# """
# 案例1:登录
# 关键字：
#     break：只能出现在循环中，表示结束或跳出循环(break跳出循环后，while后面的else代码不会执行)
#     continue：只能出现在循环中，表示中断本次循环，直接进入下一轮循环
# """
# while True:
#     # 1.接收输入的用户名和密码
#     username = input("请输入正确的用户名：")
#     password = input("请输入正确的密码：")
#     # 2.校验：输入的用户名和密码不能为空
#     if username == "" or password == "":
#         print("输入的用户名和密码不能为空！请重新输入")
#         continue
#     # 3.判断用户名和密码的正确性，执行登录操作
#     if username == "admin" and password == "666888":
#         print("登录成功，进入B站首页～")
#         break
#     elif username == "zhangsan" and password == "123456":
#         print("登录成功，进入B站首页～")
#         break
#     elif username == "taoge" and password == "888666":
#         print("登录成功，进入B站首页～")
#         break
#     else:
#         print("用户名或密码错误，请重新输入！")

# 练习：
for i in range(5):
    username = input("请输入正确的用户名：")
    password = input("请输入正确的密码：")
    if username == "admin" and password == "666888":
        print("登录成功，进入B站首页～")
        break
    elif username == "zhangsan" and password == "123456":
        print("登录成功，进入B站首页～")
        break
    elif username == "taoge" and password == "888666":
        print("登录成功，进入B站首页～")
        break
    else:
        print("用户名或密码错误，请重新输入！")
        if i == 4:
            print("输入错误五次，不允许再登录")
            break