# test 断言
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


def main():
    print(foo('0'))
    # print(foo('1'))

if __name__ == '__main__':
    main()