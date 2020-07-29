import easygui as g
import sys

# easygui.egdemo()

while 1:
    g.msgbox("嗨，欢迎进入编程语言选择器~", ok_button="开始")
    msg = "你希望学习什么语言？"
    title = "language"
    choices = ["C", "JAVA", "Python", "C++", "C#"]
    choice = g.choicebox(msg, title, choices)
    # print(choice)
    g.msgbox("你的选择是" + str(choice), "结果", ok_button="确定")
    msg = "你希望重新选择吗？"
    title = "请选择..."
    if g.ccbox(msg, title):
        pass
    else:
        sys.exit(0)
