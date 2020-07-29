# TEST_math模块
# math数值型，整数浮点数，cmath可以扩展到复数
import math, cmath
# 十进制的定点小数模块,小数计算精度
import decimal
# 有理数模块
import fractions
# 伪随机数
import random

print(0.1 + 0.1 + 0.1 - 0.3)
print(decimal.Decimal('0.1') + decimal.Decimal('0.1') + decimal.Decimal('0.1') - decimal.Decimal('0.3'))
# 生成分数
print(fractions.Fraction(1, 4))

# 随机数种子
# 随机种子相同，随机数的序列也是相同的
random.seed(a=None)
# 随机实数[,)
print(random.random())
# 随机浮点数
print(random.uniform(1, 100))
# 随机整数[,]
print(random.randint(1, 100))
# 在[,)]内以n为步长的集合中，随机选择
print(random.randrange(0, 100, 2))
# 生成K位二进制随机数
print(random.getrandbits(8))
# 抽选
a=random.choice(["FLAG","LEE","HELLO","WORLD"])
print(a)