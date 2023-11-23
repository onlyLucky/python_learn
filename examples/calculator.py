'''
Author: fg
Date: 2023-08-03 16:03:54
LastEditors: fg
LastEditTime: 2023-08-03 16:13:57
Description: 简单计算器实现
'''
# 定义函数
def add(x,y):
  # 注释
  """相加"""
  return x+y

def subtract(x,y):
  """相减"""
  return x-y

def multiply(x,y):
  """相乘"""
  return x*y

def divide(x,y):
  """相除"""
  return x/y

# 用户输入
print("选择运算：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")

choice = input("输入你的选择(1/2/3/4):")

num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

match choice:
  case '1':
    print(num1,"+",num2,"=", add(num1,num2))
  case '2':
    print(num1,"-",num2,"=", subtract(num1,num2))
  case '3':
    print(num1,"*",num2,"=", multiply(num1,num2))
  case '4':
    print(num1,"/",num2,"=", divide(num1,num2))
  case _:
    print("非法输入")