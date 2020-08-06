# test json
# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换
import json

d = dict(name='Bob', age=20, score=88)
json_str = json.dumps(d)
print(json_str)
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法
# 前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化
dd = json.loads(json_str)
print(dd)
print(dd['name'])
print(dd['age'])
print(dd['score'])


# 类json化
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)


# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象
# 只需要为Student专门写一个转换函数，再把函数传进去即可
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


print(json.dumps(s, default=student2dict))
# 把任意class的实例变为dict
# 通常class的实例都有一个__dict__属性
# 也有少数例外，比如定义了__slots__的class
print(json.dumps(s, default=lambda obj: obj.__dict__))


# loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


print(json.loads(json_str, object_hook=dict2student))
