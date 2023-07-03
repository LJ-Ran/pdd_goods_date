# txt文件的存放路径
desktop_path = "/Users/sixuncle/Desktop/MY/"
count = 0
# 需要修改的名字
file_name = "文件的名字"
#  需要创建txt 的个数
creat_txt_number = 5
for i in range(1, creat_txt_number + 1):
    # 命名格式
    full_path = desktop_path + file_name + str(i) + '.txt'
    file = open(full_path, 'w')
    file.close()
