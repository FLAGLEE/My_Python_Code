# test psutil
import psutil

print(psutil.cpu_count())  # CPU逻辑数量
print(psutil.cpu_count(logical=False))  # CPU物理核心
# 2说明是双核超线程, 4则是4核非超线程
print(psutil.cpu_times())
# 统计CPU的用户／系统／空闲时间：

# 实现类似top命令的CPU使用率，每秒刷新一次，累计10次：
for x in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))

# 使用psutil获取物理内存和交换内存信息，分别使用：
print(psutil.virtual_memory())
print(psutil.swap_memory())

# 可以通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息：
print(psutil.disk_partitions())  # 磁盘分区信息
print(psutil.disk_usage('/'))  # 磁盘使用情况
print(psutil.disk_io_counters())  # 磁盘IO

# psutil可以获取网络接口和网络连接信息：
print(psutil.net_io_counters())  # 获取网络读写字节／包的个数
print(psutil.net_if_addrs())  # 获取网络接口信息
print(psutil.net_if_stats())  # 获取网络接口状态
print(psutil.net_connections())  # 要获取当前网络连接信息
# 可能会得到一个AccessDenied错误，原因是psutil获取信息也是要走系统接口，
# 而获取网络连接信息需要root权限，这种情况下，可以退出Python交互环境，用sudo重新启动：

# 通过psutil可以获取到所有进程的详细信息：
print(psutil.pids()) # 所有进程ID
print()
print()
print()
print()
print()
print()

# psutil还提供了一个test()函数，可以模拟出ps命令的效果：
print(psutil.test())
