from importlib.resources import path
from typing import List, Tuple
from xml.dom.expatbuilder import parseString
import numpy as np
import generator as gen
import math

#USING SIMPLE GRID BFS, ASSUME THERE IS A PATH FROM A TILE TO any CHANNEL
def EZ_BFS(mapGen: gen.mapGenerator) -> Tuple(bool, int):
    tileMap = mapGen.getMap()
    tileList = mapGen.getTileLocales()
    channelList = mapGen.getChannelLocales()

    allStep = 0

    for i in len(tileList):
        curNode = tileList[i]
        curRes = False
        curStep = -1
        for j in len(channelList):
            (result, steps) = __EZ_BFS_ALGO(tileList[i], channelList[j], tileMap)
            if result == True:
                curRes = True
                if (curStep == -1) or (curStep > len(steps)):
                    curStep == len(steps)
        if curRes == False:
            return (False, -1)
        else:
            allStep += curStep
            tileMap[curNode[0]][curNode[1]] = 0 #move out the tile
    
    return (True, allStep)

def __EZ_BFS_ALGO(start: Tuple(int, int), end: Tuple(int,int), map: np.ndarray) -> Tuple(bool, int):
    
    stepQueue = [(start, [])]

    while len(stepQueue) > 0:
        curNode, curPath = stepQueue.pop(0)
        curPath.append(curNode)
        map[curNode[0]][curNode[1]] = -4 #-4 as visited

        if curNode == end:
            return (True, curPath)

        avaliableAdjNodes = __EZ_BFS_GETNEIGHBORS(curNode, map)
        for node in avaliableAdjNodes:
            stepQueue.append((node, curPath[:]))
    
    return (False, None)

def __EZ_BFS_GETNEIGHBORS(node: Tuple(int, int), map: np.ndarray) -> List[Tuple(int, int)]:
    neighborList = []
    if map[node[0] - 1][node[1]] == 0:
        neighborList.append(node[0] - 1, node[1])
    if map[node[0]][node[1] - 1] == 0:
        neighborList.append(node[0], node[1] - 1)
    if map[node[0] + 1][node[1]] == 0:
        neighborList.append(node[0] + 1, node[1])
    if map[node[0]][node[1] + 1] == 0:
        neighborList.append(node[0], node[1] + 1)

    return neighborList

