'''
Author: fg
Date: 2023-08-06 17:55:42
LastEditors: fg
LastEditTime: 2023-08-06 17:59:01
Description: 计算元素在列表中出现的次数
'''
def countX(lst,x):
  count = 0
  for ele in lst:
    if ele == x:
      count = count + 1
  return count

def countX1(lst,x):
  return lst.count(x)

lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
print(countX(lst, 8))
print(countX1(lst, 8))