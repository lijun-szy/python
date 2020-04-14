import pycurl

# close()实现关闭、回收Curl对象
# perform()实现Curl对象请求的提交
c = pycurl.Curl()  # 创建一个curl对象

c.setopt(pycurl.CONNECTTIMEOUT, 5)  # 连接等待时间，设置为0则不等待
c.setopt(pycurl.TIMEOUT, 5)  # 请求超时时间
c.setopt(pycurl.NOPROGRESS, 0)  # 是否屏蔽下载进度条，非0则屏蔽
c.setopt(pycurl.MAXREDIRS, 5)  # 指定HTTP重定向的最大数
c.setopt(pycurl.FORBID_REUSE, 1)  # 完成交互后强制断开连接，不重用
c.setopt(pycurl.FRESH_CONNECT, 1)  # 强制获取新的连接，即替代缓存中的连接
c.setopt(pycurl.DNS_CACHE_TIMEOUT, 60)  # 设置保存DNS信息的时间，默认为120s
c.setopt(pycurl.URL, "http://www.baidu.com")  # 指定请求的URL
c.setopt(pycurl.USERAGENT,  # 配置请求HTTP头的User-Agent
         "Mozilla/5.2 (compatible; MSIE 6.0; Windows NT 5.1;SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50324)")
c.setopt(pycurl.HEADERFUNCTION, getheader)  # 将返回的HTTP HEADER定向到回调函数getheader
c.setopt(pycurl.WRITEFUNCTION, getbody)  # 将返回的内容定向到回调函数getbody
c.setopt(pycurl.WRITEHEADER, fileobj)  # 将返回的HTTP HEADER定向到fileobj文件对象
c.setopt(pycurl.WRITEDATA, fileobj)  # 将返回的HTML内容定向到fileobj文件对象

# getinfo(option)方法

s = pycurl.Curl()
s.getinfo(pycurl.HTTP_CODE)  # 返回http状态码
s.getinfo(pycurl.TOTAL_TIME)  # 传输结束所消耗的总时间
s.getinfo(pycurl.NAMELOOKUP_TIME)  # DNS解析所消耗的时间
s.getinfo(pycurl.CONNECT_TIME)  # 从建立连接所消耗的时间
s.getinfo(pycurl.PRETRANSFER_TIME)  # 从建立连接到准备传输所消耗的时间
s.getinfo(pycurl.STARTTRANSFER_TIME)  # 从建立连接到传输开始消耗的时间
s.getinfo(pycurl.REDIRECT_TIME)  # 重定向所消耗的时间
s.getinfo(pycurl.SIZE_DOWNLOAD)  # 下载数据包大小
s.getinfo(pycurl.SIZE_UPLOAD)  # 上传数据包大小
s.getinfo(pycurl.SPEED_DOWNLOAD)  # 平均下载速度
s.getinfo(pycurl.SPEED_UPLOAD)  # 平均上传速度
s.getinfo(pycurl.HEADER_SIZE)  # HTTP头部大小
