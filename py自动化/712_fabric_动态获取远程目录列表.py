from fabric import api

# Fabric是基于Python的SSH命令行工具，简化了SSH的应用程序部署及系统管理任务，它提供了系统基础的操作组件
# 可以实现本地或远程shell命令，包括命令执行、文件上传、下载及完整执行日志输出等功能
# local    #执行本地命令，如local('uname -s')
# lcd      #切换本地目录，如lcd('/home')
# cd       #切换远程目录
# run     #执行远程命令
# sudo   #sudo方式执行远程命令，如sudo('/etc/init.d/httpd start')
# put     #上次本地文件导远程主机，如put('/home/user.info','/data/user.info')
# get     #从远程主机下载文件到本地，如：get('/data/user.info','/home/user.info')
# prompt  #获得用户输入信息，如：prompt('please input user password:')
# confirm  #获得提示信息确认，如：confirm('Test failed,Continue[Y/N]?')
# reboot   #重启远程主机，如：reboot()


# @task  # 函数修饰符，标识的函数为fab可调用的，非标记对fab不可见，纯业务逻辑
# @runs_once  # 函数修饰符，标识的函数只会执行一次，不受多台主机影响
# 本例使用"@task"修饰符标志入口函数go()对外部可见，配合"@run_once"修饰符接收用户输入
# 最后调用worktask()任务函数实现远程命令执行
# env对象的作用是定义fabric的全局设定，支持多个属性，包括目标主机、用户、密码、角色等
api.env.user = "root"
api.env.hosts = ["192.168.1.131", "192.168.1.132"]
api.env.password = "centos0106"


@api.runs_once  # 遍历主机过程中，只有第一台触发此函数
def input_raw():
    return api.prompt("Please input directory name:", default="/home")


def worktask(dirname):
    api.run("ls -l " + dirname)


@api.task()  # 限定只有go函数对fab命令可见
def go():
    getdirname = input_raw()
    worktask(getdirname)
