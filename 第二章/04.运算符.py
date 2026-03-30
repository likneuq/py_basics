# # 算术运算符
# print("10 + 4 = ", 10 + 4) # 加
# print("10 - 4 = ", 10 - 4) # 减
# print("10 * 4 = ", 10 * 4) # 乘
# print("10 / 4 = ", 10 / 4) # 除
# print("10 // 4 = ", 10 // 4) # 整除
# print("10 % 4 = ", 10 % 4) # 取余
# print("10 ** 4 = ", 10 ** 4) # 幂指数
#
# # 算术运算符的优先级
# print("0.1 + 10 / 4 ** 2 = ", 0.1 + 10 / 4 ** 2)

# # 案例一
# # float(..)
# x = float(input("输入x:"))
# y = float(input("输入y:"))
# print("x + y =",x + y)
# print("x - y =",x - y)

# # 案例1
# x = int(input("输入x："))
# y = int(input("输入y："))
# z = int(input("输入z："))
# print("平均数为：",(x + y + z)/3)

# # 案例2
# x = int(input("输入上底x："))
# y = int(input("输入下底y："))
# h = int(input("输入高h："))
# print("梯形面积为：",((x + y) * h) / 2)

# # 案例3
# r = int(input("输入圆的半径r："))
# print("圆的周长为：",2 * 3.14 * r )
# print("圆的面积为：",3.14 * r ** 2)

# # 案例4
# m = float(input("请输入体重m："))
# h = float(input("请输入身高h："))
# print("BMI = ",m / h ** 2)

# #赋值运算符
# num = 85
# num += 10
# print("num += 10 后，num = ",num)
# num -= 10
# print("num -= 10 后，num = ",num)
# num *= 10
# print("num *= 10 后，num = ",num)
# num /= 10
# print("num /= 10 后，num = ",num)
# num //= 10
# print("num //= 10 后，num = ",num)
# num %= 3
# print("num %= 3 后，num = ",num)
# num **= 3
# print("num **= 3 后，num = ",num)

# # 比较运算符
# print("100 == 100 吗：",100 == 100)
# print("'100' == '100' 吗：","100" == "100")
# print("100 != 100 吗：",100 != 100)
# print("100 < 100 吗：",100 < 100)
# print("100 <= 100 吗：",100 <= 100)
# print("100 > 100 吗：",100 > 100)
# print("100 >= 100 吗：",100 >= 100)

# # 逻辑运算符
# # 案例一
# n = int(input("请输入一个整数："))
# print(f"{n}在10-20之间：",n >= 10 and n <= 20)
# print(f"{n}在10-20之间：", 10 <= n <= 20)

# 案例二
n = int(input("请输入一个整数："))
print(f"{n}不在10-20之间：",n < 10 or n > 20)