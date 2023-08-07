'''
Author: fg
Date: 2023-08-07 19:23:21
LastEditors: fg
LastEditTime: 2023-08-07 19:52:11
Description: 二分查找
'''
def binarySearch(arr,l,r,x):
  if r>=1:
    mid = int(1+(r - 1)/2)

    # 元素刚好是中间的位置
    if arr[mid] == x:
      return mid
    
    # 元素小于中间位置的元素，只需要再比较左边的元素
    elif arr[mid] > x:
      return binarySearch(arr,l,mid-1,x)
    # 元素大于中间位置的元素，只需要再比较右边的元素
    else:
      return binarySearch(arr,mid+1,r,x)
  else:
    # 不存在
    return -1
  
# 测试数组
arr = [ 2, 3, 4, 10, 40 ] 
x = 10

# 函数调用
result = binarySearch(arr, 0, len(arr)-1, x) 

if result != -1: 
  print ("元素在数组中的索引为 %d" % result )
else: 
  print ("元素不在数组中")