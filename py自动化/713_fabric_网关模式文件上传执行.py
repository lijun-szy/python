# 本例通过Fabric的env对象定义网关模式，即俗称中转、堡垒机环境。
# 定义格式为"env.gateway=1921.68.1.131"，其中IP为"192.168.1.131"为堡垒机IP，再结合任务函数实现目标主机文件上传与执行的操作


from fabric import api
from fabric.context_managers import *
from fabric import confirm

api.env.user = "root"
api.env.gateway = "192.168.1.131"  # 堡垒机IP，作为文件上传、执行的中转设备
api.env.host["192.168.1.132"]
# 加入所有主机密码都不一样，可以通过env.password字典变量一一指定

api.env.passwords = {
    "root@192.168.1.131:22": "centos0106"  # 堡垒机账号信息
    "root@192.168.1.132:22": "centos0106"
}

# 本地安装包路径
lpackpath = "/home/install/lnmp0.9.tar.gz"
# 远程安装路径
rpackpath = "/tmp/insatll"


@api.task()
def put_task():
    api.run("mkdir -p /tmp/install")
    with api.settings(warn_only=True):
        result = api.put(lpackpath, rpackpath)  # 上传安装包
    if result.failed and not api.confirm("put file failed, Continue[y/n]?"):
        api.abort("Aborting file put task")


@api.task()
def run_task():
    with api.cd("/tmp/insatll"):
        api.run("tar -zxvf lnmp0.9.tar.gz")
        with api.cd("lnmp09/"):
            使用with继续继承/tmp/install目录位置状态
            run("./contos.sh")


@api.task()
def go():
    put_task()
    run_task()
