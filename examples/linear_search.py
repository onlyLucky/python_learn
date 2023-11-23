'''
Author: fg
Date: 2023-08-08 09:44:09
LastEditors: fg
LastEditTime: 2023-08-08 09:53:35
Description: 线性查找
'''
def search(arr,n,x):
  for i in range (0,n):
    if(arr[i] == x):
      return i
  return -1

arr = [ 'A', 'B', 'C', 'D', 'E' ] 
x = 'D' 
n = len(arr) 
result = search(arr, n, x) 
if(result == -1): 
  print("元素不在数组中") 
else: 
  print("元素在数组中的索引为", result)