'''
Author: fg
Date: 2023-08-03 13:39:57
LastEditors: fg
LastEditTime: 2023-08-03 13:45:18
Description: 阶乘实例
'''
num = int(input("请输入一个数字："))
factorial = 1

# 查看数字是负数，0或正数
if num < 0:
  print('负数没有阶乘')
elif num == 0:
  print('0 的阶乘是1')
else:
  for i in range(1, num+1):
    factorial = factorial*i
  print('%d 的阶乘为 %d' %(num,factorial))