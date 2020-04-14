import paramiko
import os
import sys
import time

# 定义堡垒机信息
username1 = "root"
password1 = "centos0106"
hostname1 = "192.168.1.131"

# 定义业务服务信息
username2 = "root"
password2 = "centos0106"
hostname2 = "192.168.1.132"

port = 22
passinfo = "password: "  # 输入服务器密码的前标志串
paramiko.util.log_to_file("remote.log")

ssh = paramiko.SSHClient()  # 登录堡垒机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname1, username=username1, password=password1)

channel = ssh.invoke_shell()  # 创建会话，开启命令调用
channel.settimeout(15)  # 设置会话命令超时时间，单位为秒

buf = ""
resp = ""

channel.send("ssh "+username2+"@"+hostname2+"\n")  # 执行ssh登录业务主机
while not buf.endswith(passinfo):  # ssh登录时提示信息判断，输出串尾含"\'s password:"时退出while循环
    try:
        resp = channel.recv(9999)
        resp = str(resp, encoding="utf-8")  # bytes to str
        print(resp)
    except Exception as e:
        print("Error info:%s connection time" % (str(e)))
        channel.close()
        ssh.close()
        sys.exit()
    buf += resp
    if not buf.find("yes/no") == -1:  # 输出串含有yes/no时，发送yes并回车
        channel.send("yes\n")
        buf = ""
print("11111")
channel.send(password2+"\n")  # 发送业务主机密码


buf = ""
while not buf.endswith("# "):
    # 输出串尾为："# "时说明校验通过并推出while循环
    resp = channel.recv(9999)
    resp = str(resp, encoding="utf-8")  # bytes to str
    # print(resp)
    if not resp.find("passinfo") == -1:  # 输出串尾含有"\'s password"时说明密码不正确，要求重新输入
        print("Error info: Authenication failed")
        channel.close()
        ssh.close()
        sys.exit()
    buf += resp
cmd = "ifconfig"
channel.send(cmd+"\n")  # 认证通过后发送ifconfig命令查看结果
#channel.send("ping www.qq.com -c 4\n")
buf = ""
try:
    while buf.find("# ") == -1:
        resp = channel.recv(9999)
        resp = str(resp, encoding="utf-8")  # bytes to str
        buf += resp
        print(buf)
except Exception as e:
    print("Error info:%s" % str(e))
print(buf)
channel.close()
ssh.close()


# bytes object
# b = b"example"

# str object
# s = "example"

# str to bytes
# bytes(s, encoding="utf8")

# bytes to str
# str(b, encoding="utf-8")

# an alternative method
# str to bytes
# str.encode(s)

# bytes to str
# bytes.decode(b)
