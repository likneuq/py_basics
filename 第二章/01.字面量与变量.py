#字面量的写法
# print(100)#整数(int)
# print(3.14)#浮点数/小数(float)
# print(True)#布尔(bool)
# print(False)#布尔(bool)
# print("Hello Python")#字符串(str)
# print("-----------------")#字符串(str)
# print(None)#空值(NoneType)
#
# #布尔类型本质也是整数类型(True - 1;False - 0)
# print(True + 1)#2
# print(False - 1)#-1

#变量 ---> Python是动态类型语言，一个变量是可以存储不同类型的数据的(但是项目开发中，推荐变量值存储一种类型的变量)
# num = 1114.1
# print(num)
#
# num = num + 1
# print(num)
#
# num = "OK"
# print(num)
#
# num = True
# print(num)

#案例
# base = 20.7#基础播放量
# incr = 50#每一个月新增播放量
# print("未来第一个月的播放量:",base + incr)
# print("未来第二个月的播放量:",base + incr + incr)
#
# #案例 - 升级：一次性可以定义多个变量
# base,incr = 20.7,50
# print("未来第一个月的播放量:",base + incr)
# print("未来第二个月的播放量:",base + incr + incr)

#标识符
# true = 1
# print(true)

#案例一:
# a = 10
# b = 20
#
# c = a # c = 10
# a = b # a = 20
# b = c # b = 10
# print(a, b)

#练习
a = 100
b = 200
c = 300
d = a # d = 100
e = c # e = 300
c = d # c = a = 100
d = b # d = 200
a = d # a = b = 200
b = e # b = c = 300
print(c,a,b)
