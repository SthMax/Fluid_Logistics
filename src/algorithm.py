from logging import StringTemplateStyle
from time import sleep
from typing import List, Tuple
import sys
import numpy as np
import src.generator as gen
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

def EMPTY_BLOCK_MOVEMENT(mapGen: gen.mapGenerator, block: int) ->Tuple[bool,int]:
    totalSteps = 0

    tileMap = mapGen.getMap()
    tileList = mapGen.getTileLocales()

    tileX = mapGen.X - 2
    tileY = mapGen.Y - 2

    #transform tileList into 2d array
    emptyTileList = [[tileList[j*mapGen.C + i] for i in range(mapGen.C)] for j in range(tileY)]

    rng = np.random.default_rng() #random generator

    idx = 0

    while idx < block:
        blockY = rng.integers(low = 1, high=tileY, endpoint=True)
        blockX = rng.integers(low = 1, high=tileX, endpoint=True)

        if (tileMap[blockY][blockX] == 1): #there is a block on (block Y, block X)
            #print ("CHOOSED", (blockY, blockX))
            steps = 0

            for i in range(blockY - 1, 0, -1):
                closetEmptyBlockLocale = __MIN_HORIZONTAL_DISTANCE(emptyTileList[i - 1], blockX)
                (CEBY,CEBX) = emptyTileList[i - 1][closetEmptyBlockLocale]

                #print ("MOVING", (CEBY, CEBX))
                
                if (CEBX != blockX):
                    steps += abs(CEBX - blockX)

                    tileMap[CEBY][CEBX] = 1
                    tileMap[CEBY][blockX] = 0

                    #print ("TO", (CEBY, blockX))
                    emptyTileList[i - 1][closetEmptyBlockLocale] = (CEBY,blockX)

                # print(tileMap)
                # sleep(1)
                # for i in range(len(tileMap)):
                #     sys.stdout.write("\033[F") #back to previous line 
                #     sys.stdout.write("\033[K") #clear line 
                steps += 1

            tileMap[blockY][blockX] = 0          
            emptyTileList[blockY - 1].append((blockY,blockX))
            totalSteps += steps
            idx += 1
        else:
            pass
    #print(tileMap)
    return (True, totalSteps)


def __MIN_HORIZONTAL_DISTANCE(rowList: List[Tuple[int,int]], fixed_X: int) -> int:
    returnIdx = 0
    for i in range(len(rowList)):
        prevX = rowList[returnIdx][1]
        X = rowList[i][1]
        if (abs(X - fixed_X) <= abs(prevX - fixed_X)):
            returnIdx = i

    return returnIdx
