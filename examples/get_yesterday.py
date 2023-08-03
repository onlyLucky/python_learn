'''
Author: fg
Date: 2023-08-03 17:21:52
LastEditors: fg
LastEditTime: 2023-08-03 17:21:52
Description: 获取昨天日期
'''
import datetime
def getYesterday():
  today = datetime.date.today()
  oneday = datetime.timedelta(days=1)
  yesterday = today - oneday
  print(today,oneday,yesterday)
  return yesterday

getYesterday()