from typing import List, Tuple
#from pandas import DataFrame
import numpy as np

class mapGenerator:

    #initilization
    def __init__(self, X: int, Y: int, N: int = 0, P:float = 0.1, Locales: List[str] = ["TRR"]) -> np.ndarray:
        self.X = X
        self.Y = Y
        self.P = P
        self.N = N
        self.localeStr = Locales
        self.tileNumericLocales: List[Tuple[int,int]] = []
        self.map: np.ndarray
        self.mapGen()

    #@overrides print as printing the map, using dataframe for visibility
    def __repr__(self) -> str:
        #return str(DataFrame(self.map, dtype=int))
        return str(self.map)

    #Default Tile Placement Random Generation Function, Generating Numbered Tiles
    def mapGen(self) -> None:
        self.map = np.zeros((self.Y,self.X), dtype=int)
        poolSize = self.X*self.Y
        dotPool = list(range(poolSize)) #Creating possible canditates for plates

        rng = np.random.default_rng() #random generator

        for i in range(int(self.X*self.Y*self.P)):
            candidate = rng.integers(low = 0, high = poolSize)
            candidate_locale = dotPool[candidate]

            self.map[candidate_locale % self.Y][candidate_locale // self.Y] = 1 + i
            self.tileNumericLocales.append((candidate_locale % self.Y, candidate_locale // self.Y)) 

            del dotPool[candidate]
            poolSize -= 1

    def chanelGen(self) -> None:
        
        pass

    def mapBatchify(self, B: int) -> None:
        pass

    def getMap(self) -> np.ndarray:
        return self.map

    # Setter is disabled
    # def setMap(self, inputMap: np.ndarray) -> None:
    #     self.map = inputMap

    def getTileLocales(self) -> List[Tuple[int,int]]:
        return self.tileNumericLocales

    def __strCmdToLocales(self, X:int, Y:int) -> None:
        locationsMapping = {
            "TLT": (0,1),
            "TTT": (0, X // 2),
            "TRT": (0, X - 2),
            "TLL": (1, 0),
            "TRR": (1, X - 1),
            "MLL": (Y // 2, 0),
            "MRR": (Y // 2, X - 1),
            "DLL": (Y - 2, 0),
            "DRR": (Y - 2, X - 1),
            "DLD": (Y - 1, 1),
            "DDD": (Y - 1, X // 2),
            "DRD": (Y - 1, X - 2),
        }
        for i in self.localeStr:
            loc = locationsMapping.get(i)
            if loc != None:
                self.map[loc[0]][loc[1]] = -2
            else:
                pass



