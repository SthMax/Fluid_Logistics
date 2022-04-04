from email import generator
from typing import List, Tuple
import generator as gen
import algorithm as algo

def runner(X: int, Y: int, count: int, fnc: object, N = None, P = None, Locales = None) -> List[Tuple[bool, int]]: 
    params = {
        "X": X,
        "Y": Y,
        "N": N,
        "P": P,
        "Locales": Locales,
    }    
    notNoneParams = {k:v for k, v in params.items() if v is not None}

    resultList = []
    for i in range(count):
        resultList.append(fnc(gen.mapGenerator(**notNoneParams)))

    return resultList
    