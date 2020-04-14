import os
import sys
import filecmp
import re
import shutil

holderlist = []

# 递归获取更新项函数


def mycompare(dir1, dir2):
    dircompare = filecmp.dircmp(dir1, dir2)
    only_in_one = dircompare.left_only  # 源目录新文件或目录
    diff_in_one = dircompare.diff_files  # 不匹配文件，文件已发生变化
    dirpath = os.path.abspath(dir1)  # 定义源目录绝对路径

    # 将更新文件或目录追加到holderlist
    [holderlist.append(os.path.abspath(os.path.join(dir1, x)))
     for x in only_in_one]

    [holderlist.append(os.path.abspath(os.path.join(dir2, x)))
     for x in diff_in_one]

    # 判断是否存在相同子目录，以便递归
    # 递归子目录
    if len(dircompare.common_dirs) > 0:  # 判断是否存在相同子目录，以便递归
        for item in dircompare.common_dirs:  # 递归子目录
            mycompare(os.path.abspath(os.path.join(dir1, item)),
                      os.path.abspath(os.path.join(dir2, item)))
    return holderlist


def main():
    if len(sys.argv) > 2:  # 要求输入源目录与备份目录
        dir1 = sys.argv[1]
        dir2 = sys.argv[2]
    else:
        print("Usage: %s datadir backdir" % sys.argv[0])
        sys.exit()
    sourece_file = mycompare(dir1, dir2)
    print("-----sourece_file------")
    print(sourece_file)
    print("-----sourece_file------")
    dir1 = os.path.abspath(dir1)
    if not dir2.endswith('/'):  # 备份路径加'/'符
        dir2 = dir2 + '/'
    dir2 = os.path.abspath(dir2)
    destination_files = []
    createdir_bool = False

    for item in sourece_file:  # 遍历返回的清单
        # print("-----for---")
        # print("dir1: %s" % dir1)
        # print("dir2: %s" % dir2)
        # print("item: %s" % item)
        destination_dir = re.sub(dir1, dir2, item)  # 将源目录差异路径清单对应替换成备份目录
        # print("dir1: %s" % dir1)
        # print("dir2: %s" % dir2)
        # print("-----for---")

        destination_files.append(destination_dir)
        if os.path.isdir(item):  # 如果差异路径为目录且不存在，则在备份目录中创建
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
                print(destination_dir)
                createdir_bool = True  # 调用mycompare函数标记
    print("-----destination_files---")
    print(destination_files)
    print("-----destination_files---")
    if createdir_bool:  # 重新调用mycompare函数，重新遍历新创建的内容
        destination_files = []
        sourece_file = []
        sourece_file = mycompare(dir1, dir2)
        print("-----sourece_file------")
        print(sourece_file)
        print("-----sourece_file------")

        for item in sourece_file:  # 获取源目录差异清单，对应替换成备份目录
            destination_dir = re.sub(dir1, dir2, item)
            destination_files.append(destination_dir)
        print("-----destination_files---")
        print(destination_files)
        print("-----destination_files---")

    print("update items:")
    print(sourece_file)
    # 将源目录与备份目录文件清单拆分成元组  zip()函数返回一个以元组为元素的列表
    copy_pair = zip(sourece_file, destination_files)
    for item in copy_pair:
        print(item)
        if os.path.isfile(item[0]):  # 判断是否为文件，是则复制
            shutil.copyfile(item[0], item[1])


if __name__ == "__main__":
    main()
