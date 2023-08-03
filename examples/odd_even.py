'''
Author: fg
Date: 2023-08-03 11:09:40
LastEditors: fg
LastEditTime: 2023-08-03 11:12:28
Description: 判断奇数偶数
'''
num = int(input('输入一个数字：'))
if(num%2)==0:
  print('{0}是偶数'.format(num))
else:
  print('{0}是奇数'.format(num))