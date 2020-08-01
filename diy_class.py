# 自定义类的功能
# 自己定义的类表现得和Python自带的list、tuple、dict没什么区别
class Student(object):
    def __init__(self, name):
        self.name = name

    # 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性

    # print:<__main__.Student object at 0x00000277198F0B48>不好看
    # 返回好看的字符串
    def __str__(self):
        return "Student object (name: %s)" % self.name

    # print调用__str__,直接显示变量调用__repr__()
    __repr__ = __str__

    # 不用instance.method()来调用
    # 直接在实例本身上调用，定义一个__call__()方法
    def __call__(self):
        print('My name is %s.' % self.name)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    # 被用于for ... in循环,就必须实现一个__iter__()方法
    # 不断调用该迭代对象的__next__()方法拿到循环的下一个值
    # 直到遇到StopIteration错误时退出循环
    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:  # 循环退出条件
            raise StopIteration()
        return self.a

    # 表现得像list那样按照下标取出元素，需要实现__getitem__()方法
    # 实现切片 __getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            step = stepinit = item.step  # 对step参数作处理
            if start is None:
                start = 0
            if step is None:
                step = stepinit = 1
            a, b = 1, 1
            FLAG = 1
            L = []
            for x in range(stop):
                if x >= start:
                    if FLAG == 1:
                        L.append(a)
                        FLAG = 0
                    else:
                        step -= 1
                        if step == 0:
                            L.append(a)
                            step = stepinit
                a, b = b, a + b
            return L
    # 如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str
    # __setitem__()方法，把对象视作list或dict来对集合赋值
    # 还有一个__delitem__()方法，用于删除某个元素


# REST API
# 只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
# http://api.server/user/friends
# http://api.server/user/timeline/list
# 利用完全动态的__getattr__，可以写出一个链式调用：
class Chain(object):

    def __init__(self, path=''):
        self.path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.path, path))

    def __call__(self, *args):
        _self = self
        for i in args:
            _self = Chain("%s/:%s" % (_self.path, i))
        return _self

    def __str__(self):
        return self.path

    __repr__ = __str__


f = Fib()
print('f[10]=', f[10])
print('f[0:10]=', f[0:10])
print('f[0:10:2]=', f[0:10:2])
print('f[3:10:3]=', f[3:10:3])

for i in Fib():
    print(i)

s = Student("FLAG")
print(s)
print(s())

print(Chain().status.user.timeline.list)
print(Chain().users('michael').repos)
print(Chain().a("hello").b)
