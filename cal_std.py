#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np

data_str = []
x=[]
y=[]
z=[]

def std(datas, mean):
    nfh2 = 0
    for data in datas:
        nfh2 += (data - mean) ** 2

    return np.sqrt(nfh2/len(datas))


with open(r"C:\Users\FLAG\Desktop\SPP\A000123060_GPS.pos", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line[0] == '%':
            continue
        if line[71] == "5":
            data_str.append(line[25: 68])

for i in range(len(data_str)):
    x.append(float(data_str[i][0:13]))
    y.append(float(data_str[i][16:28]))
    z.append(float(data_str[i][31:43]))

mean_x = np.mean(x)
mean_y = np.mean(y)
mean_z = np.mean(z)

print("std:")
print('x: ', std(x, mean_x))
print('y: ', std(y, mean_y))
print('z: ', std(z, mean_z))