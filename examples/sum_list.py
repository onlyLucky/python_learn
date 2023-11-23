'''
Author: fg
Date: 2023-08-06 18:02:16
LastEditors: fg
LastEditTime: 2023-08-06 18:16:58
Description: 计算列表元素之和、积
'''

total = 0
list1 = [11, 5, 17, 18, 23]

def sumOfList(list,size):
  if size == 0:
    return 0
  else:
    return list[size-1] + sumOfList(list,size-1)

total = sumOfList(list1,len(list1))

print("列表元素之和为: ", total)
  
def multiplyList(myList):
  result = 1
  for x in myList:
    result = result*x
  return result

list1 = [1, 2, 3]  
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))