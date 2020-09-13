import os
import threading


def run_rtk(path_exe, path_conf, path_out, path_rover, path_base, path_brdm, sep):
    # 调用exe程序并输入参数
    os.system(path_exe + sep + path_conf + sep + path_out + sep + path_rover + sep + path_base + sep + path_brdm)


if __name__ == '__main__':

    base_list = []
    rover_list = []
    result_list = []

    base_name = "0000GZA001"
    rovers_name = ["0000GZA002", "0000GZA005", "0000GZA006", "0000GZA007", "0000GZA008"]

    data_path_head = "D:\\data\\OBS\\"
    data_rear = ".20o"

    brdm_path_head = "D:\\data\\brdm\\"
    brdm_head = "BRDM00DLR_S_2020"
    brdm_rear = "0000_01D_MN.rnx"

    result_path_head = "C:\\Users\\FLAG\\Desktop\\Result\\"
    result_rear = ".pos"

    sep = " "

    path_exe = "C:\\Users\\FLAG\\Desktop\\RTK\\RTK-quality-control\\RTK-quality-control\\Debug\\RTK-quality-control.exe"
    path_conf = "-k" + sep + "D:\\data\\测试数据\\1\\RTK_new.conf"

    file_list = os.listdir(data_path_head)

    for file in file_list:

        if file[0:10] == base_name:
            base_list.append(file)
        elif file[0:10] in rovers_name:
            rover_list.append(file)

    out_list = os.listdir(result_path_head)
    for file in out_list:
        if file.split(".")[1] == result_rear.split(".")[1]:
            result_list.append(file)

    brdm_list = os.listdir(brdm_path_head)

    for doy in range(1, 366):
        for hour in range(0, 24):
            for rover_name in rovers_name:

                print(rover_name)
                brdm_name = brdm_head + str(doy).zfill(3) + brdm_rear
                result_name = rover_name + str(doy).zfill(3) + str(hour).zfill(2) + result_rear

                path_rover = data_path_head + rover_name + str(doy).zfill(3) + str(hour).zfill(2) + data_rear
                path_base = data_path_head + base_name + str(doy).zfill(3) + str(hour).zfill(2) + data_rear
                path_brdm = brdm_path_head + brdm_name

                if path_rover.split("\\")[-1] in rover_list and path_base.split("\\")[
                    -1] in base_list and brdm_name in brdm_list and result_name not in result_list:
                    path_out = "-o" + sep + result_path_head + rover_name + str(doy).zfill(3) + str(hour).zfill(
                        2) + result_rear

                    if rover_name == "0000GZA005":
                        print(result_name)

                    result_list.append(result_name)

                    # print(path_rover)
                    # print(path_base)
                    # print(path_brdm)
                    # print(path_out)

                    # 创建新线程来处理RTK数据
                    t = threading.Thread(target=run_rtk,
                                         args=(path_exe, path_conf, path_out, path_rover, path_base, path_brdm, sep))
                    t.start()
