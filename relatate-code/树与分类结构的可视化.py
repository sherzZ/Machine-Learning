#coding=utf-8
import os 
import sys
import numpy as np
import matplotlib.pyplot as plt
import treePlotter as tp 


# 绘制树
myTree = {'root':{0:'leaf node', 1:{'leavel 2':{0:'leaf node', 1:'leaf node'}}},2:{'level2':{0:'leaf node', 1:'leaf node'}}}

tp.createPlot(myTree)