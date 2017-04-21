# -*- coding: utf-8 -*-
"""
treePlotter.py
~~~~~~~~~~

A module with functions to plot decision tree.

Created on Thu Mar 23 17:26:57 2017

Run on Python 3.6

@author: Luo Shaozhuo

refer to 'MachineLearninginAction'

"""
#==============================================================================
# import
#==============================================================================
import matplotlib.pyplot as plt
import matplotlib


#==============================================================================
# Global variables
#==============================================================================
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-") 


#==============================================================================
# functions
#==============================================================================
def retrieveTree(i=0):
    """
    return a predefined tree
    ~~~~~~~~~~
    i: must be 0 or 1. 1 for a taller tree
    ~~~~~~~~~~
    dictTree
    """
    listOfTrees =[{'no surfacing': {0: 'no', 1: 'yes'}},
                  {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                  {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}
                  ]
    return listOfTrees[i]


def getNumLeafs(dictTree):
    """
    return the number of leafs
    ~~~~~~~~~~
    dictTree: a dictonary dipicting a decidion tree
    ~~~~~~~~~~
    nNumLeaf: number of leafs
    """
    nNumLeaf = 0
    for key in dictTree.keys():
        if type(dictTree[key]) == dict:
            nNumLeaf += getNumLeafs(dictTree[key])
        else:   nNumLeaf +=1
    return nNumLeaf


def getTreeDepth(dictTree):
    """
    return the tree depth
    ~~~~~~~~~~
    dictTree: a dictonary dipicting a decidion tree
    ~~~~~~~~~~
    nMaxDepth: tree depth
    """
    nMaxDepth = 0
    keys = list(dictTree.keys())[0]
    dictTrunk = dictTree[keys]
    for key in dictTrunk.keys():
        if type(dictTrunk[key]) == dict:
            nCurDepth = 1 + getTreeDepth(dictTrunk[key])
        else:
            nCurDepth = 1
        if nCurDepth > nMaxDepth:
            nMaxDepth = nCurDepth
    return nMaxDepth


def plotNode(pltAxis,strNodeTxt, tplCntrPt, tplPrntPt, nodeType):
    """
    plot a decision node or a leaf node depend on nodeType.
    ~~~~~~~~~~
    pltAxis: plot axis
    strNodeTxt: text in node box
    tplCntrPt: center coordinates of box
    tplPrntPt: starting coordinates of arrow
    nodeType: leafNode or decisionNode
    ~~~~~~~~~~
    N/A
    """
    pltAxis.annotate(strNodeTxt, xy=tplPrntPt, xycoords='axes fraction',
    xytext=tplCntrPt, textcoords='axes fraction',
    va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)


def plotMidText(pltAxis, cntrPt, parentPt, txtString):
    """
    add feature value in the middle of arrow
    ~~~~~~~~~~
    cntrPt:
    parentPt:
    txtString:
    ~~~~~~~~~~
    N/A
    """
    xMid = (parentPt[0]+cntrPt[0])/2.0
    yMid = (parentPt[1]+cntrPt[1])/2.0
    pltAxis.text(xMid, yMid, txtString)


def plotTree(dictTree, pltAxis, fTrunkLen, fBrchLen, tplCntrPt, tplPrntPt, strNodeTxt):
    """
    plot tree recursivly
    ~~~~~~~~~~
    dictTree: decision tree
    pltAxis: axis used for plotting
    fTrunkLen: difference of y coordinates between two decision nodes
    fBrchLen: difference of y coordinates between two leafs
    tplCntrPt: coordinates of parent node  
    strNodeTxt: text in node box
    ~~~~~~~~~~
    N/A
    """
    #plot root node
    plotNode(pltAxis, strNodeTxt, tplCntrPt, tplPrntPt, decisionNode)
    #plot branch node
    tplPrntPt = tplCntrPt
    nNumKey = len(dictTree.keys())
    fMean = sum([x for x in range(nNumKey)])/nNumKey
    for i,key in enumerate(dictTree.keys()):
        tplCntrPt = (tplPrntPt[0]+(i-fMean)*fBrchLen, tplPrntPt[1]-fTrunkLen)
        plotMidText(pltAxis, tplCntrPt, tplPrntPt, key)
        if type(dictTree[key]) == dict:
            strNodeTxt = list(dictTree[key].keys())[0]
            plotTree(dictTree[key][strNodeTxt], pltAxis, fTrunkLen, fBrchLen, tplCntrPt, tplPrntPt,strNodeTxt)
        else:
            strNodeTxt = dictTree[key]
            plotNode(pltAxis,strNodeTxt, tplCntrPt, tplPrntPt, leafNode)


if __name__ == '__main__':
    dictTree = retrieveTree(2)
    matplotlib.rcParams['toolbar'] = 'none'
    pltAxis = plt.subplot(111, frameon=False,xticks=[], yticks=[])
    fBrchLen = 1/getNumLeafs(dictTree)
    fTrunkLen= 1/getTreeDepth(dictTree)
    tplCntrPt = (0.5,1)
    tplPrntPt = tplCntrPt
    strNodeTxt = list(dictTree.keys())[0]
    plotTree(dictTree[strNodeTxt], pltAxis, fTrunkLen, fBrchLen, tplCntrPt, tplPrntPt,strNodeTxt)




