'''
Author: fg
Date: 2023-08-08 10:53:02
LastEditors: fg
LastEditTime: 2023-08-08 11:26:17
Description: 快速排序
'''
'''
description: 
param {*} arr   排序数组
param {*} low   起始索引
param {*} high  结束索引
return {*}
'''
def partition(arr,low,high):
  i = (low - 1)
  pivot = arr[high]

  for j in range(low,high):
    # 当前元素小于或等于 pivot
    if arr[j]<=pivot:
      i = i+1
      arr[i],arr[j] = arr[j],arr[i]
  arr[i+1],arr[high] = arr[high],arr[i+1]
  return ( i+1 )

# 快速排序函数
def quickSort(arr,low,high):
  if low < high:
    pi = partition(arr,low,high)
    print(pi)
    quickSort(arr,low,pi-1)
    quickSort(arr,pi+1,high)

arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("排序后的数组:") 
for i in range(n): 
  print ("%d" %arr[i])