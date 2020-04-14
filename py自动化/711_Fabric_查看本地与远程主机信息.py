from fabric import api

# Fabric是基于Python的SSH命令行工具，简化了SSH的应用程序部署及系统管理任务，它提供了系统基础的操作组件
# 可以实现本地或远程shell命令，包括命令执行、文件上传、下载及完整执行日志输出等功能

# env对象的作用是定义fabric的全局设定，支持多个属性，包括目标主机、用户、密码、角色等
api.env.user = "root"
api.env.hosts = ["192.168.1.130", "192.168.1.131"]
api.env.password = "centos0106"


@api.runs_once  # 查看本地系统信息，当有多台主机时只运行一次
def local_task():  # 本地任务函数
    api.local("uname -a")


def remote_task():
    with api.cd("/data/logs"):  # "with"的作用是让后面的表达式的语句继承当前状态，实现"cd /data/logs && ls -l"的效果
        api.run("ls -l")
# fab命令分别调用local_task任务函数
# fab -f 711_Fabric_查看本地与远程主机信息.py local_task

# fab命令分别调用remote_task任务函数
# fab -f 711_Fabric_查看本地与远程主机信息.py remote_task
