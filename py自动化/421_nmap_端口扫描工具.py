import sys
import nmap
# 1、先遍历主机
# 2、遍历协议
# 3、遍历端口
scan_row = []
input_data = input('Please input hosts and port:')
scan_row = input_data.split(' ')

if len(scan_row) != 2:
    print("Inpur error")
    sys.exit(0)
hosts = scan_row[0]
port = scan_row[1]

try:
    nm = nmap.PortScanner()  # 创建端口扫描对象
except nmap.PortScannerError:
    print("Nmap not found", sys.exc_info()[0])
    # exc_info() 方法会将当前的异常信息以元组的形式返回，该元组中包含 3 个元素，分别为 type、value 和 traceback，它们的含义分别是：
    # type：异常类型的名称，它是 BaseException 的子类（有关 Python 异常类，可阅读《Python常见异常类型》一节）
    # value：捕获到的异常实例。
    # traceback：是一个 traceback 对象。
    sys.exit(0)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(0)

try:  # 调用扫描方法，参数指定扫描主机，nmap扫描命令行参数arguments
    # -v 表示启用细节模式，可以返回非up状态主机清单，-PE表示采用TCP同步扫描（TCP SYN），-p指定扫描端口范围
    nm.scan(hosts=hosts, arguments=' -v -sS -p'+port)
except Exception as e:
    print("scan error:"+str(e))

# 遍历扫描主机
for host in nm.all_hosts():
    print("--------------")
    print("Host :%s (%s)" % (host, nm[host].hostname()))  # 输出主机及主机名
    print('State :%s ' % (nm[host].state()))  # 输出主机状态，如：up、down
    for proto in nm[host].all_protocols():  # 遍历扫描协议，如:TCP udp
        print("~~~")
        print("Protocol :%s" % proto)
        lport = nm[host][proto].keys()  # 获取协议的所有扫描端口
        # lport.sort()  # 端口排序
        print(lport)
        for port in lport:  # 遍历所有端口并输出端口状态
            print("port: %s   \t    state: %s" %
                  (port, nm[host][proto][port]['state']))
