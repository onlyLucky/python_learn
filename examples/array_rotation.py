'''
Author: fg
Date: 2023-08-05 16:44:41
LastEditors: fg
LastEditTime: 2023-08-05 17:18:27
Description: 数组翻转指定个数的元素
'''
def leftRotate(arr,d,n):
  for i in range(d):
    leftRotateByOne(arr,n)

def leftRotateByOne(arr,n):
  temp = arr[0]
  print(temp)
  for i in range(n-1):
    arr[i] = arr[i+1]
  arr[n-1] = temp

def printArray(arr,size):
  for i in range(size):
    print("%d"% arr[i],end=' ')

arr = [1,2,3,4,5,6,7]
leftRotate(arr, 2,7)
printArray(arr,7)