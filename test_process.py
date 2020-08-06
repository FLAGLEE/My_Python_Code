# 测试多进程
# 创建子进程 :Process(target= , args=(' ',))
# 启动大量的子进程 :Pool(), Pool().apply_async( , args=( ,))
from multiprocessing import Process
import os

from multiprocessing import Pool
import time, random


#

# 子进程需要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process (%s).' % os.getpid())
    # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    # 用start()方法启动
    p.start()
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    p.join()
    print('Child process end.')


#########################################
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    # p = Pool()
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocess done...')
    # 对Pool对象调用join()方法会等待所有子进程执行完毕
    # 调用join()之前必须先调用close()
    # 调用close()之后就不能继续添加新的Process了
    p.close()
    p.join()
    print('All subprocess done.')

# 注意输出的结果，task 0，1，2，3是立刻执行的
# 而task 4要等待前面某个task完成后才执行，
# 这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程
# 如果改成：p = Pool(5)就可以同时跑5个进程。
# Pool的默认大小是CPU的核数
