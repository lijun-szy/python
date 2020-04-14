import filecmp
# cmp 单文件对比
# cmpfiles 多文件
# dircmp 目录对比

bool = filecmp.cmp("./111_psutil_系统性能.py", "112_psutil_系统进程.py")
print(bool)

result = filecmp.cmpfiles("/home/tmp/ctags-test/",
                          "/home/tmp/ctags-5.8/", ['ant.c', 'args.c', 'asp.c', 'asx.c'])
print(result)

# dircmp提供了三个输出报告的方法：
#     report（）：比较当前指定目录中的内容；
#     report_partial_closure（）：比较当前指定目录及第一级子目录中 的内容；
#     report_full_closure（）：递归比较所有指定目录的内容。
# 为输出更加详细的比较结果，dircmp类还提供了以下属性：
#     left，左目录，如类定义中的a；
#     right，右目录，如类定义中的b；
#     left_list，左目录中的文件及目录列表；
#     right_list，右目录中的文件及目录列表；
#     common，两边目录共同存在的文件或目录；
#     left_only，只在左目录中的文件或目录；
#     right_only，只在右目录中的文件或目录；
#     common_dirs，两边目录都存在的子目录；
#     common_files，两边目录都存在的子文件；
#     common_funny，两边目录都存在的子目录（不同目录类型或 os.stat（）记录的错误）；
#     same_files，匹配相同的文件；
#     diff_files，不匹配的文件
#     funny_files，两边目录中都存在，但无法比较的文件；
#     subdirs，将common_dirs目录名映射到新的dircmp对象，格式为字典类型。

a = "/home/tmp/ctags-test/"
b = "/home/tmp/ctags-5.8/"

dirobj = filecmp.dircmp(a, b, ['ruby.c'])  # 忽略的文件名

print("-------------------report---------------------")
dirobj.report()
print("-------------report_partial_closure-----------")
dirobj.report_partial_closure()
print("-------------report_full_closure--------------")
dirobj.report_full_closure()

print("left_list:" + str(dirobj.left_list))
print("right_list:" + str(dirobj.right_list))
print("common:" + str(dirobj.common))
print("left_only:" + str(dirobj.left_only))
print("right_only:" + str(dirobj.right_only))
print("common_dirs:" + str(dirobj.common_dirs))
print("common_files:" + str(dirobj.common_files))
print("common_funny:" + str(dirobj.common_funny))
print("same_file:" + str(dirobj.same_files))
print("diff_files:" + str(dirobj.diff_files))
print("funny_files:" + str(dirobj.funny_files))
