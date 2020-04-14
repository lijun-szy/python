import xlsxwriter

workbook = xlsxwriter.Workbook("demo1.xlsx")  # 创建一个Excel文件
worksheet = workbook.add_worksheet()  # 创建一个工作表对象

worksheet.set_column('A:A', 20)  # 设置第一列A宽度20像素
bold = workbook.add_format({'bold': True})  # 定义一个加粗格式对象

worksheet.write('A1', 'hello')  # A1单元格写入"Hello"
worksheet.write('A2', 'world', bold)  # A2单元格写入‘world’并引用加粗格式对象bold
worksheet.write('B2', u'中文测试', bold)  # B2单元格写入中文并引用加粗格式对象bold

worksheet.write(2, 0, 32)  # 用行列表示法写入数字'32'，行列表示法的单元格下标以0作为起始值
worksheet.write(3, 0, 44.5)  # '3, 0'相当于A3

worksheet.write('B3', 44.5)
worksheet.write('B4', 44.5)
worksheet.write(4, 1, '=SUM(B3: B4)')  # 求A3和A4的和，并将结果写入'4, 0', 即'A5'

worksheet.insert_image('B7', './test.jpg')  # 插入图片

worksheet1 = workbook.add_worksheet()
worksheet2 = workbook.add_worksheet('AND')
worksheet3 = workbook.add_worksheet('DATA')
worksheet4 = workbook.add_worksheet()

workbook.close()
