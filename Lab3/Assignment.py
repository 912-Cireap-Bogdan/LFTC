

class hashTable:

    @property
    def table(self):
        return self._table

    def __init__(self, size=10):
        self._table = [[],] * size
        self.max_size = size
        self.current_size = 0

    def check_prime(self,n):
        if n == 1 or n == 0:
            return 0
        for i in range(2, n//2):
            if n % i == 0:
                return 0
        return 1

    def getPrime(self,n):
        if n % 2 == 0:
            n = n + 1
        while not self.check_prime(n):
            n += 2
        return n

    def hashFunction(self,key):
        capacity = self.getPrime(10)
        return key % capacity


    def insertData(self,key, data):
        index = self.hashFunction(key)

        if self.current_size + 1 >= self.max_size:
            aux = self.current_size
            while(aux <= self.max_size*2):
                self._table.append([])
                aux +=1

            self.max_size = self.max_size*2

        if self._table[index] != []:
            self._table.append([key,data])
            self.current_size +=1
        else:
            self._table[index] = [key, data]
            self.current_size +=1


    def removeData(self,key):
        index = self.hashFunction(key)
        aux = None

        self._table[index] = []
        for item in self._table:
            if item != []:
                if item[0] == key:
                    aux = item
                    break
        if aux:
            self._table[index] = aux


    def findData(self, key):
        index = self.hashFunction(key)
        return self._table[index]


    def __str__(self) -> str:
        return str(self.table)


class SymbolTable:
    def __init__(self,size) -> None:
        self.symbolTable = hashTable(size)
    

    def ST_tests(self):
        self.symbolTable.insertData(0,"def")
        self.symbolTable.insertData(0,"function")

        self.symbolTable.insertData(1,"a")
        self.symbolTable.insertData(2,"b")

        self.symbolTable.insertData(0,"while")

        print(self.symbolTable)

        print("searching for"+ "0: "+ str(self.symbolTable.findData(2)))

        print("removing 0")
        self.symbolTable.removeData(0)
        print(self.symbolTable)

if __name__ == "__main__":
    st_constants = SymbolTable(10)

    st_constants.ST_tests()

    st_identifiers = SymbolTable(10)