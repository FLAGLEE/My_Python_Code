#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import coordinate_transformation as ct
import matplotlib.pyplot as plt
import numpy as np


def neifuhe(datas, mean):
    nfh2 = 0
    for data in datas:
        nfh2 += (data - mean) ** 2

    return np.sqrt(nfh2/len(datas))

file_list = os.listdir("D:\\data\\VRS\\国地信VRS\\solution_clear\\py\\")

for file in file_list:
    with open("D:\\data\\VRS\\国地信VRS\\solution_clear\\py\\"+file, "r") as f:
        ref = []
        data_str = []
        x = []
        y = []
        z = []
        E = []
        N = []
        U = []
        lines = f.readlines()
        for line in lines:
            if line[0] == '%':
                if line[2:9] == 'ref pos':
                    ref.append(float(line[14:27]))
                    ref.append(float(line[30:42]))
                    ref.append(float(line[45:57]))
                continue
            if line[71] == "1":
                data_str.append(line[25: 68])

    for i in range(len(data_str)):
        x.append(float(data_str[i][0:13]))
        y.append(float(data_str[i][16:28]))
        z.append(float(data_str[i][31:43]))



    mean_x = np.mean(x)
    mean_y = np.mean(y)
    mean_z = np.mean(z)

    # print('X: ',neifuhe(x,mean_x))
    # print('Y: ',neifuhe(y,mean_y))
    # print('Z: ',neifuhe(z,mean_z))

    for i in range(len(x)):
        E.append(ct.xyz2enu([x[i], y[i], z[i]], ref)[0])
        N.append(ct.xyz2enu([x[i], y[i], z[i]], ref)[1])
        U.append(ct.xyz2enu([x[i], y[i], z[i]], ref)[2])

    mean_E = np.mean(E)
    mean_N = np.mean(N)
    mean_U = np.mean(U)

    print(file)
    print('E: ',neifuhe(E, mean_E))
    print('N: ',neifuhe(N, mean_N))
    print('U: ',neifuhe(U, mean_U))
