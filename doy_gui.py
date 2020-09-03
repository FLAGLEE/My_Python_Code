# doy GUI
from tkinter import *
from tkinter import scrolledtext
from datetime import datetime

app = Tk()
app.title("doy2date")
app.geometry("350x250")

lbl = Label(app, text="Hello")
lbl.grid(row=0)

txt = scrolledtext.ScrolledText(app, width=45, height=10)
txt.grid(row=4, padx=10)


def Fdoy2date(year, doy):
    month_leapyear = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_notleap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        for i in range(0, 12):
            if doy > month_leapyear[i]:
                if i == 11:
                    txt.insert(INSERT, "\ndate is to large!\nplease entry again!")
                doy -= month_leapyear[i]
                continue
            if doy <= month_leapyear[i]:
                month = i + 1
                if month < 10:
                    monthstr = '0' + str(month)
                else:
                    monthstr = str(month)
                day = doy
                if day < 10:
                    daystr = '0' + str(day)
                else:
                    daystr = str(day)
                break
    else:
        for i in range(0, 12):
            if doy > month_notleap[i]:
                doy -= month_notleap[i]
                continue
            if doy <= month_notleap[i]:
                month = i + 1
                if month < 10:
                    monthstr = '0' + str(month)
                else:
                    monthstr = str(month)
                day = doy
                if day < 10:
                    daystr = '0' + str(day)
                else:
                    daystr = str(day)
                break

    date = str(year) + monthstr + daystr
    return date


def doy2date():
    lbl.configure(text="doy2date was clicked!")
    var = ipt.get()
    if var:
        if len(var) != 7:
            txt.insert(END, "\nentry format error!\nplease entry again!")
            txt.see(END)
        else:
            year = int(var) // 1000
            day = int(var) % 1000
            date = Fdoy2date(year, day)
            txt.insert(END, "\nThe %s to date is %s" % (var, date))
            txt.see(END)

    else:
        txt.insert(END, "\nplease input doy")
        txt.see(END)


def date2doy():
    lbl.configure(text="date2doy was clicked!")
    var = ipt.get()
    if var:
        if len(var) != 8:
            txt.insert(END, "\nentry format error!\nplease entry again!")
            txt.see(END)
        else:
            dt = datetime.strptime(var, "%Y%m%d")
            another_dtstr = dtstr = var[:4] + '0101'
            another_dt = datetime.strptime(another_dtstr, "%Y%m%d")
            txt.insert(END, "\nThe " + var + ' to doy is ' + str(int((dt - another_dt).days) + 1))
            txt.see(END)
    else:
        txt.insert(END, "\nplease input date")
        txt.see(END)


ipt = Entry(app, show=None, font=('Arial', 14), width=10)
ipt.grid(row=1)
ipt.focus()
btn1 = Button(app, text="doy2date", command=doy2date)
btn1.grid(row=2)
btn2 = Button(app, text="date2doy", command=date2doy)
btn2.grid(row=3)

txt.insert(END, "Enter the datetime(yyyymmdd:20200723) to doy\n"
                "or Enter the doy(yyyydoy:2020192) to datetime\n\n")
# 主消息循环:
app.mainloop()
