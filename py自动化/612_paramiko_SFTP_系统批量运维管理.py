import paramiko

username = "root"
password = "centos0106"
hostname = "192.168.1.131"
port = 22

try:
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)

    #sftp.put("/home/pycode/py自动化/mylog.txt", "/home/mylog.txt")
    #sftp.get("/home/testfile", "/home/pycode/py自动化/testfile")
    #sftp.mkdir("/home/userdir", 755)
    # sftp.rmdir("/home/dir")
    sftp.rename("/home/mylog.txt", "/home/mylog2.txt")
    print(sftp.stat("/home/mylog2.txt"))  # 打印文件信息
    print(sftp.listdir("/home"))  # 打印目录列表
except Exception as e:
    print(str(e))
