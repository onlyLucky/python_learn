'''
Author: fg
Date: 2023-08-06 15:52:39
LastEditors: fg
LastEditTime: 2023-08-06 15:58:36
Description: 将列表中的指定位置的两个元素对调
'''
def swapPositions(list,pos1,pos2):
  list[pos1],list[pos2] = list[pos2],list[pos1]
  return list

def swapPositions1(list,pos1,pos2):
  first_ele = list.pop(pos1)
  second_ele = list.pop(pos2-1)

  list.insert(pos1, second_ele)
  list.insert(pos2, first_ele)
  return list

List = [23, 65, 19, 90]

print(swapPositions(List, 0, 2))
print(swapPositions1(List, 0, 2))