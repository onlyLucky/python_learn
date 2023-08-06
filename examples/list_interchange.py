'''
Author: fg
Date: 2023-08-05 17:26:34
LastEditors: fg
LastEditTime: 2023-08-06 15:50:54
Description: 列表中的头尾两个元素对调
'''
def swapList(newList):
  size = len(newList)
  temp = newList[0]
  newList[0] = newList[size-1]
  newList[size-1] = temp

  return newList

newList = [1,2,3,4]

print(swapList(newList))