# TEST_time模块
import time, datetime
import calendar

t1 = time.time()

today = datetime.date.today()
today.timetuple()
time.mktime(today.timetuple())

datetime.date.fromtimestamp(1595952000.0)
now_time = datetime.datetime.now()

yesterday = now_time - datetime.timedelta(days=1)
print(yesterday)

last_hour = now_time - datetime.timedelta(hours=1)
print(last_hour)

# 日历
print(calendar.month(2020, 7))
# print(calendar.calendar(2020))
calendar.prcal(2020)
# 嵌套列表
calendar.monthcalendar(2020, 7)
calendar.isleap(2020)

# 让程序运行到某处暂停几秒
time.sleep(1)
t2 = time.time()
print(t2 - t1)
