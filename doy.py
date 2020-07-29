# doy 与 date 相互转换
from datetime import datetime
from easygui import msgbox, enterbox, ccbox, choicebox
from sys import exit


# import easygui as g
# import datetime

def doy2data(year, doy):
    month_leapyear = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_notleap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        for i in range(0, 11):
            if doy > month_leapyear[i]:
                doy -= month_leapyear[i]
                continue
            if doy <= month_leapyear[i]:
                month = i + 1
                day = doy
                break
    else:
        for i in range(0, 11):
            if doy > month_notleap[i]:
                doy -= month_notleap[i]
                continue
            if doy <= month_notleap[i]:
                month = i + 1
                day = doy
                break
    if month < 10:
        monthstr = '0' + str(month)
    else:
        monthstr = str(month)
    if day < 10:
        daystr = '0' + str(day)
    else:
        daystr = str(day)
    date = str(year) + monthstr + daystr
    return date


# GUI
while 1:
    msg = "what do you want to do?"
    title = "doy<=>date"
    choices = ["date2doy", "doy2date"]
    choice = choicebox(msg, title, choices)

    if choice == "date2doy":
        outdtstr = dtstr = enterbox('Enter the datetime(yyyymmdd:20200723):')
        print(dtstr)
        dt = datetime.strptime(dtstr, "%Y%m%d")
        another_dtstr = dtstr = dtstr[:4] + '0101'
        another_dt = datetime.strptime(another_dtstr, "%Y%m%d")
        msgbox('The ' + outdtstr + ' to doy is ' + str(int((dt - another_dt).days) + 1), "结果", ok_button="确定")
    elif choice == "doy2date":
        year = int(enterbox('Enter the year(yyyy:2020):'))
        doy = int(enterbox('Enter the doy(ddd:192):'))
        date = doy2data(year, doy)
        msgbox('The ' + str(doy) + ' to date is: ' + str(date), "结果", ok_button="确定")

    msg = "你希望继续计算吗？"
    title = "请选择..."
    if ccbox(msg, title):
        pass
    else:
        exit(0)

# # 源码
# flag = 1
# while flag == 1:
#     n = int(input('what do you want to do?\n'
#                   '1 date2doy\n'
#                   '2 doy2date\n'
#                   'input:'))
#     if n == 1:
#         dtstr = input('Enter the datetime(yyyymmdd:20200723):')
#         dt = datetime.datetime.strptime(dtstr, "%Y%m%d")
#         another_dtstr = dtstr = dtstr[:4] + '0101'
#         another_dt = datetime.datetime.strptime(another_dtstr, "%Y%m%d")
#         print('The date to doy is', int((dt - another_dt).days) + 1, '\n')
#         flag = int(input('Do you still want to calculate?\n'
#                          '1 yes\n'
#                          '0 no\n'
#                          'input:'))
#         while flag != 1 and flag != 0:
#             print('Input error, please retype')
#             flag = int(input('Do you still want to calculate?\n'
#                              '1 yes\n'
#                              '0 no\n'
#                              'input:'))
#         continue
#     elif n == 2:
#         year = int(input('Enter the year(yyyy:2020):'))
#         doy = int(input(('Enter the doy(ddd:192):')))
#         print('The', doy, 'to date is :', doy2data(year, doy), '\n')
#         flag = int(input('Do you still want to calculate?\n'
#                          '1 yes\n'
#                          '0 no\n'
#                          'input:'))
#         while flag != 1 and flag != 0:
#             print('Input error, please retype')
#             flag = int(input('Do you still want to calculate?\n'
#                              '1 yes\n'
#                              '0 no\n'
#                              'input:'))
#         continue
#     else:
#         print('Input error, please retype')
#         continue
# print('see you~')
