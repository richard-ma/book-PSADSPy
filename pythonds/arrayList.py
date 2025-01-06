class ArrayList:
    def __init__(self):
        self.sizeExponent = 0
        self.maxSize = 0
        self.lastIndex = 0
        self.myArray = []
    
    def append(self, val):
        if self.lastIndex > self.maxSize - 1:
            self.__resize()
        self.myArray[self.lastIndex] = val
        self.lastIndex += 1
    
    def __resize(self):
        newsize = 2 ** self.sizeExponent
        print("newsize = ", newsize)
        newarray = [0] * newsize
        for i in range(self.maxSize):
            newarray[i] = self.myArray[i]
        
        self.maxSize = newsize
        self.myArray = newarray
        self.sizeExponent += 1
    
    def __getitem__(self, idx):
        if idx < self.lastIndex:
            return self.myArray[idx]
        else:
            raise LookupError('index out of bounds')
    
    def __setitem__(self, idx, val):
        if idx < self.lastIndex:
            self.myArray[idx] = val
        else:
            raise LookupError('index out of bounds')

    def insert(self, idx, val):
        if self.lastIndex > self.maxSize - 1:
            self.__resize()
        for i in range(self.lastIndex, idx-1, -1):
            self.myArray[i + 1] = self.myArray[i]
        self.lastIndex += 1
        self.myArray[idx] = val