import os
import numpy as np
from pylab import mpl
import matplotlib.pyplot as plt
import coordinate_transformation as ct

ref = []

data_allday = [[], [], [], [], [], [],
               [], [], [], [], [], []]
x = []
y = []
z = []

X = []
Y = []
Z = []

result_XYZ = [[], [], []]
result_ENU = [[], [], []]

plot_ENU = [[], [], []]
plot_times = []

file_path = 'D:\\data\\VRS\\国地信VRS\\solution_clear\\py\\'
file_list = os.listdir(file_path)

for file in file_list:
    with open(file_path + file, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line[0] == '%':
                if line[2:9] == 'ref pos':
                    ref.append(float(line[14:27]))
                    ref.append(float(line[30:42]))
                    ref.append(float(line[45:57]))
                continue
            if line[71] == "1":
                # print(line.strip('\n'))
                data_index = int(line[11:13]) // 2
                data_allday[data_index].append(line[25: 68])

    for i in range(len(data_allday)):
        if len(data_allday[i]) == 0:
            # result_XYZ[0].append(None)
            # result_XYZ[1].append(None)
            # result_XYZ[2].append(None)
            continue
        for j in range(len(data_allday[i])):
            x.append(float(data_allday[i][j][0:13]))
            y.append(float(data_allday[i][j][16:28]))
            z.append(float(data_allday[i][j][31:43]))

        # threshold_x = np.mean(x)
        # threshold_y = np.mean(y)
        # threshold_z = np.mean(z)
        #
        # for k in range(len(x)):
        #     if np.abs(x[k] - threshold_x) < 0.02:
        #         X.append(x[k])
        #     if np.abs(y[k] - threshold_y) < 0.02:
        #         Y.append(y[k])
        #     if np.abs(z[k] - threshold_z) < 0.02:
        #         Z.append(z[k])

        result_XYZ[0].append(np.mean(x))
        result_XYZ[1].append(np.mean(y))
        result_XYZ[2].append(np.mean(z))

        plot_time = file[4:8] + "-" + file[8:10] + "-" + file[10:12] + " " + str(i * 2 + 1) + ":00:00"
        plot_times.append(plot_time)

    for i in range(len(result_XYZ[0])):
        ENU = ct.xyz2enu([result_XYZ[0][i], result_XYZ[1][i], result_XYZ[2][i]], ref)
        result_ENU[0].append(ENU[0])
        result_ENU[1].append(ENU[1])
        result_ENU[2].append(ENU[2])

    ref = []

    data_allday = [[], [], [], [], [], [],
                   [], [], [], [], [], []]
    x = []
    y = []
    z = []

    X = []
    Y = []
    Z = []

    result_XYZ = [[], [], []]

print(plot_times)

for i in range(len(result_ENU[0])):
    plot_ENU[0].append((result_ENU[0][i] - result_ENU[0][0]) * 1000)
    plot_ENU[1].append((result_ENU[1][i] - result_ENU[1][0]) * 1000)
    plot_ENU[2].append((result_ENU[2][i] - result_ENU[2][0]) * 1000)

plt.figure(figsize=(20, 4), dpi=400)
plt.plot(plot_times, plot_ENU[0], label="E")
plt.plot(plot_times, plot_ENU[1], label="N")
plt.plot(plot_times, plot_ENU[2], label="U")

# 设置显示中文字体
# mpl.rcParams["font.sans-serif"] = ["SimHei"]

plt.title("VRS: GHLY-HLY1")
plt.xlabel("time/h", fontsize=16)
plt.ylabel("mm", fontsize=16)
plt.ylim(-100, 100)
plt.legend(loc="best")
plt.xticks(list(plot_times)[::11])
plt.savefig('./result.jpg')
plt.show()

with open('D:\\data\\VRS\\国地信VRS\\ref\\new.txt', 'w') as f2:
    for i in range(len(plot_ENU[0])):
        f2.writelines(plot_times[i] + ',' + str(plot_ENU[0][i]) + ',' + str(plot_ENU[1][i]) + ',' + str(plot_ENU[2][i])+'\n')
