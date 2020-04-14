import psutil

# CPU
print("CPU start")
# 获取CPU完整信息，需要显示所有逻辑CPU信息
result = psutil.cpu_times()
# 指定方法变量percpu=True
print(result)
psutil.cpu_times(percpu=True)
print(">>>>")
# 获取单项数据信息，如用户user的CPU时间比
time = psutil.cpu_times().user
print(time)
print(">>>>")
# cpu逻辑个数
num = psutil.cpu_count()
print(num)
print(">>>>")
# cpu物理个数
num = psutil.cpu_count(logical=False)
print(num)
print(">>>>")
print("CPU end")

# 内存
print("Mem start")
# 获取内存完整信息
mem = psutil.virtual_memory()
print(mem)
print(">>>>")
# 获取内存总数
print(mem.total)
print(">>>>")
# 获取空闲内存
print(mem.free)
print(">>>>")
# 获取swap分区信息
print(psutil.swap_memory())
print(">>>>")
print("Mem end")

# 磁盘信息
print("Disk start")
# 磁盘完整信息
Disk = psutil.disk_partitions()
print(Disk)
print(">>>>")
# 获取分区的使用情况
print(psutil.disk_usage('/'))
print(">>>>")
# 获取磁盘的总I/O个数、读写信息
print(psutil.disk_io_counters())
print(">>>>")
# perdisk=True获取单个I/O个数、读写信息
print(psutil.disk_io_counters(perdisk=True))
print(">>>>")
print("Disk end")

# 网络信息
print("Net start")
# 获取网络总的IO信息，默认peric=False
print(psutil.net_io_counters())
print(">>>>")
# 输出每个网络接口的IO信息
print(psutil.net_io_counters(pernic=True))
print("Net end")


# 其他信息
print("Other start")
# 获取当前用户信息
print(psutil.users())
print(">>>>")
# 获取开机时间
print(psutil.boot_time())
print("Other end")
