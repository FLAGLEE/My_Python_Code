# 推导式、生成器
# 列表推导式
# [<表达式> for <变量> in <可迭代对象> if <逻辑条件>]
print([x * x for x in range(10)])
# 字典推导式
# {<键值表达式>:<元素表达式> for <变量> in <可迭代对象> if <逻辑条件>}
print({'k%d' % (x): x ** 3 for x in range(10)})
# 集合推导式(集合无序、不可重复)
# {<元素表达式> for <变量> in <可迭代对象> if <逻辑条件>}
print({x * x for x in range(10)})
print({x + y for x in range(10) for y in range(x)})
print([x + y for x in range(10) for y in range(x)])
# 生成器推导式
# (<元素表达式> for <变量> in <可迭代对象> if <逻辑条件>)
# 返回一个生成器对象，也是可迭代对象
agen = (x * x for x in range(10))
for n in agen:
    print(n)
# 生成器函数
# 与普通函数相同，将return换成yield
def even_number(max):
    n=0
    while n < max:
        yield n
        n+=2
for i in even_number(10):
    print(i)