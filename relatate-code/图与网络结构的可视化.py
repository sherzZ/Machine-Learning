#coding=utf-8

# 图与网络结构是神经网络和贝叶斯网络中重要的数据结构
# 完整的结构一般使用dict+list进行存储
# 在算法中图一般使用邻接矩阵的形式， 使用numpy的矩阵结构存储点坐标：弧的z坐标使用距离计算公式
# 可视化时可以生成x轴的List和y轴的list显示在图片中

from numpy import *
import matplotlib.pyplot as plt

dist = mat([[0.1,0.1],[0.9,0.6],[0.9,0.1],[0.45,0.9],[0.7,0.9],[0.1,0.45],[0.45,0.1]])
m,n = shape(dist)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(dist.T.tolist()[0],dist.T.tolist()[1],c='blue', marker='o')
for point in dist.tolist():
    plt.annotate("("+str(point[0])+","+str(point[1])+")",xy=(point[0],point[1]))

xlist = []
ylist = []
for px, py in zip(dist.T.tolist()[0], dist.T.tolist()[1]):
    xlist.append([px])
    ylist.append([py])
ax.plot(xlist, ylist, 'r')
plt.show()