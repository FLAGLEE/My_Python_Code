# 计算汉诺塔移动次数与步骤

def f(n):
    if n==0:
        return 0
    else:
        return 2*f(n-1)+1

def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, '-->', c)
        hanoi(n - 1, b, a, c)

# 调用
x=int(input("请输入片的个数："))
print("需要移动",f(x),"次")
print("移动方式：")
hanoi(x, 'A', 'B', 'C')

