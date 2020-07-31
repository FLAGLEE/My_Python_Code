# 定义类
class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)


FLAG = Student('FLAGLEE', 24)
print(FLAG.study('math'))
print(FLAG.watch_movie())


# 继承和多态
class Animal(object):  # 编写Animal类
    def run(self):
        print("Animal is running...")


class Dog(Animal):  # Dog类继承Amimal类，没有run方法
    pass


class Cat(Animal):  # Cat类继承Animal类，有自己的run方法
    def run(self):
        print('Cat is running...')

    pass


class Car(object):  # Car类不继承，有自己的run方法
    def run(self):
        print('Car is running...')


class Stone(object):  # Stone类不继承，也没有run方法
    pass


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Car())


# run_twice(Stone())


# 访问限制
# 把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class People(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


# 测试:
bart = People('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')


# property
class Teacher(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


class Screen(object):
    @property  # 把函数变成class的'属性'
    def width(self):
        return self._width

    # 通过 @ property来将一个声明的方法
    #      def width（self）变成一个属性width
    #      如果不加，就是width，属性名和方法 = > 属性,就重名了
    @width.setter  # 设置'属性'的取值范围
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be intger!')
        if value < 0:
            raise ValueError('width value must be > 0!')
        self._width = value  # 给'属性'赋值

    @property  # 把函数变成class的'属性'
    def height(self):
        return self._height

    @height.setter  # 设置'属性'的取值范围
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be intger!')
        if value < 0:
            raise ValueError('height value must be > 0!')
        self._height = value  # 给'属性'赋值

    @property  # 把函数变成class的'属性'
    def resolution(self):  # 计算屏幕解析度
        return self._height * self._width


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
