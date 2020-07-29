import csv
# import openpyxl
# 工作簿
from openpyxl import workbook
# 表格
from openpyxl import  worksheet
f = open("text.txt", "w")
f.writelines(["apple\n", "pie\n"])
f.close()

f = open("text.txt", "r")
print(f.readlines())
f.close()

with open("text.txt", "rt") as my_file:
    print(my_file.read())

# CSV
w = csv.writer(open("output.csv", "w"))
w.writerow("rows")
