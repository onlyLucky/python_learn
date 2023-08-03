'''
Author: fg
Date: 2023-08-03 11:26:50
LastEditors: fg
LastEditTime: 2023-08-03 11:33:21
Description: 质数判断
'''
num = int(input('请输入一个数字: '))

if(num>1):
  # 查看因子
  for i in range(2, num):
    if(num % i) == 0:
      print(num,"不是质数")
      print(i,'乘于',num//i,'是',num)
      break
  else:
    print(num,'是质数')
# 如果输入的数字小于或等于 1，不是质数
else:
  print(num,'不是质数')