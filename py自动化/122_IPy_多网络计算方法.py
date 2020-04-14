from IPy import IP

# 两个网段是否存在包含
IP('10.0.0.0/24') < IP('10.0.0.0/16')
# 判断IP地址和网段是否包含于另一个网段中
'192.168.1.100' in IP('192.168.1.0/24')

# 判断两个网段是否存在重叠 返回1代表重叠，0不重叠
# IP('192.168.0.0/23').overlaps(192.168.1.0)
# IP('192.168.1.0/23').overlaps(192.168.2.0)
# 根据输入的IP或者网段地址返回网络、掩码、广播、反向解析、子网数、IP类型等信息

ip_s = input("Please input an IP or net-range:")
ips = IP(ip_s)
print(len(ips))
if len(ips) > 1:  # 是一个网络地址
    print('net:%s' % ips.net())  # 输出网络地址
    print('netmask:%s' % ips.netmask())
    print('broadcast:%s' % ips.broadcast())
    print('reverse address:%s' % ips.reverseNames()[0])
    print('subnet:%s' % len(ips))  # 子网数
