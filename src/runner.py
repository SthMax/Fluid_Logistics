from multiprocessing import Pool, TimeoutError
import multiprocessing
from typing import List, Tuple
from generator import mapGenerator
from algorithm import *

def runner(X: int, Y: int, fnc: object, N = None, P = None, Locales = None) -> List[Tuple[bool, int]]: 
    params = {
        "X": X,
        "Y": Y,
        "N": N,
        "P": P,
        "Locales": Locales,
    }    
    notNoneParams = {k:v for k, v in params.items() if v is not None}

    return fnc(mapGenerator(**notNoneParams))
    # resultList = []
    # for i in range(count):
    #     resultList.append(fnc(mapGenerator(**notNoneParams)))

    # return resultList

def paralleledRunner(X: int, Y: int, count: int, fnc: object, N = None, P = None, Locales = None) -> List[Tuple[bool, int]]:
    resultList = []
    workers = multiprocessing.cpu_count()

    if __name__ == '__main__':
        with Pool(processes=workers) as pool:
            multipleResults = [pool.apply_async(runner, (X,Y,fnc,N,P,Locales)) for i in range(count)]
            try:
                resultList = [res.get(timeout = 1) for res in multipleResults]
            except TimeoutError:
                print("TIMEOUT ON RUNNER")
        return resultList
    
def singleThreadRunner(X: int, Y: int, count: int, fnc: object, N = None, P = None, Locales = None) -> List[Tuple[bool, int]]:
    return [runner(X,Y,fnc,N,P,Locales) for i in range(count)]



        

    