import difflib
# '- '仅在片段1中存在
# '+ '仅在片段2中存在
# ' '片段1和2中都存在
# '? '存在疑问的
text1 = """text1: # 定义字符串1
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib document v7.4
add string
"""

text1_lines = text1.splitlines()

text2 = """text2: # 定义字符串2
This module provides classes and functions for Comparing sequences.
including HTML and context and unified diffs.
difflib document v7.5"""

text2_lines = text2.splitlines()

d = difflib.Differ()  # 创建Differ()对象
diff = d.compare(text1_lines, text2_lines)  # 采用compare方法对字符串进行比较
# print(''.join(list(diff)))

# SequenceMatcher()类支持任意类型序列的比较

# 采用HtmlDiff()类的make_file()方法可以生成美观的HTML文档
h = difflib.HtmlDiff()
print(h.make_file(text2_lines, text1_lines))
