import pexpect
import sys

# 常用FTP协议实现自动化、集中式的文件备份，要求做到账号登录、文件上传与下载、退出等实现自动化操作
from __future__ import unicode_literals  # 使用unicode编码

child = pexpect.spawnu("ftp 192.168.1.131")  # 运行ftp命令
child.expect("(?i)name .*: ")  # (?i)表示后面的字符串匹配正则表达式忽略大小写
child.sendline("root")
child.expect("(?i)password")
child.sendline("centos0106")
child.expect("ftp> ")
child.sendline("bin")  # 启用二进制传输模式
child.expect("ftp> ")
child.sendline("get ")
