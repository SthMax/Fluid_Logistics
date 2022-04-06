from time import sleep
from typing import List, Tuple
import sys
import numpy as np
import generator as gen
import math

#USING SIMPLE GRID BFS, ASSUME THERE IS A PATH FROM A TILE TO any CHANNEL
def EZ_BFS(mapGen: gen.mapGenerator) -> Tuple[bool, int]:
    tileMap = mapGen.getMap()
    tileList = mapGen.getTileLocales()

    allStep = 0

    for i in tileList:
        # print(tileMap)
    
        cpyMap = np.copy(tileMap)
        (result, steps) = __EZ_BFS_ALGO(i,cpyMap)
        if result == False:
            # print(cpyMap)
            return (False, -1)
        else:
            allStep += (len(steps) - 1)
            tileMap[i[0]][i[1]] = 0
        
        # for i in range(len(tileMap)):
        #     sys.stdout.write("\033[F") #back to previous line 
        #     sys.stdout.write("\033[K") #clear line 
            
    return (True, allStep)

def __EZ_BFS_ALGO(start: Tuple[int, int], tileMap: np.ndarray) -> Tuple[bool, int]:
    
    stepQueue = [(start, [])]

    while len(stepQueue) > 0:
        curNode, curPath = stepQueue.pop(0)
        curPath.append(curNode)
        if tileMap[curNode[0]][curNode[1]] == -2:
            return (True, curPath)
        if tileMap[curNode[0]][curNode[1]] == -4:
            pass
        else:
            # DEBUG & DISPLAY MODULE
            # sleep(0.5)
            # 
            # for i in range(len(tileMap)):
            #     sys.stdout.write("\033[F") #back to previous line 
            #     sys.stdout.write("\033[K") #clear line 

            tileMap[curNode[0]][curNode[1]] = -4 #-4 as visited
            # print(tileMap)
        

            avaliableAdjNodes = __EZ_BFS_GETNEIGHBORS(curNode, tileMap)
            for node in avaliableAdjNodes:
                stepQueue.append((node, curPath[:]))
    
    return (False, None)

def __EZ_BFS_GETNEIGHBORS(node: Tuple[int, int], tileMap: np.ndarray) -> List[Tuple[int, int]]:
    neighborList = []
    #append if either empty or ending
    if tileMap[node[0] - 1][node[1]] == 0 or tileMap[node[0] - 1][node[1]] == -2:
        neighborList.append((node[0] - 1, node[1]))
    if tileMap[node[0]][node[1] - 1] == 0 or tileMap[node[0]][node[1] - 1] == -2:
        neighborList.append((node[0], node[1] - 1))
    if tileMap[node[0] + 1][node[1]] == 0 or tileMap[node[0] + 1][node[1]] == -2:
        neighborList.append((node[0] + 1, node[1]))
    if tileMap[node[0]][node[1] + 1] == 0 or tileMap[node[0]][node[1] + 1] == -2:
        neighborList.append((node[0], node[1] + 1))

    return neighborList

#TILE SORTING USING 
def A_STAR_SORTING(mapGen: gen.mapGenerator) -> Tuple[bool,int]:
    pass

# res = EZ_BFS(gen.mapGenerator(30,30,P=0.01))
# print(res)