import rrdtool
import time
import psutil
# rrdtool主要用来跟踪对象的变化情况，生成这些变化的走势图，比如业务的访问流量、系统性能、磁盘利用率等趋势图
cur_time = str(int(time.time()))  # 获取linux当前时间戳为rrd起始时间
# 数据写频率---step为300s(即五分钟一个数据点)

# 创建RRD数据库
# create 语法
# rrdtool create filename
# [--start | -b start time]
# [--step | -s step]
# # 最后获取的数据是PDP，更新数据时要考滤DS顺序(*把所有要更新的数据，按照DS定义的顺序用冒号格开*)
# DS: ds-name: DST: dst arguments
# RRA: CF: cf arguments  # 最后获取的数据是CDP,绘图时使用的是这些数据
# # 最后获取的数据是PDP，更新数据时要考滤DS顺序(*把所有要更新的数据，按照DS定义的顺序用冒号格开*)
# DS: ds-name: DST: dst arguments
# RRA: CF: cf arguments  # 最后获取的数据是CDP,绘图时使用的是这些数据
# 参数详解：
# DS：DS 用于定义 Data Soure 。也就是用于存放结果的变量名。DS是用来申明数据源的，也可以理解为申明数据变量，也就是你要检测的端口对应的变量名，这个参数在画图的时候还要使用的。
# DST：DST 就是DS的类型。有 COUNTER、GUAGE、DERIVE、ABSOLUTE、COMPUTE 5种。由于网卡流量属于计数器型，所以这里应该为 COUNTER 。
# RRA：RRA 用于指定数据如何存放。我们可以把一个RRA 看成一个表，各保存不同 interval 的统计结果。RRA的作用就是定义更新的数据是如何记录的。比如我们每5分钟产生一条刷新的数据，那么一个小时就是12条。每天就是288条。这么庞大的数据量，一定不可能都存下来。肯定有一个合并（consolidate）数据的方式，那么这个就是RRA的作用了。
#       RRA:{AVERAGE | MIN | MAX | LAST}:xff:steps:rows 表示归档的属性：归并函数，unknown值最大占比，步长（n个step)，步数（即大小）
#       xff：表示当该RRA的时间间隔内unkown值占比为多少时，归并之后的值被记为unknown.
#       step 采集数据的间隔时间,习惯上我们会设 300 (秒)
# PDP：Primary Data Point 。正常情况下每个 interval RRDtool 都会收到一个值；RRDtool 在收到脚本给来的值后会计算出另外一个值（例如平均值），这个 值就是 PDP ；这个值代表的一般是“xxx/秒”的含义。注意，该值不一定等于RRDtool 收到的那个值。除非是GAUGE ，可以看下面的例子就知道了
# CF：CF 就是 Consolidation Function 的缩写。也就是合并（统计）功能。有 AVERAGE、MAX、MIN、LAST 四种分别表示对多个PDP 进行取平均、取最大值、取最小值、取当前值四种类型。具体作用等到 update 操作时再说。
# CDP：Consolidation Data Point 。RRDtool 使用多个 PDP 合并为（计算出）一个 CDP。也就是执行上面 的CF 操作后的结果。这个值就是存入 RRA的数据，绘图时使用的也是这些数据

# 1、创建rrd数据库
rrd = rrdtool.create('Flow.rrd', '--step', '300', '--start', cur_time,
                     # 定义数据源eth0_in(流入量)，eth0_out(流出量)；类型都为COUNTER(递增)；
                     # 600s为心跳值，其含义为600s没有收到值，则会用UNKNOWN代替；0为最小值，最大值为U代替，表示不确定
                     'DS:etho_in:COUNTER:600:0:U',
                     'DS:etho_out:COUNTER:600:0:U',
                     'RRA:AVERAGE:0.5:1:600',  # 1即300s,总共存600个
                     'RRA:AVERAGE:0.5:6:700',
                     'RRA:AVERAGE:0.5:24:775',
                     'RRA:AVERAGE:0.5:28:797',
                     'RRA:MAX:0.5:1:600',
                     'RRA:MAX:0.5:6:700',
                     'RRA:MAX:0.5:24:775',
                     'RRA:MAX:0.5:28:797',
                     'RRA:MIN:0.5:1:600',
                     'RRA:MIN:0.5:6:700',
                     'RRA:MIN:0.5:24:775',
                     'RRA:MIN:0.5:28:797')
if rrd:
    print(rrdtool.error())

# 2、采用updatev()方法更新数据库
# update filename [--template|-t ds-name[:ds-name]...] N|timestamp:value[:value...] [timestamp:value[:value...] ...] 方法，
# 存储一个新值到rrdtool数据库，updatev和update类似，区别是每次插入后会返回一个状态码，以便了解是否成功（updatev用0表示成功，–1表示失败）。参数说明如下：
# filename指定存储数据到的目标rrd文件名；
# -t ds-name[:ds-name]指定需要更新的DS名称；
# N|Timestamp表示数据采集的时间戳，N表示当前时间戳；
# value[:value...]更新的数据值，多个DS则多个值。
total_input_traffic = psutil.net_io_counters()[1]  # 网卡入流量
total_output_traffic = psutil.net_io_counters()[0]  # 网卡出流量

start_time = int(time.time())  # 获取当前时间
# 将获取到的三个数据作为updatev的参数，返回{'return_value': 0L}则说明更新成功，反之失败
update = rrdtool.updatev('/home/pycode/py自动化/Flow.rrd', '%s:%s:%s' %
                         (str(start_time), str(total_input_traffic), str(total_output_traffic)))
print(update)

# [root@localhost rrdtool]# crontab -e
# crontab: installing new crontab
# [root@localhost rrdtool]# crontab -l
# */5 * * * * /usr/bin/python /home/pycode/py自动化/322_rrdtool_网卡流量图绘制.py > /dev/null 2>&1
