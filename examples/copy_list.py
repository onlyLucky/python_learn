'''
Author: fg
Date: 2023-08-06 17:30:17
LastEditors: fg
LastEditTime: 2023-08-06 17:52:14
Description: 复制列表
'''
def clone_list(li1):
  li_copy = li1[:]
  return li_copy

def clone_list1(li1):
  li_copy = []
  li_copy.extend(li1)
  return li_copy

def clone_list2(li1):
  li_copy = list(li1)
  return li_copy
 
li1 = [4, 8, 2, 10, 15, 18] 
li2 = clone_list(li1)
li3 = clone_list1(li1)
li4 = clone_list2(li1)
print("原始列表:", li1)
print("复制后列表:", li2)
print("复制后列表:", li3)
print("复制后列表:", li4)