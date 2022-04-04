from typing import List, Tuple
#from pandas import DataFrame
import numpy as np

class mapGenerator:

    #initilization
    def __init__(self, X: int, Y: int, N: int = 1, P:float = 0.1, Locales: List[str] = ["TRR"]) -> np.ndarray:
        self.X = X
        self.Y = Y
        self.P = P
        self.N = N
        self.localeStr = Locales
        self.tileNumericLocales: List[Tuple[int,int]] = []
        self.channelNumericLocales: List[Tuple[int,int]] = []
        self.map: np.ndarray
        self.mapGen()

    #@overrides print as printing the map, using dataframe for visibility
    def __repr__(self) -> str:
        #return str(DataFrame(self.map, dtype=int))
        return str(self.map)

    #Default Tile Placement Random Generation Function, Generating Numbered Tiles
    def mapGen(self) -> None:
        self.map = np.zeros((self.Y,self.X), dtype=int)
        tilePool = np.array(range(self.X*self.Y)) #Creating possible canditates for plates

        rng = np.random.default_rng() #random generator

        for i in range(int(self.X*self.Y*self.P)):
            candidate = rng.integers(low = 0, high = len(tilePool))
            candidate_locale = tilePool[candidate]

            self.map[candidate_locale % self.Y][candidate_locale // self.Y] = 1 + i
            self.tileNumericLocales.append((candidate_locale % self.Y, candidate_locale // self.Y)) 

            tilePool = np.delete(tilePool, candidate)


    #Generate Channel
    def channelGen(self) -> None:
        self.__addWallsToMap()
        self.__strCmdToLocales()

        htwp = np.array(range(self.X))
        hdwp = htwp + ((self.Y - 1) * self.X)
        vlwp = np.array(range(1, self.Y - 1)) * self.X
        vrwp = vlwp + self.X - 1
        channelPool = np.concatenate((htwp, hdwp, vlwp, vrwp))

        rng = np.random.default_rng() #random generator

        for i in range(self.N):
            candidate = rng.integers(low = 0, high = len(channelPool))
            candidate_locale = channelPool[candidate]

            if self.map[candidate_locale % self.Y][candidate_locale // self.Y] == -3:
                self.map[candidate_locale % self.Y][candidate_locale // self.Y] = -2 #set as outbound only
                self.channelNumericLocales.append((candidate_locale % self.Y, candidate_locale // self.Y))
            else:
                pass

            channelPool = np.delete(channelPool, candidate)

    #Switch the numbering of tiles to multiple batches, IRREVERSIABLE
    def mapBatchify(self, B: int) -> None:
        if B > 0:
            for i in range(self.tileNumericLocales):
                candidate_locale = self.tileNumericLocales[i]
                self.map[candidate_locale[0]][candidate_locale[1]] = i // (len(self.tileNumericLocales) + 1 // B) + 1


    def getMap(self) -> np.ndarray:
        return self.map

    # Setter is disabled
    # def setMap(self, inputMap: np.ndarray) -> None:
    #     self.map = inputMap

    def getTileLocales(self) -> List[Tuple[int,int]]:
        return self.tileNumericLocales

    def getChannelLocales(self) -> List[Tuple[int,int]]:
        return self.channelNumericLocales

    def __strCmdToLocales(self) -> None:
        X = self.X
        Y = self.Y
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
                self.map[loc[0]][loc[1]] = -2 #set as outbound only
                self.N -= 1
            else:
                pass

    
    def __addWallsToMap(self) -> None:
        vertWall = np.zeros((self.Y,1), dtype = int) - 3
        hrznWall = np.zeros((1,self.X + 2), dtype = int) -3
        self.map = np.hstack((vertWall, np.hstack((self.map, vertWall))))
        self.map = np.vstack((hrznWall, np.vstack((self.map, hrznWall))))
        self.Y += 2
        self.X += 2


