'''
Author: fg
Date: 2023-08-03 15:48:57
LastEditors: fg
LastEditTime: 2023-08-03 15:57:15
Description: 最大公约数算法
'''
def hcf(x,y):
  # 获取最小值
  if x>y:
    smaller = y
  else:
    smaller = x
  
  for i in range(1,smaller+1):
    if((x%i==0) and (y%i==0)):
      hcf = i
  return hcf

# 用户输入两个数字
num1 = int(input("输入第一个数字"))
num2 = int(input("输入第二个数字"))

print( num1,"和", num2,"的最大公约数为", hcf(num1, num2))