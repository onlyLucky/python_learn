'''
Author: fg
Date: 2023-08-03 13:56:38
LastEditors: fg
LastEditTime: 2023-08-03 14:05:32
Description: 斐波那契数列
'''
# 获取用户输入数据
terms = int(input('你需要几项？'))

# 第一项和第二项
n1 = 0
n2 = 1
count = 2

# 判断输入的值是否合法
if terms <=0:
  print('请输入一个正整数。')
elif terms == 1:
  print('斐波那契数列：')
  print(n1)
else:
  print('斐波那契数列：')
  print(n1,',',n2,end=" , ")
  while count < terms:
    nth = n1 + n2
    if count == terms-1:
      print(nth)
    else:
      print(nth, end=' , ')
    # 更新值
    n1 = n2
    n2 = nth
    count += 1
