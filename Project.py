#Manager & Plotter, NOT IMPLEMENTED
import numpy as np
import pandas as pd

import threading

from src.algorithm import *
from src.runner import paralleledRunner

def dataCollection() -> pd.DataFrame:
    res = pd.DataFrame({
        "MN":[],
        "C":[],
        "B":[],
        "steps":[],
        "density":[],
    })
    for i in range(20, 100, 20):            #size of m & n
        for j in range(1,5):                #size of c
            for k in [1,5,10,15,20]:        #size of b
                d = paralleledRunner(i, i, j, k, 2000,EMPTY_BLOCK_MOVEMENT,Locales=["TOP"])
                e = paralleledRunner(i*2, i, j, k, 2000,EMPTY_BLOCK_MOVEMENT,Locales=["TOP"])
                f = paralleledRunner(i, i*2, j, k, 2000,EMPTY_BLOCK_MOVEMENT,Locales=["TOP"])
                res = pd.concat([res, d, e, f], ignore_index=True)
    # for i in range(100,1100,200):           #size of m & n
    #     for j in range(1,5):                #size of c
    #         for k in [1,5,10,15,20,100]:    #size of b
    #             d = paralleledRunner(i, i, j, k, 100,EMPTY_BLOCK_MOVEMENT,Locales=["TOP"])
    #             e = paralleledRunner(i*2, i, j, k, 100,EMPTY_BLOCK_MOVEMENT,Locales=["TOP"])
    #             f = paralleledRunner(i, i*2, j, k, 100,EMPTY_BLOCK_MOVEMENT,Locales=["TOP"])
    #             res = pd.concat([res, d, e, f])

    # d = paralleledRunner(20, 20, 3, 5, 100,EMPTY_BLOCK_MOVEMENT,Locales=["TOP"])
    # e = paralleledRunner(20*2, 20, 3, 5, 100,EMPTY_BLOCK_MOVEMENT,Locales=["TOP"])
    # f = paralleledRunner(20, 20*2, 3, 5, 100,EMPTY_BLOCK_MOVEMENT,Locales=["TOP"])
    # res = pd.concat([res,d,e,f],ignore_index=True)
    return res
