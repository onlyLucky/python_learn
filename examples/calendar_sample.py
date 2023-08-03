'''
Author: fg
Date: 2023-08-03 16:15:04
LastEditors: fg
LastEditTime: 2023-08-03 16:21:57
Description: 生成日历
'''
# 引入日历模块
import calendar

# 输入指定年月
yy = int(input('输入年份：'))
mm = int(input('输入月份：'))

# 显示日历
print(calendar.month(yy,mm))