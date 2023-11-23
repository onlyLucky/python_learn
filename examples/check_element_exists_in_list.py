'''
Author: fg
Date: 2023-08-06 16:08:57
LastEditors: fg
LastEditTime: 2023-08-06 17:19:57
Description: 判断元素是否在列表中存在
'''
test_list = [ 1, 6, 3, 5, 3, 4 ]

print("查看 4 是否在列表中 ( 使用循环 ) : ")

for i in test_list:
  if(i==4):
    print ("存在")

print("查看 4 是否在列表中 ( 使用 in 关键字 ) : ")

if (4 in test_list):
  print ("存在")


test_list_set = [ 1, 6, 3, 5, 3, 4 ]
test_list_bisect = [ 1, 6, 3, 5, 3, 4 ]
print("查看 4 是否在列表中 ( 使用 set() + in) : ")

test_list_set = set(test_list_set)
if 4 in test_list_set:
  print ("存在")

print("查看 4 是否在列表中 ( 使用 count()) : ")
if test_list_bisect.count(4) > 0 :
  print ("存在")

list = [1,2,3,4,5,6]
def find(keyword):
  try:
    list.index(keyword)
    print(f'{keyword}存在')
  except ValueError:
    print(f'{keyword}不存在')
find(4)