class IndexMapping:
    def __init__(self, highestX) -> None:
        mapping_dictX = {}
        for i in range(0,highestX):
            mapping_dictX[i] = (highestX - 1) - i
        
        self.indexMapDictX = mapping_dictX
        
    def MapX(self, x):
        return self.indexMapDictX[x]