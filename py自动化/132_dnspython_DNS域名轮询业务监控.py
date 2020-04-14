import dns.resolver
import os
import httplib2
iplist = []  # 定义域名IP列表变量
appdomain = "www.baidu.com"  # 定义业务域名


# 域名解析函数，解析成功IP将被追加到iplist
def get_iplist(domain=""):
    try:
        A = dns.resolver.query(domain, 'A')  # 解析A记录类型
    except Exception as e:
        print("Dns resolver error: %s" % str(e))
        return
    for i in A.response.answer:
        for j in i.items:
            if j.rdtype == 1:
                iplist.append(j.address)
    return True


def checkip(ip):
    checkurl = ip + ":80"
    getcontent = ""
    httplib2.socket.setdefaulttimeout(5)  # 定义http连接超时时间5s
    conn = httplib2.HTTPConnectionWithTimeout(checkurl)  # 创建http连接对象

    try:
        # 发起URL请求，添加host主机头
        conn.request("GET", "/", headers={"Host": appdomain})
        r = conn.getresponse()
        getcontent = r.read(15)  # 获取URL页面前15个字符，以便做可用性校验
        print(getcontent)
    finally:
        if str(getcontent, encoding="utf-8") == "<!DOCTYPE html>":  # 监控url页面的内容一般是提前定义好的，比如“HTTP200”等
            print("%s OK" % ip)
        else:
            print("%s ERROR" % ip)


if __name__ == "__main__":
    if get_iplist(appdomain) and len(iplist) > 0:
        for ip in iplist:
            checkip(ip)
    else:
        print("DNS resolver error")
