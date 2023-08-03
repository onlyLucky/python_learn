'''
Author: fg
Date: 2023-08-03 16:25:11
LastEditors: fg
LastEditTime: 2023-08-03 16:38:09
Description: 使用递归斐波那契数列
'''
def recur_fibonacci(n):
  if n<=1:
    return n
  else:
    return(recur_fibonacci(n-1)+recur_fibonacci(n-2))

# 获取用户输入
terms = int(input('您要输出几项？'))

# 检查输入的数字是否正确
if terms <= 0:
  print("输入正数")
else:
  print("斐波那契数列：")
  for i in range(terms):
    print(recur_fibonacci(i))