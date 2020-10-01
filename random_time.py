#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 生成随机时间

from random import *
from time import *

date1 = (2016, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = mktime(date1)
date2 = (2017, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = mktime(date2)
print(date1)
print(date2)
print(time1)
print(time2)

random_time = uniform(time1, time2)
print(localtime(random_time))
print(asctime(localtime(random_time)))
