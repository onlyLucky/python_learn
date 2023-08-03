'''
Author: fg
Date: 2023-08-03 11:13:22
LastEditors: fg
LastEditTime: 2023-08-03 11:21:21
Description: 判断闰年
'''
year = int(input('输入一个年份：'))
if (year % 4) == 0:
  if(year % 100) == 0:
    if(year % 400) == 0:
      print('{0} 是闰年'.format(year)) # 整百年能被400整除为闰年
    else:
      print('{0} 不是闰年'.format(year))
  else:
    print('{0} 是闰年'.format(year)) # 非整百年能被4整除的为闰年
else:
  print('{0} 不是闰年'.format(year))

