import dns.resolver
# resolver DNS解析器类，使用它的query方法来实现域名的查询功能

# query(qname, rdtype=dns.rdatatype.A, rdclass=dns.rdataclass.IN,
#          tcp=False, source=None, raise_on_no_answer=True,
#          source_port=0, lifetime=None)
# qname为查询的域名 rdtype参数用来指定RR资源的类型，常见的如下：
# A记录: 将主机名转换成IP地址
# MX记录: 邮件交换记录，定义邮件服务器的域名
# CNAME记录: 指别名记录，实现域名间的映射
# NS记录: 标记区域的域名服务器及授权子域
# PTR记录: 反向解析，与A相反

# A记录
# domain = input('Please input an domain:')  # 输入地址
# A = dns.resolver.query(domain, 'A')  # 指定查询类型为A记录
# for i in A.response.answer:  # 通过answer方法获取回应信息
#     for j in i.items:  # 遍历回应信息
#         if j.rdtype == 1:  # 避免 "AttributeError: 'CNAME' object has no attribute 'address'" 错误
#             print(j.address)

# MX
# domain = input('Please input an domain:')  # 输入地址
# MX = dns.resolver.query(domain, 'MX')  # 指定查询类型为MX记录
# for i in MX.response.answer:  # 遍历结果，输出MX记录的preference和exchange信息
#     print(i)

#  记录 （标记区域的域名服务器及授权子域） 只限输入一级域名
# ns = dns.resolver.query('baidu.com', 'NS')
# for i in ns.response.answer:
#     for j in i:
#         print(j)

#  CNAME记录 （指别名记录，实现域名间的映射）
cname = dns.resolver.query('www.uwintech.cn', 'CNAME')
for i in cname.response.answer:
    for j in i:
        print(j)
