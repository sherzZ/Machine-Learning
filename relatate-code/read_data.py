import sys
import os
from numpy import *

# ����utf-8�������
reload(sys)
sys.setdefaultencoding('utf-8')

# �����ļ�ת����
# path: �����ļ�·��
# delimiter: ���ڷָ���

def file2matrix(path , delimiter):
    recordlist= []
    fp = open(path, "rb")
    content = fp.read()
    fp.close()
    rowlist = content.splitlines() # ����ת����һά��
    # z���б����� ������ָ����ָ��������
    recordlist = [map(eval, row.split(delimiter)) for row in rowlist if row.strip()]
    return mat(recordlist) # ����ת���������ʽ

root =  "testdata" # �����ļ�����·��
pathlist = os.listdir(root)  # ��ȡ·�������������ļ�

for path in pathlist:
    recordmat = file2matrix(root+"/"+path, "\t")
    print(shape(recordmat))  # ���������У� ����
    
# ��Ч��ȡ���ı��ļ� ���ж�ȡ

# ���ж�ȡ�ļ��� ��ȡָ�������� nmax = 0 ���ж�ȡȫ��
def readfilelines(path, nmax = 0):
    fp = open(path , "rb")
    ncount = 0 # �Ѷ�ȡ����
    while True:
        content = fp.readline()
        if content=="" or (ncount > nmax and nmax !=0): # �ж��ļ�β�� �����ָ������
            break
        yield content # ���ض�ȡ��
        if nmax!=0: ncount =+1
    fp.close()
path = "testdata/01.txt"
for line in readfilelines(path, nmax = 10): # ��ȡ10��
    print (line.strip())