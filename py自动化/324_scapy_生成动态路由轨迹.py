
# Scapy是一个可以让用户发送、侦听和解析并伪装网络报文的Python程序。这些功能可以用于制作侦测、扫描和攻击网络的工具。
# Scapy 是一个强大的操纵报文的交互程序。它可以伪造或者解析多种协议的报文，还具有发送、捕获、匹配请求和响应这些报文以及更多的功能。
# Scapy 可以轻松地做到像扫描(scanning)、路由跟踪(tracerouting)、探测(probing)、单元测试(unit tests)、攻击(attacks)和
# 发现网络(network discorvery)这样的传统任务。它可以代替hping,arpspoof,arp-sk,arping,p0f 甚至是部分的Namp,tcpdump和tshark 的功能。
# scapy模块需要tcpdump程序支持，生成报表需要graphviz、ImageMagick图像包支持

from scapy.all import traceroute
import os
import sys
import time
import subprocess
import warnings
import logging

warnings.filterwarnings("ignore", category=DeprecationWarning)  # 屏蔽scapy无用告警信息
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  # 屏蔽模块IPV6多余告警

domains = input('Please input one or more Ip/Domain:')

target = domains.split(' ')
dport = [80]  # 扫描的端口列表

if len(target) >= 1 and target[0] != "":
    res, unns = traceroute(target, dport=dport, retry=-2)  # 启动路由跟踪
    res.graph(target="> test.svg")  # 生成svg矢量图
    time.sleep(1)
    subprocess.Popen("/usr/bin/convert test.svg test.png",
                     shell=True)  # svg转png格式
else:
    print("IP/domain number of errors, exit")
