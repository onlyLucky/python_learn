'''
Author: fg
Date: 2023-08-04 10:16:48
LastEditors: fg
LastEditTime: 2023-08-04 11:31:41
Description: 计算 n 个自然数的立方和
'''

def sumOfSeries(n):
  sum = 0
  for i in range(1,n+1):
    sum+=i*i*i
  return sum
n=5
print(sumOfSeries(n))