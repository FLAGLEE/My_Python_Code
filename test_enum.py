# 使用枚举类
from enum import Enum, unique

# 获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# value属性则是自动赋给成员的int常量，默认从1开始计数
print(Month.Jan)
print(Month.Jan.value)
print(Month._member_map_)
print(Month._member_names_)
print(Month._member_names_[0])
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类
# @unique装饰器可以帮助检查保证没有重复值
@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


# 访问这些枚举类型可以有若干种方法
print(Weekday.Mon)
print(Weekday.Tue.value)
print(Weekday(3))

for name, member in Weekday.__members__.items():
    print(name, '=>', member, ',', member.value)
