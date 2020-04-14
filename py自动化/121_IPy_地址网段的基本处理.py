from IPy import IP

# IP
print("IPy start")
# 区分网络类型
v = IP('10.2.1.2').version()
print(v)
v = IP('::1').version()
print(v)
# 通过指定的网段输出该网段的IP个数及所有IP地址清单
ip = IP('192.168.0.0/16')
# 输出192.168.0.0/16网段的IP个数
print(ip.len())
# 输出192.168.0.0/16网段的所有IP
# for x in ip:
#    print(x)
# 反向解析地址格式
ip1 = IP('192.168.1.3')
print(ip1.reverseNames())
# 判断是公网还是私网
print(IP('192.168.1.16').iptype())
print(IP('8.8.8.8').iptype())
# IP格式转换
print(IP('8.8.8.8').int())
print(IP('8.8.8.8').strHex())
print(IP('8.8.8.8').strBin())
# 网络地址转换，根据IP与掩码生产网段格式
print(IP('192.168.5.6').make_net('255.255.255.0'))
print(IP('192.168.5.200/255.255.255.0', make_net=True))
print(IP('192.168.5.0-192.168.5.255', make_net=True))

# strNormal方法指定不同的wantprefixlen参数值以定制不同输出类型的网段
print(IP('8.8.8.0/24').strNormal(0))  # 0:无返回
print(IP('8.8.8.0/24').strNormal(1))  # 1:prefix格式
print(IP('8.8.8.0/24').strNormal(2))  # 2:decimalnetmask模式
print(IP('8.8.8.0/24').strNormal(3))  # 0:lastIP格式
