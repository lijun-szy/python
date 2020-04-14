import xlsxwriter

workbook = xlsxwriter.Workbook('chart.xlsx')
worksheet = workbook.add_worksheet()
chart = workbook.add_chart({'type': 'column'})  # 创建一个图标对象
# 定义数据表头列表
title = [u'业务名称', u'星期一', u'星期二', u'星期三',
         u'星期四', u'星期五', u'星期六', u'星期天', u'平均流量']
# 定义频道名称
buname = [u'业务官网', u'购物频道', u'体育频道', u'新闻中心', u'亲子频道']
# 定义五个频道七天的数据流量列表
data = [
    [156, 113, 164, 225, 565, 168, 217],
    [136, 123, 184, 245, 355, 268, 327],
    [146, 133, 134, 285, 755, 468, 527],
    [176, 133, 104, 205, 255, 568, 327],
    [116, 173, 154, 105, 655, 568, 727],
]

format = workbook.add_format()  # 定义formate格式化对象
format .set_border(1)  # 定义format对象单元格边框加粗(1像素)的格式

format_title = workbook.add_format()  # 定义format_title格式对象
format_title.set_border(1)  # 单元格边框加粗
format_title.set_bg_color('#cccccc')  # 定义format_title对象单元格背景颜色为'#cccccc'
format_title.set_align('center')  # 定义format_title对象单元格居中对齐的格式
format_title.set_bold()  # 定义format_title对象单元格内容加粗

format_ave = workbook.add_format()  # 定义format_ave格式化对象
format_ave.set_border(1)
format_ave.set_num_format('0.00')  # 定义数字类别显示格式

# 开始分别以行或者列的方式将标题,业务名称等写入单元格,同时引用不用的格式对象
worksheet.write_row('A1', title, format_title)
worksheet.write_column('A2', buname, format)
worksheet.write_row('B2', data[0], format)
worksheet.write_row('B3', data[1], format)
worksheet.write_row('B4', data[2], format)
worksheet.write_row('B5', data[3], format)
worksheet.write_row('B6', data[4], format)

# 定义图表数据系列函数
# ^数字 乘方运算，如2^3结果8。
# ^(1/数字) 开方运算 8^(1/3)结果为2
# & 文本连续符，如 "A"& 1 结果为 A1
# * 通配符 表示任意字符多个字符
# ? 通配符，表示单个任意字符
# {数字} 常量数组
# {公式} 数组公式标志，在公式后按Ctrl + shift + Enter后在公式两端自动添加的。
# $ 绝对引用符号，可以在复制公式时防止行号或列标发生变动，如A&1公式向下复制时，1不会变成2,3..如果不加$则会变化
# ！ 工作表和单元格的隶属关于，如表格sheet1的单元格A1,表示为 Sheet1!A1


def chart_series(cur_row):
    # 计算（AVERAGE函数）
    worksheet.write_formula(
        'I'+cur_row, '=AVERAGE(B'+cur_row+':H'+cur_row+')', format_ave)
    chart.add_series({
        'categories': 'Sheet1!$B$1:$H$1',  # 将星期一至星期日作为图表数据标签(X轴)
        'values': '=Sheet1!$B$'+cur_row+':$H$'+cur_row,  # 频道一周所有数据作为数据区域
        'line': {'color': 'black'},  # 线条黑色
        'name': '=Sheet1!$A$'+cur_row  # 引用业务名称为图例项
    })


for row in range(2, 7):  # 数据域以2~6行进行图表数据系列函数调用
    chart_series(str(row))

chart.set_table()  # 设置X轴表格格式
chart.set_style(30)  # 设置图表样式
chart.set_size({'width': 580, 'height': 300})  # 设置图表大小
chart.set_title({'name': u'流量周报'})  # 设置图表（上方）大标题
chart.set_y_axis({'name': 'Mb/s'})  # 设置y轴（左侧小标题）

worksheet.insert_chart('A8', chart)
workbook.close()
