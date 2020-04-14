import psutil

print("进程 start")
# 列出所有进程pid
print(psutil.pids())
print("<<<")
# 实例化一个process对象，参数为进程pid
p = psutil.Process(8002)
# 进程名
print(p.name())
print("<<<")
# 进程bin路径
print(p.exe())
print("<<<")
# 进程工作目录绝对路径
print(p.cwd())
print("<<<")
# 进程状态
print(p.status())
print("<<<")
# 进程创建时间
print(p.create_time())
print("<<<")
# 进程uid信息
print(p.uids())
print("<<<")
# 进程gid信息
print(p.gids())
print("<<<")
# 进程CPU时间，包括user和system
print(p.cpu_times())
print("<<<")
# 获取进程CPU亲和度
print(p.cpu_affinity())
print("<<<")
# 进程内存利用率
print(p.memory_percent())
print("<<<")
# 进程内存rss、vms信息
print(p.memory_info())
print("<<<")
# 进程I/O信息，包括读写IO数字节数
print(p.io_counters())
print("<<<")
# 返回打开进程socket的namedutples列表，包括fs、family、laddr等信息
print(p.connections())
print("<<<")
# 进程开启的线程数
print(p.num_threads())
print("<<<")
print("进程 end")


# popen类的使用
# 用于获取用户启动的应用程序进程信息，以便跟踪程序进程的运行状态
# 通过psutil的popen方法启用应用程序，可以跟踪该程序的所有相关信息
