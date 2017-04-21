import sys
import os
from numpy import *

# 配置utf-8输出环境
reload(sys)
sys.setdefaultencoding('utf-8')

# 数据文件转矩阵
# path: 数据文件路径
# delimiter: 行内分隔符

def file2matrix(path , delimiter):
    recordlist= []
    fp = open(path, "rb")
    content = fp.read()
    fp.close()
    rowlist = content.splitlines() # 按行转换成一维表
    # z逐行遍历， 结果按分隔符分割成行向量
    recordlist = [map(eval, row.split(delimiter)) for row in rowlist if row.strip()]
    return mat(recordlist) # 返回转换后矩阵形式

root =  "testdata" # 数据文件所在路径
pathlist = os.listdir(root)  # 获取路径下所有数据文件

for path in pathlist:
    recordmat = file2matrix(root+"/"+path, "\t")
    print(shape(recordmat))  # 输出矩阵的行， 列数
    
# 高效读取大文本文件 逐行读取

# 按行读取文件， 读取指定行数， nmax = 0 按行读取全部
def readfilelines(path, nmax = 0):
    fp = open(path , "rb")
    ncount = 0 # 已读取行数
    while True:
        content = fp.readline()
        if content=="" or (ncount > nmax and nmax !=0): # 判断文件尾， 或完成指定行数
            break
        yield content # 返回读取行
        if nmax!=0: ncount =+1
    fp.close()
path = "testdata/01.txt"
for line in readfilelines(path, nmax = 10): # 读取10行
    print (line.strip())