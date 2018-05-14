'''
@author: ldc
'''
print("hello world")
# ctrl +/
# ctrl +d 复制当前行
#
print("hello","你好")
# 使用”,“进行连接

print("he" + "llo")
# 字符串相加，进行字符串的连接，且不产生空格

print(10+30)
# 没有使用引号括起来，默认为数值，若是使用引号括起来，就是字符串
# 若是数值使用加号连接，默认是表达式进行计算，返回计算的结果

print("hello"+"ni hao")
# 不同类型的数据不能使用加号连接
# 不同类型的数据能够使用”,“进行连接
print("1 2 3",2+3)
# 输入
# input()
# 带有提示信息的输入
# name = input("请输入您的姓名：")
# print(name)

# 作业：要求：1、输入姓名，2、输入年龄，3、打印出来，类似自我介绍
# name = input("请输入您的姓名：")
# age = input("请输入您的年龄：")
# print("hello I am "+name+"I am "+age)
# print("你好，我是",name,"我今年",age)

# bin(10) 十进制转换成二进制 ,带0b
a = bin(10)
print(a)
# '{0:b}'.format(10) 十进制转换成二进制 ,不带0b
b = '{0:b}'.format(10)
print(b)
# oct(10) 十进制转八进制
int("1010",2)
eval("0b10")
# eval函数比int函数慢，不推荐使用
