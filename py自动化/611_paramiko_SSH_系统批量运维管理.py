import paramiko
# paramiko是基于Python实现的SSH2远程安全链接，支持认证及秘钥方式。
# 可以实现远程命令执行、文件传输、中间SSH代理等功能，
# 相对于Pexpect，封装层次更高，更贴近SSH协议的功能

hostname = "192.168.1.131"
username = "root"
password = "centos0106"

paramiko.util.log_to_file("syslogin.log")  # 发送日志到syslogin.log

ssh = paramiko.SSHClient()  # 创建一个ssh客户端client对象
ssh.load_system_host_keys()  # 获取客户端host_keys，默认~/.ssh/know_hosts，非默认路径需要指定
ssh.connect(hostname=hostname, username=username, password=password)  # 创建ssh连接
stdin, stdout, stderr = ssh.exec_command('ps -ef')  # 调用远程执行命令方法
print(stdout.read())  # 打印命令执行结果，得到Python列表形式，可以使用stdouy.readlines()
ssh.close()
