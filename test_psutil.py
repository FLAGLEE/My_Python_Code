# test psutil
import psutil
print(psutil.cpu_count()) # CPU逻辑数量
print(psutil.cpu_count(logical=False)) # CPU物理核心
# 2说明是双核超线程, 4则是4核非超线程
print(psutil.cpu_times())
# 统计CPU的用户／系统／空闲时间：

# 实现类似top命令的CPU使用率，每秒刷新一次，累计10次：
for x in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))