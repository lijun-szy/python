# Pexpect 是个纯 Python 语言实现的模块，使用其可以轻松方便的实现与 ssh、ftp、passwd 和 telnet 等程序的自动交互，
# 而无人工干预来达到自动化的目的
import getpass
from pexpect import pxssh
import sys

# child = pexpect.spawn('ssh root@192.168.1.131')
# with open('test.log', 'wb') as fout:
#     child.logfile = fout  # 日志输出到文件
#     # 日志输出到屏幕
#     #child.logfile = sys.stdout

#     child.expect("(yes/no)?")
#     child.sendline("yes")
#     child.expect("password:")
#     child.sendline("centos0106")
#     child.expect("#")
#     child.sendline("ls /home")
#     child.expect('#')

try:
    s = pxssh.pxssh()  # 创建pxssh对象
    hostname = input("hostname: \n")
    username = input("username: \n")
    password = getpass.getpass("Please input password:")
    s.login(hostname, username=username, password=password)  # 建立连接
    s.sendline("ps -ef")  # 运行uptime命令
    s.prompt()  # 匹配系统提示符
    print(s.before)  # 打印系统提示符前的命令输出
    s.logout()  # 断开连接
except pexpect.pxssh.ExceptionPxssh as e:
    print("pxssh failed on login")
    print(str(e))
