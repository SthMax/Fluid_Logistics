from typing import List, Tuple
#from pandas import DataFrame
import numpy as np

class mapGenerator:
    #initilization
    def __init__(self, X: int, Y: int, N: int = 0, C: int = 0, P:float = 0.1, Locales: List[str] = ["TRR"]) -> np.ndarray:
        self.X = X + 2
        self.Y = Y + 2
        self.P = P
        self.N = N
        self.C = C
        self.localeStr = Locales
        self.tileNumericLocales: List[Tuple[int,int]] = []
        self.channelNumericLocales: List[Tuple[int,int]] = []
        self.globalMap = np.zeros((self.Y,self.X), dtype=int)
        self.channelGen()
        if C == 0:
            self.tileGen()
        else:
            self.tileGenLine()



    #@overrides print as printing the globalMap, using dataframe for visibility
    def __repr__(self) -> str:
        #return str(DataFrame(self.globalMap, dtype=int))
        return str(self.globalMap)

    #Default Tile Placement Random Generation Function, Generating Numbered Tiles
    def tileGen(self) -> None:
        self.tileNumericLocales = []
        self.clearTiles()
        
        #excluding walls
        tileX = self.X - 2
        tileY = self.Y - 2

        tilePool = np.array(range((tileX)*(tileY))) #Creating possible candidates for tiles

        #move candidate location to center of globalMap
        for i in range(tilePool.size):
            tilePool[i] = ((i // tileX) * 2 + 1) + self.X + i
            

        rng = np.random.default_rng() #random generator

        for i in range(int(tileX*tileY*self.P)):
            candidate = rng.integers(low = 0, high = tilePool.size)
            candidate_locale = tilePool[candidate]

            self.globalMap[candidate_locale % self.Y][candidate_locale // self.Y] = 1 + i
            self.tileNumericLocales.append((candidate_locale % self.Y, candidate_locale // self.Y)) 

            tilePool = np.delete(tilePool, candidate)

    #TileGen with specified lines, generating x empty blocks on each row.
    #In this mode, self.tileNumericLocales is the empty blocks on each row.
    def tileGenLine(self) -> None:
        self.tileNumericLocales = []
        self.clearTiles()

        #excluding walls
        tileX = self.X - 2
        tileY = self.Y - 2

        self.globalMap[1:(1 + tileX), 1:(1 + tileY)] = 1 #set all to block with priority 1

        rng = np.random.default_rng() #random generator

        for i in range(tileY):
            candidatePool = np.array(range(tileX)) + 1

            for j in range(self.C):
                candidate = rng.integers(low = 0, high = len(candidatePool))
                candidate_locale = candidatePool[candidate]

                self.globalMap[i + 1][candidate_locale] = 0
                self.tileNumericLocales.append((i + 1, candidate_locale))

                candidatePool = np.delete(candidatePool, candidate)


    #Generate Channel
    def channelGen(self) -> None:
        self.channelNumericLocales = []
        self.clearMap()

        self.__addWallsToMap()
        self.__strCmdToLocales()

        htwp = np.array(range(1, self.X - 1))
        hdwp = htwp + ((self.Y - 1) * self.X)
        vlwp = np.array(range(1, self.Y - 1)) * self.X
        vrwp = vlwp + self.X - 1
        channelPool = np.concatenate((htwp, hdwp, vlwp, vrwp))

        rng = np.random.default_rng() #random generator

        for i in range(self.N):
            candidate = rng.integers(low = 0, high = len(channelPool))
            candidate_locale = channelPool[candidate]

            while(self.globalMap[candidate_locale % self.Y][candidate_locale // self.Y] != -3):
                if len(channelPool) != 0:
                    channelPool = np.delete(channelPool, candidate)
                    candidate = rng.integers(low = 0, high = len(channelPool))
                    candidate_locale = channelPool[candidate]
                else:
                    return

            self.globalMap[candidate_locale % self.Y][candidate_locale // self.Y] = -2 #set as outbound only
            self.channelNumericLocales.append((candidate_locale % self.Y, candidate_locale // self.Y))

            channelPool = np.delete(channelPool, candidate)

            

    #Switch the numbering of tiles to multiple batches, IRREVERSIABLE
    def mapBatchify(self, B: int) -> None:
        if (B > 0) & (B < (len(self.tileNumericLocales) / 2)) :
            for i in range(len(self.tileNumericLocales)):
                candidate_locale = self.tileNumericLocales[i]
                self.globalMap[candidate_locale[0]][candidate_locale[1]] = i // ((len(self.tileNumericLocales) + B) // B) + 1


    def getMap(self) -> np.ndarray:
        return self.globalMap

    # Setter is disabled
    # def setMap(self, inputMap: np.ndarray) -> None:
    #     self.globalMap = inputMap

    def getTileLocales(self) -> List[Tuple[int,int]]:
        return self.tileNumericLocales

    def getChannelLocales(self) -> List[Tuple[int,int]]:
        return self.channelNumericLocales

    def clearTiles(self):
        for i in range(self.Y):
            for j in range(self.X):
                if self.globalMap[i][j] > 0:
                    self.globalMap[i][j] = 0

    def clearMap(self):
        self.globalMap = np.zeros((self.Y,self.X), dtype=int)

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
                self.globalMap[loc[0]][loc[1]] = -2 #set as outbound only
                self.channelNumericLocales.append(loc)
            else:
                if i == "TOP":
                    self.globalMap[0] = -2
                    for i in range(X):
                        self.channelNumericLocales.append((0, i))
                if i == "BOT":
                    self.globalMap[Y-1] = -2
                    for i in range(X):
                        self.channelNumericLocales.append((Y - 1, i))
                if i == "LEF":
                    self.globalMap[:, 0] = -2
                    for i in range(Y):
                        self.channelNumericLocales.append((i, 0))
                if i == "RIG":
                    self.globalMap[:, X-1] = -2
                    for i in range(Y):
                        self.channelNumericLocales.append((i, X-1))
                    


    def __addWallsToMap(self) -> None:
        for i in range(self.X):
            self.globalMap[0][i] = -3
            self.globalMap[self.Y - 1][i] = -3
        for i in range(self.Y):
            self.globalMap[i][0] = -3
            self.globalMap[i][self.X - 1] = -3


        # vertWall = np.zeros((self.Y,1), dtype = int) - 3
        # hrznWall = np.zeros((1,self.X + 2), dtype = int) -3
        # self.globalMap = np.hstack((vertWall, np.hstack((self.globalMap, vertWall))))
        # self.globalMap = np.vstack((hrznWall, np.vstack((self.globalMap, hrznWall))))
        # self.Y += 2
        # self.X += 2
        # self.tileNumericLocales = [(a+1, b+1) for (a,b) in self.tileNumericLocales]


