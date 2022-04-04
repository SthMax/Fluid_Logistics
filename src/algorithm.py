from typing import List, Tuple
import numpy as np
import generator as gen
import math

#USING SIMPLE GRID BFS, ASSUME THERE IS A PATH FROM A TILE TO any CHANNEL
def EZ_BFS(mapGen: gen.mapGenerator) -> Tuple[bool, int]:
    tileMap = mapGen.getMap()
    tileList = mapGen.getTileLocales()
    channelList = mapGen.getChannelLocales()

    allStep = 0

    for i in tileList:
        cpyMap = np.copy(tileMap)
        (result, steps) = __EZ_BFS_ALGO(i,cpyMap)
        if result == False:
            print(cpyMap)
            return (False, -1)
        else:
            allStep += (len(steps) - 1)
            tileMap[i[0]][i[1]] = 0
    
    return (True, allStep)

def __EZ_BFS_ALGO(start: Tuple[int, int], map: np.ndarray) -> Tuple[bool, int]:
    
    stepQueue = [(start, [])]

    while len(stepQueue) > 0:
        curNode, curPath = stepQueue.pop(0)
        curPath.append(curNode)
        if map[curNode[0]][curNode[1]] == -2:
            return (True, curPath)

        map[curNode[0]][curNode[1]] = -4 #-4 as visited

        avaliableAdjNodes = __EZ_BFS_GETNEIGHBORS(curNode, map)
        for node in avaliableAdjNodes:
            stepQueue.append((node, curPath[:]))
    
    return (False, None)

def __EZ_BFS_GETNEIGHBORS(node: Tuple[int, int], map: np.ndarray) -> List[Tuple[int, int]]:
    neighborList = []
    #append if either empty or ending
    if map[node[0] - 1][node[1]] == 0 or map[node[0] - 1][node[1]] == -2:
        neighborList.append((node[0] - 1, node[1]))
    if map[node[0]][node[1] - 1] == 0 or map[node[0]][node[1] - 1] == -2:
        neighborList.append((node[0], node[1] - 1))
    if map[node[0] + 1][node[1]] == 0 or map[node[0] + 1][node[1]] == -2:
        neighborList.append((node[0] + 1, node[1]))
    if map[node[0]][node[1] + 1] == 0 or map[node[0]][node[1] + 1] == -2:
        neighborList.append((node[0], node[1] + 1))

    return neighborList

