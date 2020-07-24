# 列表元素相加运算
def mysum(mylist):
    sum = mylist[0]
    for item in mylist[1:]:
        sum += item
    return sum


alst = [1, 2, 3, 4]
print("整数：", mysum(alst))

alst = ['a', 'b', 'c', 'd']
print("字符串：", mysum(alst))

alst = [1, 2.2, 3, 4.5]
print("混合数：", mysum(alst))
