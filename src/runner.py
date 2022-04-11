from multiprocessing import Pool, TimeoutError
import time
import multiprocessing
from typing import List, Tuple
import pandas

from pytz import country_timezones
from src.generator import mapGenerator
from src.algorithm import *
from pandas import DataFrame

def runner(X: int, Y: int, C: int, B:int, fnc: object, N = None, P = None, Locales = None) -> List[Tuple[bool, int]]: 
    params = {
        "X": X,
        "Y": Y,
        "N": N,
        "P": P,
        "C": C,
        "Locales": Locales,
    }    
    notNoneParams = {k:v for k, v in params.items() if v is not None}

    return fnc(mapGenerator(**notNoneParams), B)
    # resultList = []
    # for i in range(count):
    #     resultList.append(fnc(mapGenerator(**notNoneParams)))

    # return resultList

def paralleledRunner(X: int, Y: int, C:int, block: int, count: int, fnc: object, N = None, P = None, Locales = None) -> pandas.DataFrame:
    resultList = []
    workers = multiprocessing.cpu_count()

    #if __name__ == '__main__':
    print("paralleledRunner(X={},Y={},C={},Loop={},block={},fnc={},N={},P={}) Starting".format(X,Y,C,count,block,fnc,N,P))
    start = time.time()
    with Pool(processes=workers) as pool:
        multipleResults = [pool.apply_async(runner, (X,Y,C,block,fnc,N,P,Locales)) for i in range(count)]
        try:
            resultList = [res.get() for res in multipleResults]
        except TimeoutError:
            print("TIMEOUT ON RUNNER")
    end = time.time()
    print("Using {} seconds".format(end - start))
    d = {
        "MN": [(Y, X)], 
        "C": [C],
        "B": [block],
        "steps": [[x[1] for x in resultList]],
        "density": [1 - C/X],
    }
    return DataFrame(data=d)
    
def singleThreadRunner(X: int, Y: int, count: int, fnc: object, N = None, P = None, Locales = None) -> List[Tuple[bool, int]]:
    return [runner(X,Y,fnc,N,P,Locales) for i in range(count)]



        

    