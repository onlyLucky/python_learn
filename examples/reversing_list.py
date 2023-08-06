'''
Author: fg
Date: 2023-08-06 15:59:03
LastEditors: fg
LastEditTime: 2023-08-06 16:07:52
Description: 翻转列表
'''

def Reverse(lst):
  return [ele for ele in reversed(lst)]

def Reverse1(lst):
  lst.reverse()
  return lst

def Reverse2(lst):
  new_lst = lst[::-1]
  return new_lst

def fanZhuAn(list):
  a=[]
  i=len(list)
  while i>0:
    a.append(list[i-1])
    i-=1
  return a


lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))
print(Reverse1(lst))
print(Reverse2([10, 11, 12, 13, 14, 15]))
print(fanZhuAn([34,12,54,234,65,122]))

li = [*range(10,16)]
print(li)

#降序排列
li.sort(reverse=True)
print(li)

