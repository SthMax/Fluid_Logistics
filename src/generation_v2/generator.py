from os import X_OK
from typing import List, Tuple
import numpy as np

class newMapGenerator:
    #initialization
    #@params: X: X length, Y: Y length, D: Density: 0 <= Density < 1
    def __init__(self, X: int, Y: int, D: float = 0.5) -> np.ndarray:
        self.X = X
        self.Y = Y
        self.D = D

        self.globalMap = np.zeros((Y, X), dtype=int)

        self.tileNum = int (Y * D)
        



